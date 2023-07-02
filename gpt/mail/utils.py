import json

def config(key) -> str:
    try:
        with open('gpt/config.json', 'r') as file:
            config = json.load(file)
        return (config[key])
    except FileNotFoundError:
        return ''