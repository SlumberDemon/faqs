import fastapi
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

app = fastapi.FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"])
pages = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def home(request: fastapi.Request):
    return pages.TemplateResponse(
        "index.html",
        {"request": request},
    )


@app.get("/{id}")
async def page(request: fastapi.Request, id):
    return pages.TemplateResponse(
        f"/faqs/{id}.html", {"request": request, "page": f"{id}.html"}
    )
