"""
PyReviewer - Automated Code Quality Checker
---------------------------------------------
Scans Python files and flags common code-quality issues so a developer
can fix them before requesting a code review (PEP 8 line length, unused
imports, overly long functions, missing docstrings).

Demonstrates: Python's `ast` module, OOP design, file handling,
software design principles (single-responsibility classes).

Run: python pyreviewer.py path/to/your_script.py
"""

import ast
import sys


class Issue:
    def __init__(self, line, category, message):
        self.line = line
        self.category = category
        self.message = message

    def __str__(self):
        return f"  Line {self.line:<4} [{self.category}] {self.message}"


class CodeReviewer:
    MAX_LINE_LENGTH = 79
    MAX_FUNCTION_LINES = 30

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, "r") as f:
            self.source = f.read()
        self.lines = self.source.splitlines()
        self.issues = []

    def check_line_length(self):
        for i, line in enumerate(self.lines, start=1):
            if len(line) > self.MAX_LINE_LENGTH:
                self.issues.append(
                    Issue(i, "STYLE", f"Line exceeds {self.MAX_LINE_LENGTH} characters")
                )

    def check_unused_imports(self):
        tree = ast.parse(self.source)
        imported_names = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imported_names.append((alias.asname or alias.name, node.lineno))
            elif isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    imported_names.append((alias.asname or alias.name, node.lineno))

        for name, lineno in imported_names:
            base_name = name.split(".")[0]
            occurrences = self.source.count(base_name)
            if occurrences <= 1:  # only appears in the import line itself
                self.issues.append(
                    Issue(lineno, "UNUSED_IMPORT", f"'{base_name}' appears unused")
                )

    def check_long_functions(self):
        tree = ast.parse(self.source)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                length = (node.end_lineno or node.lineno) - node.lineno
                if length > self.MAX_FUNCTION_LINES:
                    self.issues.append(
                        Issue(node.lineno, "COMPLEXITY",
                              f"Function '{node.name}' is {length} lines long "
                              f"(consider splitting)")
                    )

    def check_missing_docstrings(self):
        tree = ast.parse(self.source)
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                if not ast.get_docstring(node):
                    kind = "class" if isinstance(node, ast.ClassDef) else "function"
                    self.issues.append(
                        Issue(node.lineno, "DOCS",
                              f"{kind.capitalize()} '{node.name}' has no docstring")
                    )

    def run_all_checks(self):
        self.check_line_length()
        self.check_unused_imports()
        self.check_long_functions()
        self.check_missing_docstrings()
        self.issues.sort(key=lambda i: i.line)
        return self.issues

    def print_report(self):
        print(f"\nCode Review Report: {self.filepath}")
        print("=" * 50)
        if not self.issues:
            print("  No issues found. Looks clean!")
        else:
            for issue in self.issues:
                print(issue)
            print(f"\nTotal issues found: {len(self.issues)}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python pyreviewer.py <path_to_python_file>")
        return

    filepath = sys.argv[1]
    reviewer = CodeReviewer(filepath)
    reviewer.run_all_checks()
    reviewer.print_report()


if __name__ == "__main__":
    main()
