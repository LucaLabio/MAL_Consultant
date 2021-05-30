from server.routes.anime import router as AnimeRouter
from dotenv import load_dotenv
from bson.json_util import dumps
from server.database import *
from fastapi import FastAPI
import requests
import pymongo
import json
import re
import os

load_dotenv()

app = FastAPI()

app.include_router(AnimeRouter, tags=["Controller"], prefix="/Controller")

@app.get("/", tags=["Root"])
def hello():
    return {"Hello":"World"}

@app.get("/{id}", tags=["Anime Info"])
async def get_anime_info(id):
    try:
        myquery = { "id": int(id) }

        mydoc = await anime_collection.find_one(myquery,{'_id': False })


        if mydoc:
            return json.loads(dumps(mydoc))
        else:
            print("deu errado")
            response = requests.get(
                f'https://api.myanimelist.net/v2/anime/{id}',
                params={'fields': 'genres,mean,num_episodes,popularity,rank,status,studios,synopsis,start_date,end_date'},
                headers={'Authorization': os.getenv("TOKEN")},
            )
            
            await anime_collection.insert_one(anime_helper(response.json()))

            return response.json()
    except Exception as e:
        return {"message":"Nao foi possivel encontrar um anime com o ID especificado"}

@app.get("/name/{name}", tags=["Anime Info"])
async def get_anime_info_by_name(name):
    regx = re.compile(f"^{name}", re.IGNORECASE)

    myquery = {"title":regx}

    mydoc = await anime_collection.find(myquery,{'_id': False }).to_list(length=20)

    if mydoc:
        return mydoc
    else:
        return {"message":f"Nao foram encontrados animes com o nome {name} no banco de dados"}
        
@app.on_event("shutdown")
def shutdown_event():
    print("connection closed")
    client.close()