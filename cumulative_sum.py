#!/usr/bin/env python



def test1():
  '''
  (none) -> none
  
  this function implements a cumulative sum by taking the sum of 
  sublists from the original list

  We expect this to run in quadratic time.
  '''

  lst = range(20)
  return [reduce(lambda x,y: x + y, lst[:i]) for i in range(1,len(lst))]


def test2():
  '''
  (none) -> none

  This function implements a cumulative sum by keeping a trailing sum
  from sublists and incrementing by the next num from the original
  list.

  We expect this to run in linear time.
  '''

  lst = range(20)
  tmp = []
  itmp = 0

  for item in lst:
    tmp.append(item + itmp)
    itmp = tmp[-1]  
  return tmp



if __name__ == '__main__':
  
  import timeit
  
  print(timeit.timeit("test1()", setup="from __main__ import test1"))
  print(timeit.timeit("test2()", setup="from __main__ import test2"))
