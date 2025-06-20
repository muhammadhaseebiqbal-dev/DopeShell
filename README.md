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

[![Status](https://img.shields.io/badge/Status-Core%20Development-yellow?style=for-the-badge&logo=python)](https://github.com)
[![Platform](https://img.shields.io/badge/Platform-Cross--Platform-blue?style=for-the-badge&logo=windows)](https://github.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Author](https://img.shields.io/badge/Author-Muhammad%20Haseeb%20Iqbal-red?style=for-the-badge)](https://github.com)

*A minimalistic, cross-platform shell with custom command mapping and future AI integration*

**Absolutely Scalable System Manipulator**

</div>

---

## 🚀 **Overview**

**DopeShell** is a lightweight, custom shell implementation written in Python that provides essential file system navigation commands with a sleek interface. Built with extensibility in mind, it features a modular component architecture and cross-platform compatibility.

### ✨ **Key Features**

- 🖥️ **Cross-Platform Support** - Works seamlessly on Windows and Linux
- 🏗️ **Modular Architecture** - Clean separation with engine/components structure
- 🎨 **ASCII Branding** - Eye-catching startup banner with system diagnostics
- 🔧 **Extensible Design** - Easy to add new commands via component system
- ⚡ **Lightweight** - Minimal dependencies, maximum performance
- 🛡️ **Error Handling** - Robust error management with user-friendly messages
- 📁 **Advanced File Operations** - Complete file/directory manipulation suite

---

## 📁 **Project Structure**

```
DopeShell/
├── 📄 main.py                        # Main entry point - application launcher
├── 📄 README.md                      # Project documentation
├── 📄 requirments.txt                # Python dependencies
├── 📄 LICENSE                        # MIT license file
├── 📄 .gitignore                     # Git ignore rules
├── 📁 engine/                        # Core shell engine
│   ├── 📄 dopeshell.py              # Main DopeShell class implementation
│   └── 📁 components/               # Modular components
│       ├── 📄 core.py               # Command implementations
│       ├── 📄 utils.py              # Utility functions & path parsing
│       └── 📄 imports.py            # Import management
└── 📁 .git/                         # Git repository metadata
```

---

## 🛠️ **Installation & Setup**

### Prerequisites
- Python 3.6 or higher
- Git (optional)

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/HaseebIqbal1199/DopeShell.git
   cd DopeShell
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirments.txt
   ```

3. **Run DopeShell**
   ```bash
   python main.py
   ```

---

## 🎯 **Currently Supported Commands**

| Command | Description | Usage Example |
|---------|-------------|---------------|
| `spitdir` | List files and folders in current directory | `spitdir` |
| `dive` | Change directory to specified path | `dive 'C:/Users/Documents'` |
| `reveal` | Show present working directory path | `reveal` |
| `whoami` | Display current user account name | `whoami` |
| `halt` | Terminate the current shell session | `halt` |
| `throw` | Move file/directory from source to destination | `throw 'source.txt' 'destination/'` |
| `clone` | Copy file/directory from source to destination | `clone 'file.txt' 'backup/file.txt'` |
| `swap` | Rename files and folders | `swap 'oldname.txt' 'newname.txt'` |
| `snap` | Delete files and directories | `snap 'unwanted_file.txt'` |
| `wipe` | Clear the console screen | `wipe` |
| `--helpme` | Show list of all supported commands | `--helpme` |

### 📝 **Command Examples**

```bash
# Navigation and Directory Operations
dive Documents                    # Navigate to Documents folder
dive 'C:/Program Files'          # Navigate using absolute path
spitdir                          # List current directory contents
reveal                           # Show current working directory

# File and Directory Management
clone 'report.pdf' 'backup/'     # Copy file to backup folder
throw 'temp.txt' 'archive/'      # Move file to archive folder
swap 'draft.docx' 'final.docx'   # Rename file
snap 'old_project/'              # Delete entire directory

# System Operations
whoami                           # Get current user information
wipe                             # Clear console screen
--helpme                         # View all available commands
halt                             # Exit DopeShell
```

---

## ⚙️ **Architecture Overview**

### 🏗️ **Core Components**

```python
# Main Entry Point
main.py                          # Application launcher with main() function

# Core Engine
engine/dopeshell.py             # Main DopeShell class
    def __init__()                # Initialize shell environment  
    def diagnostic()              # System health check
    def executeCommand()          # Command execution engine
    def asciiArt()               # Display ASCII banner
    def goToRoot()               # Handle root directory navigation
    def _init_env()              # Environment initialization with diagnostics

# Component Modules  
engine/components/
    core.py                      # All command implementations
    utils.py                     # Path parsing utilities (pathTokeniser functions)
    imports.py                   # Centralized import management
```

### 🔧 **Key Design Patterns**

- **Modular Architecture**: Clean separation of concerns with engine/components
- **Command Mapping**: Dictionary-based command-to-function mapping in engine
- **Path Intelligence**: Smart path parsing with file/directory type detection
- **Cross-Platform Compatibility**: Automatic Windows/Linux command adaptation
- **Error Resilience**: Comprehensive exception handling with user feedback

---

## 🎨 **Interface Design**

### Startup Sequence
```
Checking instance Config!
Current Platform check "Windows" ✅
Dope Shell is working perfectly ✅
Checking system integrity ✅

[ASCII BANNER DISPLAY]

~/Desktop/DopeShell: 
```

### Command Prompt Format
- **Windows**: `~/path/to/directory: `
- **Linux**: `~/path/to/directory: `

---

## 🚧 **Development Status**

### ✅ **Completed Features**
- [x] Modular shell framework with component architecture
- [x] Cross-platform file operations (Windows/Linux)
- [x] Complete file manipulation suite (copy, move, rename, delete)
- [x] Directory navigation and listing
- [x] Console management utilities
- [x] Advanced path parsing with type detection
- [x] Error handling and user feedback system
- [x] ASCII branding with system diagnostics
- [x] Session management and lifecycle control

### 🔮 **Future Roadmap**

#### Phase 1: Extended Command Support
- [x] File manipulation commands (`throw`, `clone`, `swap`, `snap`)
- [x] Console utilities (`wipe`)
- [ ] Text processing commands (`cat`, `grep`, `find`)
- [ ] System monitoring commands (`ps`, `top`, `df`)
- [ ] Network utilities (`ping`, `curl`, `wget`)

#### Phase 2: Advanced Features
- [ ] Command history and autocomplete
- [ ] Tab completion for paths
- [ ] Custom aliases and shortcuts
- [ ] Script execution support
- [ ] Environment variable management
- [ ] Configuration file support

#### Phase 3: AI Integration 🤖
- [ ] **Agentic AI Assistant** for system management
- [ ] Natural language command interpretation
- [ ] Intelligent file organization
- [ ] Automated system optimization
- [ ] Predictive command suggestions
- [ ] AI-powered troubleshooting

#### Phase 4: Enterprise Features
- [ ] Multi-user support
- [ ] Permission management
- [ ] Logging and audit trails
- [ ] Plugin architecture
- [ ] Remote system management

---

## 🔧 **Technical Implementation**

### Path Parsing System
DopeShell features an intelligent path parsing system in `utils.py`:

- **pathTokeniserMulti()**: Handles commands with source and destination paths
- **pathTokenizerSingle()**: Handles commands with single path arguments
- **Type Detection**: Automatically identifies files vs directories using regex patterns
- **Cross-Platform**: Handles both Windows (`\`) and Unix (`/`) path separators

### Command Engine
The command execution system maps user input to specific functions:

```python
self.engine = {
    "spitdir": spitdir,    "dive": dive,      "halt": halt,
    "whoami": whoami,      "--helpme": helpme, "reveal": reveal,
    "clone": clone,        "throw": throw,     "swap": swap,
    "snap": snap,          "wipe": wipe
}
```

---

## 🐛 **Known Issues & Limitations**

### Current Limitations
- Path parsing requires quotes for paths with spaces
- No command history persistence
- No tab completion
- Limited to basic file operations

### Reported Issues
- Some Unicode characters may not display correctly in all terminals
- Path resolution edge cases with nested directories
- Error messages could be more descriptive for complex scenarios

---

## 🤝 **Contributing**

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

### 📋 **Contribution Guidelines**
- Follow PEP 8 style guide
- Add comments for complex logic
- Update documentation for new features
- Test on both Windows and Linux
- Add new commands to both `core.py` and `keywords` array

---

## 📜 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 **Author**

**Muhammad Haseeb Iqbal**

*Core Developer & Project Maintainer*

- 🌐 Building the future of interactive shells
- 🚀 Passionate about system tools and AI integration
- 💡 Always open to collaboration and new ideas

---

## 🙏 **Acknowledgments**

- Python community for excellent cross-platform libraries
- ASCII art generators for the beautiful banner
- Open source contributors worldwide

---

<div align="center">

### ⭐ **If you found DopeShell useful, please consider giving it a star!**

*Built with ❤️ by Muhammad Haseeb Iqbal*

---

**Status**: `Core Development` | **Next Release**: `v1.1.0` | **Last Updated**: `June 2025`

</div>
