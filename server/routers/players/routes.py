from fastapi import APIRouter

from ...conf.config.config import Config

playerRoutes = APIRouter()

@playerRoutes.get("/api/players/player/<player_id>")
def say_hello(player_id: int):
    return { Config.db_return_title : f"getting player by id, id given {player_id}" }
