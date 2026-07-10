"""
DOCUMENTATION for models.py:

========================

GENERAL INFORMATION:

        - ErrorForm is used for raising errors without crashes and to be friendly
        
        - SpaceField, InputField, RedirectField, TextField: fields for your own models
        
        - ErrorHelper is used for automatical type error checks

        - ListErrorHelper is used for automatical list length checks
        
        - check is used for checking user errors related to InputField

        - Embedding is used for storing data about multiple fields and managing them

        - CanvasEmbedding is an embedding that is used for Tkinter

        - ImageField is used for displaying images with Tkinter

        - TextFieldAdv is used for displaying text with Tkinter

        - ButtonField is used for displaying button with Tkinter

        - InputForm is used for displaying input with Tkinter

        - BackgroundForm is used for displaying tiled images(e.g. backgrounds) with Tkinter

        - GeometryField is used for displaying geometric shapes with Tkinter

        - InteractiveUserErrorForm is used for displaying user errors with Tkinter

        - Container is used for containing multiple Tkinter fields/forms and positioning them

        - PygameEmbedding is an embedding that is used for Pygame

        - ImageSprite is used for displaying sprites from images in Pygame

        - ButtonPressField is used for commanding program what to do on specific key press events

        - ButtonFieldAdv is used for displaying buttons in Pygame

        - TextFieldExp is used for displaying text in Pygame
        

========================

VALUE INFORMATION:
        
        - page must be STR unless Redirect field where it must be class with self.name and self.call()
        
        - InputField's argument "type" supports only int, bool, str, float

========================
        
ERROR INFORMATION:
        
        - 1xx: Framework/developer fault - PREFIX
        
        - 2xx: User fault - PREFIX

        - 3xx: Developer fault - PREFIX

        - 4xx: Warning - PREFIX
        
        - 100 INTERNAL ERROR:
                Used by framework, raises when something within framework does not work.
                                
        - 101 REDIRECT ERROR:
                Used by framework, raises when page isn't valid(page in development, developer should setup VALID_PAGES to not raise this error).
        
        - 102 DATABASE ERROR:
                Used by framework (look in data.py), raises when database key does not exist or database is not found.

        - 103 NON-EXISTENT ERROR:
                Used by framework to indicate that something within framework does not exist

        - 104 IMAGE ERROR:
                Used by framework (look in data.py), raises when something is wrong with image

        - 105 INSTANCE ERROR:
                Used by framework, raises when an instance is invalid

        - 106 CALLABILITY ERROR:
                Used by framework, raises when an object has incorrect callability(can be called while shouldn't or can't be called while should)

        - 107 ARGUMENT ERROR:
                Used by framework when an object has incorrect signature

        - 108 SOUND ERROR:
                Used by framework, raises when something is wrong with sound
                
        - 200 INPUT ERROR:
                Used by framework AND by developer to show user they have entered incorrect input
        
        - 201 ACCESS ERROR:
                Used by developer to show user that they have tried to access something without respective permission(when creating pages)

        - 300 PAGE ERROR:
                Used by framework when page is non-existent, doesn't have name or .call() with ctx.

        - 301 PROGRAM ERROR:
                Used by framework(look in program.py) when program is non existent, doesn't have name, etc
                 
        - 302 HISTORY ERROR:
                Used by framework(look in program.py) when developer tries to access a history page which is unreachable

        - 303 CANVAS ERROR:
                Used by framework when developer tries to do something illegal with CanvasEmbedding

        - 304 GAME ERROR:
                Used by framework(look in program.py) when developer tries to do something illegal with Game

        - 400 EXIT WARNING:
                Used by framework(look in program.py) when developer or user tries to force-quit the program
"""

"""CODE"""
from inspect import signature as s
from math import floor, ceil
from tkinter import *
from time import sleep
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
import pygame.font
import sys
class ErrorForm:
        def __init__(self, text, occurrence, type="200 INPUT ERROR"):
                self.t=text
                self.o=occurrence
                self.ty=type
                self.w=""
                if "warning" not in self.ty.lower():
                        self.w=f"An error occurred on page {self.o}: "
        def call(self):
                SpaceField("=", 40, "ERRS").call()
                TextField(self.ty, "ERRS", fancy=True, fancytotal=40).call()
                TextField(f"{self.w}{self.t}", "ERRS",delim=0).call()
                SpaceField("=", 40, "ERRS").call()
                
class SpaceField:
                def __init__(self, sym, amo, page):
                        self.s=sym
                        self.a=amo
                        asr=["page", "symbol", "amount"]
                        args=[page, sym, amo]
                        types=[str, str, int]
                        self.c=ErrorHelper(asr, args, types)
                                
                def __str__(self):
                        return self.s*self.a
                        
                def call(self):
                        if self.c:
                                return 1
                        else:
                                print(self)
                        return 0
                        
def ErrorHelper(argstrrep, args, types, ignore=False):
        caller=True
        if type(argstrrep) is not list:
                ErrorForm(f"Invalid type for ErrorHelper argument 'argument string representation': {type(argstrrep).__name__}", "ERRHELP", type="100 INTERNAL ERROR").call()
                caller=False
        elif type(args) is not list:
                ErrorForm(f"Invalid type for ErrorHelper argument 'arguments': {type(args).__name__}", "ERRHELP", type="100 INTERNAL ERROR").call()
                caller=False
        elif type(types) is not list:
                ErrorForm(f"Invalid type for ErrorHelper argument 'types': {type(types).__name__}", "ERRHELP", type="100 INTERNAL ERROR").call()
                caller=False
        elif type(ignore) is not bool:
                ErrorForm(f"Invalid type for ErrorHelper argument 'ignore': {type(ignore).__name__}", "ERRHELP", type="100 INTERNAL ERROR").call()
                caller=False
        if caller:
                for x in range(0, len(argstrrep)):
                        if argstrrep[x]=="page" or ignore:
                                pfp="UNDEFINED"
                        else:
                                pfp=args[argstrrep.index("page")]
                        if type(types[x]) is list:
                                if args[x] not in types[x]:
                                        ErrorForm(f"Invalid type for argument '{argstrrep[x]}': {type(args[x]).__name__} not in {types[x]}", f"{pfp}", type="100 INTERNAL ERROR").call()
                                        caller=False
                                        break
                        elif not isinstance(args[x],types[x]):
                                ErrorForm(f"Invalid type for argument '{argstrrep[x]}': {type(args[x]).__name__}", f"{pfp}", type="100 INTERNAL ERROR").call()
                                caller=False
                                break
        return not caller

def ListErrorHelper(lists):
        caller=True
        for x in range(len(lists)):
                if type(lists[x]) is not list:
                        ErrorForm(f"Invalid type for ListErrorHelper argument 'lists[{x}]': {type(lists).__name__}", "ERRHELP", type="100 INTERNAL ERROR").call()
                        caller=False
        if caller:
                lens=[]
                for x in range(0, len(lists)):
                        lens.append(len(lists[x]))
                prev=lens[0]
                for x in range(1, len(lens)):
                        if prev==lens[x]:
                                prev=lens[x]
                        else:
                                ErrorForm(f"Invalid length for list 'lists[{x}]': {lens[x]}", "ERRHELP", type="100 INTERNAL ERROR").call()
                                caller=False
                                break
        return not caller

