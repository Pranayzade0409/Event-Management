from pydantic import BaseModel

class Eventcreate(BaseModel):
    event_name: str
    event_date: str
    event_type: str

class EventResponse(Eventcreate):
    id: int

    class Config:
        from_attributes = True