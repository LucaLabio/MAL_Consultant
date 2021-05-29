from typing import Optional
from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


class AnimeSchema(BaseModel):
    id: int = Field(...)
    title: str = Field(...)
    main_picture: dict = Field(...)
    genres: Optional[list] = None
    mean: Optional[float] = "0.0"
    num_episodes: Optional[int] = 0
    popularity: Optional[int] = 0
    rank: Optional[int] = 0
    status: Optional[str]
    studios: Optional[list] = None
    synopsis: Optional[str]
    start_date: str = Field(...)
    end_date: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                    "id": 5114,
                    "title": "John Doe",
                    "main_picture": {
                    "medium": "https://api-cdn.myanimelist.net/images/anime/1223/96541.jpg",
                    "large": "https://api-cdn.myanimelist.net/images/anime/1223/96541l.jpg"
                    },
                    "genres": [
                    {
                        "id": 1,
                        "name": "Action"
                    },
                    {
                        "id": 38,
                        "name": "Military"
                    }
                    ],
                    "mean": "9.17",
                    "num_episodes": 64,
                    "popularity": 3,
                    "rank": 1,
                    "status": "finished_airing",
                    "studios": [
                    {
                        "id": 4,
                        "name": "Bones"
                    }
                    ],
                    "synopsis": "\"In order for something to be obtained, something of equal value must be lost.\"\n\nAlchemy is bound by this Law of Equivalent Exchange—something the young brothers Edward and Alphonse Elric only realize after attempting human transmutation: the one forbidden act of alchemy. They pay a terrible price for their transgression—Edward loses his left leg, Alphonse his physical body. It is only by the desperate sacrifice of Edward's right arm that he is able to affix Alphonse's soul to a suit of armor. Devastated and alone, it is the hope that they would both eventually return to their original bodies that gives Edward the inspiration to obtain metal limbs called \"automail\" and become a state alchemist, the Fullmetal Alchemist.\n\nThree years of searching later, the brothers seek the Philosopher's Stone, a mythical relic that allows an alchemist to overcome the Law of Equivalent Exchange. Even with military allies Colonel Roy Mustang, Lieutenant Riza Hawkeye, and Lieutenant Colonel Maes Hughes on their side, the brothers find themselves caught up in a nationwide conspiracy that leads them not only to the true nature of the elusive Philosopher's Stone, but their country's murky history as well. In between finding a serial killer and racing against time, Edward and Alphonse must ask themselves if what they are doing will make them human again... or take away their humanity.\n\n[Written by MAL Rewrite]",
                    "start_date": "2009-04-05",
                    "end_date": "2010-07-04"
                }
            }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}