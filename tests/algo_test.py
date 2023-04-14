import unittest
import format
import verification
import algo

class AlgoTest(unittest.TestCase):
    def test_row_1(self):
        b = "hm0000hm0000hm0000000000000000000000000000"
        f = format.Format(b)
        self.assertEqual(f.is_valid(), True)
        v = verification.Verification(f.formatted_board())
        format.print_board(v.board)
        self.assertEqual(v.is_valid(), True)
        m = algo.best_move(v.board, 1)
        print(m)

    def test_col_1(self):
        b = "hhh000mm0000m00000000000000000000000000000"
        f = format.Format(b)
        self.assertEqual(f.is_valid(), True)
        v = verification.Verification(f.formatted_board())
        format.print_board(v.board)
        self.assertEqual(v.is_valid(), True)
        m = algo.best_move(v.board, 1)
        print(m)

if __name__ == '__main__':
    unittest.main()
