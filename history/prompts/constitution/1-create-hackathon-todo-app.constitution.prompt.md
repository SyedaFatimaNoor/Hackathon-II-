---
id: 1
title: Create Hackathon Todo App Constitution
stage: constitution
date_iso: 2025-12-30
surface: agent
model: Qwen
feature: none
branch: main
user: Bilal
command: /sp.constitution
labels:
  - constitution
  - hackathon-todo
  - python
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
  - .specify/memory/constitution.md
  - pyproject.toml
  - history/prompts/constitution/1-create-hackathon-todo-app.constitution.prompt.md
tests_yaml: []
prompt_text: |
  /sp.constitution Project Name: Hackathon Todo App (Phase 1)

  Vision:
  Develop a robust Command-Line Interface (CLI) Todo application that serves as the foundation for future cloud-native evolution.

  Technology Constraints:
  1. Language: Python 3.13+ strictly.
  2. Storage: In-Memory data storage (using Python Lists and Dictionaries). No Database, No File I/O allowed in Phase 1.
  3. Dependencies: Zero external dependencies. Use only Python Standard Library (os, sys, typing, etc.).

  Code Quality Standards:
  1. Type Hints: Every function MUST have return types and argument types (e.g., def add_task(title: str) -> bool).
  2. Documentation: Use Docstrings for all classes and functions.
  3. Compliance: Code must strictly follow PEP 8 style guidelines.

  Architectural Rules:
  1. Modularity: Code must be modular. Separate logic for Input, Display, and Data Management.
  2. Structure: All source code MUST reside inside the `src/` directory.
  3. User Experience: The app must have a simple loop (While True) that allows users to perform multiple actions until they explicitly choose to exit.

  Non-Negotiables:
  1. Do not create any database connection strings or ORM models.
  2. Do not install any external packages via pip.
response_text: |
  ## Final Summary

  I have successfully updated the project constitution based on your requirements. Here's the summary:

  - **New Version**: 1.0.0 (initial version)
  - **Bump Rationale**: This is the first version of the constitution for the Hackathon Todo App (Phase 1), establishing the foundational principles for the project
  - **Files Updated**: 
    - `.specify/memory/constitution.md` - Contains the complete constitution with all 6 principles
    - `pyproject.toml` - Updated to reflect Python 3.13+ requirement and project description
  - **Suggested Commit Message**: `docs: create constitution for Hackathon Todo App Phase 1 (Python 3.13+, zero dependencies, in-memory storage)`

  The constitution now includes 6 core principles based on your requirements:
  1. Python 3.13+ Strict Compliance
  2. Zero External Dependencies
  3. In-Memory Data Storage (Phase 1)
  4. Mandatory Type Hints
  5. PEP 8 Style Compliance
  6. Modular Architecture

  Additionally, it includes sections on Documentation Requirements, Development Workflow, and Governance rules.

  All templates have been checked for consistency with the new principles, and the README and pyproject.toml files have been updated to align with the constitution.

  The constitution is now ready for use in your project development.
outcome: |
  Successfully created the Hackathon Todo App constitution based on the specified requirements, including 6 core principles covering Python version compliance, zero external dependencies, in-memory storage, mandatory type hints, PEP 8 compliance, and modular architecture.
evaluation: |
  The constitution has been created with all required principles and properly integrated with the project structure. All validation checks passed, and the appropriate files have been updated to align with the new constitution.
---