class TextField:
        def __init__(self, text, page, modifs=[], delim=0, fancy=False, fancytotal=40, sign="="):
                self.d=delim
                self.t=text
                self.m=modifs
                self.f=fancy
                self.ft=fancytotal
                asr=["page", "modifiers", "delimiter", "fancy", "fancytotal"]
                args=[page, modifs, delim, fancy, fancytotal]
                types=[str, list, int, bool, int]
                caller=ErrorHelper(asr, args, types)
                if self.ft<len(self.t) and not caller and self.f:
                        ErrorForm(f"Invalid amount for argument 'fancytotal': {self.ft} is less than length of text", page, type="100 INTERNAL ERROR").call()
                        caller=True
                self.s=sign
                self.p=page
                self.c=caller
                
        def __str__(self):
                if self.c:
                        return "ERR"
                out=""
                txt=self.t
                if self.f:
                        oka=self.s*floor((self.ft-len(self.t))/2)
                else:
                        oka=self.s*self.d
                out+=oka
                e=True
                for mod in self.m:
                        if mod.lower()=="up":
                                txt=txt.upper()
                        elif mod.lower()=="lo":
                                txt=txt.lower()
                        else:
                                ErrorForm(f"Unknown modifier {mod}", page, type="100 INTERNAL ERROR").call()
                                e=False
                                break
                if e:
                        out+=txt
                        if self.f:
                                oka=self.s*ceil((self.ft-len(self.t))/2)
                        else:
                                oka=self.s*self.d
                        out+=oka
                        return out
                else:
                        self.c=True
                        return "ERR"
                
        def call(self):
                val=self.__str__()
                if self.c:
                        return 1
                else:
                        print(val)
                return 0

class InputField:
        def __init__(self, prompt, name, page, req=True, inp_type=str, minimum=0, maximum=100, discretes=None):
                self.TYPES=[str, float, int, bool]
                self.p=page
                self.pr=prompt
                self.r=req
                self.n=name
                self.m=minimum
                self.ma=maximum
                self.t=inp_type
                self.d=discretes
                val=[]
                if discretes:
                        val=discretes
                asr=["page", "prompt", "required", "minimum","maximum", "discrete values"]
                args=[self.p, self.pr, self.r, self.m, self.ma, val]
                types=[str, str, bool, int, int, list]
                self.c=ErrorHelper(asr, args, types)
                if not self.c and inp_type not in self.TYPES:
                        ErrorForm(f"Type {inp_type} cannot be parsed", self.p, type="100 INTERNAL ERROR").call()
                        self.c=True
        def call(self):
                if self.c:
                        return "ERR"
                res=""
                if self.r:
                        bad=True
                        while res=="" or res==None or bad:
                                print(self.pr+"(field required):")
                                val=input()
                                if val=="" or val==None:
                                        ErrorForm(f"Field {self.n} is required", self.p).call()
                                else:
                                        res, bad=check(val, self.t, self.p, self.m, self.ma, self.d)
                else:
                        bad=True
                        while bad:
                                print(self.pr+":")
                                val=input()
                                res, bad=check(val, self.t, self.p, self.m, self.ma, self.d)
                return res

def check(val, req, page, mini, maxi, dis, adv=False, cne=None, canvas=None, element=None):
        res=val
        bad=False
        rk=False
        rk2=False
        def s(req, page, cne, canvas, element):
                if not adv:
                        ErrorForm(f"Wrong type: '{req}' type required", page).call()
                else:
                        InteractiveUserErrorForm(cne, canvas, element, f"Wrong type: '{req}' type required", page).call()
                return True
        def k(mini, page, cne, canvas, element):
                if not adv:
                        ErrorForm(f"Minimum limit is {mini}. Your input is not sufficiently large", page).call()
                else:
                        InteractiveUserErrorForm(cne, canvas, element, f"Minimum limit is {mini}. Your input is not sufficiently large", page).call()
        def u(maxi, page, cne, canvas, element):
                if not adv:
                        ErrorForm(f"Maximum limit is {maxi}. Your input is too large", page).call()
                else:
                        InteractiveUserErrorForm(cne, canvas, element, f"Maximum limit is {maxi}. Your input is too large", page).call()
        if req==bool:
                try:
                        if val.lower()=="true" or val=="1":
                                res=True
                        elif val.lower()=="false" or val=="0":
                                res=False
                        else:
                                raise ValueError()
                except:
                        bad=s("bool", page, cne, canvas, element)
        elif req==int:
                try:
                        res=int(val)
                        if res<mini:
                                rk=True
                        elif res>maxi:
                                rk2=True
                except:
                        bad=s("int", page, cne, canvas, element)
        elif req==str:
                try:
                        res=str(val)
                        if len(res)<mini:
                                rk=True
                        elif len(res)>maxi:
                                rk2=True
                except:
                        bad=s("str", page, cne, canvas, element)
        elif req==float:
                try:
                        res=float(val)
                        if res<mini:
                                rk=True
                        elif res>maxi:
                                rk2=True
                except:
                        bad=s("float", page, cne, canvas, element)
        if rk:
                k(mini, page, cne, canvas, element)
                bad=True
        elif rk2:
                u(maxi, page, cne, canvas, element)
                bad=True
        if dis and (req!=bool):
                if res not in dis and not bad:
                        distxt="Possible input values are: "
                        for di in dis:
                                distxt+=f"'{di}', "
                        distxt+=". You did not input one of them."
                        ErrorForm(distxt, page).call()
                        bad=True
        return res, bad
        
class RedirectField:
        def __init__(self, target, page, program, ctx={}):
                self.pr=program
                try:
                        self.t=target()
                        self.tc=target
                        self.p=page()
                except:
                        ErrorForm("Target or starter page class for redirect isn't a class","UNDEFINED", type="300 PAGE ERROR").call()
                        self.c=True
                        return
                self.ct=ctx
                err=False
                if not self.pr:
                        ErrorForm("Program isn't defined", "UNDEFINED", type="301 PROGRAM ERROR").call()
                        self.c=True
                        return
                else:
                        try:
                                if program.vpgs!=[]:
                                        VALID_PAGES=program.vpgs
                                else:
                                        raise ValueError()
                        except:
                                ErrorForm("Program doesn't have any valid pages", "UNDEFINED", type="301 PROGRAM ERROR").call()
                                self.c=True
                                return
                if not self.p:
                        ErrorForm("Starter page of redirect does not exist", "UNDEFINED", type="300 PAGE ERROR").call()
                        err=True
                else:
                        try:
                                if type(self.p.name)==str:
                                        pass
                                else:
                                        raise ValueError()
                        except:
                                ErrorForm("Starter page of redirect has an invalid name/type", "UNDEFINED", type="300 PAGE ERROR").call()
                                err=True
                if not err and (self.p.name not in VALID_PAGES):
                        ErrorForm(f"Page {self.p.name} is not a valid page for a redirect starter", self.p.name, type="101 REDIRECT ERROR").call()
                        err=True
                elif not self.t:
                        ErrorForm("Target page of redirect does not exist", self.p.name, type="300 PAGE ERROR").call()
                        err=True
                else:
                        try:
                                if type(self.t.name)==str:
                                        pass
                                else:
                                        raise ValueError()
                        except:
                                ErrorForm("Target page of redirect has an invalid name/type or it does not exist", self.p.name, type="300 PAGE ERROR").call()
                                err=True
                if not err and (self.t.name not in VALID_PAGES):
                        ErrorForm(f"Page {self.t.name} is not a valid page for a redirect target", self.p.name, type="101 REDIRECT ERROR").call()
                        err=True
                if not err:
                        try:
                                si=s(self.t.call)
                                args=list(si.parameters)
                                if "ctx" not in args:
                                        err=True
                                        ErrorForm(f"Target page does not conform to standards: a page must have a context argument 'ctx' in target.call", self.p.name, type="300 PAGE ERROR").call()
                        except:
                                err=True
                                ErrorForm(f"Target page does not conform to standards: target.call function not found", self.p.name, type="300 PAGE ERROR").call()

                if not err:
                        self.c=ErrorHelper(["page", "context"], [self.p.name, self.ct], [str, dict])
                else:
                        self.c=False
                self.c=self.c or err
        def call(self):
                global control
                global page_class
                global page_ctx
                if self.c:
                        return 1
                else:
                        self.pr.control=self.t.name
                        self.pr.page_class=self.tc
                        self.pr.page_ctx=self.ct
                        return 0
                
