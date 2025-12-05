"""
=========================================================
  🧩 Mini Project: The Data Heist of Codex-9
=========================================================

TEAM: himikalka
MEMBERS: 24101018 , 24101022

STORY:
The AI system Codex-9 has been hacked. Fragments of its digital blueprint 
have been scattered and corrupted across the network. 
Your mission as the Forensic Programmer is to restore it step by step.

Each function (Task 1–10) represents a part of the restoration process.
The output from each function becomes the input for the next one.
Complete all tasks to successfully reboot Codex-9!

INSTRUCTIONS:
1. Complete each function according to its docstring.
2. Use only standard Python libraries. Do not import external packages.
3. You can test each function individually before proceeding to the next.
4. Do not change the function signatures, docstrings, names & arguments.
5. Ensure your code is clean, well-commented, and efficient.
6. Upon completion, Codex-9 should reboot successfully!
7. After completing all tasks, commit your changes to your branch and raise a pull request. Unit Tests will be executed automatically to validate your solutions.
8. If all tests pass and after your submission is approved, your code will be merged into the master branch.
9. In case that tests fail or you get code reviews, address the issues, commit the changes in your branch and update the pull request.

=========================================================
"""

from collections import deque
import json
import heapq


# =======================================================
# 🧩 TASK 1 — Decode the Fragment (Strings → Lists)
# =======================================================
def decode_fragment(fragment: str) -> list:
    """
    Splits a corrupted string by ';', reverses each segment,
    and returns a list of decoded words.
    
    Arguments:
        fragment (str): A semicolon-separated string of corrupted words.
        
    Returns:
        list: A list of decoded words.

    Example Input:
        "edoc;nohtyp;ataD;erutcurts;smhtiroglA"
    Example Output:
        ['code', 'python', 'Data', 'structure', 'Algorithms']
    """
    parts = fragment.split(";")
    decoded = [p[::-1] for p in parts]

   
    return decoded


# =======================================================
# 🧩 TASK 2 — Organize the Blueprint Segments (Lists → Tuples)
# =======================================================
def organize_segments(words: list, module_numbers: list) -> list:
    """
    Combines two lists into a list of tuples (word, id).
    
    Arguments:
        words (list): A list of decoded words.
        module_numbers (list): A list of corresponding module IDs.
        
    Returns:
        list: A list of tuples where each tuple contains a word and its corresponding ID.

    Example Input:
        words = ['code', 'python', 'Data', 'structure', 'Algorithms']
        module_numbers = [104, 215, 309, 412, 518]
    Example Output:
        [('code', 104), ('python', 215), ('Data', 309), ('structure', 412), ('Algorithms', 518)]
    """
    # TODO: Combine words and IDs into tuples
    combined = []
    for i in range(len(words)):
        combined.append((words[i], module_numbers[i]))
    return combined


# =======================================================
# 🧩 TASK 3 — Verify Module Uniqueness (Sets)
# =======================================================
def unique_modules(modules: list) -> list:
    """
    Removes duplicate module tuples and returns a list of unique ones.
    
    Arguments:
        modules (list): A list of tuples (word, id) which may contain duplicates.
        
    Returns:
        list: A list of unique module tuples.

    Example Input:
        [('code', 104), ('python', 215), ('python', 215)]
    Example Output:
        [('code', 104), ('python', 215)]
    """
    # TODO: Convert to set and back to list
    seen = set()
    unique = []
    for item in modules:
        if item not in seen:
            seen.add(item)
            unique.append(item)
    return unique


# =======================================================
# 🧩 TASK 4 — Build the Restoration Queue (Queue)
# =======================================================
def build_restoration_queue(unique_list: list) -> list:
    """
    Simulates restoring modules using a FIFO queue.
    Prints restoration messages and returns the order of restored module IDs.
    
    Arguments:
        unique_list (list): A list of unique module tuples (word, id).
        
    Returns:
        list: A list of restored module IDs in the order they were processed.

    Example Input:
        [('code', 104), ('python', 215), ('Data', 309)]
    Example Output:
        [104, 215, 309]
    """
    queue = unique_list.copy()
    restored_ids = []

    while queue:
        module = queue.pop(0)
        word, module_id = module
        print(f"Restoring module '{word}' with ID {module_id}...")
        restored_ids.append(module_id)

    return restored_ids

