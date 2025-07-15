# Standard library imports
import platform
from os import getcwd, chdir
from os.path import expanduser
from getpass import getuser
from time import sleep

# Import specific command functions from components
from .components.core import (
    spitdir, dive, halt, whoami, helpme, 
    reveal, clone, throw, swap, snap, wipe,
    readout
)
from .components.keywords import keywords

class DopeShell:
    def __init__(self):        
        self.basePath = getcwd() # Directory in which dopeshell files placed
        self.root = chdir(expanduser("~")) # Path of the root (Dopeshell operates from here at starting)
        self.platform = platform.system() # Current operating System name
        self.history = [] # Stores history in the form of dicts
        self.life = 0 # to manage the session life (just for console operation)

        # Set of defined keywords load here from mapping
        self.keywords = keywords

        # Mapping to execute each keyword implemetation
        self.engine = {
            "spitdir": spitdir,
            "dive": dive,
            "halt": halt,
            "whoami": whoami,
            "--helpme": helpme,
            "reveal": reveal,
            "clone": clone,
            "throw": throw,
            "swap": swap,
            "snap": snap,
            "wipe": wipe,
            "readout": readout
        }

        # initialize the environment
        self._init_env();
    def asciiArt(self):
        print(
            r'''
                ██████╗  ██████╗ ██████╗ ███████╗     ███████╗██╗  ██╗███████╗██╗     ██╗     
                ██╔══██╗██╔═══██╗██╔══██╗██╔════╝     ██╔════╝██║  ██║██╔════╝██║     ██║     
                ██║  ██║██║   ██║██████╔╝█████╗       ███████╗███████║█████╗  ██║     ██║     
                ██║  ██║██║   ██║██╔═══╝ ██╔══╝       ╚════██║██╔══██║██╔══╝  ██║     ██║     
                ██████╔╝╚██████╔╝██║     ███████╗     ███████║██║  ██║███████╗███████╗███████╗
                ╚═════╝  ╚═════╝ ╚═╝     ╚══════╝     ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝
            '''
        )

    # Handle initial rooth redirection    
    def goToRoot(self):
        if self.platform == "Windows":
            chdir(f"C:/users/{getuser()}")
        else:
            expanduser("~")

        self.root = getcwd()

    def executeCommand(self, command):    
        if not command:
            return # return if not any command input found
        else:
            command_name = command.split(' ')[0].strip()
            
            # check if it exist in library
            if command_name in self.engine:
                self.engine[command_name](self, command)
            else:
                print("⚠️  Command is not available in keyword set! Type --helpme to get documentation")

    # TO daignoses the health of system
    def diagnostic(self):
        return True

    # Initiallise the environment
    def _init_env(self):
        self.executeCommand("wipe")
        print("Checking instance Config!")
        sleep(0.5)
        print(f"Current Platform check \"{self.platform}\" ✅")
        sleep(0.5)

        if self.diagnostic():
            print("Dope Shell is working perfectly ✅")
        else:
                print("🪲 encountered!")
        sleep(0.5)

        print("Checking system integrity ✅")
        sleep(2)
        
        self.executeCommand("wipe")
        self.goToRoot()
        self.asciiArt();
        print("\n");

        while True:
            if self.platform == "Windows":
                command = input(f"{self.root.replace("C:", "~").replace("\\", "/").strip() + ": "}")
                self.executeCommand(command.strip())
            else:
                command = input(f"~{self.root}:")
                self.executeCommand(command.strip())

