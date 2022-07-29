from pydantic import BaseModel


class PingResponseSchema(BaseModel):
    status: int
    message: str

    class Config:
        schema_extra = {"example": {"status": 2, "message": "pong"}}
