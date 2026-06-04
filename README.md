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
- *maximum*(default 0): This is the maximum value(or length) for int, float, str types. Will notify user and ask for another input if input is wrong else will return the input
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

### program.py
This file is the framework manager. It manages your pages and objects on them

#### DummyPage
Look DummyPage in models.py

#### Singleton
This is a singleton metaclass. It manages creating singletons(such as Games). It also makes all variables from *on_begin* method of said class available globally

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
