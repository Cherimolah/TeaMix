from fastapi.responses import JSONResponse

from loader import app
from framework.game import Game

a = Game()

@app.get("/start", response_class=JSONResponse)
async def start_game():
    a.field.init_tiles()
    return a

@app.get("/check_steps", response_class=JSONResponse)
async def check_steps():
    steps = a.field.exist_steps()
    return {"steps": steps}
