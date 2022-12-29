from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Mathieu's API",
    description="Simple API to be used as a docker/k8S tutorial",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(
    "/hello/",
    tags=["hello"],
    status_code=status.HTTP_200_OK,
    response_description="Hello !",
    summary="resume",
)
async def get_hello():
    return {"Hello": "World"}
