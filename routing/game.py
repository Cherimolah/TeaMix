from fastapi.responses import JSONResponse

from loader import app
from framework.game import Game


@app.get("/start", response_class=JSONResponse)
async def start_game():
    return Game()
