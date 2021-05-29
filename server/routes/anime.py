from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from server.database import (
    add_anime,
    delete_anime,
    retrieve_anime,
    retrieve_animes,
    update_anime,
)
from server.models.anime import (
    ErrorResponseModel,
    ResponseModel,
    AnimeSchema,
)
router = APIRouter()