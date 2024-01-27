from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controller import parts_router, other_accessories_router


def create_app():
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include your routers (controllers)
    app.include_router(parts_router)
    app.include_router(other_accessories_router)

    return app
