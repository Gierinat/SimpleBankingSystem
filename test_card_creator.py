import card as cc
from unittest import TestCase


class TestCardCreator(TestCase):
    def test_generate_card_number(self):
        self.assertEqual(len(cc.generate_card_number()), 16)
        self.assertTrue(str(cc.generate_card_number()).startswith('400000'), True)

    def test_generate_pin(self):
        self.assertEqual(len(cc.generate_pin()), 4)
