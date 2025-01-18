import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_create_cells_different_size(self):
        num_cols = 5
        num_rows = 5
        m2 = Maze(0, 0, num_rows, num_cols, 20, 20)
        self.assertEqual(len(m2._cells), num_cols)
        self.assertEqual(len(m2._cells[0]), num_rows)

    def test_maze_create_cells_large_size(self):
        num_cols = 20
        num_rows = 15
        m3 = Maze(0, 0, num_rows, num_cols, 15, 15)
        self.assertEqual(len(m3._cells), num_cols)
        self.assertEqual(len(m3._cells[0]), num_rows)
    
    def test_break_entrance_and_exit(self):
        num_cols = 5
        num_rows = 5
        m4 = Maze(0, 0, num_rows, num_cols, 20, 20)
        self.assertFalse(m4._cells[0][0].top_wall)
        self.assertFalse(m4._cells[num_cols - 1][num_rows - 1].bottom_wall)
    
    def test_maze_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in m1._cells:
            for cell in col:
                self.assertEqual(
                    cell.visited,
                    False,
                )


if __name__ == "__main__":
    unittest.main()