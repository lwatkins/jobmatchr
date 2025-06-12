from pydantic import BaseModel


class Job(BaseModel):
    title: str
    description: str
    location: str
    salary: float