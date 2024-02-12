from http import HTTPStatus

from fastapi import HTTPException

from app.repositories import DataRepository
from app.schemes import DataRequest, DataResponse


class DataService:
    def __init__(self):
        self.data_repository = DataRepository()

    async def add_data(self, item: DataRequest) -> DataResponse:
        result: DataResponse | None = await self.data_repository.add_data(item)
        if not result:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail=f'Failed to create data',
            )
        return result
