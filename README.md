<div align=center><h1> MAL Consultant</h1></div>
<h3 align=center>Simple API that uses the basic search route from MyAnimeList API</h3>
<h4>Requesting for a anime by id</h4>

|property|description|
|---|---|
|**URL** | `/{id}`|
|**Method** | `GET`|

**Request**: First it looks into the database to see if the requested id mathes a previusly registered anime, if it doesn't, then a request onto MAL API is made

|field|description|
|---|---|
|**id** | `anime id on MyAnimeList`|
|**title** | `anime name`|
|**genres** | `list with every genre`|
|**mean** | `Overall score on MyAnimeList`|
|**num_episodes** | `total episodes`
|**popularity** | `Popularity ranking on MAL`|
|**rank** | `Overall score ranking on MAL`|
|**status** | `wheather it is still airing, if it's finished or not yet aired`|
|**studios** | `List of studios`|
|**synopsis** | `anime synopsis`|
|**start_date** | `When it started airing`|
|**end_date** | `When it stopped airing (optional)`|

<h4>Requesting for a anime by name</h4>

|property|description|
|---|---|
|**URL** | `/name/{name}`|
|**Method** | `GET`|

**Request**: Look for the specific name on mongo database, then returns every match (if found any)

|field|description|
|---|---|
|**Array** | `Returns a list with every anime found that matches provided name`|
