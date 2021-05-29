import motor.motor_asyncio
from bson.objectid import ObjectId
import os



client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGO_DETAILS"))

database = client[os.getenv("DATABASE")]

anime_collection = database.get_collection(os.getenv("COLLECTION"))


def anime_helper(anime) -> dict:
    return {
        "id":  anime["id"],
        "title":  anime["title"],
        "main_picture":  anime["main_picture"],
        "genres":  anime["genres"],
        "num_episodes":  anime["num_episodes"],
        "popularity":  anime["popularity"],
        "rank":  anime["rank"],
        "status":  anime["status"],
        "studios":  anime["studios"],
        "synopsis":  anime["synopsis"],
        "start_date":  anime["start_date"],
        "end_date":  anime["end_date"] if "end_date" in anime.keys() else None,
    }

async def retrieve_animes():
    animes = []
    async for anime in anime_collection.find():
        animes.append(anime_helper(anime))
    return animes


# Add a new anime into to the database
async def add_anime(anime_data: dict) -> dict:
    anime = await anime_collection.insert_one(anime_data)
    new_anime = await anime_collection.find_one({"_id": anime.inserted_id})
    return anime_helper(new_anime)


# Retrieve a anime with a matching ID
async def retrieve_anime(id: str) -> dict:
    anime = await anime_collection.find_one({"_id": ObjectId(id)})
    if anime:
        return anime_helper(anime)


# Update a anime with a matching ID
async def update_anime(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    anime = await anime_collection.find_one({"_id": ObjectId(id)})
    if anime:
        updated_anime = await anime_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_anime:
            return True
        return False


# Delete a anime from the database
async def delete_anime(id: str):
    anime = await anime_collection.find_one({"_id": ObjectId(id)})
    if anime:
        await anime_collection.delete_one({"_id": ObjectId(id)})
        return True