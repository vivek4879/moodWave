#endpoints only
#will contain  FastAPI instance (app = FastAPI(...)) and endpoints.

from fastapi import FastAPI

app = FastAPI(title = "MoodWave API", version = "0.1.0")


@app.get("/api/v1/health")
def health():
    #FastAPI will automatically convert the return value(python dictionary here) to a JSON response.
    return {"Ok": True}