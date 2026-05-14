import requests

class PokemonClient:
    BASE_URL = "https://pokeapi.co/api/v2/pokemon"

    def get_pokemon(self, name):
        try:
            response = requests.get(f"{self.BASE_URL}/{name.lower()}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return None

class Pokemon:
    def __init__(self, data):
        self.name = data.get("name", "Unknown").capitalize()
        self.id = data.get("id", 0)
        self.types = [t["type"]["name"] for t in data.get("types", [])]

    def display(self):
        print(f"--- Pokemon Info ---")
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Types: {', '.join(self.types)}")

client = PokemonClient()
data = client.get_pokemon("pikachu")

if data:
    pokemon = Pokemon(data)
    pokemon.display()
else:
    print("Pokemon not found.")