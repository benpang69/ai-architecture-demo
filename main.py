from fastapi import FastAPI
from pydantic import BaseModel
# Import the orchestrator's question handler
from orchestrator import handle_question, handle_summarize

app = FastAPI(title="AI Architecture Demo")


# Request and response models for the API
class QuestionRequest(BaseModel):
    question: str


class AnswerResponse(BaseModel):
    answer: str

class SummarizeRequest(BaseModel):
    text: str

class SummaryResponse(BaseModel):
    summary: str


# Health check endpoint
@app.get("/health")
async def health():
    return {"status": "healthy"}


# Question answering endpoint - delegates to the orchestrator
@app.post("/ask", response_model=AnswerResponse)
async def ask(request: QuestionRequest):
    answer = handle_question(request.question)
    return AnswerResponse(answer=answer)

@app.post("/summarize", response_model=SummaryResponse)
async def summarize(request: SummarizeRequest):
    summary = handle_summarize(request.text)
    return SummaryResponse(summary=summary)