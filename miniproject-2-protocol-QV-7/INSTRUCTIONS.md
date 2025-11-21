### 🧠 Storyline

Deep beneath the abandoned research complex Helion Prime, a classified experimental containment system known as the Quantum Vault has suffered a catastrophic breach.

Inside the Vault lie encrypted algorithmic artifacts — predictive AIs, mathematical models, temporal distortion engines — all stored as quantum shards.
When the breach occurred, these shards were fragmented, scrambled, and scattered across corrupted memory sectors.

The Quantum Recovery Task Unit (you) has been activated.

### 🧠 Project Overview

* Number of tasks: 10
* Recommended team size: 1–4 students
* Topics covered:
Strings, lists, sets, tuples, stacks, queues, dictionaries, searching/sorting algorithms, binary search trees, graphs
* Final goal: Rebuild the Quantum Lattice Map and secure The Vault.

### ⚙️ TASKS

#### Task 1 — Extract Quantum Shards

You are given a corrupted quantum data stream where shards are separated by #.

```
"23noitazimitpO#gnirts_001#eman-tceles"
```

You must:
* Split the string into fragments
* Reverse each fragment
* Remove all characters except letters, digits, and hyphens
* Return the resulting cleaned list

```py
['Optimization32', '100_string', 'select-name']
```


#### Task 2 —  Pair Shards with Sequence Codes

You receive a list of decoded shard strings and a list of integer sequence codes.

You must pair them into tuples:

```py
(shard_string, code)
```

```py
shards = ['alpha', 'beta', 'gamma', 'alpha']
codes = [7, 12, 18, 22]
```

```py
[('alpha', 7), ('beta', 12), ('gamma', 18), ('alpha', 22)]
```


#### TASK 3 — Stabilize Shard Registry 

Duplicates may exist due to memory corruption.

You must:
* Convert the list of shard tuples to a set
* Convert it back to a list
* Return only unique shard entries

```py
[('alpha', 7), ('beta', 12), ('gamma', 18), ('alpha', 22)]
```

```py
[('alpha', 7), ('beta', 12), ('gamma', 18)]
```

#### Task 4 — Initialize Reconstruction Queue

Processing must occur in the exact order that unique shard pairs appear.

```py
[('alpha', 7), ('beta', 12), ('gamma', 18)]
```

You must:
* Create a FIFO queue (collections.deque)
* Enqueue each (shard, code) tuple
* Dequeue items one by one
* Return a list only of the sequence codes in processed order

```py
[7, 12, 18]
```

#### TASK 5 — Action Log Stack

For each code, generate two actions:
* `decode_<code>`
* `validate_<code>`


```py
[7, 12, 18]
```


```py
['decode_7', 'validate_7', 'decode_12', 'validate_12', 'decode_18', 'validate_18']
# after removing 2:
['decode_7', 'validate_7', 'decode_12', 'validate_12']
```

#### TASK 6 — Annotate Shards

You must:
* Use each action name (e.g., "decode_7")
* Extract the code (e.g., 7)
* Map the action to metadata found in shard_info[code]

```py
actions = ['decode_7']
shard_info = {7: {"energy": 1.2, "state": "stable"},
              12: {"energy": 2.5, "state": "unstable"},
              18: {"energy": 3.1, "state": "stable"},
              22: {"energy": 4.0, "state": "critical"},
              2: {"energy": 0.9, "state": "stable"}}
```


```py
{'decode_7': {'energy': 1.2, 'state': 'stable'},
 'validate_7': {'energy': 1.2, 'state': 'stable'},
 'decode_12': {'energy': 2.5, 'state': 'unstable'},
 'validate_12': {'energy': 2.5, 'state': 'unstable'}}
```


#### TASK 7 — Sort Shards by Energy

You will receive a list of tuples:

```
(code, energy)
```

You must:
* Implement a sort algorithm manually(by your choice, e.g., quick sort, merge sort, bubble sort)
* Sort by energy in ascending order
* Return the sorted list

```py
[(18, 3.1), (7, 1.2), (12, 2.5)]
```

```py
[(7, 1.2), (12, 2.5), (18, 3.1)]
```


#### TASK 8 — Rebuild Quantum Integrity Tree

You must implement a Binary Search Tree where:
* The tree is ordered by energy
* Each node stores (code, energy)
* You must implement:
  * insert_qv
  * inorder_qv

**Inorder traversal must return items sorted by energy.**

```py
[(18, 3.1), (2, 0.9), (22, 4.0), (7, 1.2), (12, 2.5)]
```

```py
[(2, 0.9), (7, 1.2), (12, 2.5), (18, 3.1), (22, 4.0)]
```

#### TASK 9 — Build Shard Dependency Map

You receive a dependency mapping:

```py
{
  "7": ["12"],
  "12": ["18"],
  "18": []
}
```

You must return a clean adjacency list (likely identical to input).
Build a Graph representation using a dictionary of lists.



#### TASK 10 — Activate Vault Sequence

Perform a Depth-First Search starting from a given code.

You must return:
* The activation order (list)
* A final status message

```py
graph = {"7": ["12"], "12": ["18"], "18": []}
start = "7"
```

```py
(['7', '12', '18'], "Quantum Vault fully restored. Protocol QV-7 complete.")
```
