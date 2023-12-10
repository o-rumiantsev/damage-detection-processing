import json

import aiofiles


async def save(polygons):
    async with aiofiles.open("api-data/polygons.json", "w") as file:
        await file.write(json.dumps(polygons, indent=4))
