from fastapi import APIRouter, HTTPException, Body
from fastapi.responses import JSONResponse

from ...conf.config.config import get_http_codes
from ...lib.util.util import util

playerRoutes = APIRouter()

ut = util()
new_player_id = ut.generate_random_string(256) # will save their "login" as a pin

@playerRoutes.post("/api/player/new_player")
async def new_player(data: dict = Body(...)):
    return JSONResponse( { "Server" : f"New Player created with id {new_player_id}"} )


@playerRoutes.get("/api/players/player/<player_id>")
async def get_player_by_id(player_id: int):
    return JSONResponse( { "Server" : f"getting player by id, id given {player_id}" } )


@playerRoutes.post("/api/players/player/")
async def new_char_sheet(data: dict = Body(...)):
    if data is None:
        return JSONResponse( { "Server" : "Body cannot be empty" } )
    

    # parse data into the controller
    pass