import json


def extract(link):
    data = {}
    for i in link.split("?")[-1].split("&"):
        query, value = i.split("=")
        data[query] = value
    return json.dumps(data, indent=4)
