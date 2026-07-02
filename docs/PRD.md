# DOCUMENT 1 — Product Requirements Document (PRD)
 
## 1.1 Executive Summary
LLM Financial Risk Analyzer is an AI-powered platform that ingests financial reports (10-K, 10-Q, annual reports) and produces structured KPIs, financial ratios, risk scores, investment recommendations, and explainable insights — through an interactive dashboard and a RAG-powered chatbot. It is designed to run on modest hardware by using hosted Hugging Face inference instead of local GPU compute.
 
## 1.2 Business Problem
Reading a 200-page 10-K to extract meaningful signal is slow and error-prone. Retail investors and students lack the tooling that analysts use; analysts themselves spend excessive time on manual extraction rather than judgment. There is no accessible, explainable, open-source tool that turns a raw filing into a structured risk/investment view.
 
## 1.3 Business Goals
- Reduce time-to-insight from a financial report from hours to minutes
- Make every AI claim traceable to a source (no black-box outputs)
- Keep the system runnable on low-spec hardware using free/open models
- Produce a portfolio/hackathon-grade, demo-able product incrementally
## 1.4 Target Users
Retail investors, financial analysts, students, researchers, auditors, corporate finance teams, portfolio managers.
 
## 1.5 Competitive Analysis
| Product | Strength | Gap this project fills |
|---|---|---|
| Bloomberg Terminal | Deep data, real-time | Expensive, closed, no explainability layer |
| AlphaSense | Good search over filings | No open-source path, no local/low-cost option |
| ChatGPT + manual prompting | Flexible | No structured extraction, no persistent dashboard, no citations |
 
## 1.6 User Personas
- **Retail Investor Raj**: wants a quick buy/hold/sell signal with plain-language reasoning
- **Analyst Priya**: wants fast KPI extraction and ratio computation to cross-check her own models
- **Student Aman**: wants to learn financial analysis by seeing AI reasoning + citations
## 1.7 Pain Points Addressed
- Manual KPI extraction from unstructured PDFs
- No traceability of AI-generated financial claims
- No easy way to compare companies side-by-side
- No lightweight/local-friendly financial AI tool
## 1.8 Functional Requirements
Auth, document upload/management, OCR + extraction, KPI extraction, ratio calculation, risk analysis + scoring, investment recommendation, dashboard, chatbot (RAG), company comparison, historical trends, report generation, alerts, news/sentiment, portfolio management, admin panel, forecasting, explainability, knowledge graph.
 
## 1.9 Non-Functional Requirements
- Runs on low-spec hardware (no local LLM inference required)
- Report processing (50-page 10-K) completes in under 3 minutes
- All AI outputs include source citation
- System available as a single-user local deployment, extensible to multi-user cloud
## 1.10 Success Metrics
- KPI extraction accuracy ≥ 90% vs. manual ground truth on test filings
- Risk flag precision reviewed against actual filing risk sections
- End-to-end report processing time
- Chatbot answer relevance (manual review on 20 sample Qs)
## 1.11 User Stories (sample)
- As a user, I can upload a 10-K and see extracted KPIs within minutes.
- As a user, I can ask the chatbot "what is the debt trend?" and get a cited answer.
- As a user, I can compare two companies' risk scores side by side.
- As a user, I get an alert if a tracked company's risk score jumps.
## 1.12 Acceptance Criteria (sample)
- Upload → processing → KPI cards populate without manual intervention
- Every risk flag links to the exact filing page/section it was derived from
- Chatbot never answers without retrieved context; refuses if no relevant chunk found
## 1.13 Constraints
- No paid API dependency required for core functionality
- Must function without local GPU (Hugging Face Inference API only)
## 1.14 Future Scope
Multi-user SaaS, real-time filing ingestion (EDGAR webhook), mobile app, broker integration for live portfolio sync.
 
## 1.15 Risks
- Hosted HF inference rate limits under free tier
- Financial table extraction accuracy on scanned/poorly formatted PDFs
- LLM hallucination on numeric extraction (mitigated via structured JSON + validation)
## 1.16 Milestones & Release Plan
See Document 6 (12-week roadmap).
 
