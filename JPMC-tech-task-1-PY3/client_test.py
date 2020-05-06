import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'},
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        self.assertEqual(getDataPoint(quote),(quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'],(quote['top_bid']['price']+quote['top_ask']['price'])/2))


  """ ------------ Add more unit tests ------------ """
  def test_getRatio(self):
      nums = [
        {'price_a': 45, 'price_b': 35},
        {'price_a': 18, 'price_b': 69},
        {'price_a': 0, 'price_b': 25},
        {'price_a': 178, 'price_b': 0},
        {'price_a': 0, 'price_b': 0},
        {'price_a': 35, 'price_b': 35},
        {'price_a': 99999995848, 'price_b': 6431684651},
      ]
      for num in nums:
          ans = None if num['price_b']==0 else num['price_a']/num['price_b']
          self.assertEqual(getRatio(num['price_a'],num['price_b']), ans)

if __name__ == '__main__':
    unittest.main()
