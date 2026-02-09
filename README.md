# 🔥 DopeShell

```
    ██████╗  ██████╗ ██████╗ ███████╗     ███████╗██╗  ██╗███████╗██╗     ██╗     
    ██╔══██╗██╔═══██╗██╔══██╗██╔════╝     ██╔════╝██║  ██║██╔════╝██║     ██║     
    ██║  ██║██║   ██║██████╔╝█████╗       ███████╗███████║█████╗  ██║     ██║     
    ██║  ██║██║   ██║██╔═══╝ ██╔══╝       ╚════██║██╔══██║██╔══╝  ██║     ██║     
    ██████╔╝╚██████╔╝██║     ███████╗     ███████║██║  ██║███████╗███████╗███████╗
    ╚═════╝  ╚═════╝ ╚═╝     ╚══════╝     ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝
```

<div align="center">

[![Status](https://img.shields.io/badge/Status-Core%20Development-yellow?style=for-the-badge&logo=python)](https://github.com/muhammadhaseebiqbal-dev/dopeshell)
[![Platform](https://img.shields.io/badge/Platform-Cross--Platform-blue?style=for-the-badge&logo=windows)](https://github.com/muhammadhaseebiqbal-dev/dopeshell)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.6+-blue?style=for-the-badge&logo=python)](https://www.python.org)

*A minimalistic, cross-platform shell with custom command mapping*

</div>

---

## 📖 Introduction

**DopeShell** is a lightweight, custom shell implementation written in Python that provides essential file system operations with a sleek interface. Built with extensibility in mind, it features a modular component architecture and cross-platform compatibility for both Windows and Linux systems.

### ✨ Key Features

- 🖥️ **Cross-Platform** - Works seamlessly on Windows and Linux
- 🏗️ **Modular Design** - Clean separation with engine/components structure
- 🎨 **Custom Commands** - Intuitive command names for common operations
- 🔧 **Extensible** - Easy to add new commands via component system
- ⚡ **Lightweight** - Minimal dependencies, maximum performance

---

## 🛠️ Installation

### Install via Pip (Recommended)
You can easily install DopeShell using pip:

```bash
pip install dopeshell-cli
```

### Add Python Scripts to Your PATH (Mandatory)

Before running dopeshell from anywhere in your terminal, ensure that the Python Scripts directory is added to your system’s PATH.

#### **Windows**

1. **Find your Scripts path:**  
   It's usually one of:
   - `C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python<version>\Scripts`
   - Or run this in Command Prompt to find it:
     ```bash
     python -m site --user-base
     ```
     Add `\Scripts` at the end of the printed path.

2. **Add to PATH:**
   - Search for "Environment Variables" in the Start menu.
   - Click "Environment Variables".
   - Under "User variables", select `Path`, then click "Edit".
   - Click "New" and paste your Scripts path.
   - Click OK to close all dialogs.

3. **Restart your terminal** for changes to take effect.

#### **Linux / macOS**

1. Open your terminal.
2. Find your Python scripts path by running:
   ```bash
   python3 -m site --user-base
   ```
   The Scripts path will be:  
   `<the above path>/bin`
3. Add it to your `PATH`. For example, if your scripts are in `~/.local/bin`:
   ```bash
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
   source ~/.bashrc
   ```
   > For zsh, replace `.bashrc` with `.zshrc`.

4. Verify:
   ```bash
   which dopeshell
   ```
   It should show the path if installed and set correctly.

Now you can run:

```bash
dopeshell
```

from anywhere in your terminal.

---


### Manual Installation (For Development)

1. **Clone the repository**
   ```bash
   git clone https://github.com/muhammadhaseebiqbal-dev/dopeshell.git
   cd dopeshell
   ```

2. **Install dependencies**
   ```bash
   pip install .
   ```

3. **Run DopeShell**
   ```bash
   dopeshell
   ```

---

## 📝 Command List

### Basic Commands

| Command | Format | Description |
|---------|--------|-------------|
| `ld` | `ld` | List all files and folders in the current directory |
| `sd` | `sd <path>` | Change directory to the specified path (relative or absolute) |
| `wd` | `wd` | Display the current working directory path |
| `whoami` | `whoami` | Display the current user account name |
| `wipe` | `wipe` | Clear the console screen |
| `halt` | `halt` | Exit and terminate the current shell session |

### File Operations

| Command | Format | Description |
|---------|--------|-------------|
| `proc` | `proc <file>` | Read and display file contents |
| `proc` | `proc -n <file>` | Read file with line numbers |
| `proc` | `proc <file1> <file2> >>> <output>` | Concatenate multiple files into one |
| `proc` | `proc > <file>` | Write user input to a file (overwrite) |
| `proc` | `proc >> <file>` | Append user input to a file |

### File Management

| Command | Format | Description |
|---------|--------|-------------|
| `cpy` | `cpy <source> <destination>` | Copy file or directory from source to destination |
| `mov` | `mov <source> <destination>` | Move file or directory from source to destination |
| `rn` | `rn <old_name> <new_name>` | Rename files or folders |
| `snap` | `snap <path>` | Delete files or directories |

### Network Commands

| Command | Format | Description |
|---------|--------|-------------|
| `ping` | `ping <host>` | Test network connectivity to a host |
| `curl` | `curl <url>` | Fetch and display content from a URL |
| `dsp` | `dsp <url>` | Download file from URL (DopeShell Package Manager) |

### Help

| Command | Format | Description |
|---------|--------|-------------|
| `--helpme` | `--helpme` | Display list of all supported commands |

---

## 💡 Usage Examples

```bash
# Navigate to a directory
sd Documents

# List files
ld

# Read a file
proc myfile.txt

# Copy a file
cpy file.txt backup/file.txt

# Move a file
mov file.txt documents/file.txt

# Rename a file
rn oldname.txt newname.txt

# Delete a file
snap unwanted.txt

# Check network connectivity
ping google.com

# Download a file
dsp https://example.com/file.zip
```

---

## 🤝 Contributing

Want to contribute? Check out our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to help improve DopeShell!

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Muhammad Haseeb Iqbal**  
GitHub: [@muhammadhaseebiqbal-dev](https://github.com/muhammadhaseebiqbal-dev)
