# Page Framework
## v.1.0
This is the initial version of Page Framework.
This version supports the usage of:
- console
- tkinter
- pygame
- *Your own models and files as long as you take the responsibility*
  
### Definitions and general information
- A field is a model that does a specific separate function.
- A form is a model that uses multiple fields
- An embedding is a general manager of an imported module or a dictionary
- Every field, form, page has a *call* method which is an entry, execution and exit method of class. In general only it is called upon execution
- Some fields or forms may have an *upd* method which is updater of the class that is executed on update tick.
- Some fields or forms may have *redraw* or *ignored* parameters. Those are if we want to redraaw the field/form on screen or ignore drawing

### models.py
This file is a collection of models for usage in projects made with python.

#### Error forms and functions
##### ErrorForm
This is the most basic form for errors/warnings(to console). If the type contains "WARNING" it will be treated differently
- *text*: This is the text of error/warning that gives the information
- *occurrence*: This is the page name where the error/warning occurred
- *type*(default "200 INPUT ERROR"): This is the type of error/warning

##### ErrorHelper
This is a helper for error form that checks if values adhere to their required types and outputs errors if they don't
- *argstrrep*: This is the list of string representations of values. Only those representations will be shown to the user
- *args*: This is the list of values to be checked
- *types*: This is the list of types for values being checked. If types[x] is a list then it will accept only if value is strictly ib list, else it will just check if type of value is the type here
- *ignore*(default True): This is the flag to ignore the abscence of page in what we are checking(else an error will be shown). It will set the page to undefined

##### ListErrorHelper
This is a helper for error form that checks if lists have same length and outputs error if they don't
- *lists*: This is the list of lists we are checking

##### InteractiveUserErrorForm
This is an error form for displaying on canvas
- *cne*: *CanvasEmbedding* that the error will be displayed on
- *canvas*: Canvas number that the error will be displayed on
- *element*: This is the element on Canvas to link the form to
- *text*: This is the text of error/warning that gives the information
- *occurrence*: This is the page name where the error/warning occurred
- *type*(default "200 INPUT ERROR"): This is the type of error/warning

#### Technical fields and other technical things
##### RedirectField
This field is used for redirecting to another page in program
- *target*: This is the class of target page for redirect
- *page*: This is the class of current page for redirect
- *program*: This is the instance of program inside which we are redirecting
- *ctx*(default {}): This is the in-page context that will be given to the call method of the page we are redirecting to. If {}, default context of that page will be used

##### Embedding
This is an embedding used to store multiple values
- *page*: This is the page name of the page the embedding is linked to
- *grouped*(default {}): This is the data we are grouping in the embedding

##### DummyPage
This is a dummy page used as a substitution for a real page in some cases. It has a name "dummy" and a call method which does nothing

##### DummyCmd
This is a dummy command that does nothing and accepts no arguments

##### DummyCmdArgs
This is a dummy command that accepts any amount of unspecified arguments and does nothing

