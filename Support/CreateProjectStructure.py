import os

# Define base project path
base_path = "C:/Users/jlawrence/OneDrive - Photronics/Source/DocuTech_ai"

# Define project structure
project_structure = {
    "README.md": "# DocuTech_ai\n\nA comprehensive AI system for generating professional IT documentation and training materials.",
    ".gitignore": "virtual_env/\n__pycache__/\n*.pyc\n.env",
    "setup.py": """from setuptools import setup, find_packages

setup(
    name="DocuTech_ai",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    description="AI-powered documentation and training material generator.",
    author="Jason Lawrence",
    python_requires=">=3.8",
)
""",
    "requirements.txt": "numpy\npandas\nflask\n",
    "docutech_ai/__init__.py": "",
    "docutech_ai/main.py": """def main():
    print("Welcome to DocuTech_ai")

if __name__ == "__main__":
    main()
""",
    "docutech_ai/utils.py": """def helper_function():
    return "This is a helper function."
""",
    "docutech_ai/config.py": """CONFIG = {
    'version': '1.0.0',
    'author': 'Jason Lawrence'
}
""",
    "docutech_ai/models/__init__.py": "",
    "docutech_ai/models/document_model.py": """class DocumentModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def summary(self):
        return f"Document: {self.title[:50]}..."
""",
    "docutech_ai/tests/__init__.py": "",
    "docutech_ai/tests/test_main.py": """import unittest
from docutech_ai.main import main

class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertIsNone(main())

if __name__ == "__main__":
    unittest.main()
""",
    "docs/architecture.md": "# Architecture\n\nDetails about the system architecture.",
    "docs/user_guide.md": "# User Guide\n\nInstructions on using DocuTech_ai.",
}

# Function to create the directory structure and populate files
def create_project_structure(base_path, structure):
    for file_path, content in structure.items():
        full_path = os.path.join(base_path, file_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w") as f:
            f.write(content)

# Create the project structure
create_project_structure(base_path, project_structure)

base_path  # Return the project base path for verification