class DummyPage:
        name="dummy"
        def call(self, ctx={}):
                pass

class Embedding:
        def __init__(self,page, grouped={}):
                self.pg=page
                self.gr=grouped
                asr=["page","grouped data"]
                args=[page, grouped]
                types=[str, dict]
                self.c=ErrorHelper(asr,args,types)
                
class CanvasEmbedding:
        def __init__(self, page, name, width, height, program, resizex=0, resizey=0, thick=0, highlight_thick=0):
                asr=["page", "name", "width", "height", "resizable - x-axis", "resizable - y-axis", "border thickness", "border highlight thickness"]
                args=[page, name, width, height, resizex, resizey, thick, highlight_thick]
                types=[str, str, int, int, int, int, int, int]
                self.c=ErrorHelper(asr,args,types)
                self.wins=[]
                self.cnvs=[]
                if not self.c:
                        self.embed=Embedding(page, {"page": page, "name":name, "program": program, "width":width, "height": height, "rx":resizex, "ry":resizey, "thick":thick, "hlt":highlight_thick})
        def NewWindow(self):
                if self.c:
                        return 1
                gr=self.embed.gr
                self.tk = Tk()
                self.tk.title(gr["name"])
                self.tk.resizable(gr["rx"], gr["ry"])
                self.tk.wm_attributes("-topmost",1)
                self.wins.append(self.tk)
                return 0

        def NewCanvas(self, window):
                if self.c:
                        return 1
                if self.wins==[]:
                        ErrorForm("Canvas Embedding did not find any valid windows. Please create a window by using NewWindow.", self.embed.gr["page"], type="103 NON-EXISTENT ERROR").call()
                        return 1
                if ErrorHelper(["page", "window"], [self.embed.gr["page"], window], [str,int]):
                        return 1
                if window>len(self.wins)-1 or window<0:
                        ErrorForm(f"Canvas Embedding did not find the window in question(Window #{window}). Please select another window ID.", self.embed.gr["page"], type="103 NON-EXISTENT ERROR").call()
                        return 1
                self.cnv=Canvas(self.wins[window], width=self.embed.gr["width"], height=self.embed.gr["height"], bd=self.embed.gr["thick"], highlightthickness=self.embed.gr["hlt"])
                self.cnvs.append({"tk":self.wins[window], "cnv":self.cnv})
                self.cnv.pack()
                return 0
                                
        def call(self):
                if self.c:
                        return 1
                if self.tk:
                        self.tk.update_idletasks()
                        self.tk.update()
                        return 0
                else:
                        ErrorForm("Canvas Embedding did not find any valid windows. Please create a window by using NewWindow.", self.embed.gr["page"], type="103 NON-EXISTENT ERROR").call()
                        return 1


class ButtonField:
        def __init__(self, canvas_embed, cmd, name, canvas, background="None", foreground="None", anchor="nw", x=150, y=100):
                self.c=False
                if not isinstance(canvas_embed, CanvasEmbedding):
                        ErrorForm("Wrong Embedding", "UNKNOWN", "304 CANVAS ERROR").call()
                        self.c=True
                else:
                        self.cne=canvas_embed
                if not self.c:
                        asr=["page", "button name", "button background color", "button foreground color", "canvas number", "button window position x", "button window position y", "button window anchor"]
                        args=[self.cne.embed.gr["page"], name, background, foreground, canvas, x, y, anchor]
                        types=[str, str, str, str, int, int, int, ["nw", "sw", "w", "n", "s", "e","ne", "se", "center"]]
                        self.c=self.c or ErrorHelper(asr, args, types)
                if not self.c and len(self.cne.cnvs)==0:
                        ErrorForm("Canvas Embedding did not find any valid canvases.", self.cne.embed.gr["page"], type="103 NON-EXISTENT ERROR").call()
                        self.c=True
                if not self.c and canvas>len(self.cne.cnvs)-1 or canvas<0:
                        ErrorForm(f"Canvas Embedding did not find the canvas in question(Canvas #{canvas})", self.cne.embed.gr["page"], type="103 NON-EXISTENT ERROR").call()
                        self.c=True
                if not self.c:
                        self.embed=Embedding(self.cne.embed.gr["page"],{"canvas":canvas, "background":background, "foreground":foreground, "name":name, "command":cmd, "anchor":anchor, "x":x,"y":y,"w":0,"container":None, "special":False,"window":None}) 
        def call(self, redraw=False, ignored=False):
                if self.c:
                        return 1
                if redraw and self.embed.gr["window"]:
                        self.cne.cnvs[self.embed.gr["canvas"]]["cnv"].delete(self.embed.gr["window"])
                if ignored:
                        return 0
                if self.embed.gr["background"]=="None" and self.embed.gr["foreground"]=="None":
                        self.btn=Button(self.cne.cnvs[self.embed.gr["canvas"]]["tk"], text=self.embed.gr["name"], command=self.embed.gr["command"])
                elif self.embed.gr["background"]=="None":
                        self.btn=Button(self.cne.cnvs[self.embed.gr["canvas"]]["tk"], text=self.embed.gr["name"], command=self.embed.gr["command"], fg=self.embed.gr["foreground"])
                elif self.embed.gr["foreground"]=="None":
                        self.btn=Button(self.cne.cnvs[self.embed.gr["canvas"]]["tk"], text=self.embed.gr["name"], command=self.embed.gr["command"], bg=self.embed.gr["background"])
                else:
                        self.btn=Button(self.cne.cnvs[self.embed.gr["canvas"]]["tk"], text=self.embed.gr["name"], command=self.embed.gr["command"], bg=self.embed.gr["background"], fg=self.embed.gr["foreground"])
                self.embed.gr["window"]=self.cne.cnvs[self.embed.gr["canvas"]]["cnv"].create_window(self.embed.gr["x"], self.embed.gr["y"], window=self.btn, anchor=self.embed.gr["anchor"])
                self.cne.call()
                return 0

