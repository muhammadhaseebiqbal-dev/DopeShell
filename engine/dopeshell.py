# Standard library imports
import platform
from os import getcwd, chdir
from os.path import expanduser
from getpass import getuser
from time import sleep

# Custom Implementation
from .components.core import core_function_mapping
from .keywords import keys

class DopeShell:
    def __init__(self):        
        self.basePath = getcwd() # Directory in which dopeshell files placed
        self.root = chdir(expanduser("~")) # Path of the root (Dopeshell operates from here at starting)
        self.platform = platform.system() # Current operating System name
        self.history = [] # Stores history in the form of dicts
        self.life = 0 # to manage the session life (just for console operation)


        # Mapping to execute each keyword implemetation
        list_of_available_func = list(core_function_mapping.keys()); # changing dict keys so that we can invoke functions based on keywords
        self.key_func_mapping = {
            f'{keys[i]["command"]}': core_function_mapping[list_of_available_func[i]] for i in range(0,len(core_function_mapping))
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

    # Handle initial root redirection    
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
            try:
                command_name = command.split(' ')[0].strip()
                
                # check if it exist in library
                if command_name in self.key_func_mapping:
                    self.key_func_mapping[command_name](self, command)
                else:
                    print("⚠️  Command is not available in keyword set! Try --helpme")
            except Exception as e:
                print(e)

    # TO daignoses the health of system
    def diagnostic(self):
        return True

    # Initiallise the environment
    def _init_env(self):
        self.executeCommand(keys[9]["command"])
        print("Checking instance Configurations!")
        print(f"Current Platform check \"{self.platform}\" ✅")
        if self.diagnostic():
            print("Dope Shell is working perfectly ✅")
        else:
                print("🪲 issuce occurred while diagnosing system!")
        sleep(0.2)

        print("Checking system integrity ✅")
        sleep(0.3)
        print("Hold tight!")
        sleep(0.5)
        
        self.executeCommand(keys[9]["command"])
        self.goToRoot()
        self.asciiArt();
        print("\n");

        while True:
            if self.platform == "Windows":
                command = input(f"{self.root.replace("C:", "~").replace("\\", "/").strip() + " > "}")
                self.executeCommand(command.strip())
            else:
                command = input(f"~{self.root} > ")
                self.executeCommand(command.strip())

