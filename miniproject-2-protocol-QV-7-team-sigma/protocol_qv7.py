"""
=========================================================
  🧩 Mini Project: The Quantum Vault Breach — Protocol QV-7
=========================================================

TEAM: # sigma
MEMBERS: # 24071002, 24101012

STORY:
Deep beneath the abandoned research facility *Helion Prime*, a classified
containment system known as the **Quantum Vault** has been breached.

Its encrypted artifacts—mathematical models, neural blueprints, and 
time-distortion algorithms—have fragmented into quantum shards scattered 
across corrupted memory sectors.

Your mission as the **Quantum Recovery Task Unit**:
Reconstruct every shard, rebuild the data structures, re-link dependencies,
and stabilize the Vault before the containment field collapses.

Every function (Task 1–10) represents a stage of the reconstruction protocol.
Output from each task becomes the input for the next one.

Follow the protocol. Restore the Vault. Prevent total system collapse.

INSTRUCTIONS:
1. Complete each function according to its docstring.
2. Use only standard Python libraries. Do not import external packages.
3. You may test each function independently.
4. Do not change function names, arguments, or docstrings.
5. Write clean, optimized, well-commented code.
6. When all tasks are completed and unit tests pass, the Vault stabilizes.
7. After finishing: commit → create PR → tests will run automatically.
8. Fix test failures or review comments and update your PR.
9. Only after approval, your code will be merged into the master branch.

=========================================================
"""

from collections import deque
import json
import heapq
import re


# =======================================================
# 🧩 TASK 1 — Extract Quantum Shards (Strings → List)
# =======================================================
def extract_shards(corrupted_stream: str) -> list:
    """
    Splits a corrupted quantum stream where shards are separated by '#'.
    Each shard is reversed and cleaned of non-alphanumeric characters.

    Arguments:
        corrupted_stream (str): The raw corrupted shard string.

    Returns:
        list: A list of cleaned, decoded shard strings.

    Example Input:
        "23noitazimitpO#gnirts_001#eman-tceles"
    Example Output:
        ['Optimization32', '100_string', 'select-name']
    """
    # TODO: Implement extraction + cleaning
    shards = corrupted_stream.split("#")
    cleaned_shards = []

    for shard in shards:
        reversed_shard = shard[::-1]
        cleaned_shard = re.sub(r'[^a-zA-Z0-9_]', '', reversed_shard)
        cleaned_shards.append(cleaned_shard)
    
    return cleaned_shards


# =======================================================
# 🧩 TASK 2 — Pair Shards with Sequence Codes (List → Tuple)
# =======================================================
def pair_shards(shards: list, codes: list) -> list:
    """
    Combines the decoded shard strings with their associated sequence codes
    into tuples of the form (shard, code).

    Arguments:
        shards (list): List of decoded shard strings.
        codes (list): List of integer sequence codes.

    Returns:
        list: List of (shard, code) tuples.

    Example:
        shards = ['alpha', 'beta', 'gamma', 'alpha']
        codes = [7, 12, 18, 22]
    Output:
        [('alpha', 7), ('beta', 12), ('gamma', 18), ('alpha', 22)]
    """
    # TODO: Combine the two lists into tuples
    return list(zip(shards, codes))


# =======================================================
# 🧩 TASK 3 — Stabilize Shard Registry (Sets)
# =======================================================
def stabilize_registry(pairs: list) -> list:
    """
    Removes duplicate shard entries using a set and returns a list of
    unique shard tuples.

    Arguments:
        pairs (list): List of (shard, code) tuples that may include duplicates.

    Returns:
        list: A list of unique shard tuples.

    Example Input:
        [('alpha', 7), ('beta', 12), ('gamma', 18), ('alpha', 22)]
    Example Output:
        [('alpha', 7), ('beta', 12), ('gamma', 18)]
    """
    # TODO: Convert to set then back to list
    seen = set()
    unique_pairs = []

    for shard, code in pairs:
        if shard not in seen:
            seen.add(shard)
            unique_pairs.append((shard, code))
    
    return unique_pairs


# =======================================================
# 🧩 TASK 4 — Initialize Reconstruction Queue (Queue)
# =======================================================
def initialize_queue(unique_pairs: list) -> list:
    """
    Initializes a FIFO queue using deque and simulates shard processing.
    Returns the sequence codes in the order they were handled.

    Arguments:
        unique_pairs (list): List of unique (shard, code) tuples.

    Returns:
        list: Ordered list of processed sequence codes.

    Example:
        [('alpha', 7), ('beta', 12), ('gamma', 18)]
    Output:
        [7, 12, 18]
    """
    # TODO: Use deque to simulate queue operations
    queue = deque(unique_pairs)
    processed_codes = []

    while queue:
        shard, code = queue.popleft()
        processed_codes.append(code)
    
    return processed_codes


