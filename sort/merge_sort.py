#! /usr/bin/env python
# 
# Ben Osment
# Sun May 26 17:24:32 EDT 2013

def merge_sort(l):
  length = len(l)
  if length == 0 or length == 1:
    return l
  else:
    first_half = l[length/2:]
    second_half = l[:length/2]
    return merge(merge_sort(first_half),
                 merge_sort(second_half))

def merge(a, b):
  if not a:
    return b
  if not b:
    return a
  c = [] # result list
  while True:
    # TODO -- are there some list iterators for Python?
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
      c.append(a.pop(0))
    else:
      c.append(b.pop(0))
    

if __name__ == '__main__':
  # TODO - call testing infra
  sorted = merge_sort([1,4,3,2,5])
  print sorted
