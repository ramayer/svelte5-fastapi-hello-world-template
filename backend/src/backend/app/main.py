import uvicorn
from fastapi import FastAPI
from fastapi.responses import Response

app = FastAPI()


@app.get("/")
def root():
    return {"txt": "Hello World"}


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    svg = """<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
            <circle cx="100" cy="100" r="80" fill="yellow" stroke="black" stroke-width="4"/>
            <circle cx="70" cy="80" r="10" fill="black">
                <animate attributeName="cx" values="70;60;70" dur="2s" repeatCount="indefinite"/>
            </circle>
            <circle cx="130" cy="80" r="10" fill="black">
                <animate attributeName="cx" values="130;120;130" dur="2s" repeatCount="indefinite"/>
            </circle>
            <path d="M 60 120 Q 100 160, 140 120" stroke="black" stroke-width="4" fill="transparent"/>
            </svg>"""
    return Response(content=svg, media_type="image/svg+xml")


def run():
    uvicorn.run(app, host="0.0.0.0", port=8000)  # noqa: S104
