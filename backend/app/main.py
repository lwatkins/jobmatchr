from fastapi import FastAPI
from app.models.job import Job

app: FastAPI = FastAPI()


@app.get("/", response_model=dict[str, str])
def read_root() -> dict[str, str]:
    return {"message": "JobMatchr backend API"}


@app.post("/job", response_model=Job)
def create_job(job: Job) -> Job:
    return job # Temp

