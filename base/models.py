from sqlalchemy import Column, DateTime, func, String, Enum
from config import db
import uuid
from common.utils.json_utils import serialize


def default_uuid():
    return uuid.uuid4().hex


class BaseModel(db.Model):
    __abstract__ = True

    __mapper_args__ = {
        'confirm_deleted_rows': False
    }
    id = Column(String(40), primary_key=True, default=lambda: default_uuid())
    created_at = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    update_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), default=None)
    created_by = Column(String(40), default=None)
    updated_by = Column(String(40), default=None)
    deleted_by = Column(String(40), default=None)

    def _asdict(self):
        return serialize(self)

    def objects(*args):
        return db.session.query(*args)
