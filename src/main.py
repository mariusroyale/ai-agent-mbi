from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Agent 007 here, Bond. App under Development."}
