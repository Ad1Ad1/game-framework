# Examples for Page Framework(v1.0)

## Useful links

[View official API documentation](README.md)

## Example 01: Hello World!

```python
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
```

## Example 02: A button on a screen

```python
from models import CanvasEmbedding, RedirectField, ButtonField, TextField
from program import Program, Game

class MyGame(Game):
	pass

class StartPage:
	name="start"
	def call(self, ctx={}):
		RedirectField(MainPage, StartPage, program).call()

def hello_from_button():
	TextField("Hello World!", "main").call()

program=Program("start", {}, StartPage, ["start", "main"], MyGame())
example_embedding=CanvasEmbedding("main", "Example Canvas", 300, 300, program)
example_embedding.NewWindow()
example_embedding.NewCanvas(0)
example_embedding.call()
example_button_field=ButtonField(example_embedding, hello_from_button, "Greet", 0)
example_button_field.call()

class MainPage:
	name="main"
	config="pgwin"
	def call(self, ctx={}):
		example_embedding.call()

program.run()
```

## Example 03: A button on a screen, structured
*Note: on_begin inserts into global variables*

```python
from models import CanvasEmbedding, RedirectField, ButtonField, TextField
from program import Program, Game

class MyGame(Game):
	def on_begin(self):
		self.global0="Hello"

	def hello_from_button():
		TextField(f"{global0} World!", "main").call()


class StartPage:
	name="start"
	def call(self, ctx={}):
		RedirectField(MainPage, StartPage, program).call()

program=Program("start", {}, StartPage, ["start", "main"], MyGame())

example_embedding=CanvasEmbedding("main", "Example Canvas", 300, 300, program)
example_embedding.NewWindow()
example_embedding.NewCanvas(0)
example_embedding.call()
example_button_field=ButtonField(example_embedding, MyGame.hello_from_button, "Greet", 0)
example_button_field.call()

class MainPage:
	name="main"
	config="pgwin"
	def call(self, ctx={}):
		example_embedding.call()

program.run()
```
