# Algorithms & Data Structures MiniProjects (Python)

## SCOPE OF THE REPO
This repository contains mini-projects for **Algorithms and Data Structures** implemented in **Python**.  
Each mini-project is designed as a set of **connected tasks**, where the output of one task serves as input for the next.  
The main goal is to help students practice:

- Strings, Lists, Tuples, Sets
- Queue, Deque, Stack
- Dictionaries
- Sorting & Searching Algorithms
- Binary Search Trees (BST)
- Graphs and Graph Traversals
- Datastructes implementation, Problem-solving and Algorithm Design

---


## MINI-PROJECTS: 

### Miniproject-1: The Data Heist of Codex-9
The AI system **Codex-9** has been hacked. Fragments of its digital blueprint have been scattered and corrupted across the network.  
Your mission as a Forensic Programmer is to restore it **step by step**.

Each function (Task 1–10) represents a part of the restoration process.  
The output from each function becomes the input for the next one.  
Complete all tasks to successfully reboot Codex-9!

---


## INSTRUCTIONS

1. **Team Setup**  
   - Work **individually** or in **teams of 1-3**.
   - Create a copy of the project dir with the name of your team
      ```bash
      cp miniproject-1-codex miniproject-1-codex9-team-alpha
      ```
   - Fill your team info in the file:
     ```python
     TEAM: # Your team's name
     MEMBERS: # List of team members
     ```

2. **Task Completion**  
   - Complete each function according to its **docstring** in project file:
   - For Miniproject-1: (`codex9.py`).  
   - **Do not modify function names, signatures, or docstrings.**  

3. **Testing**  
   - You can test each function individually before moving to the next.  
   - Unit tests are in `test_*.py` and will validate your solutions automatically.

4. **Code Style & Libraries**  
   - Use **only standard Python libraries**.  
   - Ensure your code is **clean, readable, and efficient**.  
   - Comment your code when necessary.

5. **Git & GitHub Workflow**  
   - **Create a new branch** for your work:
     ```bash
     git checkout -b teamname_task_branch
     ```
     - Use a **unique branch name** (team + project).  
       Example: `teamalpha_codex9`
   - **Commit your changes** frequently:
     ```bash
     git add .
     git commit -m "Implement tasks 1-3: decode and organize modules"
     ```
   - **Push your branch** to GitHub:
     ```bash
     git push origin teamalpha_codex9
     ```
   - **Open a Pull Request (PR)**:
     - Target branch: `master`
     - Fill PR description and use the PR template (see below)
   - **Review & Tests**:
     - Automated unit tests will run on the PR.  
     - If tests fail, fix the issues, commit, and update your PR.

6. **Submission**  
   - Once all tasks are complete and tests pass, your PR will be merged.  
   - Make sure your branch is up to date with the base branch before merging.

---

## PR TEMPLATE

Use this template when creating a PR:

```markdown
# PR Title: Codex-9 Mini-Project Submission Team Alpha

## Team Info
- Team: # Your team name
- Members: # List of members

## Summary
Short summary of changes made in this PR.

## Notes
- Any assumptions or clarifications made during implementation.
- Any known issues (if any).
