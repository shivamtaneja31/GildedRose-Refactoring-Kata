# -*- coding: utf-8 -*-
import unittest
from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)  # Fixed the assertion to check the name

    def test_conjured_item(self):
        items = [Item("Conjured Mana Cake", 3, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 4)  # Conjured items degrade by 2
        self.assertEqual(items[0].sell_in, 2)

    def test_conjured_item_after_sell_in(self):
        items = [Item("Conjured Mana Cake", 0, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 2)  # Conjured items degrade by 2 after sell_in
        self.assertEqual(items[0].sell_in, -1)

    def test_aged_brie(self):
        # Test that Aged Brie increases in quality over time
        items = [Item("Aged Brie", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 11)  # Quality increases by 1
        self.assertEqual(items[0].sell_in, 4)   # Sell-in decreases by 1
    
    def test_aged_brie_after_sell_in(self):
        # Test that Aged Brie increases in quality twice as fast after sell-in
        items = [Item("Aged Brie", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 12)  # Quality increases by 2 after sell-in
        self.assertEqual(items[0].sell_in, -1)  # Sell-in decreases by 1

    def test_sulfuras_after_sell_in(self):
        # Test that Sulfuras never changes, even when sell_in is negative
        items = [Item("Sulfuras, Hand of Ragnaros", -1, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 80)  # Quality remains 80
        self.assertEqual(items[0].sell_in, -1)  # Sell-in remains unchanged


if __name__ == '__main__':
    unittest.main()