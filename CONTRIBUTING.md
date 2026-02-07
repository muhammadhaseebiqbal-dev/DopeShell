# 🤝 Contributing to DopeShell

Thank you for your interest in contributing to DopeShell! We welcome contributions from developers of all skill levels. This guide will help you get started.

---

## 📋 Table of Contents

- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Contribute](#how-to-contribute)
- [Adding New Commands](#adding-new-commands)
- [Code Standards](#code-standards)
- [Pull Request Process](#pull-request-process)
- [Reporting Issues](#reporting-issues)

---

## 🚀 Getting Started

Before you begin contributing, please:

1. Read the main [README.md](README.md) to understand the project
2. Check existing [issues](https://github.com/muhammadhaseebiqbal-dev/dopeshell/issues) to see if your idea/bug is already being worked on
3. Join discussions to understand ongoing development

---

## 💻 Development Setup

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/muhammadhaseebiqbal-dev/dopeshell.git
cd dopeshell
```

### 2. Create a Development Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b bugfix/issue-description
```

### 3. Install Dependencies

**On Linux:**
```bash
pip3 install -r requirements.txt
```

**On Windows:**
```powershell
pip install -r requirements.txt
```

### 4. Test Your Setup

```bash
python main.py
```

---

## 🔧 How to Contribute

### Types of Contributions We Welcome

- 🐛 **Bug Fixes** - Fix issues or bugs in existing functionality
- ✨ **New Features** - Add new commands or capabilities
- 📚 **Documentation** - Improve README, add examples, write tutorials
- 🎨 **UI/UX** - Enhance the shell interface and user experience
- ⚡ **Performance** - Optimize existing code
- 🧪 **Testing** - Add unit tests or integration tests
- 🔍 **Code Review** - Review pull requests from other contributors

---

## ➕ Adding New Commands

DopeShell uses a modular architecture. Here's how to add a new command:

### Step 1: Add Command Keyword

Edit `dopeshell/keywords.py` and add your command to the `keys` list:

```python
{
    "command": "yourcommand",
    "description": "description of what your command does"
}
```

### Step 2: Implement the Function

Edit `dopeshell/components/core.py` and create your function:

```python
def your_function_name(self, input):
    """
    Brief description of what this function does
    
    Args:
        self: DopeShell instance
        input: Full command string from user
    """
    try:
        # Parse the input
        args = input.split(' ')[1:]  # Get arguments after command
        
        # Your implementation here
        # ...
        
        print("✅ Operation successful!")
    except Exception as err:
        print(f"⚠️ Error: {err}")
```

### Step 3: Register the Function

Add your function to the `core_function_mapping` dictionary in `dopeshell/components/core.py`:

```python
core_function_mapping = {
    # ... existing mappings ...
    "your_function_name": your_function_name,
}
```

### Step 4: Test Your Command

```bash
python main.py
# Try your new command
yourcommand arg1 arg2
```

---

## 📐 Code Standards

### Python Style Guide

- Follow [PEP 8](https://pep8.org/) style guidelines
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions focused on a single responsibility

### Example Code Style

```python
# Good ✅
def calculate_file_size(file_path):
    """Calculate size of a file in bytes"""
    try:
        return os.path.getsize(file_path)
    except OSError as e:
        print(f"Error accessing file: {e}")
        return 0

# Avoid ❌
def calc(f):
    return os.path.getsize(f)
```

### Error Handling

- Always use try-except blocks for operations that might fail
- Provide clear, user-friendly error messages
- Use emoji indicators: ✅ for success, ⚠️ for warnings/errors

### Cross-Platform Compatibility

- Test your code on both Windows and Linux if possible
- Use `os.path` functions for path operations (they're cross-platform)
- Check `self.platform` when platform-specific code is needed

```python
if self.platform == "Windows":
    # Windows-specific code
else:
    # Linux-specific code
```

---

## 🔄 Pull Request Process

### Before Submitting

1. **Test thoroughly** - Test your changes on your local machine
2. **Check existing code** - Ensure your code follows the existing style
3. **Update documentation** - If you add features, update README.md
4. **No breaking changes** - Ensure backward compatibility

### Submitting Your PR

1. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: brief description of your changes"
   ```

2. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

3. **Create Pull Request**
   - Go to the original repository on GitHub
   - Click "New Pull Request"
   - Select your branch
   - Fill in the PR template with:
     - **Description** of changes
     - **Why** the change is needed
     - **How** you tested it
     - **Screenshots** (if applicable)

### Commit Message Format

Use clear, descriptive commit messages:

```
Add: new command for file compression
Fix: path resolution bug on Windows
Update: documentation for network commands
Refactor: simplify directory navigation logic
```

---

## 🐛 Reporting Issues

### Before Creating an Issue

- Search existing issues to avoid duplicates
- Verify the issue exists on the latest version
- Collect relevant information (OS, Python version, error messages)

### Creating a Good Issue

Include:

1. **Clear Title** - Brief description of the problem
2. **Description** - Detailed explanation of the issue
3. **Steps to Reproduce** - How to trigger the bug
4. **Expected Behavior** - What should happen
5. **Actual Behavior** - What actually happens
6. **Environment**:
   - Operating System: Windows 10 / Ubuntu 22.04 / etc.
   - Python Version: 3.9.5
   - DopeShell Version: (commit hash or release)
7. **Screenshots/Logs** - If applicable

### Example Issue

```markdown
**Title:** `snap` command fails with directories containing spaces

**Description:**
When using the snap command to delete a directory with spaces in its name,
the command fails with a path error.

**Steps to Reproduce:**
1. Create a folder named "My Documents"
2. Run: snap "My Documents"
3. Error occurs

**Expected:** Directory should be deleted
**Actual:** Error: Could not find path

**Environment:**
- OS: Windows 11
- Python: 3.10.2
```

---

## 🌟 Code Review Process

- All submissions require review before merging
- Reviewers may suggest changes or improvements
- Be patient and responsive to feedback
- Maintainers will merge once approved

---

## 💬 Communication

- **Issues** - For bugs and feature requests
- **Pull Requests** - For code contributions
- **Discussions** - For questions and ideas

---

## 🎯 Priority Areas

Current areas where we especially welcome contributions:

1. **Testing Framework** - Add unit tests and integration tests
2. **Error Handling** - Improve error messages and edge case handling
3. **Documentation** - More examples and tutorials
4. **New Commands** - Useful file/system operations
5. **Performance** - Optimize existing commands

---

## 📜 License

By contributing to DopeShell, you agree that your contributions will be licensed under the MIT License.

---

## 🙏 Thank You!

Every contribution, no matter how small, makes DopeShell better. We appreciate your time and effort!

**Happy Coding! 🚀**
