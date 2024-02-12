from fastapi import APIRouter, Depends

from app.schemes import DataRequest, DataResponse
from app.services import DataService

router = APIRouter(prefix='/data', tags=['Data'])


@router.post(path='/', response_model=DataResponse)
async def add_data(
    item: DataRequest, data_service: DataService = Depends()
) -> DataResponse:
    return await data_service.add_data(item)
