from datetime import datetime

from sqlalchemy import SMALLINT, TIMESTAMP, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    __abstract__ = True

    type_annotation_map = {
        int: SMALLINT,
        datetime: TIMESTAMP(timezone=False),
        str: String(),
    }
