# DOCUMENT 2 — Technical Requirements Document (TRD)
 
## 2.1 System Architecture (ASCII)
```
                        ┌─────────────────────┐
                        │   React + Vite UI    │
                        │  (Dashboard/Chatbot)  │
                        └──────────┬───────────┘
                                   │ REST/WS
                        ┌──────────▼───────────┐
                        │      FastAPI Core      │
                        │  Auth | Docs | KPI |   │
                        │  Risk | Chat | Alerts  │
                        └──────────┬───────────┘
              ┌────────────────────┼────────────────────┐
              ▼                    ▼                     ▼
     ┌────────────────┐  ┌──────────────────┐  ┌──────────────────┐
     │  PostgreSQL      │  │   FAISS/Chroma    │  │  HF Inference API │
     │  (structured data)│  │ (vector store)     │  │ (LLM + embeddings)│
     └────────────────┘  └──────────────────┘  └──────────────────┘
              ▲
              │
     ┌────────┴─────────┐
     │  Document Pipeline │
     │ PyMuPDF→OCR→Chunk  │
     └────────────────────┘
```
 
## 2.2 Technology Stack
- **Backend:** FastAPI (async), Python 3.11
- **Frontend:** React + Vite + Tailwind + Recharts/Plotly
- **DB:** MySQL (structured), FAISS or ChromaDB (vectors)
- **PDF/OCR:** PyMuPDF, Tesseract (fallback for scanned docs)
- **LLM Orchestration:** LangChain (RAG pipelines), LangGraph (future multi-agent)
- **LLM/Embeddings:** Hugging Face Inference API (see model table in Doc 6)
- **Auth:** JWT + bcrypt
- **Background jobs:** APScheduler (lightweight, avoids Redis dependency initially)
- **Deployment:** Docker Compose (local) → cloud (future)
## 2.3 RAG Architecture
1. PDF → PyMuPDF text/table extraction → OCR fallback for scanned pages
2. Section detection (regex + heading heuristics: "Risk Factors", "MD&A", "Financial Statements")
3. Chunking (semantic, ~500 tokens, overlap 50)
4. Embedding via HF `sentence-transformers/all-MiniLM-L6-v2`
5. Store in FAISS/Chroma with metadata (page, section, company, filing date)
6. Retrieval: top-k similarity + section-filtered retrieval for targeted queries (e.g., risk queries only search Risk Factors chunks)
7. LLM generation with retrieved context + forced citation of chunk IDs
## 2.4 LLM Pipeline (Extraction)
- Use **forced JSON schema prompting** — never free-text parse numbers
- Validate extracted KPIs against expected types/ranges (e.g., margins between -100% and 100%)
- Flag low-confidence extractions for user review rather than silently failing
## 2.5 Database Design
See Document 5 for full schema.
 
## 2.6 Caching
Cache embeddings per document hash (avoid re-embedding on re-upload). Cache LLM responses for identical KPI extraction prompts per document version.
 
## 2.7 Error Handling
- Structured error responses (code, message, retry-able flag)
- Graceful degradation: if HF inference fails, queue and retry; never silently show stale/wrong data
## 2.8 Testing Strategy
- Unit tests: ratio calculations (pure functions, 100% coverage target)
- Integration tests: upload → extraction → KPI pipeline on 5 sample real 10-Ks
- LLM eval: golden-set of Q&A pairs per test filing, scored for accuracy/citation validity
## 2.9 Security
JWT expiry + refresh tokens, input sanitization on file upload (type/size limits), rate limiting on API, role-based access (user/admin).
 
## 2.10 Deployment
Docker Compose for local dev (FastAPI + Postgres + Chroma); single VM or container deployment for demo/production later.
 
## 2.11 Monitoring & Logging
Structured JSON logs, request tracing IDs, basic admin dashboard showing processing queue/failures.