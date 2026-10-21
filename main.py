
import os

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Everyday Calculator")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Set APP_BASE_URL to your real HTTPS domain after deployment.
BASE_URL = os.getenv(
    "APP_BASE_URL",
    "http://127.0.0.1:8000"
).rstrip("/")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"title": "Everyday Calculator"}
    )


@app.get("/robots.txt")
async def robots():
    content = (
        "User-agent: *\n"
        "Allow: /\n"
        f"Sitemap: {BASE_URL}/sitemap.xml\n"
    )

    return Response(
        content=content,
        media_type="text/plain"
    )


@app.get("/sitemap.xml")
async def sitemap():
    content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>{BASE_URL}/</loc>
  </url>
</urlset>
"""

    return Response(
        content=content,
        media_type="application/xml"
    )
