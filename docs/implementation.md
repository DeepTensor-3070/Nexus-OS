# DOCUMENT 6 — Implementation Plan
 
## 6.1 Phased Development
 
### Phase 1 (Weeks 1–3): Core Pipeline
**Objectives:** Auth, upload, extraction, KPI extraction, basic dashboard
**Tasks:** FastAPI scaffold, Postgres schema, JWT auth, PyMuPDF extraction, chunking + embeddings, HF KPI extraction prompt, React dashboard shell
**Deliverable:** Upload a 10-K → see KPI cards populate
**Definition of Done:** End-to-end flow works on 3 real test filings without manual intervention

### Phase 2 (Weeks 4–6): Intelligence Layer
**Objectives:** Ratios, risk scoring, explainability, forecasting
**Tasks:** Ratio calculator (pure Python), risk analysis agent + scoring, citation linking UI, simple forecasting (linear regression/Prophet on historical KPIs)
**Deliverable:** Risk heatmap + explainable citations working
 
### Phase 3 (Weeks 7–9): Differentiators
**Objectives:** Chatbot (RAG), knowledge graph, sentiment, comparison
**Tasks:** RAG chat endpoint, NER-based entity extraction for knowledge graph, HF sentiment model on news, comparison view
**Deliverable:** Working chatbot with citations; graph visualization
 
### Phase 4 (Weeks 10–12): Polish & Product
**Objectives:** Alerts, portfolio, report export, admin panel
**Tasks:** APScheduler alert jobs, portfolio CRUD, PDF/Excel export (docx/xlsx generation), admin dashboard
**Deliverable:** Fully demo-able product
 
## 6.2 Recommended Folder Structure
```
llm-financial-risk-analyzer/
├── backend/
│   ├── app/
│   │   ├── api/            # route handlers
│   │   ├── core/           # config, security
│   │   ├── models/         # ORM models
│   │   ├── schemas/        # Pydantic schemas
│   │   ├── services/
│   │   │   ├── extraction/
│   │   │   ├── kpi/
│   │   │   ├── risk/
│   │   │   ├── forecasting/
│   │   │   ├── rag/
│   │   │   └── knowledge_graph/
│   │   ├── db/
│   │   └── main.py
│   ├── tests/
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── hooks/
│   │   ├── charts/
│   │   └── api/
│   └── package.json
├── docker-compose.yml
└── README.md
```
 
## 6.3 Git Branching Strategy
`main` (stable) ← `develop` ← feature branches `feature/kpi-extraction`, `feature/risk-scoring`, etc. PRs squash-merged into `develop`, periodic merges to `main` at phase completion.
 
## 6.4 Coding Standards
Python: PEP8 + type hints + Pydantic validation everywhere. JS/React: ESLint + Prettier, functional components + hooks only. Commit style: Conventional Commits (`feat:`, `fix:`, `docs:`).
 
## 6.5 Recommended Hugging Face Models (free-tier friendly)
| Task | Model |
|---|---|
| General LLM reasoning / KPI extraction / risk analysis | `mistralai/Mistral-7B-Instruct-v0.3` or `meta-llama/Meta-Llama-3-8B-Instruct` |
| Embeddings | `sentence-transformers/all-MiniLM-L6-v2` |
| Sentiment analysis | `distilbert-base-uncased-finetuned-sst-2-english` |
| Financial-domain sentiment (better fit) | `ProsusAI/finbert` |
| NER (for knowledge graph) | `dslim/bert-base-NER` |
| Summarization (fallback, lighter than full LLM) | `facebook/bart-large-cnn` |
 
## 6.6 Recommended Datasets (dev/testing)
- SEC EDGAR full-text search (free, real 10-K/10-Q filings)
- Financial PhraseBank (sentiment benchmark)
- FiQA dataset (financial Q&A benchmark)
## 6.7 Production Deployment Architecture (future)
Docker containers behind Nginx reverse proxy → FastAPI (multiple workers) → managed Postgres → managed vector DB (or self-hosted Chroma on persistent volume) → HF Inference Endpoints (dedicated, if scaling beyond free tier) → object storage (S3-compatible) for uploaded PDFs.
 
## 6.8 Future Scalability Roadmap
Multi-tenant architecture, queue-based processing (Celery + Redis at scale), fine-tuned smaller model for KPI extraction to reduce inference cost, real-time EDGAR filing ingestion webhook, mobile client.
 
## 6.9 Sprint Planning (12-Week Agile Roadmap)
| Sprint | Weeks | Focus |
|---|---|---|
| 1 | 1–2 | Auth + upload + extraction pipeline |
| 2 | 3 | KPI extraction agent + validation |
| 3 | 4–5 | Ratio calculator + risk analysis agent |
| 4 | 6 | Risk scoring + explainability UI |
| 5 | 7 | RAG chatbot |
| 6 | 8 | Knowledge graph + sentiment |
| 7 | 9 | Company comparison + forecasting |
| 8 | 10 | Alerts + portfolio management |
| 9 | 11 | Report generation + admin panel |
| 10 | 12 | Polish, testing, demo prep |
 
## 6.10 GitHub Milestones (suggested)
`v0.1 - Core Pipeline`, `v0.2 - Risk & Ratios`, `v0.3 - RAG Chatbot`, `v0.4 - Knowledge Graph`, `v0.5 - Portfolio & Alerts`, `v1.0 - Demo Release`