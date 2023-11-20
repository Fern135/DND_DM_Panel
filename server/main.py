from conf.config.config import Config

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

# from .routers import example

app = FastAPI()

# CORS (Cross-Origin Resource Sharing) middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development; modify for production
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Include routers
# app.include_router(example.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}


def run(): # running the server
    import uvicorn

    if Config.DEBUG == True:
        uvicorn.run(
            "main:app", 
            host=Config.host, 
            port=Config.PORT, 
            reload=True
        )

    else:
        uvicorn.run(
            "main:app", 
            host=Config.host, 
            port=Config.PORT, 
            reload=False
        )



# if __name__ == "__main__":
#     run()