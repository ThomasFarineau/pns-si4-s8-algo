import unittest

import format
import verification


class VerificationTest(unittest.TestCase):
    def test_connect_4_1(self):
        b = "hm0000hm0000hm0000h00000000000000000000000"
        f = format.Format(b)
        self.assertEqual(f.is_valid(), True)
        v = verification.Verification(f.formatted_board())
        self.assertEqual(v.is_valid(), False)

    def test_connect_4_2(self):
        b = "hhhh00mmm000000000000000000000000000000000"
        f = format.Format(b)
        self.assertEqual(f.is_valid(), True)
        v = verification.Verification(f.formatted_board())
        self.assertEqual(v.is_valid(), False)

    def test_connect_4_3(self):
        b = "hm0000mh0000hmh000hmhh00mm0000000000000000"
        f = format.Format(b)
        self.assertEqual(f.is_valid(), True)
        v = verification.Verification(f.formatted_board())
        self.assertEqual(v.is_valid(), False)

    def test_connect_4_4(self):
        b = "hmhh00hmh000mh0000hm0000mm0000000000000000"
        f = format.Format(b)
        self.assertEqual(f.is_valid(), True)
        v = verification.Verification(f.formatted_board())
        self.assertEqual(v.is_valid(), False)

    def test_board_full(self):
        b = "hmhmhmhmhmhmmhmhmhmhmhmhhmhmhmhmhmhmhmhmhm"
        f = format.Format(b)
        self.assertEqual(f.is_valid(), True)
        v = verification.Verification(f.formatted_board())
        self.assertEqual(v.is_valid(), False)
        self.assertEqual(v.message, "Le plateau est plein")


if __name__ == '__main__':
    unittest.main()