# =======================================================
# 🧩 TASK 5 — Action Log Stack (Stack)
# =======================================================
def action_log(codes: list) -> list:
    """
    Builds an action log using a LIFO stack where each code generates
    'decode_<code>' and 'validate_<code>' actions. The last two actions
    represent corrupted operations and must be removed (undo).

    Arguments:
        codes (list): List of sequence codes.

    Returns:
        list: Stack after removing the last two invalid operations.

    Example Input:
        [7, 12, 18]
    Example Generated Actions:
        ['decode_7', 'validate_7', 'decode_12', 'validate_12', 'decode_18', 'validate_18']
        after removing 2:
        ['decode_7', 'validate_7', 'decode_12', 'validate_12']
    """
    # TODO: Use Python list as stack
    stack = []

    for code in codes:
        stack.append(f"decode_{code}")
        stack.append(f"validate_{code}")
    
    if len(stack) >= 2:
        stack.pop()
        stack.pop()
    
    return stack


# =======================================================
# 🧩 TASK 6 — Annotate Shards (Dictionary)
# =======================================================
def annotate_shards(actions: list, shard_info: dict) -> dict:
    """
    Uses the action names (e.g., 'decode_7') to map each action
    to its corresponding shard metadata stored in a dictionary.

    Arguments:
        actions (list): Action names in the format 'action_code'.
        shard_info (dict): Maps integer codes to metadata dictionaries.

    Returns:
        dict: Mapping from action name → metadata.

    Example:
        actions = ['decode_7']
        shard_info = {7: {"energy": 1.2, "state": "stable"}}
    Output:
        {'decode_7': {'energy': 1.2, 'state': 'stable'}}
    """
    # TODO: Extract code from action name and map
    pass


# =======================================================
# 🧩 TASK 7 — Sort Shards by Energy (Sorting Algorithm)
# =======================================================
def merge_sort_energy(shards: list) -> list:
    """
    Sorts a list of (code, energy) tuples by energy using merge sort.

    Arguments:
        shards (list): List of (code, energy) tuples.

    Returns:
        list: Sorted list by ascending energy.

    Example:
        [(18, 3.1), (7, 1.2), (12, 2.5)]
    Output:
        [(7, 1.2), (12, 2.5), (18, 3.1)]
    """
    # TODO: Implement merge sort
    pass


# =======================================================
# 🧩 TASK 8 — Rebuild Quantum Integrity Tree (Binary Search Tree)
# =======================================================
class QuantumNode:
    """A BST node storing code and energy."""
    def __init__(self, code, energy):
        self.code = code
        self.energy = energy
        self.left = None
        self.right = None

def insert_qv(root: QuantumNode, code: int, energy: float) -> QuantumNode:
    """
    Inserts (code, energy) into a BST ordered by energy value.

    Arguments:
        root (QuantumNode): The root of the BST.
        code (int): Sequence code.
        energy (float): Energy value.
    """
    # TODO: Implement BST insertion logic
    pass


def inorder_qv(root: QuantumNode) -> list:
    """
    Performs an inorder traversal of the Quantum Vault BST.

    Arguments:
        root (QuantumNode): BST root.

    Returns:
        list: List of (code, energy) tuples sorted by energy.
    
    Example:
        [(18, 3.1), (2, 0.9), (22, 4.0), (7, 1.2), (12, 2.5)]
    Output:
        [(2, 0.9), (7, 1.2), (12, 2.5), (18, 3.1), (22, 4.0)]
    """
    # TODO: Implement inorder traversal
    pass


# =======================================================
# 🧩 TASK 9 — Build Shard Dependency Map (Graph)
# =======================================================
def build_shard_graph(mapping: dict) -> dict:
    """
    Builds an adjacency list representing quantum shard dependencies.

    Arguments:
        mapping (dict): Maps shard codes to a list of dependent codes.

    Returns:
        dict: Adjacency list representing the dependency graph.

    Example:
        {
          "7": ["12"],
          "12": ["18"],
          "18": []
        }
    """
    # TODO: Return adjacency list
    pass


# =======================================================
# 🧩 TASK 10 — Activate Vault Sequence (DFS Traversal)
# =======================================================
def dfs_sequence(graph: dict, start: str) -> list:
    """
    Performs DFS to determine the activation order of quantum shards.

    Arguments:
        graph (dict): Adjacency list of dependencies.
        start (str): Starting shard code.

    Returns:
        list: Activation order of shard codes.
        str: Completion message.

    Example:
        graph = {"7": ["12"], "12": ["18"], "18": []}
        start = "7"
    Output:
        ['7', '12', '18']
        "Quantum Vault fully restored. Protocol QV-7 complete."
    """
    # TODO: Implement DFS recursively
    pass