#!/usr/bin/env python3

def return_evens(num_list):
   # print([n / 2 for n in num_list])
   # print([(n **2) - 1 for n in range(1, 11)])
  even_num = list()
  print(num_list)
  for n in num_list:
    print('n', n)
    if(n % 2 == 0):
      even_num.append(n)
  return even_num


def make_exclamation(sentence_list):
    pass