# models/state.py
from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits from BaseModel."""
    name = ""

# models/city.py


class City(BaseModel):
    """City class that inherits from BaseModel."""
    state_id = ""
    name = ""

# models/amenity.py


class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel."""
    name = ""

# models/place.py


class Place(BaseModel):
    """Place class that inherits from BaseModel."""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

# models/review.py


class Review(BaseModel):
    """Review class that inherits from BaseModel."""
    place_id = ""
    user_id = ""
    text = ""
