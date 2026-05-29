import data
import time
import builtins
from models import RedirectField, ErrorForm, ErrorHelper, PygameEmbedding, pygame
from inspect import signature as s

class DummyPage:
        name="dummy"
        def call(self, ctx={}):
                pass

class Singleton(type):
        _instances = {}
        def __call__(cls, *args, **kwargs):
                if cls not in cls._instances:
                        inst = super().__call__(*args, **kwargs)
                        cls._instances[cls] = inst
                        try:
                                si=s(inst.on_begin)
                                args=list(si.parameters)
                                if len(args)>0:
                                        ErrorForm(f"on_begin of Game cannot accept any arguments", "INITIALIZATION", type="304 GAME ERROR").call()
                                else:
                                        inst.on_begin()
                                        for k, v in inst.__dict__.items():
                                            setattr(builtins, k, v)
                        except AttributeError:
                                pass
                return cls._instances[cls]

class Game(metaclass=Singleton):
        pass
        
class Program:
        def __init__(self, ps, pctx, pcs, vpgs, game, pps=25, gfile="g.json", globals={}):
                asr=["page", "page context", "file", "globals", "valid pages","pages per second", "game"]
                args=[ps, pctx, gfile, globals, vpgs, pps, game]
                types=[str, dict, str, dict, list, int, Game]
                self.c=ErrorHelper(asr, args, types)
                self.db=data.Database(gfile, ps, globals)
                self.vpgs=vpgs
                self.g=game
                if not self.c:
                        self.vpgs.append("dummy")
                if self.db.retrieve("", total=True)=="ERR" or self.db.retrieve("", total=True)=={}:
                        self.db.new()
                self.page_ctx=pctx
                self.exit_now=False
                self.page_class=pcs
                self.history=[]
                self.PPS=pps
                self.gfile=gfile
                result=1
                if not self.c:
                        result=RedirectField(pcs, DummyPage, self, pctx).call()
                self.globals=globals
                self.st=globals
                self.sv=globals
                self.gload()
                if result==1:
                        self.c=True
        def run(self):
                if not self.c:
                        cl=None
                        try:
                                while True:
                                        time.sleep(1/self.PPS)
                                        if not isinstance(cl,self.page_class):
                                                self.cl, cl=self.page_class(), self.page_class()
                                        config=None
                                        try:
                                                config=self.page_class.config
                                        except:
                                                pass
                                        if config=="pgwin":
                                                cl.call()
                                        elif type(config) == tuple:
                                                if isinstance(config[1], PygameEmbedding):
                                                        if config[0]=="scene":
                                                                self.gload()
                                                                config[1].ebf=cl.call
                                                                config[1].call()
                                                                if config[1].exit:
                                                                        pygame.quit()
                                                                        self.exit_now=True
                                                                self.write_history(cl.name)
                                                                self.gstore()
                                                else:
                                                        ErrorForm(f"Invalid config for a page: {config}", self.page_class.name, "100 INTERNAL ERROR").call()
                                        else:
                                                self.gload()
                                                if self.page_ctx=={}:
                                                        cl.call()
                                                else:
                                                        cl.call(self.page_ctx)
                                                self.write_history(cl.name)
                                                self.gstore()
                                        if self.exit_now:
                                                break
                                return 0
                        except KeyboardInterrupt:
                                ErrorForm("Warning: KeyboardInterrupt used to exit the framework program. Some data may have not been saved.", self.page_class.name, "400 EXIT WARNING").call()
                else:
                        return 1
        def gstore(self):
                self.db.change("",self.globals, total=True)
        def gload(self):
                globals=self.db.retrieve("", total=True)
                if globals=="ERR":
                        self.globals=self.st
                else:
                        self.globals=globals
        def write_history(self, page):
                c=ErrorHelper(["page"], [page], [str])
                if not c:
                        self.history.append({"page": page, "context": self.page_ctx, "class": self.page_class})
                else:
                        return "ERR"
        def read_history(self, block_err=False):
                if len(self.history)==0 and not block_err:
                        ErrorForm("Accessing unknown value in history is not possible", self.control, "302 HISTORY ERROR")
                        return "ERR"
                package=self.history.pop()
                self.page_class=package["class"]
                self.page_ctx=package["context"]
