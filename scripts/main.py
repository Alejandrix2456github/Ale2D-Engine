# main.py

class Mod:
    def __init__(self, game):
        self.game = game
        self.name = "Example Mod"
        self.version = "1.0"
        self.author = "TuNombre"

    def initialize(self):
        print(f"{self.name} v{self.version} by {self.author} is initializing...")
        # Aquí puedes agregar cualquier lógica de inicialización del mod
        self.add_custom_entity()

    def add_custom_entity(self):
        # Ejemplo de cómo agregar una entidad personalizada al juego
        custom_entity = {
            "name": "CustomEntity",
            "type": "NPC",
            "position": (100, 200),
            "sprite": "C:/users/aleja/Documents/OneDrive/Escritorio/Ale2D/assets/sprite.png"
        }
        self.game.add_entity(custom_entity)
        print(f"Custom entity {custom_entity['name']} added to the game.")

# Función principal para cargar el mod
def load_mod(game):
    mod = Mod(game)
    mod.initialize()
    return mod

# Ejemplo de uso
if __name__ == "__main__":
    # Supongamos que 'game' es una instancia de tu motor de juego
    game = None  # Reemplaza esto con la instancia real de tu motor de juego
    load_mod(game)