class ChoiceForm:
        def __init__(self, canvas_embed, choicenames, choicecmds, canvas, backgrounds=[], foregrounds=[], anchor="nw", x=150, y=100, distance=30):
                self.cne=canvas_embed
                self.ca=canvas
                self.d=distance
                self.bg=backgrounds
                self.fg=foregrounds
                self.nm=choicenames
                self.cmd=choicecmds
                self.an=anchor
                self.w=0
                self.x=x
                self.y=y
                if backgrounds==[]:
                        self.bg=["None"]*len(choicenames)
                if foregrounds==[]:
                        self.fg=["None"]*len(choicenames)
                self.c=ErrorHelper(["distance from choice to choice"], [distance], [int], ignore=True)
                self.c=self.c or ListErrorHelper([choicenames, choicecmds, self.bg, self.fg])
                self.cont=None
                self.special=False
                self.wind=None

        def call(self, redraw=False, ignored=False):
                if self.c:
                        return 1
                for x in range(len(self.bg)):
                        ButtonField(self.cne, self.cmd[x], self.nm[x], self.ca, self.bg[x], self.fg[x], self.an, self.x+x*self.d, self.y).call(redraw=redraw, ignored=ignored)
                return 0

class TextFieldAdv:
        def __init__(self, canvas_embed, text, canvas, x, y, font_color="black", font_type="Times", font_size=15, anchor="nw"):
                self.c=False
                if not isinstance(canvas_embed, CanvasEmbedding):
                        ErrorForm("Wrong Embedding", "UNKNOWN", "304 CANVAS ERROR").call()
                        self.c=True
                else:
                        self.cne=canvas_embed
                if not self.c:
                        asr=["page", "font size", "font color", "text", "canvas number", "text window position x", "text window position y", "anchor"]
                        args=[self.cne.embed.gr["page"], font_size, font_color, text, canvas, x, y, anchor]
                        types=[str, int, str, str, int, int, int, ["nw", "sw", "w", "n", "s", "e","ne", "se", "center"]]
                        self.c=self.c or ErrorHelper(asr, args, types)
                if not self.c and len(self.cne.cnvs)==0:
                        ErrorForm("Canvas Embedding did not find any valid canvases.", self.cne.embed.gr["page"], type="103 NON-EXISTENT ERROR").call()
                        self.c=True
                if not self.c and canvas>len(self.cne.cnvs)-1 or canvas<0:
                        ErrorForm(f"Canvas Embedding did not find the canvas in question(Canvas #{canvas})", self.cne.embed.gr["page"], type="103 NON-EXISTENT ERROR").call()
                        self.c=True
                if not self.c:
                        self.fs=font_size
                        self.fc=font_color
                        self.tx=text
                        self.ca=canvas
                        self.x=x
                        self.y=y
                        self.ft=font_type
                        self.an=anchor
                        self.w=(font_size/3)*len(text)
                        self.cont=None
                        self.special=False
                        self.wind=None
                        self.iuef=None
        def call(self, redraw=False, ignored=False):
                if self.c:
                        return 1
                if redraw and self.wind:
                        self.cne.cnvs[self.ca]["cnv"].delete(self.wind)
                if ignored:
                        return 0
                self.wind=self.cne.cnvs[self.ca]["cnv"].create_text(self.x, self.y, text=self.tx, font=(self.ft, self.fs), fill=self.fc, anchor=self.an)
                self.cne.call()
                return self.wind

class ImageField:
        def __init__(self, canvas_embed, x, y, canvas, img="./uploads/example.png", anchor="nw"):
                self.c=False
                if not isinstance(canvas_embed, CanvasEmbedding):
                        ErrorForm("Wrong Embedding", "UNKNOWN", "304 CANVAS ERROR").call()
                        self.c=True
                else:
                        self.cne=canvas_embed
                if not self.c:
                        asr=["page", "image x coordinate", "image y coordinate", "canvas number", "anchor"]
                        args=[self.cne.embed.gr["page"], x, y, canvas, anchor]
                        types=[str, int, int, int, ["nw", "sw", "w", "n", "s", "e","ne", "se", "center"]]
                        if not isinstance(img, PhotoImage):
                                asr.append("image path")
                                args.append(img)
                                types.append(str)
                                flag=True
                        self.c=self.c or ErrorHelper(asr, args, types)
                if not self.c and len(self.cne.cnvs)==0:
                        ErrorForm("Canvas Embedding did not find any valid canvases.", self.cne.embed.gr["page"], type="103 NON-EXISTENT ERROR").call()
                        self.c=True
                if not self.c and canvas>len(self.cne.cnvs)-1 or canvas<0:
                        ErrorForm(f"Canvas Embedding did not find the canvas in question(Canvas #{canvas})", self.cne.embed.gr["page"], type="103 NON-EXISTENT ERROR").call()
                        self.c=True
                if not self.c:
                        self.x=x
                        self.y=y
                        self.ca=canvas
                        self.img=img
                        self.an=anchor
                        if not isinstance(self.img, PhotoImage):
                                self.imgf=PhotoImage(file=self.img)
                        else:
                                self.imgf=self.img
                        self.w=self.imgf.width()
                        self.cont=None
                        self.special=False
                        self.wind=None

        def call(self, redraw=False, ignored=False):
                if self.c:
                        return 1
                if redraw and self.wind:
                        self.cne.cnvs[self.ca]["cnv"].delete(self.wind)
                if ignored:
                        return 0
                self.wind=self.cne.cnvs[self.ca]["cnv"].create_image(self.x, self.y, image=self.imgf, anchor=self.an)
                self.cne.call()
                return self

        def updimg(self, image):
                asr=["page"]
                args=[self.cne.embed.gr["page"]]
                types=[str]
                if not isinstance(image, PhotoImage):
                        asr.append("image path")
                        args.append(image)
                        types.append(str)
                if ErrorHelper(asr, args, types):
                        return 1
                if not isinstance(image, PhotoImage):
                        self.imgf=PhotoImage(file=image)
                else:
                        self.imgf=image
                self.w=self.imgf.width()
                return 0

class BackgroundForm:
        def __init__(self, canvas_embed, beginx, beginy, copyx, copyy, canvas, img="./uploads/example.png", anchor="nw"):
                self.c=False
                flag=False
                if not isinstance(canvas_embed, CanvasEmbedding):
                        ErrorForm("Wrong Embedding", "UNKNOWN", "304 CANVAS ERROR").call()
                        self.c=True
                else:
                        self.cne=canvas_embed
                if not self.c:
                        asr=["page", "begin x coordinate", "begin y coordinate", "times to copy on x axis", "times to copy on y axis", "canvas number", "anchor"]
                        args=[self.cne.embed.gr["page"], beginx, beginy, copyx, copyy, canvas, anchor]
                        types=[str, int, int, int, int, int,["nw", "sw", "w", "n", "s", "e","ne", "se", "center"]]
                        if not isinstance(img, PhotoImage):
                                asr.append("image path")
                                args.append(img)
                                types.append(str)
                                flag=True
                        self.c=self.c or ErrorHelper(asr, args, types)
                if not self.c and len(self.cne.cnvs)==0:
                        ErrorForm("Canvas Embedding did not find any valid canvases.", self.cne.embed.gr["page"], type="103 NON-EXISTENT ERROR").call()
                        self.c=True
                if not self.c and canvas>len(self.cne.cnvs)-1 or canvas<0:
                        ErrorForm(f"Canvas Embedding did not find the canvas in question(Canvas #{canvas})", self.cne.embed.gr["page"], type="103 NON-EXISTENT ERROR").call()
                        self.c=True
                if not self.c:
                        self.bx=beginx
                        self.by=beginy
                        self.cx=copyx
                        self.cy=copyy
                        self.ca=canvas
                        self.img=img
                        self.tiles=[]
                        self.an=anchor
                        if flag:
                                self.imgf=PhotoImage(file=self.img)
                        else:
                                self.imgf=self.img
                        self.wi = self.imgf.width()
                        self.w=self.wi*self.cx
                        self.cont=None
                        self.special=False
                        self.wind=None
        def call(self, redraw=False, ignored=False):
                if self.c:
                        return 1
                if redraw:
                        self.tiles=[]
                h = self.imgf.height()
                for x in range(self.cx):
                        self.tiles.append([])
                        for y in range(self.cy):
                                self.tiles[x].append(ImageField(self.cne, self.bx+x*self.wi, self.by+y*h,self.ca, self.imgf,self.an).call(redraw=redraw, ignored=ignored))
                return 0

