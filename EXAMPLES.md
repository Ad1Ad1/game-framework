# Examples for Page Framework(v1.0)

[View official API documentation](README.md)

## Example 01: Hello World!

from models import TextField, SpaceField, RedirectField
from program import Program, Game

class MyGame(Game):
	pass

class StartPage:
	name="start"
	def call(self, ctx={}):
		RedirectField(MainPage, StartPage, program).call()

program=Program("start", {}, StartPage, ["start", "main"], MyGame())

class MainPage:
	name="main"
	def call(self, ctx={}):
		space_field=SpaceField("=", 40, self.name)
		space_field.call()
		TextField("Hello World", self.name, fancy=True, sign=" ").call()
		space_field.call()
		program.exit_now=True

program.run()
