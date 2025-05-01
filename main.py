from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from workflows.home_office import HomeOfficeWorkflow

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(q: Question):
    return {"answer": "You asked: " + q.question}

# Conversational endpoint
class Message(BaseModel):
    input: str

workflow = HomeOfficeWorkflow()

@app.post("/chat/home-office")
async def chat_home_office(msg: Message):
    reply = workflow.next(msg.input)
    return {"response": reply}

# Create Account endpoint
class NewAccount(BaseModel):
    name: str
    email: str
    city: str
    state: str

@app.post("/create-account")
async def create_account(account: NewAccount):
    print("New user registered:", account)
    return {"message": "Account created"}
