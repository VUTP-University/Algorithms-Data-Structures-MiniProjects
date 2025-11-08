import unittest
from solutions import (decode_fragment, organize_segments, unique_modules, 
                       build_restoration_queue, track_actions, 
                       map_actions_to_metadata, quick_sort_modules, 
                       insert_bst, inorder_bst, build_dependency_graph, 
                       dfs_activation)

class TestCodex9Project(unittest.TestCase):
    """Unit tests for the codex9 mini-project tasks.

    Args:
        unittest: Python's built-in unit testing framework.
        
    Methods:
        test_task1_decode_fragment: Tests decoding of corrupted string fragments.
        test_task2_organize_segments: Tests organizing words and IDs into tuples.
        test_task3_unique_modules: Tests verification of unique module tuples.
        test_task4_build_restoration_queue: Tests building a restoration queue from module data.
        test_task5_track_actions: Tests tracking actions with undo functionality.
        test_task6_map_actions_to_metadata: Tests mapping actions to metadata.
        test_task7_quick_sort_modules: Tests quick sorting of modules by size.
        test_task8_integrity_bst: Tests building and traversing a binary search tree.
        test_task9_build_dependency_graph: Tests building a dependency graph from connections.
        test_task10_dfs_activation: Tests depth-first search activation of modules.
    """

    def test1_task1_decode_fragment(self):
        self.assertEqual(decode_fragment("edoc;nohtyp;ataD"), ['code', 'python', 'Data'])

    def test2_task1_decode_fragment(self):
        self.assertEqual(decode_fragment("olleh;dlrow"), ['hello', 'world'])
        
    def test3_task1_decode_fragment(self):
        self.assertEqual(decode_fragment("1tupni;2tuptuo;3elif"), ['input1', 'output2', 'file3'])

    def test1_task2_organize_segments_var1(self):
        words = ['code', 'python', 'Data']
        ids = [101, 202, 303]
        expected = [('code', 101), ('python', 202), ('Data', 303)]
        self.assertEqual(organize_segments(words, ids), expected)

    def test_task3_unique_modules(self):
        data = [('code', 104), ('python', 215), ('python', 215)]
        expected = [('code', 104), ('python', 215)]
        self.assertEqual(sorted(unique_modules(data)), sorted(expected))

    def test_task4_build_restoration_queue(self):
        data = [('code', 104), ('python', 215), ('Data', 309)]
        self.assertEqual(build_restoration_queue(data), [104, 215, 309])

    def test_task5_track_actions(self):
        ids = [104, 215, 309, 412, 518]
        output = track_actions(ids)
        # Check first part of list after 3 undos
        self.assertTrue(output == ['load_104', 'verify_215'])

    def test_task6_map_actions_to_metadata(self):
        actions = ['load_104', 'verify_215']
        metadata = {
            104: {"size": 3.4, "status": "ok"},
            215: {"size": 5.2, "status": "ok"}
        }
        result = map_actions_to_metadata(actions, metadata)
        self.assertIn('load_104', result)
        self.assertEqual(result['verify_215']['status'], 'ok')

    def test_task7_quick_sort_modules(self):
        modules = [(104, 3.4), (215, 5.2), (309, 2.1)]
        expected = [(309, 2.1), (104, 3.4), (215, 5.2)]
        self.assertEqual(quick_sort_modules(modules), expected)

    def test_task8_integrity_bst(self):
        data = [(309, 2.1), (104, 3.4), (215, 5.2)]
        root = None
        for mid, size in data:
            root = insert_bst(root, mid, size)
        traversal = inorder_bst(root)
        self.assertEqual(traversal, [(309, 2.1), (104, 3.4), (215, 5.2)])

    def test_task9_build_dependency_graph(self):
        graph = build_dependency_graph({
            "104": ["215", "309"],
            "215": ["412"],
            "309": ["518"],
            "412": ["518"],
            "518": []
        })
        self.assertIn("104", graph)
        self.assertIn("518", graph["412"])

    def test_task10_dfs_activation(self):
        graph = {
            "104": ["215", "309"],
            "215": ["412"],
            "309": ["518"],
            "412": ["518"],
            "518": []
        }
        visited, msg = dfs_activation(graph, "104")
        self.assertIn('215', visited)
        self.assertEqual(visited[-1], '309')
        self.assertEqual(msg, "Blueprint successfully restored. Codex-9 reboot complete.")

if __name__ == '__main__':
    unittest.main()