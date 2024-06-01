from app import App

class HelloWorld(App):
  def __init__(self):
    pass

  def update(self, delta):
    pass

  def draw(self, ctx):
    ctx.move_to(0, 0).text("I'm Richard!")

__app_export__ = HelloWorld