##### check
- *val*: This is the value to check
- *req*: This is the required type of *val*
- *page*: This is the page name of the page the embedding is linked to
- *mini*: This is the minimum value(or length) for int, float, str types.
- *maxi*: This is the maximum value(or length) for int, float, str types.
- *dis*: Those are values that are accepted(all other values will ask for another input. If empty, accepts any value of *req* type
- *adv*(default False): This is flag for whether this is console mode(False) or canvas mode(True)
- *cne*(default None): This is the *CanvasEmbedding* embedding if the function is in the Advanced mode
- *canvas*(default None): This is the canvas number if the function is in the Advanced mode
- *element*(default None): This is the canvas element to which link and display the error if the function is in the Advanced mode

#### Console fields
##### TextField
This field is used for outputting text in console
- *text*: This is the text to be displayed
- *page*: This is the page name of the page the field is linked to
- *modifs*(default []):This is a list of text modificators such as "lo" - lowercase or "up" - uppercase
- *delim*(default 0): This is a delimiter from sides. In regular mode it draws *sign*s on sides of text
- *fancy*(default False): This is a "fancy mode" boolean. If true it will center text at center of *fancytotal* amount of *sign*s
- *fancytotal*(default 40): This is "fancy mode" signs amount. Text is centered at center of this amount
- *sign*(default "="): This is a character(characters) to use as a separator on sides of text

##### InputField
This field is used for requesting input from console
- *prompt*: This is your text to be displayed in console upon input request
- *name*: This is your name of the field
- *page*: This is the page name of the page the field is linked to
- *req*(default True): This is a boolean flag that marks if the field is required. If it isn't, the user can input nothing
- *inp_type*(default str): This is the input type of this field. Will notify user and ask for another input if input is wrong else will turn the input into specified type and return it.
- Only accepted types are str, float, int, bool
- *minimum*(default 0): This is the minimum value(or length) for int, float, str types. Will notify user and ask for another input if input is wrong else will return the input
- *maximum*(default 100): This is the maximum value(or length) for int, float, str types. Will notify user and ask for another input if input is wrong else will return the input
- *discretes*(default []): Those are values that are accepted(all other values will ask for another input. If empty, accepts any value of *inp_type* type

##### SpaceField
This field is used for drawing multiple of same character to console. Recommended for use on beginning and end of pages
- *sym*: This is the symbol to duplicate to console
- *amo*: This is the amount of duplications to make
- *page*: This is the page name of the page the field is linked to

#### Tkinter fields and embedding
##### CanvasEmbedding
This is an embedding for tkinter built-in module
- *page*: This is the page name of the page the field is linked to
- *name*: This is the name of window
- *width*: This is the width of window
- *height*: This is the height of window
- *program*: This is the program we are currently in
- *resizex*(default 0): This is how much the window is resizable on x-axis
- *resizey*(default 0): This is how much the window is resizable on y-axis
- *thick*(default 0): This is the thickness of the border of window
- *highlight_thick*(default 0): This is the highlight thickness of the border of window

**Methods**:
  - *NewWindow* - creates a new window. Accepts no parameters
  - *NewCanvas*(parameters: *window*) - creates a new canvas on a window. Accepts the number of a window(from 0)
  - *call* - updates all windows

##### ButtonField
This is a simplificator for a button on tkinter screen
- *canvas_embed*: *CanvasEmbedding* that the button will be displayed on
- *cmd*: Button command to execute
- *name*: Name of the field
- *canvas*: Canvas number that the button will be displayed on
- *background*(default "None"): Background color
- *foreground*(default "None"): Foreground color
- *anchor*(default "nw"): Anchor direction for the coordinates
- *x*(default 150): x position of the button
- *y*(default 100): y position of the button

##### ChoiceForm
This is a simplificator for multiple buttons at same distance on tkinter screen
- *canvas_embed*: *CanvasEmbedding* that the buttons will be displayed on
- *choicecmds*: Button commands to execute
- *choicenames*: Name of the field
- *canvas*: Canvas number that the buttons will be displayed on
- *backgrounds*(default []): Background colors 
- *foreground*(default []): Foreground colors
- *anchor*(default "nw"): Anchor direction for the coordinates
- *x*(default 150): x begin position for the buttons
- *y*(default 100): y begin position for the buttons
- *distance*(default 30): Distance between the buttons

##### TextFieldAdv
This is an advanced text field for canvas
- *canvas_embed*: *CanvasEmbedding* that the text will be displayed on
- *text*: text to display
- *canvas*: Canvas number that the text will be displayed on
- *x*: x begin position of text
- *y*: y begin position of text
- *font_color*(default "black"): color of font
- *font_type*(default "Times"): type of font
- *font_size*(default 15): size of font
- *anchor*(default "nw"): Anchor direction for the coordinates
 
##### ImageField
This is an image field for canvas
- *canvas_embed*: *CanvasEmbedding* that the image will be displayed on
- *x*: x begin position of image
- *y*: y begin position of image
- *canvas*: Canvas number that the image will be displayed on
- *img*(default "./uploads/example.png"): Link to image to display
- *anchor*(default "nw"): Anchor direction for the coordinates

##### BackgroundForm
This is a form for covering canvas with tiled images
- *canvas_embed*: *CanvasEmbedding* that the background will be displayed on
- *beginx*: x begin position of background
- *beginy*: y begin position of background
- *copyx*: copies on x-axis
- *copyy*: copies on y-axis
- *canvas*: Canvas number that the image will be displayed on
- *img*(default "./uploads/example.png"): Link to image to tile
- *anchor*(default "nw"): Anchor direction for the coordinates

##### GeometryField
This is a field for displaying geometry figures on canvas
- *canvas_embed*: *CanvasEmbedding* that the geometry figure will be displayed on
- *xs*: x positions of figure
- *ys*: y positions of figure
- *canvas*: Canvas number that the figure will be displayed on
- *extent*(default 180): Extent of arc(if type is arc)
- *bd*(default 1): Border width
- *outline*(default "black"): Color of border/outline
- *fill*(default ""): Fill color
- *typea*(default "arc"): Type of figure

##### InputForm
This is a form for inputting things on canvas
- *canvas_embed*: *CanvasEmbedding* that the form will be displayed on
- *width*: Width of input space
- *x*: x begin position of form
- *y*: y begin position of form
- *canvas*: Canvas number that the figure will be displayed on
- *prompt*: This is your text to be displayed in window upon input request
- *anchor*(default "nw"): Anchor direction for the coordinates
- *type_req*(default str): This is the input type of this field. Will notify user and ask for another input if input is wrong else will turn the input into specified type and return it.
- Only accepted types are str, float, int, bool
- *minimum*(default 0): This is the minimum value(or length) for int, float, str types. Will notify user and ask for another input if input is wrong else will return the input
- *maximum*(default 100): This is the maximum value(or length) for int, float, str types. Will notify user and ask for another input if input is wrong else will return the input
- *discretes*(default []): Those are values that are accepted(all other values will ask for another input. If empty, accepts any value of *inp_type* type

**Methods**:
- *get* - gets and returns the value input by user

##### Container
This is a container for grouping forms or fields on canvas
- *canvas_embed*: *CanvasEmbedding* that the container will be displayed on
- *beginx*: x begin position of the container
- *beginy*: y begin position of the container
- *endx*: x end position of the container
- *canvas*: Canvas number that the button will be displayed on
- *fields*(default []): Fields to group
- *height*(default 40): Distance between fields
- *pos*(default "center"): Position of elements("begin", "center" or "end")

**Methods**:
- *get_pos*(parameters: *fld2*) - gets and returns the pos of field/form *fld2* if it is inside container else doesn't return anything

#### Pygame fields and embedding
##### PygameEmbedding
This is an embedding for pygame built-in module. It creates a window on initialization.
*Special*: Set exit=False to close window
- *width*: Width of screen
- *height*: Height of screen
- *name*: Name(title) of screen
- *page*: Page we are currently on
- *color*(default (230, 230, 230)): tuple indicating color to use on background

**Methods**
- *link*(parameters: *sprite*) - link ImageSprite to be displayed in window
- *linkbtn*(parameters: *sprite*) - link ButtonFieldAdv to be displayed in window
- *linkkey*(parameters: *keypress*) - link ButtonPressField for window to react to
- *register_keys*(parameters: *btns*) - link all ButtonPressFields in a list for window to react to
- *setup*(parameters: *exec_before_flip*(default *DummyCmd*), *ticks*(default *DummyCmd*), *before_imgs*(default *DummyCmd*), *custom_event_checker*(default *DummyCmdArgs*)) - link hooks for custom logic. exec_before_flip - executed after all standard drawing immediately before flipping to next screen. ticks - executed after link checker, before standard logic(for example, for pygame clock). before_imgs - executed after drawing buttons, before drawing sprites. custom_event_checker - called in event checking loop. Must accept one argument - event.

##### ImageSprite
This is a sprite to move in pygame window
- *embed*: *PygameEmbedding* that the sprite will be displayed on
- *center*: tuple (x,y) for center position of sprite
- *imgpath*: Link to image to display

**Methods**
- *call* - show the sprite(blit)
- *upd* - update the sprite
- *toggle_move*(parameters: *pix*, *dire*) - dire must be "left", "right", "up" or "down*. Start moving sprite(on next update) in direction dire with speed pix pixels/tick

##### ButtonPressField
This is keyboard keypress detection class
- *key*: Key ID to link to(pygame key)
- *cmd*: Function to execute on key press
- *cmdr*(default *DummyCmd*): Function to execute on key release 
- *continuous*(default True): whether to report keypress when key is being held down continuously or only on the exact time of key press/release

#### ButtonFieldAdv
This is a button for Pygame
- *embed*: *PygameEmbedding* that the button will be displayed on
- *text*: Text to display on the button
- *width*: Width of the button
- *height*: Height of the button
- *begin_x*: Begin(topleft) x position of button
- *begin_y*: Begin(topleft) y position of button
- *on_click*: Function to execute on button click
- *color*(default (150,150,200)): Color of button
- *text_color*(default (255,255,255)): Color of button text
- *fonttype*(default None): Font type for text on button
- *fontsize*(default 48): Font size for text on button
- *begin_state*(default 0): Beginning state of button(0 - on, 1 - disabled(cannot press but can see), 2 - off)

**Methods**
- *_prep_msg*(parameters: *msg*) - prepare message for display. Internal
- *change_text*(parameters: *nxt*) - change text on message to nxt
- *call* - show the button(blit)
- *upd* - update the button also includes click events
- *disable* - disable the button(disabled)
- *enable* - enable button(on)
- *off* - hide button(off)

### program.py
This file is the framework manager. It manages your pages and objects on them

#### DummyPage
Look DummyPage in models.py/Technical fields and other technical things

#### Singleton
This is a singleton metaclass. It manages creating singletons(such as Games). It also makes all variables from *on_begin* method of said class(if such method exists) available globally

#### Game
This is a class for games or views. You should make a class that follows from game. If it has *on_begin*, it will make all valriables defined there with self. global. Otherwise it is just container for your functions which can be accessed anytime with YourGameClass().YourFunction(params)

#### Program
- *ps*: This is the page the program execution starts on. It should be defined before program and should redirect to actual first page
- *pctx*: This is the initial page context for the first(*ps*) page.
- *pcs*: This is the class of the initial(*ps*) page.
- *vpgs*: This is the list of valid pages(pages that can be redirected to or started on)
- *game*: This is your game class(should follow from Game)
- *pps*(default 25): This is pages per second your program will run. Used for delaying some pages
- *gfile*(default "g.json"): This is the file your globals will be saved to
- *globals*(default {}): This is your initial globals when there is nothing in file. You should manipulate program.globals["thing"] for storing in file and accessing data

**Methods**:
  - *run* - Runs the program from start(*ps*) to end(program.exit_now=True or pygameembedding.exit=True)
  - *gstore* - Stores the globals to file
  - *gload* - Loads the globals from file
  - *write_history*(parameters: *page*): Writes the page and context to history
  - *read_history*(parameters: *block_err*): Reads the last written context from history, if the history is empty it will output an error. Can be blocked if block_err is True.

### data.py
This file is a special database module that is made to store, upload and delete files and/or their contents. Works with .json files
