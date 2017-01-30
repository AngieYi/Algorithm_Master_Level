#!/usr/bin/env python
import sys

def sort(a):
    if a == []:
        return []
    pivot = a[0]
    left = [x for x in a if x < pivot]
    right = [x for x in a[1:] if x >= pivot]
    return [sort(left)] + [pivot] + [sort(right)]

def sorted(tree):
    return [] if tree == [] else sorted(tree[0]) + [tree[1]] + sorted(tree[2])

def search0(tree, x):
    if tree == [] or tree[1] == x:
        return tree
    return search0(tree[0], x) if x < tree[1] else search0(tree[2], x)

def search(tree, x):
    return search0(tree,x) != []

def insert(tree, x):
    r = search0(tree, x)
    if r == []:
        r += [[], x, []]
