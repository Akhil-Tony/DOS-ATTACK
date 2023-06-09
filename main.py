from fastapi import FastAPI, Request, WebSocket
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
import time
import uvicorn

app = FastAPI()

templates = Jinja2Templates(directory="static")

global weight_v
weight_v = 1

global height_v
height_v = 1

global security
security = False

global old_time
old_time = 0

active_websockets = set()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    print("inside web socket function")
    await websocket.accept()
    active_websockets.add(websocket)

    try:
        while True:
            data = await websocket.receive_text()
    except Exception as e:
        active_websockets.remove(websocket)

@app.get('/checkbox') # security checkbox
async def callapi(request: Request):
    global security
    if security == False:
        security = True
    else:
        security = False
    print('security is ',security)
    return {"message": "security clicked "}
@app.get('/')
async def root(request: Request): 
    print('root function called')
    global weight_v,height_v
    global security
    security = False
    return templates.TemplateResponse("bmi.html", {"request": request,"weight": weight_v, 
                                                   "height":height_v})

@app.get("/items/{weight}/{height}")
async def read_item(request: Request,weight: int,height: int):
    global weight_v
    weight_v = weight

    global height_v
    height_v = height
    
    print('recived ',weight_v,height_v)
    
    for websocket in active_websockets:
        await websocket.send_text("reload")

    if security == False:
        return True
    else:
        return False