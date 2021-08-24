# previous solution:
# def get_max_profit(stock_prices):
#   max_profit = 0

#   # go through every price (indexed by it's time)
#   for earlier_time, earlier_price in enumerate(stock_prices):
#     # check each price after that time
#     for later_time in range(earlier_time + 1, len(stock_prices)):
#       later_price = stock_prices[later_time]

#       # calc profit with this pair of prices
#       curr_profit = later_price - earlier_price

#       # update max_profit if needed
#       max_profit = max(max_profit, curr_profit)

#   return max_profit
 
# time: O(N) 
# space: O(1)
def get_max_profit(stock_prices):
  if len(stock_prices) < 2:
    raise ValueError("only one price")

  max_profit = stock_prices[1] - stock_prices[0]
  min_price = stock_prices[0]
 
  # after changing order (previously updated min_price before max_profit)
  for current_time in range(1, len(stock_prices)):
    current_price = stock_prices[current_time]

    current_profit = current_price - min_price
    max_profit = max(current_profit, max_profit)
    min_price = min(min_price, current_price)
    
  return max_profit


if __name__ == "__main__":
  stock_prices = [10, 7, 5, 8, 11, 9]
  down = [9]

  print(get_max_profit(down))

# tests
# import unittest

# class Test(unittest.TestCase):

#     def test_price_goes_up_then_down(self):
#         actual = get_max_profit([1, 5, 3, 2])
#         expected = 4
#         self.assertEqual(actual, expected)

#     def test_price_goes_down_then_up(self):
#         actual = get_max_profit([7, 2, 8, 9])
#         expected = 7
#         self.assertEqual(actual, expected)

#     def test_big_increase_then_small_increase(self):
#         actual = get_max_profit([2, 10, 1, 4])
#         expected = 8
#         self.assertEqual(actual, expected)                

#     def test_price_goes_up_all_day(self):
#         actual = get_max_profit([1, 6, 7, 9])
#         expected = 8
#         self.assertEqual(actual, expected)

#     def test_price_goes_down_all_day(self):
#         actual = get_max_profit([9, 7, 4, 1])
#         expected = -2
#         self.assertEqual(actual, expected)

#     def test_price_stays_the_same_all_day(self):
#         actual = get_max_profit([1, 1, 1, 1])
#         expected = 0
#         self.assertEqual(actual, expected)

#     def test_error_with_empty_prices(self):
#         with self.assertRaises(Exception):
#             get_max_profit([])

#     def test_error_with_one_price(self):
#         with self.assertRaises(Exception):
#             get_max_profit([1])


# unittest.main(verbosity=2)