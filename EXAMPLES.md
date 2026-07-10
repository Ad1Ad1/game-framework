# Examples for Page Framework(v1.0)

## Useful links

[View official API documentation](README.md)

[View official Quick Start page](QUICK_START.md)

## Example 01: Hello World!

```python
from framework_lib import models, program
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
from framework_lib import models, program
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
from framework_lib import models, program
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

## Example 04: Contained

```python
from framework_lib import models, program
from models import CanvasEmbedding, RedirectField, ButtonField, TextField, TextFieldAdv, Container
from program import Program, Game

class MyGame(Game):
	def on_begin(self):
		self.global0="Hello"

	def hello_from_button():
		print("Hello!")


class StartPage:
	name="start"
	def call(self, ctx={}):
		RedirectField(MainPage, StartPage, program).call()

program=Program("start", {}, StartPage, ["start", "main"], MyGame())

example_embedding=CanvasEmbedding("main", "Example Canvas", 300, 300, program)
example_embedding.NewWindow()
example_embedding.NewCanvas(0)
example_embedding.call()
example_text_field=TextFieldAdv(example_embedding, f"{global0} World!", 0, 0, 0)
example_button_field=ButtonField(example_embedding, MyGame.hello_from_button, "Greet", 0)
example_container=Container(example_embedding, 100, 100, 200, 0, [example_text_field, example_button_field])
example_container.call()

class MainPage:
	name="main"
	config="pgwin"
	def call(self, ctx={}):
		example_embedding.call()

program.run()
```

## Example 05: Hello Pygame World!

```python
from framework_lib import models, program
from models import PygameEmbedding, RedirectField, TextFieldExp
from program import Program, Game

class MyGame(Game):
	def on_begin(self):
		self.example_embedding=PygameEmbedding(500, 500, "Example Window", "main")
		self.example_text=TextFieldExp(self.example_embedding, "Hello Pygame World!", 100, 200, text_color=(255, 255, 0))


class StartPage:
	name="start"
	def call(self, ctx={}):
		RedirectField(MainPage, StartPage, program).call()

program=Program("start", {}, StartPage, ["start", "main"], MyGame())

class MainPage:
	name="main"
	config=("scene", example_embedding)
	def call(self, ctx={}):
		example_text.call()


program.run()
```

## Example 06: Pages

```python
from framework_lib import models, program
from models import PygameEmbedding, RedirectField, TextFieldExp, ButtonFieldAdv
from program import Program, Game

class MyGame(Game):
	def on_begin(self):
		self.example_embedding=PygameEmbedding(500, 500, "Example Window", "main")
		self.example_text=TextFieldExp(self.example_embedding, "Hello Main World!", 100, 200, text_color=(255, 255, 0))
		self.example_button=ButtonFieldAdv(self.example_embedding, "Switch to OtherPage", 300, 50, 100, 300, self.switch_other, fontsize=24)
		self.example_embedding.linkbtn(self.example_button)

	def switch_other(self):
		if program.control=="main":
			example_button.change_text("Switch to MainPage")
			example_text.change_text("Hello Other World!")
			RedirectField(OtherPage,MainPage,program).call()
		else:
			example_button.change_text("Switch to OtherPage")
			example_text.change_text("Hello Main World!")
			RedirectField(MainPage,OtherPage,program).call()

class StartPage:
	name="start"
	def call(self, ctx={}):
		RedirectField(MainPage, StartPage, program).call()

program=Program("start", {}, StartPage, ["start", "main", "other"], MyGame())

class MainPage:
	name="main"
	config=("scene", example_embedding)
	def call(self, ctx={}):
		example_text.call()

class OtherPage:
	name="other"
	config=("scene", example_embedding)
	def call(self, ctx={}):
		example_text.call()

program.run()
```

## Example 07: Group Control

```python
from framework_lib import models, program
from models import PygameEmbedding, RedirectField, TextFieldExp, ButtonFieldAdv, PygameObjectGroup
from program import Program, Game

class MyGame(Game):
	def on_begin(self):
		self.example_embedding=PygameEmbedding(500, 500, "Example Window", "main")
		self.example_text=TextFieldExp(self.example_embedding, "Hello Main World!", 100, 200, text_color=(255, 255, 0))
		self.example_text_2=TextFieldExp(self.example_embedding, "Group control example text", 100, 100, text_color=(0,255,255), fontsize=24)
		self.example_button=ButtonFieldAdv(self.example_embedding, "Switch to OtherPage", 300, 50, 100, 300, self.switch_other, fontsize=24)
		self.example_embedding.linkbtn(self.example_button)
		self.example_group=PygameObjectGroup(self.example_embedding, [self.example_text, self.example_text_2])

	def switch_other(self):
		if program.control=="main":
			example_button.change_text("Switch to MainPage")
			example_group.off_all()
			RedirectField(OtherPage,MainPage,program).call()
		else:
			example_button.change_text("Switch to OtherPage")
			example_group.on_all()
			RedirectField(MainPage,OtherPage,program).call()

class StartPage:
	name="start"
	def call(self, ctx={}):
		RedirectField(MainPage, StartPage, program).call()

program=Program("start", {}, StartPage, ["start", "main", "other"], MyGame())

class MainPage:
	name="main"
	config=("scene", example_embedding)
	def call(self, ctx={}):
		example_group.call()

class OtherPage:
	name="other"
	config=("scene", example_embedding)
	def call(self, ctx={}):
		example_group.call()

program.run()
```

## Example 08: Hooks

```python
from framework_lib import models, program
from models import PygameEmbedding, RedirectField, TextFieldExp, ButtonFieldAdv, PygameObjectGroup, pygame
from program import Program, Game

class MyGame(Game):
	def on_begin(self):
		self.example_embedding=PygameEmbedding(500, 500, "Example Window", "main")
		self.example_text=TextFieldExp(self.example_embedding, "Hello Main World!", 100, 200, text_color=(255, 255, 0))
		self.example_text_2=TextFieldExp(self.example_embedding, "Group control example text", 100, 100, text_color=(0,255,255), fontsize=24)
		self.example_button=ButtonFieldAdv(self.example_embedding, "Switch to OtherPage", 300, 50, 100, 300, self.switch_other, fontsize=24)
		self.example_embedding.linkbtn(self.example_button)
		self.example_group=PygameObjectGroup(self.example_embedding, [self.example_text, self.example_text_2])
		self.example_embedding.setup(custom_event_checker=self.example_event_checker)

	def switch_other(self):
		if program.control=="main":
			example_button.change_text("Switch to MainPage")
			example_group.off_all()
			RedirectField(OtherPage,MainPage,program).call()
		else:
			example_button.change_text("Switch to OtherPage")
			example_group.on_all()
			RedirectField(MainPage,OtherPage,program).call()

	def example_event_checker(self, event):
		if event.type==pygame.MOUSEMOTION:
			print("A hook for you!")

class StartPage:
	name="start"
	def call(self, ctx={}):
		RedirectField(MainPage, StartPage, program).call()

program=Program("start", {}, StartPage, ["start", "main", "other"], MyGame())

class MainPage:
	name="main"
	config=("scene", example_embedding)
	def call(self, ctx={}):
		example_group.call()

class OtherPage:
	name="other"
	config=("scene", example_embedding)
	def call(self, ctx={}):
		example_group.call()

program.run()
```
