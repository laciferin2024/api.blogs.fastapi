from fastapi import FastAPI
from datetime import datetime
from articles_router import router as articles_router

app = FastAPI()

app.include_router(articles_router, prefix="/articles", tags=["articles"])

@app.middleware("http")
async def log_requests(request, call_next):
    start_time = datetime.utcnow()
    response = await call_next(request)
    process_time = (datetime.utcnow() - start_time).total_seconds()
    log_data = {
        "method": request.method,
        "url": request.url.path,
        "time": start_time.isoformat(),
        "process_time": process_time,
    }
    print(log_data)  # Replace with actual logging
    return response

def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
