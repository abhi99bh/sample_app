from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

items_dict = {
    "car": 10.99,
    "bus": 8.50,
    "truck": 15.00
}


@app.get("/", response_class=HTMLResponse)
async def show_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def read_form(request: Request, item1: str = Form(...), item2: str = Form(...)):
    item1_price = items_dict.get(item1, 0)
    item2_price = items_dict.get(item2, 0)
    
    return templates.TemplateResponse("index.html", {"request": request, "item1": item1, "item1_price": item1_price, "item2": item2, "item2_price": item2_price})