class GeometryField:
        def __init__(self, canvas_embed, xs, ys, canvas, extent=180, bd=1, outline="black", fill="", typea="arc"):
                self.c=False
                if not isinstance(canvas_embed, CanvasEmbedding):
                        ErrorForm("Wrong Embedding", "UNKNOWN", "304 CANVAS ERROR").call()
                        self.c=True
                else:
                        self.cne=canvas_embed
                if not self.c:
                        asr=["page", "x coordinates", "y coordinates", "extent", "outline", "fill", "border width","type"]
                        args=[self.cne.embed.gr["page"], xs, ys, extent, outline, fill, bd, typea]
                        types=[str, list, list, int, str, str, int, ["arc", "polygon"]]
                        self.c=self.c or ErrorHelper(asr, args, types)
                if not self.c and len(self.cne.cnvs)==0:
                        ErrorForm("Canvas Embedding did not find any valid canvases.", self.cne.embed.gr["page"], type="103 NON-EXISTENT ERROR").call()
                        self.c=True
                if not self.c and canvas>len(self.cne.cnvs)-1 or canvas<0:
                        ErrorForm(f"Canvas Embedding did not find the canvas in question(Canvas #{canvas})", self.cne.embed.gr["page"], type="103 NON-EXISTENT ERROR").call()
                        self.c=True
                if not self.c and len(xs)!=len(ys):
                        ErrorForm(f"Lengths of lists don't match", self.cne.embed.gr["page"], type="100 INTERNAL ERROR").call()
                        self.c=True
                if not self.c and len(xs)<2:
                        ErrorForm(f"Lengths of lists aren't large enough", self.cne.embed.gr["page"], type="100 INTERNAL ERROR").call()
                        self.c=True
                if not self.c:
                        self.xs=xs
                        self.ys=ys
                        self.ca=canvas
                        self.ex=extent
                        self.ol=outline
                        self.fl=fill
                        self.ty=typea
                        self.cont=None
                        self.special=False
                        self.wind=None
                        self.bdw=bd
        def call(self, redraw=False,ignored=False):
                if self.c:
                        return 1
                if redraw and self.wind:
                        self.cne.cnvs[self.ca]["cnv"].delete(self.wind)
                if ignored:
                        return 0
                if self.ty=="arc":
                        self.wind=self.cne.cnvs[self.ca]["cnv"].create_arc(self.xs[0], self.ys[0], self.xs[1], self.ys[1], extent=self.ex, style=ARC, width=self.bdw, fill=self.fl, outline=self.ol)
                elif self.ty=="polygon":
                        res=[]
                        for x in range(len(self.xs)):
                                res.append(self.xs[x])
                                res.append(self.ys[x])
                        self.wind=self.cne.cnvs[self.ca]["cnv"].create_polygon(*res, fill=self.fl, width=self.bdw, outline=self.ol)
                self.cne.call()
                return 0

class InteractiveUserErrorForm:
        def __init__(self, cne, canvas, element, text,occurrence, type="200 INPUT ERROR"):
                self.t=text
                self.o=occurrence
                self.ty=type
                self.e=element
                self.cne=cne
                self.ca=canvas
                self.cont=None
                self.special=False
                self.wind=None
        def call(self, redraw=False, ignored=False):
                if redraw and self.wind:
                        self.cne.cnvs[self.ca]["cnv"].delete(self.wind)
                if ignored:
                        self.e.special=False
                        self.e.cont.call()
                        return 0
                self.e.y+=20
                if self.e.cont:
                        ignore, ypos=self.e.cont.get_pos(self.e)
                        xpos=self.e.cont.x
                        self.e.special=True
                else:
                        xpos, ypos=self.e.x, self.e.y-20
                self.wind=TextFieldAdv(self.cne, f"{self.ty}: {self.t}", self.ca, xpos, ypos, font_color="red", font_size=10).call(redraw=redraw)
                self.e.cont.call()
                self.e.iuef=self
                return 0

class InputForm:
        def __init__(self, canvas_embed, width, x, y, canvas, prompt, anchor="nw", type_req=str, minimum=0, maximum=100, discretes=[]):
                required=type_req
                self.c=False
                if not isinstance(canvas_embed, CanvasEmbedding):
                        ErrorForm("Wrong Embedding", "UNKNOWN", "304 CANVAS ERROR").call()
                        self.c=True
                else:
                        self.cne=canvas_embed
                if not self.c:
                        asr=["page", "x coordinate", "y coordinate", "width", "canvas number", "anchor", "field required", "minimum value", "maximum value", "discrete values"]
                        args=[self.cne.embed.gr["page"], x, y, width, canvas, anchor, required, minimum, maximum, discretes]
                        types=[str, int, int, int, int, ["nw", "sw", "w", "ne", "e", "se", "center"], [str, int, bool, float], int, int, list]
                        self.c=self.c or ErrorHelper(asr, args, types)
                if not self.c and len(self.cne.cnvs)==0:
                        ErrorForm("Canvas Embedding did not find any valid canvases.", self.cne.embed.gr["page"], type="103 NON-EXISTENT ERROR").call()
                        self.c=True
                if not self.c and canvas>len(self.cne.cnvs)-1 or canvas<0:
                        ErrorForm(f"Canvas Embedding did not find the canvas in question(Canvas #{canvas})", self.cne.embed.gr["page"], type="103 NON-EXISTENT ERROR").call()
                        self.c=True
                if not self.c:
                        if not isinstance(prompt, TextFieldAdv):
                                ErrorForm("Wrong Prompt Field: Field is not TextFieldAdv", self.cne.embed.gr["page"], type="105 INSTANCE ERROR").call()
                                self.c=True
                if not self.c:
                        self.x=x
                        self.y=y
                        self.p=prompt
                        self.w=max(self.p.w, width)
                        self.wi=width
                        self.ca=canvas
                        self.an=anchor
                        self.r=required
                        self.mi=minimum
                        self.ma=maximum
                        self.d=discretes
                        self.cont=None
                        self.special=False
                        self.wind=None
                        self.ch_b=False
                        self.iuef=None
        def call(self, redraw=False, ignored=False):
                if self.c:
                        return 1
                if redraw and self.wind:
                        self.cne.cnvs[self.ca]["cnv"].delete(self.wind)
                if ignored:
                        return 0
                x=self.p.x
                y=self.p.y
                self.p.x=self.x
                self.p.y=self.y
                self.p.call(redraw=redraw)
                self.p.x=x
                self.p.y=y
                self.e=Entry(self.cne.tk, width=self.wi)
                self.wind=self.cne.cnvs[self.ca]["cnv"].create_window(self.x, self.y+self.p.fs+10, window=self.e, anchor=self.an)
                self.cne.call()
                return 0
        def get(self):
                if self.c:
                        return "ERR"
                ch=check(self.e.get(), self.r, self.cne.embed.gr["page"], self.mi, self.ma, self.d, adv=True, cne=self.cne, canvas=self.ca, element=self)
                if ch[1]==False and self.ch_b:
                        self.iuef.call(redraw=True,ignored=True)
                if not self.ch_b and ch[1]==True:
                        self.ch_b=True
                return ch

