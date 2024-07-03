from fastapi import FastAPI
from venv import users, projects

app = FastAPI()

app.include_router(users.router, prefix="/api")
app.include_router(projects.router, prefix="/api")

@app.get("/")
def read_root():
    return {"im up"}

