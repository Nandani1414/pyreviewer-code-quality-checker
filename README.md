# PyReviewer – Automated Code Quality Checker

A lightweight static-analysis tool built in Python that scans any Python file and flags common code-quality issues — before you even submit it for a code review. It checks for style violations, unused imports, overly complex functions, and missing documentation, then prints a clear, line-by-line report.

## Why I built this

Code reviews and maintaining code quality are a key part of any software engineering workflow. This tool automates the first pass of a code review — catching common issues early so developers can fix them before a teammate even looks at the code, saving review time and keeping the codebase clean and maintainable.

## Features

- **Line length check** — flags lines that exceed 79 characters (PEP 8 standard)
- **Unused import detection** — flags imports that are never used in the file
- **Function complexity check** — flags functions longer than 30 lines, suggesting they be split up
- **Missing docstring check** — flags functions and classes that don't have a description
- Generates a clean, sorted report showing the line number, issue category, and message for every problem found

## Tech Stack

- **Language:** Python 3
- **Core module:** `ast` (Abstract Syntax Tree) — Python's built-in tool for parsing and analyzing code structure
- **Concepts used:** Object-Oriented Programming (OOP), static code analysis, file handling, software design principles (single-responsibility classes)

## How It Works

The project is built around two classes:

- **`Issue`** — represents a single problem found in the code (line number, category, message)
- **`CodeReviewer`** — does the actual analysis: reads the file, parses it into an AST, and runs each check (line length, unused imports, long functions, missing docstrings)

Python's `ast` module converts the source code into a tree structure that represents its logical layout — every function, class, and statement becomes a node in that tree. This lets the tool reliably identify functions and classes anywhere in the file, rather than relying on fragile text-matching.

## How to Run

**Requirements:** Python 3 installed on your system (no external libraries needed — `ast` comes built-in with Python).

1. Clone or download this repository
2. Open a terminal in the project folder
3. Run the tool against any Python file you want to check:
   ```
   python pyreviewer.py path/to/your_script.py
   ```

## Example Usage

```
python pyreviewer.py pyreviewer.py

Code Review Report: pyreviewer.py
==================================================
  Line 18   [DOCS] Class 'Issue' has no docstring
  Line 43   [STYLE] Line exceeds 79 characters
  Line 46   [DOCS] Function 'check_unused_imports' has no docstring

Total issues found: 18
```

## Possible Future Improvements

- Add an auto-fix option for simple issues (e.g., trimming trailing whitespace)
- Add support for checking an entire folder of files at once
- Turn it into a pre-commit Git hook so checks run automatically before every commit
- Export the report as an HTML or Markdown file

## Author

**Nandani Kumari**
[GitHub](https://github.com/Nandani1414) • [LinkedIn](https://www.linkedin.com/in/nandani-gupta-8425242b3)
