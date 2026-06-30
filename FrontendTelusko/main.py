from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def greet():
    return {"message": "Welcome to FastAPI Learnings"}

@app.get("/api/greet")
def api_greet():
    return {"message": "API endpoint working"}

@app.get("/health")
def health():
    return {"status": "ok"}
