### 🧠 Storyline

The central AI of Codex-9, a futuristic data fortress, has been hacked.
Fragments of its blueprint code have been scattered in corrupted files.
You are the Forensic Programmer tasked with recovering the blueprint, step by step — every operation you perform produces a new dataset you’ll use next.



### 🧠 Project Overview

* Number of tasks: 10
* Recommended team size: 1–4 students
* Topics covered: strings, lists, tuples, sets, stacks, queues, dictionaries, searching, sorting, trees, and graphs
* Final goal: Reconstruct a stolen digital blueprint by progressively decoding, organizing, and connecting data pieces.


### ⚙️ TASKS

#### Task 1: Decode the Fragment
You receive a corrupted data transmission:

```
"edoc;nohtyp;ataD;erutcurts;smhtiroglA"
```

Write a function that:
	1.	Splits the string by ;
	2.	Reverses each word
	3.	Returns a list of decoded words.


#### Task 2: Organize the Blueprint Segments

Each decoded word corresponds to a module number in Codex-9:
```python
module_numbers = [104, 215, 309, 412, 518]
```

Combine both lists (from Task 1 and above) into a list of tuples:


#### Task 3: Verify Module Uniqueness

Some tuples may repeat due to transmission errors.
Convert your tuple list into a set to remove duplicates.
Then convert back to a list and return the list of unique tuples.


#### Task 4: Build the Restoration Queue

Modules must be rebuilt in the order they were received.
Use a queue (collections.deque) to enqueue all unique modules.
Then simulate restoring them one by one and return the list of restored modules IDs in the order processed.


#### Task 5: Track Actions with Stack

While restoring, record your operations (e.g., "load_215", "verify_309") in a stack to support undo.
After processing, pop the last 3 actions to simulate undoing failed repairs.

Return the list of successful actions after undoing.

#### Task 6: Map Actions to Metadata

Now link every successful action to metadata describing module properties:

```python
metadata = {
  104: {"size": 3.4, "status": "ok"},
  215: {"size": 5.2, "status": "ok"},
  309: {"size": 2.1, "status": "ok"},
  412: {"size": 7.3, "status": "ok"},
  518: {"size": 4.8, "status": "ok"}
}
```
Create a dictionary mapping action_name → metadata and return the dictionary.


#### Task 7: Sort Modules by Size

From your dictionary, extract all (module_id, size) pairs.
Implement quick sort to order them by size ascending.
Return the sorted list.

#### Task 8: Build the Integrity Tree

Insert each (module_id, size) pair into a Binary Search Tree, where the key is size.
Implement:
* Node class
* Insert function
* Inorder traversal (to confirm sorted order)

Return the inorder traversal list of module IDs (should match Task 7).

##### Task 9: Connect Modules with Graph

Now that all modules are repaired, you receive a connection map defining dependencies between module IDs:

```json
{
  "104": ["215", "309"],
  "215": ["412"],
  "309": ["518"],
  "412": ["518"],
  "518": []
}
```

Represent this as an adjacency list (dictionary of lists).
Return the adjacency list.


##### Task 10: Reboot Codex-9

Implement Depth-First Search (DFS) on your graph to determine the sequence of module activations needed to reboot Codex-9.
Start from the smallest module ID (by numeric value).
Each node visited represents an activated module.