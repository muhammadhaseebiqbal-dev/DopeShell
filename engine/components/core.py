# / ********************************************************************************************************************* /

# This file is probaly the ebrain of this marvelous shell. I know you are wondering Haseeb why are you making this shell 
# in the era of AI powered autonomous shell. Its my choice Don't Judge me. Sometime i develop thing that does'nt make sense


# / ********************************************************************************************************************* /


# Standard library imports
import platform
import subprocess
from time import sleep
import builtins

# OS and path operations
from os import system, getcwd, chdir, rename, remove
from os.path import expanduser
from getpass import getuser

# File operations
from shutil import copy, copytree, move, rmtree

# Networking
from ping3 import ping as ping_network
import requests
import wget

# Custom Implementation
from .utils import pathTokeniserMulti, pathTokenizerSingle, pathtokenizerMultiple
from ..keywords import keys


# Handle directory exposure implemetation. (ie: expore directory files)
def directories_exploration(self, input):
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
def change_directory(self, input):                
        input = input[len("fd")+1:]
        if input.startswith("'") and input.endswith("'"):
            input = input.replace("'", "")
            try:
                chdir(input)
                self.root = getcwd();
            except Exception as e:
                print("⚠️  System unable to parse this! Kindly use valid absolute path", e)
                        
        else:
            if input.startswith("/") or input.startswith("\\"):
                input = input[1:]
                try: 
                    chdir(f"{self.root}/{input.strip()}")
                    self.root = getcwd();

                except Exception as e:
                    print("⚠️  Could'nt find path! Try entering valid relative path")
            else:
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


# Show present working directory
def current_wording_directory(self, input):
    print(f"\n Current Path: \n ----------------------------------------------\n {self.root }\n\n")

# Handles copy implemetation
def copy(self, input):
    # if not pathTokeniserMulti(input):
    #     print("⚠️  Invalid command! Try --helpme")

    try:
        src, des, map = pathTokeniserMulti(input)
        if map["src_type"] == "dir" and map["des_type"] == "dir":
            try:
                copytree(src, des, dirs_exist_ok=True)
                print("✅ Successfully copied!")
            except Exception as err:
                print(err)
        else:
            try:
                copy(src, des)
                print("✅ Successfully copied!")
            except Exception as err:
                print(err)
    except Exception as err:
                pass     

# Handles move implementation
def move(self, input):
    if not pathTokeniserMulti(input):
        print("⚠️  Invalid command! Try --helpme")

    try:
        src, des, map = pathTokeniserMulti(input)
        move(src, des)
        print("✅ Successfully moved!")
    except Exception as err:
            print(err)
    

# Handles rename implementation
def rename(self, input):
    try:
        src, des, map = pathTokeniserMulti(input)
        if map["src_type"] == "file" and map["des_type"] == "file" or map["src_type"] == "dir" and map["des_type"] == "dir":
            try:
                rename(src, des)
                print("✅ Successfully renamed!")
            except Exception as err:
                print(err)
        else:
            print("⚠️  Invalid command! Try --helpme")
    except Exception as err:
        print(err)

# Handle delete implemetation
def delete_anthing(self, input):
    src, map = pathTokenizerSingle(input)
    try:
        if map["src_type"] == "file":
            remove(src)
            print("✅  Deleted Successfully")
        else:
            rmtree(src)
            print("✅  Deleted Successfully")
    except Exception as err:
        print(err)

# Clear the console
def clear_console(self, input):
    if self.platform == "Windows":
        system("cls")
    else:
        system("clear")

    # To manage the art for monoload
    # why `>1` ? because the wipe called in _init_env once so we don't need to reprint art twice at starting  
    if self.life > 1:
        self.asciiArt()
    
    # incrementing the life by 1
    self.life += 1

# Handle readout implementation
def process_file_content(self, input):
    if not input: return
                
    try:
        paths, types = pathtokenizerMultiple(input)
        accumulator = '' # contain the whole text content to cover concat
        counter = 0 # to track the file being opened
        line_number = 0 # for line numbering

        if '>' in input:
            try:
                if '>>>' in input:

                    for type in types:
                        with open(paths[counter], "a+") as file:
                            file.seek(0)
                            if counter == (len(types)-1):
                                    file.write(accumulator)
                            else:
                                accumulator += file.read()
                                counter += 1
                        file.close()
                else:
                    if len(paths) > 1:
                        print("Yet supported for only single file! \n")

                    if types[0] == 'file':
                        capture = builtins.input("Enter you response: ");
                        if '>>' in input: # to append the captured text
                            with open(paths[0], "r") as seed, open(paths[2], "a") as resultant:
                                seed_content = seed.read();
                                accum = seed_content + capture
                                resultant.write(accum)
                            seed.close()
                            resultant.close()

                        else: # to owerite the appended text
                            with open(paths[2], "w") as file:
                                file.write(capture)
                            file.close()
                    else:
                        print("Trying again with file! \n")
            except Exception as e:
                print(f"Exception Occurred: {e} \n")

        else:
            # Iterating type to determine weather the type is file or dir
            for type in types:
                if type == 'file':
                        with open(paths[counter], "r+") as file:
                            if '-n' in input: 
                                for line in file.readlines():
                                    accumulator += (f"{line_number}: {line}\n")
                                    line_number += 1
                            else: accumulator += file.read() # populating accumulator
                            counter += 1
                        file.close() # closing file to free up resources
                else:
                    print(f"Path {counter} is directory not file \n")
            
            # printing result finally
            print(f"--------files content--------\n {"empty" if not accumulator else accumulator}")

    except Exception as e:
        print("Exception Occurred: ", e)

def check_connection(self, input):
    host = input.split(' ')[1].strip();

    try:      
        result = ping_network(host)

        if result is None:
            print(f"Ping to {host} failed!")
        else:
            print(f"{host} {result*1000:.2f}ms")
    except Exception as err:
        print(err)


def make_request(self, input):
    url = input.split(' ')[1].strip();
    
    try:      
        response = requests.get(url)

        if response is None:
            print(f"Host is unavailable right now!")
        else:
            print(f"{response.text}")
    except requests.exceptions.RequestException as err:
        print(err)


def package_manager(self, input):
    url = input.split(' ')[1].strip();
    try:
        filename = wget.download(url)
        print(f"\nDownloaded to: {filename}")
    except Exception as e:
        print(f"Download failed: {e}")




# / ********************************************************************************************************************* /
# Here are The implemntation of flags


# Show all the supported keywords
def helpme(self, input):
    try:
        print(" \n Supported commands: \n ----------------------------------------------------------------------------- \n")
        for e in keys:
            print(f"{  e["command"]:<8}        {e["description"]}\n")  
    except Exception as err:
         print("Error while performing operation. Try again!") 




# / ********************************************************************************************************************* /

# Dictionary of helper funtions. WHY? Cause it helps in customizability of shell

core_function_mapping = {
    "directories_exploration" : directories_exploration,
    "change_directory" : change_directory,
    "current_wording_directory": current_wording_directory,
    "whoami": whoami,
    "halt" : halt,
    "move": move,
    "copy": copy,
    "rename": rename,
    "delete_anthing": delete_anthing,
    "clear_console": clear_console,
    "process_file_content": process_file_content,
    "check_connection": check_connection,
    "make_request": make_request,
    "package_manager": package_manager,
    "helpme": helpme,
}

