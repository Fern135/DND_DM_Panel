from fastapi import APIRouter

from ...conf.config.config import get_http_codes

playerRoutes = APIRouter()


@playerRoutes.post("/api/player/new_player")
async def new_player():
    return { "Server" : "New Player created"}


@playerRoutes.get("/api/players/player/<player_id>")
async def get_player_by_id(player_id: int):
    return { "Server" : f"getting player by id, id given {player_id}" }