class Container:
        def __init__(self, canvas_embed, beginx, beginy, endx, canvas, fields=[], height=40, pos="center"):
                instances=[TextFieldAdv, ImageField, ButtonField, InputForm, GeometryField, ChoiceForm, self.__class__]
                self.c=False
                if not isinstance(canvas_embed, CanvasEmbedding):
                        ErrorForm("Wrong Embedding", "UNKNOWN", "304 CANVAS ERROR").call()
                        self.c=True
                else:
                        self.cne=canvas_embed
                if not self.c:
                        asr=["page", "begin x coordinate", "begin y coordinate", "canvas number", "fields list", "height of one field", "end x coordinate", "position in container"]
                        args=[self.cne.embed.gr["page"], beginx, beginy, canvas, fields, height, endx, pos]
                        types=[str, int, int, int, list, int, int, ["begin", "end", "center"]]
                        self.c=self.c or ErrorHelper(asr, args, types)
                if not self.c and len(self.cne.cnvs)==0:
                        ErrorForm("Canvas Embedding did not find any valid canvases.", self.cne.embed.gr["page"], type="103 NON-EXISTENT ERROR").call()
                        self.c=True
                if not self.c and canvas>len(self.cne.cnvs)-1 or canvas<0:
                        ErrorForm(f"Canvas Embedding did not find the canvas in question(Canvas #{canvas})", self.cne.embed.gr["page"], type="103 NON-EXISTENT ERROR").call()
                        self.c=True
                if not self.c:
                        for field in fields:
                                back=False
                                for instance in instances:
                                        if isinstance(field, instance):
                                                back=True
                                                break
                                if not back:
                                        self.c=True
                                        ErrorForm("Non-valid instance detected", self.cne.embed.gr["page"], type="105 INSTANCE ERROR").call()
                                        break
                if not self.c:
                        self.x=beginx
                        self.y=beginy
                        self.ca=canvas
                        self.fs=fields
                        self.h=height
                        self.po=pos
                        self.ex=endx
                        self.w=self.ex-self.x
                        for el in fields:
                                el.cont=self
                                el.special=False

        def call(self, ignored=False):
                if self.c:
                        return 1
                for fld in range(len(self.fs)):
                        xp=self.fs[fld].x
                        if self.po=="begin":
                                self.fs[fld].x=self.x
                        elif self.po=="center":
                                self.fs[fld].x=int(max(self.x, self.x+self.w/2-self.fs[fld].w/2))
                        elif self.po=="end":
                                self.fs[fld].x=int(self.ex-self.fs[fld].w)
                        yp=self.fs[fld].y
                        self.fs[fld].y=self.y+fld*self.h
                        if self.fs[fld].special:
                                self.fs[fld].y+=20
                        self.fs[fld].call(redraw=True, ignored=ignored)
                        self.fs[fld].y=yp
                        self.fs[fld].x=xp
                return 0

        def get_pos(self, fld2):
                for fld in range(len(self.fs)):
                        if self.fs[fld] == fld2:
                                if self.po=="begin":
                                        xx=self.x
                                elif self.po=="center":
                                        xx=int(max(self.x, self.x+self.w/2-self.fs[fld].w/2))
                                elif self.po=="end":
                                        xx=int(self.ex-self.fs[fld].w)
                                return xx, self.y+fld*self.h
                        
def DummyCmd():
        pass
def DummyCmdArgs(*args):
        pass
class PygameEmbedding:
        def __init__(self, width, height, name,page, color=(230,230,230)):
                asr=["page", "width", "height", "red", "green", "blue", "name"]
                args=[page, width, height, color[0], color[1], color[2], name]
                types=[str, int, int, int, int, int, str]
                self.c=ErrorHelper(asr, args, types)
                self.sprites=[]
                self.kys=[]
                if not self.c:
                        pygame.init()
                        self.color=color
                        self.center=(width/2,height/2)
                        self.screen = pygame.display.set_mode((width, height))
                        self.width, self.height=width, height
                        pygame.display.set_caption(name)
                        self.page=page
                        self.rect=self.screen.get_rect()
                        self.exit=False
                        self.setup()
        def link(self,sprite):
                if self.c:
                        return 1
                if ErrorHelper(["page","sprite"], [self.page,sprite], [str,ImageSprite]):
                        return 1
                elif sprite.c:
                        return 1
                self.sprites.append(sprite)
                return 0

        def linkbtn(self,sprite):
                if self.c:
                        return 1
                if ErrorHelper(["page","sprite"], [self.page,sprite], [str,ButtonFieldAdv]):
                        return 1
                elif sprite.c:
                        return 1
                self.sprites.append(sprite)
                return 0
        
        def linkkey(self,keypress):
                if self.c:
                        return 1
                elif ErrorHelper(["page","key press field"], [self.page,keypress], [str,ButtonPressField]):
                        return 1
                elif keypress.c:
                        return 1
                self.kys.append(keypress)
                return 0

        def register_keys(self,*btns):
                for btn in btns:
                        self.linkkey(btn)
                return 0
        
        def setup(self,exec_before_flip=DummyCmd, ticks=DummyCmd, before_imgs=DummyCmd, custom_event_checker=DummyCmdArgs):
                if self.c:
                        return 1
                if not callable(exec_before_flip):
                        ErrorForm("Non-callable object recieved, exec_before_flip should be a callable", self.page, "106 CALLABILITY ERROR").call()
                        return 1
                si=s(exec_before_flip)
                args=list(si.parameters)
                if len(args)!=0:
                        ErrorForm(f"exec_before_flip does not conform to standards: should accept no arguments", self.page, type="107 ARGUMENT ERROR").call()
                        return 1
                
                if not callable(ticks):
                        ErrorForm("Non-callable object recieved, clock ticks function should be a callable", self.page, "106 CALLABILITY ERROR").call()
                        return 1
                si=s(ticks)
                args=list(si.parameters)
                if len(args)!=0:
                        ErrorForm(f"clock ticks function does not conform to standards: should accept no arguments", self.page, type="107 ARGUMENT ERROR").call()
                        return 1

                if not callable(before_imgs):
                        ErrorForm("Non-callable object recieved, before drawing images function should be a callable", self.page, "106 CALLABILITY ERROR").call()
                        return 1
                si=s(before_imgs)
                args=list(si.parameters)
                if len(args)!=0:
                        ErrorForm(f"before drawing images function does not conform to standards: should accept no arguments", self.page, type="107 ARGUMENT ERROR").call()
                        return 1

                if not callable(custom_event_checker):
                        ErrorForm("Non-callable object recieved, custom event checking function should be a callable", self.page, "106 CALLABILITY ERROR").call()
                        return 1
                si=s(custom_event_checker)
                args=list(si.parameters)
                if len(args)!=1:
                        ErrorForm(f"custom event checking function does not conform to standards: should accept event argument", self.page, type="107 ARGUMENT ERROR").call()
                        return 1
                
                self.ebf=exec_before_flip
                self.tks=ticks
                self.bim=before_imgs
                self.cec=custom_event_checker
                
        def call(self):
                if self.c:
                        return 1

                self.mouse=pygame.mouse.get_pos()
                
                self.tks()
                for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                                self.exit=True
                        elif event.type==pygame.KEYUP:
                                for fld in self.kys:
                                        if event.key==fld.key and not fld.cont:
                                                fld.cmdr()
                        elif event.type==pygame.KEYDOWN:
                                for fld in self.kys:
                                        if event.key==fld.key and not fld.cont:
                                                fld.cmd()
                        self.cec(event)
                keys=pygame.key.get_pressed()
                for fld in self.kys:
                        if fld.cont and keys[fld.key]:
                                fld.cmd()
                self.screen.fill(self.color)
                self.bim()
                for sprite in self.sprites:
                        sprite.upd()
                        sprite.call()
                self.ebf()
                pygame.display.flip()
                return 0

