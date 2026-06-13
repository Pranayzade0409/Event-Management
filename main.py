from fastapi import FastAPI
from app.routes.event_routes import event_router
from app.database.connection import Base,engine

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(event_router)


@app.get("/")
def ChecHealth():
    return {"message": "FastApi is working"}
