from fastapi import FastAPI
import uvicorn

app = FastAPI(title="test-backend")


@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.2", port=8000, reload=True)
