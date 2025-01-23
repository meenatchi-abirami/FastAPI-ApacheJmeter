from fastapi import FastAPI
from dataforge.src.api.routes import router
from dataforge.src.seedwork.logger import logging_component

app = FastAPI()
logger = logging_component.get_gray_logger()


app.include_router(router)
