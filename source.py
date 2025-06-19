from os import system, getcwd, path
import platform
from time import sleep
from engine import core

class DopeShell:
    def __init__(self):
        self.basePath = getcwd() # Directory in which dopeshell files placed
        self.root = path.expanduser("~") # Path of the root (Dopeshell operates from here at starting)
        self.platform = platform.system() # Current operating System name
        self.history = [] # Stores history in the form of dicts

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

    def executeCommand(self, commandX): 
        
        if not commandX:
            return # return if not any command input found
        else:
            command_name = commandX.split(' ')[0].strip()
            if command_name in self.engine:
                self.engine[command_name](self, commandX)
            else:
                print("⚠️  Command is not available in intriction set! Type --helpme to get documentation")

    # TO daignoses the health of system
    def diagnostic(self):
        return True

def setupEnvironment(_instance, is_start):
    if is_start:
        system("echo off")
        # engine["wipe"](_instance, "hello")
        print("Checking instance Config!")
        sleep(0.5)

        print(f"Current Platform check \"{_instance.platform}\" ✅")

        sleep(0.5)

        if _instance.diagnostic():
            print("Dope Shell is working perfectly ✅")
        else:
            print("🪲 encountered!")

        sleep(0.5)

        print("Instruction Set loadded successfuly ✅")

        sleep(2)
        # _instance.clearConsole(
    _instance.asciiArt();
    print("\n");


if __name__ == "__main__":
    _instance = DopeShell()
    setupEnvironment(_instance, True)
    print(_instance.basePath)
    print(_instance.root)

    while True:
        if _instance.platform == "Windows":
            commandX = input(f"{_instance.root.replace("C:", "~").replace("\\", "/").strip() + ": "}")
            _instance.executeCommand(commandX.strip())
        else:
            commandX = input(f"~{_instance.root}:")
            _instance.executeCommand(commandX.strip())
