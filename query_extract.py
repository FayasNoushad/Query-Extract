import json


def extract(link):
    data = {}
    for i in link.split("?")[-1].split("&"):
        query, value = i.split("=")
        data[query] = value
    return json.dumps(data, indent=4)


def stringify(data):
    strings = []
    for i in data:
        query, value = i, data[i]
        string += query + "+" + value
        strings.append(string)
    strings = "&".join(strings)
    return strings
