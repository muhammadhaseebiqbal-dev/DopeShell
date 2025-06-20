from os import  getcwd, path, chdir
from getpass import getuser
import platform
from time import sleep
from engine.components import core

class DopeShell:
    def __init__(self):
        self.basePath = getcwd() # Directory in which dopeshell files placed
        self.root = chdir(path.expanduser("~")) # Path of the root (Dopeshell operates from here at starting)
        self.platform = platform.system() # Current operating System name
        self.history = [] # Stores history in the form of dicts
        self.life = 0 # to manage the session life (just for console operation)

        # Set of defined keywords load here from mapping
        self.keywords = [
            {
                "command": "spitdir",
                "description": "list down file/folders of current directory"
            },
            {
                "command": "dive",
                "description": "change directory to specified path"
            },
            {
                "command": "reveal",
                "description": "show present working directory path"
            },
            {
                "command": "whoami",
                "description": "show user account name"
            },           
            {
                "command": "halt",
                "description": "terminate the current shell session"
            },
            {
                "command": "throw",
                "description": "move any file/dir from src path to destined path"
            },
            {
                "command": "clone",
                "description": "copy any file/dir from src path to destined path (must use absolute paths)"
            },
            {
                "command": "swap",
                "description": "to remane files and folders"
            },
            {
                "command": "snap",
                "description": "delete the file and the whole directory"
            },
            {
                "command": "wipe",
                "description": "clear the console"
            },
            {
                "command": "--helpme",
                "description": "show list of supported commands"
            }
        ]
        self.engine = {
            "spitdir": core.spitdir,
            "dive": core.dive,
            "halt": core.halt,
            "whoami": core.whoami,
            "--helpme": core.helpme,
            "reveal": core.reveal,
            "clone": core.clone,
            "throw": core.throw,
            "swap": core.swap,
            "snap": core.snap,
            "wipe": core.wipe
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
            path.expanduser("~")

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

