# Zecpath AI Job Portal
## Coding Standards & Documentation Guidelines

### 1. Purpose
This document defines the coding standards and documentation practices to be followed throughout the Zecpath AI Job Portal project. These standards ensure code consistency, readability, maintainability, and scalability.

---

## 2. Coding Standards

### 2.1 Naming Conventions

#### Variables
- Use snake_case.
- Use meaningful and descriptive names.

Example:

```python
candidate_score = 85
resume_text = ""
```

#### Functions
- Use snake_case.
- Function names should describe the action performed.

Example:

```python
def parse_resume():
    pass

def calculate_ats_score():
    pass
```

#### Classes
- Use PascalCase.

Example:

```python
class ResumeParser:
    pass

class InterviewAgent:
    pass
```

---

### 2.2 Code Formatting

- Follow PEP 8 Python Style Guide.
- Use 4 spaces for indentation.
- Avoid unnecessary blank lines.
- Keep code clean and readable.
- Maximum recommended line length: 100 characters.

---

### 2.3 Comments

- Use comments only when necessary.
- Explain complex logic rather than obvious code.

Example:

```python
# Calculate final ATS score based on weighted criteria
final_score = calculate_score(resume_data)
```

---

### 2.4 Logging

- Use Python's logging module instead of print statements.
- Log important system activities and errors.
- Store logs inside the logs/ directory.

Example:

```python
logger.info("Resume uploaded successfully")
logger.error("Failed to parse resume")
```

---

### 2.5 Error Handling

- Use try-except blocks for critical operations.
- Log all exceptions before handling them.

Example:

```python
try:
    process_resume(file)
except Exception as e:
    logger.error(f"Error processing resume: {e}")
```

---

### 2.6 Testing

- Use pytest for unit testing.
- Every major module should have a corresponding test file.
- Test files should be stored inside the tests/ directory.

Example:

```python
def test_sample():
    assert True
```

---

## 3. Documentation Standards

### 3.1 Module Documentation

Every Python module should begin with a short description.

Example:

```python
"""
Resume Parser Module

Responsible for extracting text and information
from candidate resumes.
"""
```

---

### 3.2 Function Documentation

All functions should include docstrings.

Example:

```python
def parse_resume(file_path):
    """
    Extract text from a resume file.

    Args:
        file_path (str): Path to the resume.

    Returns:
        str: Extracted resume text.
    """
```

---

### 3.3 Project Documentation

The README file must contain:

- Project Overview
- Objectives
- Folder Structure
- Installation Instructions
- Usage Guide
- Contributors
- License Information

---

## 4. Version Control Standards

- Commit changes frequently.
- Use meaningful commit messages.
- Push code regularly to GitHub.
- Create separate branches for major features when required.

Example Commit Messages:

- Initial project setup
- Added logging configuration
- Implemented ATS scoring module
- Added unit tests

---

## 5. Conclusion

Following these coding and documentation standards will ensure consistency, maintainability, and scalability throughout the development of the Zecpath AI Job Portal system.