#! /usr/bin/env python
#
# Ben Osment
# Sun May 26 18:47:41 EDT 2013

import unittest

""" 
An inversion is when an element of a list is larger than an 
element with a higher index

Example:
  l = [1, 3, 5, 2, 4, 6]
  
  There are three inversions in l, (3,2), (5,2), (5,4)
"""

def count_inv(l):
  # wrapper around count_inv
  sorted_array, count = count_inv_helper(l)
  return count

def count_inv_helper(l):
  """ return the number of inversions """
  length = len(l)
  if length == 0 or length == 1:
    return l, 0
  else:
    mid = length / 2
    first_half = l[:mid]
    second_half = l[mid:]
    sorted_first, first_count = count_inv_helper(first_half)
    sorted_second, second_count = count_inv_helper(second_half)
    final_array, split_count = inv_merge(sorted_first, sorted_second)
    # number of inversions = number for left split + number from right split
    # + the number of split inversions (spanning across both halves)
    return final_array, first_count + second_count + split_count


def inv_merge(a, b):
  """ merges the list and returns a sorted list with the 
      number of inversions """
  if not a:
    return b, 0 # no inversions with an empty list
  if not b:
    return a, 0 # no inversions with an empty list
  c = []  # result list
  count = 0
  while True:
    if len(a) == 0:
      # list a is exhausted, append remainder of b
      c.extend(b)
      return c, count
    if len(b) == 0:
      # similarily, list b is exhausted, append remainder of a
      c.extend(a)
      return c, count
    # lists are not exhausted, compare the first element in each list
    if a[0] <= b[0]:
      c.append(a.pop(0))
    else:
      # this is the only place where we increment the inversion count
      # if we are taking an item off the second list, it must be lower
      # than all the items on the first list, so bump up the inversion
      # count by the amount
      count += len(a)
      c.append(b.pop(0))



class TestCountingInversions(unittest.TestCase):
  def test_basic_inv(self):
    l = [1, 3, 5, 2, 4, 6]
    self.assertEqual(count_inv(l), 3)


if __name__ == '__main__':
  unittest.main()
