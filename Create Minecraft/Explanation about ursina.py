from ursina import *


class Test_cube(Entity):
    def __init__(self):
        super().__init__(
            model='cube',
            color=color.white,
            texture='white_cube',
            rotation=Vec3(45, 45, 45)
        )


class Test_button(Button):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='cube',
            texture='brick',
            color=color.blue,
            highlight_color=color.red,
            pressed_color=color.lime
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                print('button pressed')


def update():
    if held_keys['a']:
        test_square.x -= 4 * time.dt


app = Ursina()
sans_texture = load_texture('assets/sans.png')
test_square = Entity(model='quad', color=color.red, scale=(1, 4), position=(4, 2))
sans = Entity(model='quad', texture=sans_texture)

test_cube = Test_cube()
test_button = Test_button()

app.run()



