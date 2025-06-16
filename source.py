from os import system, getcwd, getlogin, chdir, listdir, path, chmod, rename, remove, rmdir
import platform
from time import sleep
import json
import subprocess
from re import fullmatch
from shutil import copy, copytree, move, rmtree
from stat import S_IWRITE

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
                pathx = commandX[len("dive")+1:]
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

            elif commandX.lower().startswith("clone") or commandX.lower().startswith("throw") or commandX.lower().startswith("swap"):
                # clone <src> <des>
                try:
                    cmdx = commandX.replace('\\','/')
                    typeX = "";
                    if commandX.lower().startswith("clone"):
                        typeX = "clone"
                    elif commandX.lower().startswith("throw"):
                        typeX = "throw"
                    else:
                        typeX = "swap"
                    tokenize_cmdx = cmdx.split('\'');
                    clean_tokens = [e.strip() for e in tokenize_cmdx if e.strip()]
                    src = clean_tokens[1];
                    des = clean_tokens[2];

                    map = {}
                    pattern = r"^\w+\.\w+$"

                    if len(src.split("/")) > 1 :
                        if fullmatch(pattern, src.split("/")[-1]):
                            map["src_type"] = "file";
                        else:
                            map["src_type"] = "dir"          
                    else:
                        if fullmatch(pattern, src.split("\\")[-1]):
                            map["src_type"] = "file";
                        else:
                            map["src_type"] = "dir"

                    if len(des.split("/")) > 1 :
                        if fullmatch(pattern, des.split("/")[-1]):
                            map["des_type"] = "file";
                        else:
                            map["des_type"] = "dir"          
                    else:
                        if fullmatch(pattern, des.split("\\")[-1]):
                            map["des_type"] = "file";
                        else:
                            map["des_type"] = "dir"

                    if not map["src_type"]and not map["des_type"]:
                        print("⚠️  Error! Invalid Paths follow the correct format ( clone <src> <des> )")

                    if map["src_type"] == "file" and map["des_type"] == "dir":
                        if typeX == "clone":
                            copy(src, des)
                            print("✅ Successfully copied!")
                        if typeX == "throw":
                            move(src, des)
                            print("✅ Successfully moved!")

                    elif map["src_type"] == "file" and map["des_type"] == "file":
                        if typeX == "clone":
                            copy(src, des)
                            print("✅ Successfully copied!")
                        if typeX == "throw":
                            move(src, des)
                            print("✅ Successfully moved!")
                        if typeX == "swap":
                            rename(src, des)

                    elif map["src_type"] == "dir" and map["des_type"] == "dir":
                        def handle_permission_contraint(func, path, exc_info):
                            chmod(path, S_IWRITE)
                            func(path)
                        
                        if typeX == "copy":
                            copytree(src, des)
                            print("✅ Successfully copied!")
                        if typeX == "throw":
                            move(src, des)
                            print("✅ Successfully moved!")
                        if typeX == "swap":
                            rename(src, des)

                    else:
                        print("⚠️ Error! Copying file, might be there is an issue directory/file.")

                except Exception as err:
                    print("❌  Command Not Supported!", err)
                
                except FileNotFoundError as err:
                    print("❌  Command Not Supported!", err)



            elif commandX.lower() == "wipe":
                clearConsole()
                setupEnvironment(self, False)

# TODO: fix snap for absolute path
            elif commandX.lower().startswith("snap"):
                try:
                    cmdx = commandX.replace("\\","/")
                    tokenize_cmdx = cmdx.split('\'');
                    clean_tokens = [e.strip() for e in tokenize_cmdx if e.strip()]
                    src = clean_tokens[1];
                    pattern = r"^\w+\.\w+$"
                    if len(src.split("/")) > 1 :
                        if fullmatch(pattern, src.split("/")[-1]):
                            remove(src)
                            print("✅  Deleted Successfully")
                        else:
                            rmtree(src)
                            print("✅  Deleted Successfully")

                except Exception as err:
                    print(err)

        else:
            print("⚠️  Command is not available in intriction set! Type --helpme to get documentation")
           

    def showOutput():
        print("Here to implemet Electution")

def clearConsole():
    if platform.system() == "Windows":
        system("cls")
    else:
        system("clear")

def setupEnvironment(_instance, is_start):
    if is_start:
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
    setupEnvironment(_instance, True)

    while True:
        if platform.system() == "Windows":
            commandX = input(f"{_instance.currPath.replace("C:", "~").replace("\\", "/").strip() + ": "}")
            _instance.executeCommand(commandX.strip())
        else:
            commandX = input(f"~{_instance.currPath}:")
            _instance.executeCommand(commandX.strip())
