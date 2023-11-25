from fastapi import APIRouter

from ...conf.config.config import get_http_codes
from ...lib.util.util import util

playerRoutes = APIRouter()

ut = util()
new_player_id = ut.generate_random_string(256)

@playerRoutes.post("/api/player/new_player")
async def new_player():
    return { "Server" : f"New Player created with id {new_player_id}"}


@playerRoutes.get("/api/players/player/<player_id>")
async def get_player_by_id(player_id: int):
    return { "Server" : f"getting player by id, id given {player_id}" }
