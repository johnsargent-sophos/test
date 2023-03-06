#!/usr/bin/python

print("Hello")


def MyFunc(foo):
    print(foo)
  

def input():
    # example code snippet py_vuln00: Arbitrary Code Execution:
    compute_user_input = input('\nType something here to compute: ')

    if not compute_user_input:
            print ("No input")
    else:
            print ("Result: ", eval(compute_user_input))


MyFunc("World")

input()
