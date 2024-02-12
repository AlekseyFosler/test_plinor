from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, model_validator


class DataRequest(BaseModel):
    a: int | None = Field(example=1)
    b: int | None = Field(example=2)
    c: int | None = Field(example=3)
    d: int | None = Field(example=7)
    e: int | None = Field(example=8)
    f: int | None = Field(example=9)
    ts: int = Field(example=int(datetime.now().timestamp()))

    @model_validator(mode='before')
    def check_card_number_omitted(cls, data: dict) -> dict:
        lowercase_keys = {key.lower() for key in data.keys()}
        if len(lowercase_keys) != len(data.keys()):
            raise ValueError(f"Key not unique")
        return {k.lower(): v for k, v in data.items()}


class DataResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    data_uuid: UUID
    a: int | None = Field(example=1)
    b: int | None = Field(example=2)
    c: int | None = Field(example=3)
    d: int | None = Field(example=7)
    e: int | None = Field(example=8)
    f: int | None = Field(example=9)
    ts: int = Field(example=int(datetime.now().timestamp()))
