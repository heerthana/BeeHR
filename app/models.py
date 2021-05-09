import uuid

from sqlalchemy import Column, DateTime, func, BigInteger, String

from app import db
from common.utils.json_utils import serialize


def default_uuid():
    return uuid.uuid4().hex


class BaseModel(db.Model):
    __abstract__ = True
    id = Column(String(40), primary_key=True, default=lambda: default_uuid())
    created_at = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    update_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), default=None)

    def _asdict(self):
        return serialize(self)

    def objects(*args):
        return db.session.query(*args)
