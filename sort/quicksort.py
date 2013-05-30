#! /usr/bin/env python
#
# Ben Osment
# Wed May 29 22:29:43 EDT 2013

import unittest
import random

# TODO -- have some util to measure the time for sorting 1 million integers
# with mergesort, quicksort, randomized quicksort and parallel quicksort
# also quicksort in place and with copies


def swap(l, a, b):
  l[a], l[b] = l[b], l[a]


def orig_quicksort(l):
  return orig_qsort_helper(l, len(l))


def orig_qsort_helper(l, n):
  if n <= 1:
    return l
  l, pivot = orig_partition(l)
  # split into left of pivot and right of pivot
  left = l[:pivot]
  pivot_element = [l[pivot]]
  right = l[pivot + 1:]
  # recursively call on the left and right
  # TODO - parallelize this operation?
  return orig_qsort_helper(left, len(left)) + pivot_element + \
      orig_qsort_helper(right, len(right))


def orig_partition(l):
  # TODO have a randomized partition
  pivot = 0
  i = 1
  pivot_value = l[pivot]
  for j in range(1, len(l)):
    if l[j] < pivot_value:
      # if less, swap
      swap(l, i, j)
      i += 1
  # swap the pivot into place
  swap(l, pivot, i - 1)
  l[pivot], l[i - 1] = l[i - 1], l[pivot]
  return l, i - 1


def quicksort(l):
  qsort_helper(l, 0, len(l))
  return l


def qsort_helper(l, beg, end):
  if (end - beg) <= 1:
    return
  # partition
  pivot = partition(l, beg, end)
  # split into left of pivot and right of pivot
  qsort_helper(l, beg, pivot)
  qsort_helper(l, pivot + 1, end)


def partition(l, beg, end):
  # TODO have a randomized partition
  pivot = beg
  i = beg + 1
  pivot_value = l[pivot]
  for j in range(beg + 1, end):
    if l[j] < pivot_value:
      # if less, swap
      swap(l, i, j)
      i += 1
  # swap the pivot into place
  swap(l, pivot, i - 1)
  return i - 1  # final position of pivot


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
