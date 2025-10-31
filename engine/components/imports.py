# Standard library imports
import platform
import subprocess
from time import sleep

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