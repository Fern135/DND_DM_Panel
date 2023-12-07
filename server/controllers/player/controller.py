from ...models.player import Player
from lib.util.util import util

class PlayerController(util):

    def __init__(self) -> None:
        self.temp_pin           = self.generate_random_string(8)
        self.temp_psw           = self.generate_random_string(16)
        self.pin                = None
        self.name               = None
        self.race               = None
        self.class_             = None
        self.level              = None
        self.alignment          = None
        self.background         = None
        self.xp_points          = None
        self.hit_points         = None
        self.profile_picture    = None  # Store file path or URL for profile picture
        self.character_picture  = None  # Store file path or URL for character picture


    def setData(self, data:dict) -> None:
        """Set the player's information"""
        if data is not None:
            self.pin         = data['pin']
            self.name        = data['name']
            self.race        = data['race']
            self.class_      = data['class']
            self.level       = data['level']
            self.alignment   = data['alignment']
            self.background  = data['background']
            self.xp_points   = data['xp_points']
            self.hit_points  = data['hit_points']

            # figure out how to handle with
            self.profile_picture    = data['profile_picture']
            self.character_picture  = data['character_picture']

    
    def new_player(self) -> bool:
        """Create a new player and save in database"""
        
        return self

    def get(self, id) -> dict:
        """Get player by ID"""

        return self
    
    def get_all(self) -> dict:
        """Get all players"""

        return self