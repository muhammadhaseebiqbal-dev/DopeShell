from os import system, getcwd, getlogin, chdir, listdir, path
import platform
from time import sleep
import json
import subprocess

class DopeShell:
    def __init__(self):
        self.basePath = getcwd()

        if platform.system() == "Linux":
            chdir(f"{path.expanduser("~")}")
        else:
            chdir(f"C:/Users/{getlogin()}")
        self.history = []
        self.instructSet = []
        self.currPath = getcwd()

    def diagnostic(self):
        return True
    
    def loadInstructionSet(self):
        with open(f"{self.basePath}/mapping/mapping.json") as intructionSet:
            parseList = json.load(intructionSet);

            for dictItem in parseList:
                self.instructSet.append({"command": dictItem["command"], "description": dictItem["description"]});
            
            intructionSet.close()
            return True;
        return False;
    
    
    def asciiBranding(self):
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
            return
        
        if any(cmdX["command"].lower().strip() == commandX.split()[0].lower().strip() for cmdX in self.instructSet):
            if commandX.lower() == "spitdir":
                if platform.system() == "Linux":
                    result = subprocess.run( "ls", shell=True, capture_output=True, text=True )
                    if result.stdout:
                        print(result.stdout)
                    else:
                        print(result.stderr)
                else:
                    result = subprocess.run( "dir", shell=True, capture_output=True, text=True )
                    if result.stdout:
                        print(result.stdout)
                    else:
                        print(result.stderr)

            elif commandX.lower().startswith("dive"):
                pathx = commandX[len("dive"):].strip()
                if pathx.startswith("'") and pathx.endswith("'"):
                    pathx = pathx.replace("'", "")
                    if platform.system() == "Windows":
                        try:
                            chdir(pathx)
                            self.currPath = getcwd();
                        except Exception as e:
                            print("⚠️  System unable to parse this! Try again", e)
                    else:
                        try:
                            chdir(pathx)
                            self.currPath = getcwd();
                        except Exception as e:
                            print("⚠️  System unable to parse this! Try again", e)
                        
                else:
                    pathx = commandX[len("dive"):]
                    if pathx.startswith("/") or pathx.startswith("\\"):
                        pathx = pathx[1:]

                    try: 
                        chdir(f"{getcwd()}/{pathx.strip()}")
                        self.currPath = getcwd();

                    except Exception as e:
                            print("⚠️  Could'nt find path!")
            elif commandX.lower() == "endsesh":
                print("😒 Quiting DopeShell!")
                quit()
            
            elif commandX.lower() == "whoami":
                if platform.system() == "Linux":
                    process = subprocess.run("whoami", shell=True, capture_output=True, text=True)
                    if process.stdout:
                        print(process.stdout);
                    else:
                        print("⚠️  Error Encountered! ", process.stderr)
                else:
                    print(f"{getlogin()}") 

            elif commandX.lower() == "--helpme" :
                print(" \n Supported commands: \n ----------------------------------------------------------------------------- \n")
                for e in self.instructSet:
                    print(f"{e["command"]:<8}        {e["description"]}\n")   

            elif commandX.lower() == "reveal":
                print(f"\n Current Path: \n ----------------------------------------------\n {self.currPath }\n\n")
        else:
            print("⚠️  Command is not available in intriction set! Type --helpme to get documentation")
           

    def showOutput():
        print("Here to implemet Electution")

def clearConsole():
    if platform.system() == "Windows":
        system("cls")
    else:
        system("clear")

def setupEnvironment(_instance):
    system("echo off")
    clearConsole()
    print("Checking instance Config!")
    sleep(0.5)

    print(f"Current Platform check \"{platform.system()}\" ✅")

    sleep(0.5)

    if _instance.diagnostic():
        print("Dope Shell is working perfectly ✅")
    else:
        print("🪲 encountered!")

    sleep(0.5)

    if _instance.loadInstructionSet():
        print("Instruction Set loadded successfuly ✅")
    else:
        print("🪲 encountered!")

    sleep(2)
    clearConsole()
    _instance.asciiBranding();
    print("\n");


if __name__ == "__main__":
    _instance = DopeShell()
    setupEnvironment(_instance)

    while True:
        if platform.system() == "Windows":
            commandX = input(f"{_instance.currPath.replace("C:", "~").replace("\\", "/").strip() + ": "}")
            _instance.executeCommand(commandX.strip())
        else:
            commandX = input(f"~{_instance.currPath} ")
            _instance.executeCommand(commandX.strip())

    