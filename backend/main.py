from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.gzip import GZipMiddleware
import os
from contextlib import asynccontextmanager

from backend.api import leads, deals
from backend.database import create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan handler for startup and shutdown events."""
    # Startup: Create database tables
    create_db_and_tables()
    yield
    # Shutdown: Cleanup resources if needed

app = FastAPI(
    title="Cortex CRM",
    description="Premium AI-Powered CRM",
    lifespan=lifespan
)

# Add GZip compression middleware for faster responses
app.add_middleware(GZipMiddleware, minimum_size=1000)

# Include Routers
app.include_router(leads.router)
app.include_router(deals.router)


# Mount Static Files
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../frontend/static"))
templates_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../frontend/templates"))
# Ensure directories exist
os.makedirs(static_dir, exist_ok=True)
os.makedirs(templates_dir, exist_ok=True)

app.mount("/static", StaticFiles(directory=static_dir), name="static")
templates = Jinja2Templates(directory=templates_dir)

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "title": "Dashboard",
        "user_name": "Administrador"
    })

@app.get("/leads", response_class=HTMLResponse)
async def leads_page(request: Request):
    return templates.TemplateResponse("leads.html", {
        "request": request,
        "title": "Prospectos",
        "user_name": "Administrador"
    })

@app.get("/pipeline", response_class=HTMLResponse)
async def pipeline_page(request: Request):
    return templates.TemplateResponse("pipeline.html", {
        "request": request,
        "title": "Embudo",
        "user_name": "Administrador"
    })

@app.get("/settings", response_class=HTMLResponse)
async def settings_page(request: Request):
    return templates.TemplateResponse("settings.html", {
        "request": request,
        "title": "Ajustes",
        "user_name": "Administrador"
    })



# To run: uvicorn backend.main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)

