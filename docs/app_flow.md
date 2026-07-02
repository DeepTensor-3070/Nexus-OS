# DOCUMENT 3 — Complete Application Flow
 
## 3.1 Authentication Flow
Landing → Register/Login → JWT issued → stored in httpOnly cookie or localStorage → protected routes check token → refresh flow on expiry → logout clears token.
 
## 3.2 Upload & Processing Flow
Dashboard → "Upload Report" → select company (or create new) → upload PDF → processing status (queued → extracting → chunking → embedding → analyzing → done) shown via polling/WebSocket → KPI cards populate → risk panel populates → chatbot becomes available for that document.
 
## 3.3 Dashboard Flow
Home → company selector → Financial Health Score card → KPI cards row → Revenue/Profit/Cash Flow charts → Risk Heatmap → Recommendation panel → "Ask a question" chatbot entry point → "Compare" button → "Export Report" button.
 
## 3.4 Chatbot Flow
User types question → retrieval over document's vector chunks → LLM answers with inline citations (page/section) → user can click citation → jumps to source excerpt → follow-up question retains conversation context.
 
## 3.5 Company Comparison Flow
Select 2+ companies → side-by-side KPI table → side-by-side risk radar chart → AI-generated comparison summary with citations from both documents.
 
## 3.6 Admin Flow
Admin login → user management table → system health (processing queue, failures) → model usage/logs → document management (all users' uploads).
 
## 3.7 Decision Tree — Document Processing
```
Upload received
 ├─ Valid PDF? ── No → reject, show error
 └─ Yes → Extract text
      ├─ Text extraction successful (>threshold)? 
      │    ├─ Yes → proceed to chunking
      │    └─ No → run OCR fallback → proceed to chunking
      └─ Chunk → Embed → Store → Run extraction agents → Update UI
```