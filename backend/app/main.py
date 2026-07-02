from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Nexus-OS LLM Financial Risk Analyzer",
    description="A FastAPI application for analyzing financial risk using LLMs.",
    version="1.0.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Welcome to the Nexus-OS LLM Financial Risk Analyzer API!"}

@app.get("/health")
def health_check():
    return {"status": "healthy","message": "The API is running smoothly."}