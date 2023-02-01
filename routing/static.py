from loader import app
from fastapi.responses import FileResponse
from fastapi import Request

folder = "assets/"


@app.get("/")
async def index():
    return FileResponse("assets/static/index.html")


@app.get("/assets/{catchall:path}")
def read_index(request: Request):
    path: str = request.path_params['catchall']
    return FileResponse(f"{folder}{path}")

