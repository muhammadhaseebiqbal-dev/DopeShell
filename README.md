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

**DopeShell** is a lightweight, custom shell implementation written in Python that provides essential file system navigation commands with a sleek interface. Built with extensibility in mind, it features a JSON-based command mapping system and cross-platform compatibility.

### ✨ **Key Features**

- 🖥️ **Cross-Platform Support** - Works seamlessly on Windows and Linux
- 🗂️ **Custom Command Mapping** - JSON-based command configuration
- 🎨 **ASCII Branding** - Eye-catching startup banner
- 🔧 **Extensible Architecture** - Easy to add new commands
- ⚡ **Lightweight** - Minimal dependencies, maximum performance
- 🛡️ **Error Handling** - Robust error management system

---

## 📁 **Project Structure**

```
DopeShell/
├── 📄 source.py              # Main shell implementation
├── 📄 requirments.txt        # Python dependencies
├── 📄 README.md              # This documentation
├── 📁 mapping/
   └── 📄 mapping.json       # Command definitions and descriptions
```

---

## 🛠️ **Installation & Setup**

### Prerequisites
- Python 3.6 or higher
- Git (optional)

### Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd DopeShell
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirments.txt
   ```

3. **Run DopeShell**
   ```bash
   python source.py
   ```

---

## 🎯 **Currently Supported Commands**

| Command | Description | Usage |
|---------|-------------|--------|
| `spitdir` | List files and folders in current directory | `spitdir` |
| `dive` | Change directory to specified path | `dive /path/to/directory` |
| `reveal` | Show present working directory path | `reveal` |
| `whoami` | Display current user account name | `whoami` |
| `endsesh` | Terminate the current shell session | `endsesh` |
| `--helpme` | Show list of all supported commands | `--helpme` |

### 📝 **Command Examples**

```bash
# Navigate to a directory
dive Documents
dive 'C:/Program Files'

# List directory contents
spitdir

# Check current location
reveal

# Get user information
whoami

# View all commands
--helpme

# Exit shell
endsesh
```

---

## ⚙️ **Core Architecture**

### 🏗️ **DopeShell Class Structure**

```python
class DopeShell:
    def __init__(self)              # Initialize shell environment
    def diagnostic(self)            # System health check
    def loadInstructionSet(self)    # Load command mappings from JSON
    def asciiBranding(self)         # Display ASCII banner
    def executeCommand(self, cmd)   # Command execution engine
```

### 🔧 **Key Components**

- **Command Parser**: Interprets user input and maps to functions
- **Cross-Platform Handler**: Adapts commands for Windows/Linux
- **JSON Configuration**: External command mapping for easy extensibility
- **Error Management**: Comprehensive error handling and user feedback

---

## 🎨 **Interface Design**

### Startup Sequence
```
Checking instance Config!
Current Platform check "Windows" ✅
Dope Shell is working perfectly ✅
Instruction Set loaded successfully ✅

[ASCII BANNER DISPLAY]

~/Desktop/DopeShell: 
```

### Command Prompt Format
- **Windows**: `~/path/to/directory: `
- **Linux**: `~/path/to/directory `

---

## 🚧 **Development Status**

### ✅ **Completed Features**
- [x] Basic shell framework
- [x] Cross-platform file operations
- [x] JSON command mapping system
- [x] Error handling and validation
- [x] ASCII branding and UI
- [x] Core navigation commands

### 🔮 **Future Roadmap**

#### Phase 1: Extended Command Support
- [ ] File manipulation commands (`copy`, `move`, `delete`)
- [ ] Text processing commands (`cat`, `grep`, `find`)
- [ ] System monitoring commands (`ps`, `top`, `df`)
- [ ] Network utilities (`ping`, `curl`, `wget`)

#### Phase 2: Advanced Features
- [ ] Command history and autocomplete
- [ ] Tab completion for paths
- [ ] Custom aliases and shortcuts
- [ ] Script execution support
- [ ] Environment variable management

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

## 🔧 **Configuration**

### Adding Custom Commands

Edit `mapping/mapping.json` to add new commands:

```json
{
    "command": "your_command",
    "description": "Description of what your command does"
}
```

Then implement the command logic in `source.py` within the `executeCommand` method.

---

## 🐛 **Known Issues & Limitations**

### Current Limitations
- Limited command set (6 core commands)
- No command history
- No tab completion
- Basic error messages

### Reported Issues
- Path handling with spaces requires quotes
- Some Unicode characters may not display correctly
- Limited customization options

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
