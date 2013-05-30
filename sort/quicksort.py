#! /usr/bin/env python
#
# Ben Osment
# Wed May 29 22:29:43 EDT 2013

import unittest
import random

# TODO -- have some util to measure the time for sorting 1 million integers
# with mergesort, quicksort, randomized quicksort and parallel quicksort

def quicksort(l):
  return qsort_helper(l, len(l))


def qsort_helper(l, n):
  if n <= 1: 
    return l
  # partition
  l, pivot = partition(l)
  # split into left of pivot and right of pivot
  left = l[:pivot]
  pivot_element = [l[pivot]]
  right = l[pivot+1:]
  # recursively call on the left and right
  # TODO - parallelize this operation?
  return qsort_helper(left, len(left)) + pivot_element + \
         qsort_helper(right, len(right))

def partition(l):
  # TODO have a randomized partition
  pivot = 0
  i = 1
  pivot_value = l[pivot]
  for j in range(1,len(l)):
    if l[j] < pivot_value:
      # if less, swap
      l[i], l[j] = l[j], l[i]
      #swap(l, i, j)
      i += 1
  # swap the pivot into place
  #swap(l, pivot, i-1)
  l[pivot], l[i-1] = l[i-1], l[pivot]
  return l, i-1


class TestQuickSort(unittest.TestCase):
  def test_basic_even_list(self):
    # even list size
    l = [random.randint(0, 100) for i in range(10)]
    self.assertEqual(quicksort(l), sorted(l))

  def test_basic_odd_list(self):
    # odd list size
    l = [random.randint(0, 100) for i in range(21)]
    self.assertEqual(quicksort(l), sorted(l))

  def test_large_list(self):
    l = [random.randint(0, 100000) for i in range(10000)]
    self.assertEqual(quicksort(l), sorted(l))

  def test_negative_values(self):
    l = [random.randint(-100, 100) for i in range(10)]
    self.assertEqual(quicksort(l), sorted(l))

  def test_null(self):
    self.assertEqual(quicksort([]), [])


if __name__ == '__main__':
  unittest.main()
