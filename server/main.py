from conf.config.config import DEBUG, HOST, API_PORT

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from routers.players import routes

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
app.include_router(routes.playerRoutes)

@app.get("/")
def read_root():
    return { "SERVER": "Online!!!" }


def runner(debug):
    import uvicorn
    uvicorn.run(
        "main:app", 
        host=HOST, 
        port=API_PORT, 
        reload=debug
    )

def run(): # running the server
    match DEBUG:
        case True:
            runner(True) # auto reload
        case _:
            runner(False)


# if __name__ == "__main__":
#     run()