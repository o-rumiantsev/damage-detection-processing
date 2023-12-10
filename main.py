from fastapi import FastAPI, UploadFile
from pydantic import BaseModel

from src.api import files as files_service
from src.api import analyzing_jobs as analyzing_jobs_service
from src.api import polygons as polygons_service

app = FastAPI()


class CreateAnalyzingJobModel(BaseModel):
    file_id: str


@app.post("/files")
async def create_files(files: list[UploadFile]):
    data = await files_service.create_many(files)
    return {"data": data}


@app.post('/analyzing-jobs')
async def create_analyzing_job(dto: CreateAnalyzingJobModel):
    data = await analyzing_jobs_service.create(dto.file_id)
    return {"data": data}


@app.get('/polygons')
async def get_polygons():
    data = await polygons_service.get_many()
    return {"data": data}
