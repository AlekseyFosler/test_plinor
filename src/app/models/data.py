import uuid
from datetime import datetime

from sqlalchemy import func
from sqlalchemy.dialects.postgresql import BIGINT, SMALLINT, UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Data(Base):
    __tablename__ = 'data'  # noqa

    data_uuid: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    a: Mapped[int] = mapped_column(SMALLINT, nullable=True)
    b: Mapped[int] = mapped_column(SMALLINT, nullable=True)
    c: Mapped[int] = mapped_column(SMALLINT, nullable=True)
    d: Mapped[int] = mapped_column(SMALLINT, nullable=True)
    e: Mapped[int] = mapped_column(SMALLINT, nullable=True)
    f: Mapped[int] = mapped_column(SMALLINT, nullable=True)
    ts: Mapped[BIGINT] = mapped_column(BIGINT, nullable=False)
    create_date: Mapped[datetime] = mapped_column(server_default=func.now())
    update_date: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