class ImageSprite:
        def __init__(self,embed,center, imgpath):
                self.c=ErrorHelper(["page", "path to image", "Pygame embedding", "center x", "center y"],["Sprite loader", imgpath,embed,center[0], center[1]],[str,str, PygameEmbedding, int,int])
                if not self.c:
                        if "/" in imgpath:
                                actpath=imgpath
                        else:
                                actpath=f"uploads/{imgpath}"
                        try:
                                self.img=pygame.image.load(actpath)
                        except:
                                self.c=True
                                ErrorForm(f"Image {imgpath} was not found or had a wrong extension", "Sprite loader", "104 IMAGE ERROR").call()
                        if embed.c:
                                ErrorForm(f"Invalid CanvasEmbedding object: Object had an error", "Sprite loader","105 INSTANCE ERROR").call()
                        self.c=self.c or embed.c
                        
                if not self.c:
                        self.screen=embed.screen
                        self.srect=embed.rect
                        self.rect=self.img.get_rect()
                        self.rect.center=center
                        self.embed=embed
                        self.moving=[False,False,False,False]
                        self.pix=[0,0,0,0]
                        self.x=float(self.rect.x)
                        self.y=float(self.rect.y)
                        
        def call(self):
                if self.c:
                        return 1
                self.screen.blit(self.img,self.rect)
                return 0

        def toggle_move(self, pix,dire="left"):
                if self.c:
                        return 1
                elif ErrorHelper(["page", "direction", "pixels"], [self.embed.page,dire,pix],[str, ["left", "right", "up", "down"], float]):
                        return 1
                if dire=="left":
                        self.moving[0]=not self.moving[0]
                        self.pix[0]=pix
                elif dire=="right":
                        self.moving[1]=not self.moving[1]
                        self.pix[1]=pix
                elif dire=="up":
                        self.moving[2]=not self.moving[2]
                        self.pix[2]=pix
                elif dire=="down":
                        self.moving[3]=not self.moving[3]
                        self.pix[3]=pix
                return 0
        def upd(self):
                if self.c:
                        return 1
                if self.moving[0] and self.rect.left>0:
                        self.x-=self.pix[0]
                if self.moving[1] and self.rect.right<self.srect.right:
                        self.x+=self.pix[1]
                if self.moving[2] and self.rect.top>0:
                        self.y-=self.pix[2]
                if self.moving[3] and self.rect.bottom<self.srect.bottom:
                        self.y+=self.pix[3]
                self.rect.x=self.x
                self.rect.y=self.y
                if self.rect.top<0:
                        self.rect.top=0
                        self.y=self.rect.y
                if self.rect.bottom>self.srect.bottom:
                        self.rect.bottom=self.srect.bottom
                        self.y=self.rect.y
                if self.rect.right>self.srect.right:
                        self.rect.right=self.srect.right
                        self.x=self.rect.x
                if self.rect.left<0:
                        self.rect.left=0
                        self.x=self.rect.x
                return 0

class ButtonPressField:
        def __init__(self, key, cmd,cmdr=DummyCmd, continuous=True):
                self.c=False
                if pygame.key.name(key)=="unknown key":
                        self.c=True
                if not self.c:
                        self.key=key
                        self.cmd=cmd
                        self.cmdr=cmdr
                        self.cont=continuous

class ButtonFieldAdv:
        def __init__(self, embed, text, width, height, begin_x, begin_y,on_click,color=(150,150,200), text_color=(255,255,255), fonttype=None, fontsize=48, begin_state=0):
                if fonttype==None:
                        fonttype=""
                self.c=ErrorHelper(["page", "Pygame embedding", "text","width","height","red button color", "green button color","blue button color","red text color","green text color","blue text color","font type","font size", "begin x coordinate", "begin y coordinate","begin state"],["Button loader", embed,text,width,height,color[0],color[1],color[2],text_color[0],text_color[1],text_color[2], fonttype,fontsize, begin_x,begin_y,begin_state],[str, PygameEmbedding,str,int,int,int,int,int,int,int,int,str,int,int,int, [0,1,2]])
                if not callable(on_click):
                        ErrorForm("Non-callable object recieved, on_click should be a callable", self.page, "106 CALLABILITY ERROR").call()
                        self.c=True
                if not self.c:
                        if fonttype=="":
                                fonttype=None
                        self.ft=fonttype
                        self.embed=embed
                        self.color=color
                        self.width=width
                        self.height=height
                        self.tc=text_color
                        self.font=pygame.font.SysFont(fonttype,fontsize)
                        self.screen=embed.screen
                        self.srect=embed.rect
                        self.text=text
                        self.rect=pygame.Rect(0,0,self.width,self.height)
                        self.rect.topleft=(begin_x, begin_y)
                        self.oc=on_click
                        self.state=begin_state
                        self.pressed=False
                        self._prep_msg(text)
                        
        def _prep_msg(self,msg):
                self.mimg=self.font.render(msg, True, self.tc, self.color)
                self.mimgrect = self.mimg.get_rect()
                self.mimgrect.center=self.rect.center
                return 0

        def change_text(self,nxt):
                self.c=ErrorHelper(["page","new text"], ["Pygame Button Text Changer", nxt], [str,str])
                if self.c:
                        return 1
                self._prep_msg(nxt)
                self.text=nxt

        def call(self):
                if self.c:
                        return 1
                if self.state!=2:
                        self.screen.fill(self.color,self.rect)
                        self.screen.blit(self.mimg, self.mimgrect)
                return 0

        def upd(self):
                if self.c:
                        return 1
                if self.rect.collidepoint(self.embed.mouse) and self.state==0 and pygame.mouse.get_pressed()[0] and not self.pressed:
                        self.pressed=True
                        return 2
                if self.rect.collidepoint(self.embed.mouse) and self.state==0 and not pygame.mouse.get_pressed()[0] and self.pressed:
                        self.pressed=False
                        self.oc()
                return 0

        def disable(self):
                self.state=1

        def enable(self):
                self.state=0

        def off(self):
                self.state=2

