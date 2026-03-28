#endpoints only
#will contain  FastAPI instance (app = FastAPI(...)) and endpoints.

from fastapi import FastAPI


#creates web server app object, title and vrsion shows up in swagger doc later
app = FastAPI(title = "MoodWave API", version = "0.1.0")


# a decorator that says when a client sends a HTTP Get request to this path, run the function below
@app.get("/api/v1/health")
def health():
    #FastAPI will automatically convert the return value(python dictionary here) to a JSON response.
    return {"Ok": True}


@app.get("/api/v1/demo-query")
def demo_query(use_spotify: bool = False):
    return {"use_spotify": use_spotify}