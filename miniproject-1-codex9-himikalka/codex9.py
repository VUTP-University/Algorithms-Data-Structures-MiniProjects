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
    # TODO: Implement the decoding logic here
  parts = fragment.split(';')
    decoded = [word[::-1] for word in parts]
   
    return 1


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
    pass


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
    pass


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
    # TODO: Use deque for queue logic
    pass

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
    # TODO: Use list as stack and pop last 3
    pass


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
    pass


# =======================================================
# 🧩 TASK 7 — Sort Modules by Size (Sorting Algorithm)
# =======================================================
def quick_sort_modules(modules: list) -> list:
    """
    Implements quick sort to order (id, size) pairs by size ascending.
    
    Arguments:
        modules (list): A list of tuples (id, size).
        
    Returns:
        list: A list of tuples sorted by size in ascending order.

    Example Input:
        [(104, 3.4), (215, 5.2), (309, 2.1)]
    Example Output:
        [(309, 2.1), (104, 3.4), (215, 5.2)]
    """
    # TODO: Implement quick sort
    pass


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
    """
    Inserts (id, size) into BST ordered by size.
    
    Arguments:
        root (BSTNode): The root of the BST.
        key (int): The module ID.
        value (float): The module size.
    """
    # TODO: Insert node correctly
    pass

def inorder_bst(root: BSTNode) -> list:
    """
    Returns inorder traversal of BST as list of (id, size) pairs.
    
    Arguments:
        root (BSTNode): The root of the BST.
    """
    # TODO: Implement inorder traversal
    pass



# =======================================================
# 🧩 TASK 9 — Connect the Modules (Graph)
# =======================================================
def build_dependency_graph(connection_map: dict) -> dict:
    """
    Builds adjacency list representing module dependencies.
    
    Arguments:
        connection_map (dict): A dictionary mapping module IDs to lists of dependent module IDs.
    Returns:
        dict: An adjacency list representing the graph of module dependencies.

    Example Input:
        {
          "104": ["215", "309"],
          "215": ["412"],
          "309": ["518"],
          "412": ["518"],
          "518": []
        }
    Example Output:
        Same dictionary (adjacency list)
    """
    # TODO: Return adjacency list
    pass


# =======================================================
# 🧩 TASK 10 — Reboot Codex-9 (Graph Traversal)
# =======================================================
def dfs_activation(graph: dict, start: str) -> list:
    """
    Performs Depth-First Search (DFS) to determine activation order.
    
    Arguments:
        graph (dict): An adjacency list representing module dependencies.
        start (str): The starting module ID for activation.
        
    Returns:
        list: A list of module IDs in the order they are activated.
        str: A system message indicating successful reboot.

    Example Input:
        {
          "104": ["215", "309"],
          "215": ["412"],
          "309": ["518"],
          "412": ["518"],
          "518": []
        }, start="104"

    Example Output:
        Activation order: ['104', '215', '412', '518', '309']
        System Message: Blueprint successfully restored. Codex-9 reboot complete.
    """
    # TODO: Implement recursive DFS
    pass


