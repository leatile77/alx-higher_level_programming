#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
   new_dict =  list(a_dictionary.keys())
   new_dict.sort()
   for i in new_dict:
      print("{}: {}".format(i, a_dictionary.get(i)))
