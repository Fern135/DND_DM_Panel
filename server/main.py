from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import os

# config
from conf.config.config import DEBUG, HOST, API_PORT

# models
from .models.player.player import Player  

# routes
from .routers.players.routes import playerRoutes

app = FastAPI()

# CORS (Cross-Origin Resource Sharing) middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development; modify for production
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Get the absolute path to the desired folder
db_path = './db/'

# Specify the location for the database file in the specified folder
database_location = f'sqlite:///{os.path.join(db_path, "dnd_dm_panel.db")}'

engine = create_engine(database_location, echo=True)
Player._session = sessionmaker(bind=engine)

# Create the table in the database
Player.metadata.create_all(engine)

# Include routers
app.include_router(playerRoutes)

@app.get("/") # root
def read_root():
    return {"SERVER": "Online!!!"}

def runner(debug):
    import uvicorn
    uvicorn.run(
        "main:app",
        host=HOST,
        port=API_PORT,
        reload=debug
    )

def run():  # running the server
    match DEBUG:
        case True:
            runner(True)  # auto reload
        case _:
            runner(False)

# if __name__ == "__main__":
#     run()
