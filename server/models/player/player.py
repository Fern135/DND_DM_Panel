from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'

    id                 = Column(Integer, primary_key=True, autoincrement=True)
    pin                = Column(float) # login
    name               = Column(String, nullable=False)
    race               = Column(String)
    class_             = Column(String)
    level              = Column(Integer, default=1)
    alignment          = Column(String)
    background         = Column(String)
    experience_points  = Column(Integer, default=0)
    hit_points         = Column(Integer, default=10)
    profile_picture    = Column(String)  # Store file path or URL for profile picture
    character_picture  = Column(String)  # Store file path or URL for character picture

    # Class variable for the SQLAlchemy session
    _session = None

    def __repr__(self):
        return f"<Player(id={self.id}, name={self.name}, class_={self.class_}, level={self.level})>"

#     @classmethod
#     def create_database(cls, db_location='sqlite:///example.db'):
#         # Create the engine and bind the session to the class
#         engine = create_engine(db_location, echo=True)
#         cls._session = sessionmaker(bind=engine)

#         # Create the table in the database
#         Base.metadata.create_all(engine)

#     @classmethod
#     def add_player(cls, player_data):
#         # Example: Adding a player to the database
#         new_player = cls(**player_data)
#         cls._session.add(new_player)
#         cls._session.commit()

# if __name__ == '__main__':
#     # Specify the location for the database file
#     database_location = 'sqlite:///custom_location.db'

#     # Create the database and session
#     Player.create_database(db_location=database_location)

#     # Example: Adding a player to the database
#     player_data = {
#         'name': 'John Doe',
#         'race': 'Human',
#         'class_': 'Wizard',
#         'profile_picture': 'path/to/profile.jpg',
#         'character_picture': 'path/to/character.jpg'
#     }
#     Player.add_player(player_data)
