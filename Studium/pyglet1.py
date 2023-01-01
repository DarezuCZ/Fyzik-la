import pyglet
window = pyglet.window.Window()

def napis_text(text):
    print('KUNDOOOOOOOOOOOOO!!!!!')

window.push_handlers(on_text=napis_text)


pyglet.app.run()