#! /usr/bin/env python
#
# Ben Osment
# Sun May 26 17:24:32 EDT 2013

import unittest
import random
# TODO -- add a hook for running PEP check before commit?


def merge_sort(l):
  length = len(l)
  if length == 0 or length == 1:
    return l
  else:
    mid = length / 2
    first_half = l[mid:]
    second_half = l[:mid]
    return merge(merge_sort(first_half),
                 merge_sort(second_half))


def merge(a, b):
  if not a:
    return b
  if not b:
    return a
  c = []  # result list
  while True:
    if len(a) == 0:
      # list a is exhausted, append remainder of b
      c.extend(b)
      return c
    if len(b) == 0:
      # similarily, list b is exhausted, append remainder of a
      c.extend(a)
      return c
    # lists are not exhausted, compare the first element in each list
    if a[0] <= b[0]:
      # TODO - is it faster to use an index instead of pop?
      c.append(a.pop(0))
    else:
      c.append(b.pop(0))


class TestMergeSort(unittest.TestCase):
  def test_basic_even_list(self):
    # even list size
    l = [random.randint(0, 100) for i in range(10)]
    self.assertEqual(merge_sort(l), sorted(l))

  def test_basic_odd_list(self):
    # odd list size
    l = [random.randint(0, 100) for i in range(21)]
    self.assertEqual(merge_sort(l), sorted(l))

  def test_large_list(self):
    l = [random.randint(0, 100000) for i in range(10000)]
    self.assertEqual(merge_sort(l), sorted(l))

  def test_negative_values(self):
    l = [random.randint(-100, 100) for i in range(10)]
    self.assertEqual(merge_sort(l), sorted(l))

  def test_null(self):
    self.assertEqual(merge_sort([]), [])

if __name__ == '__main__':
  unittest.main()
