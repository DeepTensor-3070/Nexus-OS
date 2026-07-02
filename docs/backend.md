# DOCUMENT 5 — Backend Schemas
 
## 5.1 ER Diagram (text)
```
users ──< documents ──< kpis
   │           │
   │           ├──< risks
   │           ├──< chunks (vector metadata)
   │           └──< forecasts
   │
   ├──< portfolios ──< portfolio_holdings ──> companies
   ├──< alerts
   └──< chat_sessions ──< chat_messages
 
companies ──< documents
companies ──< knowledge_graph_nodes ──< knowledge_graph_edges
```
 
## 5.2 Core Tables (SQL)
```sql
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash TEXT NOT NULL,
  role VARCHAR(20) DEFAULT 'user', -- user | admin
  created_at TIMESTAMP DEFAULT now()
);
 
CREATE TABLE companies (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name VARCHAR(255) NOT NULL,
  ticker VARCHAR(20),
  sector VARCHAR(100)
);
 
CREATE TABLE documents (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id),
  company_id UUID REFERENCES companies(id),
  filename TEXT NOT NULL,
  filing_type VARCHAR(20), -- 10-K | 10-Q | annual
  filing_date DATE,
  status VARCHAR(20) DEFAULT 'queued',
  uploaded_at TIMESTAMP DEFAULT now()
);
 
CREATE TABLE kpis (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  document_id UUID REFERENCES documents(id),
  kpi_name VARCHAR(100),
  value NUMERIC,
  unit VARCHAR(20),
  confidence FLOAT,
  source_chunk_id UUID
);
 
CREATE TABLE risks (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  document_id UUID REFERENCES documents(id),
  category VARCHAR(50), -- liquidity, debt, legal, etc.
  severity INT, -- 1-5
  description TEXT,
  evidence_chunk_id UUID,
  confidence FLOAT
);
 
CREATE TABLE chunks (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  document_id UUID REFERENCES documents(id),
  section VARCHAR(100),
  page_number INT,
  text TEXT,
  embedding_ref VARCHAR(255) -- pointer into FAISS/Chroma
);
 
CREATE TABLE forecasts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  document_id UUID REFERENCES documents(id),
  metric VARCHAR(50),
  period VARCHAR(20),
  predicted_value NUMERIC,
  confidence_interval_low NUMERIC,
  confidence_interval_high NUMERIC
);
 
CREATE TABLE portfolios (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id),
  name VARCHAR(100)
);
 
CREATE TABLE portfolio_holdings (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  portfolio_id UUID REFERENCES portfolios(id),
  company_id UUID REFERENCES companies(id),
  weight FLOAT
);
 
CREATE TABLE alerts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id),
  company_id UUID REFERENCES companies(id),
  trigger_type VARCHAR(50),
  threshold NUMERIC,
  is_active BOOLEAN DEFAULT true
);
 
CREATE TABLE knowledge_graph_nodes (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  company_id UUID REFERENCES companies(id),
  node_type VARCHAR(50), -- exec, subsidiary, competitor, product, risk
  name VARCHAR(255)
);
 
CREATE TABLE knowledge_graph_edges (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  source_node_id UUID REFERENCES knowledge_graph_nodes(id),
  target_node_id UUID REFERENCES knowledge_graph_nodes(id),
  relationship VARCHAR(100)
);
```

## 5.3 Sample API Endpoints
```
POST   /auth/register
POST   /auth/login
POST   /documents/upload
GET    /documents/{id}/status
GET    /documents/{id}/kpis
GET    /documents/{id}/risks
POST   /chat/{document_id}/message
GET    /companies/{id}/history
POST   /compare
GET    /portfolio
POST   /alerts
GET    /admin/users
GET    /admin/logs
```

## 5.4 Sample JSON Schema — KPI Extraction (forced output)
```json
{
  "kpi_name": "Revenue",
  "value": 12500000000,
  "unit": "USD",
  "period": "FY2025",
  "confidence": 0.94,
  "source": {"page": 45, "section": "Financial Statements", "chunk_id": "uuid"}
}
```