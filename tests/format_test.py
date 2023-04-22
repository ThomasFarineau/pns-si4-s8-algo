import unittest

from src import format

class FormatTest(unittest.TestCase):
    def test_not_42(self):
        b = "0" * 41
        f = format.Format(b)
        self.assertEqual(f.is_valid(), False)
        self.assertEqual(f.message, "La chaîne de caractères doit contenir 42 caractères, actuellement 41 caractères")

    def test_empty_board(self):
        b = "0" * 42
        f = format.Format(b)
        self.assertEqual(f.is_valid(), True)
        self.assertEqual(f.message, None)

    def test_other_char(self):
        b = "0" * 42
        b = b.replace("0", "a")
        f = format.Format(b)
        self.assertEqual(f.is_valid(), False)
        self.assertEqual(f.message, "La chaîne de caractères ne doit contenir que des 0, des m ou des h")

    def test_0_before_m(self):
        b = "0m" + ("0" * 40)
        f = format.Format(b)
        self.assertEqual(f.is_valid(), False)
        self.assertEqual(f.message, "Il ne peut pas y avoir de 0 avant un m ou un h dans la même colonne")

    def test_0_before_h(self):
        b = "h0h" + ("0" * 39)
        f = format.Format(b)
        self.assertEqual(f.is_valid(), False)
        self.assertEqual(f.message, "Il ne peut pas y avoir de 0 avant un m ou un h dans la même colonne")

    def test_h_len_sup_m_len(self):
        b = "hhm" + ("0" * 39)
        f = format.Format(b)
        self.assertEqual(f.is_valid(), True)
        self.assertEqual(f.message, None)

    def test_m_len_sup_h_len(self):
        b = "mmh" + ("0" * 39)
        f = format.Format(b)
        self.assertEqual(f.is_valid(), False)
        self.assertEqual(f.message, "Le nombre de H doit être égal au nombre de M (ou n(M)+1)")

    def test_h_len_eq_m_len(self):
        b = "mh" + ("0" * 40)
        f = format.Format(b)
        self.assertEqual(f.is_valid(), True)
        self.assertEqual(f.message, None)

    def test_valid_board(self):
        b = "m00000h00000mm0000hmh000h00000h00000000000"
        f = format.Format(b)
        self.assertEqual(f.is_valid(), True)
        self.assertEqual(f.message, None)

    def test_valid_board2(self):
        b = "hm0000hm0000hm0000h00000000000000000000000"
        f = format.Format(b)
        self.assertEqual(f.is_valid(), True)
        self.assertEqual(f.message, None)

    def test_valid_board3(self):
        b = "hhhh00mmm000000000000000000000000000000000"
        f = format.Format(b)
        self.assertEqual(f.is_valid(), True)
        self.assertEqual(f.message, None)

    def test_valid_board4(self):
        b = "hm0000mh0000hmh000hmhh00mm0000000000000000"
        f = format.Format(b)
        self.assertEqual(f.is_valid(), True)
        self.assertEqual(f.message, None)


    def test_valid_board5(self):
        b = "hmhh00hmh000mh0000hm0000mm0000000000000000"
        f = format.Format(b)
        self.assertEqual(f.is_valid(), True)
        self.assertEqual(f.message, None)


    def test_valid_board6(self):
        b = "hmhmhmhmhmhmmhmhmhmhmhmhhmhmhmhmhmhmhmhmhm"
        f = format.Format(b)
        self.assertEqual(f.is_valid(), True)
        self.assertEqual(f.message, None)


if __name__ == '__main__':
    unittest.main()
