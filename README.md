# Page Framework
## v.1.0
This is the initial version of Page Framework.
This version supports the usage of:
- console
- tkinter
- pygame
- *Your own models and files as long as you take the responsibility*
  
### Definitions and general information
A field is a model that does a specific separate function.
A form is a model that uses multiple fields
Every field, form, page has a *call* method which is an entry, execution and exit method of class. In general only it is called upon execution
Some fields or forms may have an *upd* method which is updater of the class that is executed on update tick.

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

### program.py
This file is the framework manager. It manages your pages and objects on them

### data.py
This file is a special database module that is made to store, upload and delete files and/or their contents. Works with .json files
