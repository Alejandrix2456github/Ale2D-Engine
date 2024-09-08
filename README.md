# Ale2D Mod Loader

Este es un mod loader para el Ale2D Game Engine. Permite cargar y gestionar mods escritos en Python.

## Estructura del Proyecto
Ale2DGameEngine/ ├── mods/ │ ├── Mod1/ │ │ ├── assets/ │ │ │ ├── images/ │ │ │ ├── sounds/ │ │ ├── scripts/ │ │ │ ├── main.py │ │ ├── config.json

## Cómo Usar

1. Coloca tus mods en la carpeta `mods/`.
2. Cada mod debe tener la estructura descrita anteriormente.
3. Ejecuta el motor de juego para cargar los mods.

## Ejemplo de Mod

```python
# main.py

class Mod:
    def __init__(self, game):
        self.game = game
        self.name = "Example Mod"
        self.version = "1.0"
        self.author = "TuNombre"

    def initialize(self):
        print(f"{self.name} v{self.version} by {self.author} is initializing...")
        self.add_custom_entity()

    def add_custom_entity(self):
        custom_entity = {
            "name": "CustomEntity",
            "type": "NPC",
            "position": (100, 200),
            "sprite": "path/to/sprite.png"
        }
        self.game.add_entity(custom_entity)
        print(f"Custom entity {custom_entity['name']} added to the game.")

def load_mod(game):
    mod = Mod(game)
    mod.initialize()
    return mod
