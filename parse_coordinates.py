import csv
import json

coordinate_json = []
with open("travis_county.tsv") as fd:
    rd = csv.reader(fd, delimiter="\t")
    for row in rd:
        lng = float(row[0])
        lat = float(row[1])
        coordinate_json .append({"lat": lat, "lng": lng})

with open("travis_county_1.json", "w") as f:
    json.dump(coordinate_json, f)
