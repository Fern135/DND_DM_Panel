from fastapi import APIRouter

from ...conf.config.config import Config

playerRoutes = APIRouter()

@playerRoutes.post("/api/player/new_player")
def new_player():
    return { Config.db_return_title : "New Player created"}

@playerRoutes.get("/api/players/player/<player_id>")
def get_player_by_id(player_id: int):
    return { Config.db_return_title : f"getting player by id, id given {player_id}" }
