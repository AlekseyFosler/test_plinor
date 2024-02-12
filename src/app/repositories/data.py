from sqlalchemy.dialects.postgresql import insert

from app.database import Session
from app.models import Data
from app.schemes import DataRequest, DataResponse


class DataRepository:
    def __init__(self):
        self.session = Session()

    async def add_data(self, item: DataRequest) -> DataResponse | None:
        stmt = insert(Data).values(**item.model_dump()).returning(Data)
        result: Data | None = await self.session.execute(stmt)  # noqa
        return DataResponse.model_validate(result) if result else None
