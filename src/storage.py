import json


def store_polygons(polygons):
    with open("api-data/polygons.json", "w") as file:
        file.write(json.dumps(polygons, indent=4))