# =======================================================
# 🧩 TASK 5 — Track Actions with Stack (Stack)
# =======================================================
def track_actions(module_ids: list) -> list:
    """
    Simulates restoring modules and tracks operations in a stack.
    Pops the last three actions to simulate undo.
    
    Arguments:
        module_ids (list): A list of module IDs to be restored.
        
    Returns:
        list: A list of remaining actions after undoing the last three.

    Example Input:
        [104, 215, 309, 412, 518]
    Example Output:
        ['load_104', 'verify_215', 'load_309', 'verify_412', 'load_518']
        (after 3 undos)
        ['load_104', 'verify_215']
    """
    action_stack = []
    for i, module_id in enumerate(module_ids):
        action_type = 'load' if i % 2 == 0 else 'verify'
        action = f"{action_type}_{module_id}"
        print(f"Performing action: {action}")
        action_stack.append(action)
    for _ in range(3):
        if action_stack:
            undone_action = action_stack.pop()
            print(f"Undoing action: {undone_action}")
    return action_stack
    


# =======================================================
# 🧩 TASK 6 — Map Actions to Metadata (Dictionaries)
# =======================================================
def map_actions_to_metadata(actions: list, metadata: dict) -> dict:
    """
    Maps action names to their metadata using module IDs.
    
    Arguments:
        actions (list): A list of action names in the format 'action_moduleID'.
        metadata (dict): A dictionary mapping module IDs to their metadata.
        
    Returns:
        dict: A dictionary mapping action names to their corresponding metadata.

    Example Input:
        actions = ['load_104', 'verify_215']
        metadata = {
          104: {"size": 3.4, "status": "ok"},
          215: {"size": 5.2, "status": "ok"}
        }
    Example Output:
        {
          'load_104': {'size': 3.4, 'status': 'ok'},
          'verify_215': {'size': 5.2, 'status': 'ok'}
        }
    """
    # TODO: Extract module IDs from actions and map metadata
    
    mapped_data = {}
    for act in actions:
        _, mod_id_str = act.split('_')
        mod_id = int(mod_id_str)
        if mod_id in metadata:
            mapped_data[act] = metadata[mod_id]
    return mapped_data


# =======================================================
# 🧩 TASK 7 — Sort Modules by Size (Sorting Algorithm)
# =======================================================
def quick_sort_modules(modules: list) -> list:
     if len(modules) <= 1:
        return modules
    
    pivot = modules[len(modules) // 2][1]  
    left = [m for m in modules if m[1] < pivot]
    middle = [m for m in modules if m[1] == pivot]
    right = [m for m in modules if m[1] > pivot]
    
    return quick_sort_modules(left) + middle + quick_sort_modules(right)
   


# =======================================================
# 🧩 TASK 8 — Build the Integrity Tree (Binary Search Tree)
# =======================================================
class BSTNode:
    """A node in a binary search tree.
    
    Attributes:
        key (int): The module ID.
        value (float): The module size.
        left (BSTNode): Left child node.
        right (BSTNode): Right child node.
    
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

def insert_bst(root: BSTNode, key: int, value: float) -> BSTNode:
     if root is None:
        return BSTNode(key, value)

    if value < root.value:
        root.left = insert_bst(root.left, key, value)
    else:
        root.right = insert_bst(root.right, key, value)
    
    return root

def inorder_bst(root: BSTNode) -> list:
    if root is None:
        return []
    
    return inorder_bst(root.left) + [(root.key, root.value)] + inorder_bst(root.right)
    # TODO: Implement inorder traversal
    pass



# =======================================================
# 🧩 TASK 9 — Connect the Modules (Graph)
# =======================================================
def build_dependency_graph(connection_map: dict) -> dict:
    return {node: neighbors[:] for node, neighbors in connection_map.items()}


# =======================================================
# 🧩 TASK 10 — Reboot Codex-9 (Graph Traversal)
# =======================================================
visited = set()
    order = []

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        order.append(node)

        for neighbor in graph.get(node, []):
            dfs(neighbor)

    dfs(start)

    return order
   

