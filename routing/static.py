from loader import app
from fastapi.responses import FileResponse
from fastapi import Request


@app.get("/")
async def index():
    return FileResponse("assets/static/index.html")


@app.get("/favicon.ico")
async def favicon_ico():
    return FileResponse("data/favicon.ico")


@app.get("/{catchall:path}")
async def read_index(request: Request):
    path: str = request.path_params['catchall']
    print(path)
    return FileResponse(f"{path}")