class TextFieldExp:
        def __init__(self, embed, text, begin_x, begin_y,color=(230,230,230), text_color=(255,255,255), fonttype=None, fontsize=48, begin_state=0, nobg=0):
                if fonttype==None:
                        fonttype=""
                self.c=ErrorHelper(["page", "Pygame embedding", "text","red outside color", "green outside color","blue outside color","red text color","green text color","blue text color","font type","font size", "begin x coordinate", "begin y coordinate","begin state", "no background"],["Text loader", embed,text,color[0],color[1],color[2],text_color[0],text_color[1],text_color[2], fonttype,fontsize, begin_x,begin_y,begin_state, nobg],[str, PygameEmbedding,str,int,int,int,int,int,int,str,int,int,int, [0,1], [0,1]])
                if not self.c:
                        if fonttype=="":
                                fonttype=None
                        self.ft=fonttype
                        self.embed=embed
                        self.color=color
                        self.tc=text_color
                        self.font=pygame.font.SysFont(fonttype,fontsize)
                        self.screen=embed.screen
                        self.srect=embed.rect
                        self.text=text
                        self.tl=(begin_x,begin_y)
                        self.state=begin_state
                        self.nobg=nobg
                        self._prep_msg(text)
                        
        def _prep_msg(self,msg):
                if self.nobg:
                        self.mimg=self.font.render(msg, True, self.tc)
                else:
                        self.mimg=self.font.render(msg, True, self.tc, self.color)
                self.mimgrect = self.mimg.get_rect()
                self.mimgrect.topleft=self.tl
                return 0

        def change_text(self,nxt):
                self.c=ErrorHelper(["page","new text"], ["Pygame Text Changer", nxt], [str,str])
                if self.c:
                        return 1
                self.text=nxt
                self._prep_msg(nxt)

        def call(self):
                if self.c:
                        return 1
                if self.state==0:
                        self.screen.blit(self.mimg, self.mimgrect)
                return 0

        def on(self):
                self.state=0

        def off(self):
                self.state=1

class Music:
        def __init__(self, embed, filepath, type="sound", permanent=0, volume=0.5):
                self.c=ErrorHelper(["page", "pygame embedding", "music type", "permanent music", "path to file", "volume"], ["Music loader and player", embed, type, permanent,filepath, volume], [str, PygameEmbedding, ["music", "sound"], [0,1],str, float])
                if not self.c:
                        if "/" in filepath:
                                actpath=filepath
                        else:
                                actpath=f"uploads/{filepath}"
                        try:
                                if type=="music":
                                        snd=pygame.mixer.music.load(actpath)
                                elif type=="sound":
                                        snd=pygame.mixer.Sound(actpath)
                        except:
                                self.c=True
                                ErrorForm(f"Sound {filepath} was not found or had a wrong extension", "Sound loader", "108 SOUND ERROR").call()
                if not self.c:
                        self.type=type
                        self.sound=snd
                        self.permanent=permanent
                        self.volume=volume

        def call(self):
                if self.c:
                        return 1
                if self.type=="music":
                        pygame.mixer.music.set_volume(self.volume)
                        if self.permanent:
                                pygame.mixer.music.play(-1)
                        else:
                                pygame.mixer.music.play()
                else:
                        self.sound.set_volume(self.volume)
                        self.sound.play()

                return 0

        def newvolume(self, volume):
                self.c=self.c or ErrorHelper(["page", "volume"], ["Sound changer", volume], [str, float])
                if self.c:
                        return 1
                self.volume=volume
                if self.type=="music":
                        pygame.mixer.music.set_volume(volume)
                else:
                        self.sound.set_volume(self.volume)
class Slider:
        def __init__(self, embed, pos, size, limit, slidercolor, rectcolor, initialpercentage=0):
                self.c=ErrorHelper(["page", "pygame embedding", "position", "x coordinate", "y coordinate", "size", "limit", "slider color", "slider color red", "slider color green", "slider color blue", "rect color", "rect color red", "rect color green", "rect color blue", "initial percentage"],["Slider loader", embed, pos, pos[0],pos[1], size, limit, slidercolor, slidercolor[0], slidercolor[1], slidercolor[2], rectcolor, rectcolor[0], rectcolor[1], rectcolor[2], initialpercentage],[str, PygameEmbedding, tuple, int, int, int, int, tuple, int, int, int, tuple, int, int, int, float])
                if not self.c:
                        self.track=pygame.Rect(pos, (limit-pos[0]+size, size+4))
                        self.slidecirclepos=(self.track.midleft[0]+size/2, self.track.midleft[1])
                        self.slidecircleradius=size/2
                        self.held=False
                        self.embed=embed
                        self.slider_color=slidercolor
                        self.rect_color=rectcolor
                        self.size=size
                        self.limit=(self.track.midleft[0]+size/2, self.track.midright[0]-size/2)
                        self.slidecirclepos=(min(max(self.limit[0]+initialpercentage*(self.limit[1]-self.limit[0]), self.limit[0]), self.limit[1]), self.slidecirclepos[1])

        def call(self):
                if self.c:
                        return 2
                mouse=self.embed.mouse
                if self.held:
                        self.slidecirclepos=(min(max(mouse[0], self.limit[0]), self.limit[1]), self.slidecirclepos[1])
                pygame.draw.rect(self.embed.screen, self.rect_color, self.track, border_radius=int(2+self.size/2))
                pygame.draw.circle(self.embed.screen, self.slider_color, self.slidecirclepos, self.slidecircleradius)
                if pygame.mouse.get_pressed()[0] and (mouse[0]-self.slidecirclepos[0])**2+(mouse[1]-self.slidecirclepos[1])**2<=self.slidecircleradius**2:
                        self.held=True
                else:
                        self.held=False
                return (self.slidecirclepos[0]-self.limit[0])/(self.limit[1]-self.limit[0])

class PygameObjectGroup:
        AVAILABLE_TYPES=[ImageSprite, ButtonFieldAdv, TextFieldExp, Music, Slider]
        def __init__(self, embed, togroup):
                self.c=ErrorHelper(["page", "pygame embedding"], ["Pygame group creator", embed], [str, PygameEmbedding])
                if not self.c:
                        self.grouped=[]
                        for obj in togroup:
                                calc=0
                                for type_ in self.AVAILABLE_TYPES:
                                        if not isinstance(obj, type_):
                                                calc+=1
                                if calc==len(self.AVAILABLE_TYPES):
                                        ErrorForm(f"Invalid type for subargument of argument togroup: Can't group object of type {(obj).__class__} into a group", "100 INTERNAL ERROR").call()
                                elif obj.c:
                                        ErrorForm(f"Invalid state for subargument of argument togroup: Can't group errored object {obj} of type {(obj).__class__} into a group", "100 INTERNAL ERROR").call()
                                else:
                                        self.grouped.append(obj)
        def off_all(self):
                for obj in self.grouped:
                        objclass=(obj).__class__
                        if objclass==TextFieldExp or objclass==ButtonFieldAdv:
                                obj.off()
                        elif objclass==Music:
                                obj.newvolume(0.0)

        def on_all(self):
                for obj in self.grouped:
                        objclass=(obj).__class__
                        if objclass==TextFieldExp:
                                obj.on()
                        elif objclass==ButtonFieldAdv:
                                obj.enable()
                        elif objclass==Music:
                                obj.newvolume(1.0)

        def disable_all(self):
                for obj in self.grouped:
                        objclass=(obj).__class__
                        if objclass==ButtonFieldAdv:
                                obj.disable()

        def call(self):
                values=[]
                for obj in self.grouped:
                        values.append(obj.call())
                return values


