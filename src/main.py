from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from settings import settings
from agent.agent_007 import Agent007

app = FastAPI()

agent007 = Agent007()

# Define the request body schema
class MessagePayload(BaseModel):
    role: str
    content: str

@app.get("/")
def read_root():

    for setting in settings:
        print(setting)

    return {"message": "Agent 007 here, Bond. App under Development."}

@app.post("/messages")
def add_messages(payload: MessagePayload):
    agent007.add_message(payload.role, payload.content)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Message added successfully"}
    )

@app.get("/messages")
def read_messages():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"messages": agent007.get_messages()}
    )

@app.delete("/messages")
def clear_messages():
    agent007.reset()
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"status": "messages cleared"}
    )
