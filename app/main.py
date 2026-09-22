from fastapi import FastAPI

app = FastAPI(
    title="Cloud Platform API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Cloud Platform API"}

@app.get("/health")
def health():
    return {"status": "healthy"}
