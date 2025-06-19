import subprocess
from getpass import getuser
from regex import fullmatch
from .utils import pathTokeniser
from shutil import copy, copytree, move, rmtree
from os import system, getcwd, chdir, listdir, path, chmod, rename, remove, rmdir

# Handle directory exposure implemetation. (ie: expore directory files)
def spitdir(self, input):
    try:     
        if self.platform == "Linux":
            result = subprocess.run("ls", shell=True, capture_output=True, text=True)
            if result.stdout:
                print(result.stdout)
            else:
                print(result.stderr)
        else:
            result = subprocess.run("dir", shell=True, capture_output=True, text=True)
            if result.stdout:
                print(result.stdout)
            else:
                print(result.stderr)

    except Exception as err:
        print(err)

# Handle Directory changing implemetation (i.e: changing the current directory)   
def dive(self, input):                
        input = input[len("dive")+1:]
        if input.startswith("'") and input.endswith("'"):
            input = input.replace("'", "")
            try:
                chdir(input)
                self.root = getcwd();
            except Exception as e:
                print("⚠️  System unable to parse this! Kindly use valid absolute path", e)
                        
        else:
            input = input[len("dive"):]
            if input.startswith("/") or input.startswith("\\"):
                input = input[1:]
                try: 
                    chdir(f"{self.root}/{input.strip()}")
                    self.root = getcwd();

                except Exception as e:
                    print("⚠️  Could'nt find path! Try entering valid relative path")

# Handle session ending implemetation
def halt(self, input):
    print("😒 Quiting DopeShell!")
    quit()

# Show User details
def whoami(self, input):
    try:
        print(f"{getuser()}")
    except Exception as err:
         print("Error while performing operation. Try again!") 

# Show all the supported keywords
def helpme(self, input):
    try:
        print(" \n Supported commands: \n ----------------------------------------------------------------------------- \n")
        for e in self.keywords:
            print(f"{e["command"]:<8}        {e["description"]}\n")  
    except Exception as err:
         print("Error while performing operation. Try again!") 

# Show present working directory
def reveal(self, input):
    print(f"\n Current Path: \n ----------------------------------------------\n {self.root }\n\n")

# Handles copy implemetation
def clone(self, input):
    if not pathTokeniser(input):
        print("⚠️  Invalid command! Try --helpme")

    src, des, map = pathTokeniser(input)
    if map["src_type"] == "dir" and map["des_type"] == "dir":
        try:
            copytree(src, des)
            print("✅ Successfully copied!")
        except Exception as err:
            print(err)
    else:
        try:
            copy(src, des)
            print("✅ Successfully copied!")
        except Exception as err:
            print(err)

# Handles move implementation
def throw(self, input):
    if not pathTokeniser(input):
        print("⚠️  Invalid command! Try --helpme")
    
    src, des = pathTokeniser(input)
    try:
        move(src, des)
        print("✅ Successfully moved!")
    except Exception as err:
            print(err)

# Handles rename implementation
def swap(self, input):
    src, des, map = pathTokeniser(input)
    if map["src_type"] == "file" and map["des_type"] == "file" or map["src_type"] == "dir" and map["des_type"] == "dir":
        try:
            rename(src, des)
            print("✅ Successfully renamed!")
        except Exception as err:
            print(err)
    else:
        print("⚠️  Invalid command! Try --helpme")
# Handle delete implemetation
def snap(self, input):
    src = pathTokeniser(input)
    pattern = r"^\w+\.\w+$"

    try:
       if len(src.split("/")) > 1 :
            if fullmatch(pattern, src.split("/")[-1]):
                remove(src)
                print("✅  Deleted Successfully")
            else:
                rmtree(src)
                print("✅  Deleted Successfully")
    except Exception as err:
        print(err)

# Clear the console
def wipe(self, input):
    if self.platform == "Windows":
        system("cls")
    else:
        system("clear")

    self.setupEnvironment(self, False)
