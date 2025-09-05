import card_creator as cc
from unittest import TestCase


class TestCardCreator(TestCase):
    def test_generate_card_number(self):
        self.assertEqual(len(cc.generate_card_number()), 16)
        self.assertTrue(str(cc.generate_card_number()).startswith('400000'), True)

    def test_generate_pin(self):
        self.assertEqual(len(cc.generate_pin()), 4)

    def test_generate_checksum(self):
        self.assertEqual(cc.generate_checksum("400000844943340"), "3")
        self.assertEqual(cc.generate_checksum("400000493832089"), "6")
        self.assertEqual(cc.generate_checksum("400000250000100"), "1")
        self.assertEqual(cc.generate_checksum("400000124000000"), "0")
