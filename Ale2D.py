import arcade

# Constantes para el movimiento del jugador
MOVEMENT_SPEED = 5

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.player_x = 400
        self.player_y = 300
        self.change_x = 0
        self.change_y = 0

    def on_show(self):
        arcade.set_background_color(arcade.color.GREEN)

    def on_draw(self):
        self.clear()
        arcade.draw_triangle_filled(self.player_x, self.player_y + 25,
                                    self.player_x - 25, self.player_y - 25,
                                    self.player_x + 25, self.player_y - 25,
                                    arcade.color.BLUE)

    def on_key_press(self, key, _):
        if key == arcade.key.ESCAPE:
            arcade.close_window()
        elif key == arcade.key.W or key == arcade.key.UP:
            self.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S or key == arcade.key.DOWN:
            self.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.A or key == arcade.key.LEFT:
            self.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D or key == arcade.key.RIGHT:
            self.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, _):
        if key in [arcade.key.W, arcade.key.UP, arcade.key.S, arcade.key.DOWN]:
            self.change_y = 0
        elif key in [arcade.key.A, arcade.key.LEFT, arcade.key.D, arcade.key.RIGHT]:
            self.change_x = 0

    def on_update(self, _):
        self.player_x += self.change_x
        self.player_y += self.change_y

def main():
    window = arcade.Window(800, 600, "Ale2D Game Engine")
    game_view = GameView()
    window.show_view(game_view)
    arcade.run()

if __name__ == "__main__":
    main()
