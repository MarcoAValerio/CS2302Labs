# -*- coding: utf-8 -*-
"""
Lab 3
Professer: Olac Fuentes
MW 10:30-11:50
@author: Marco Valerio
"""

# Code to implement a binary search tree 
# Programmed by Olac Fuentes
# Last modified February 27, 2019

class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
        
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

def Delete(T,del_item):
    if T is not None:
        if del_item < T.item:
            T.left = Delete(T.left,del_item)
        elif del_item > T.item:
            T.right = Delete(T.right,del_item)
        else:  # del_item == T.item
            if T.left is None and T.right is None: # T is a leaf, just remove it
                T = None
            elif T.left is None: # T has one child, replace it by existing child
                T = T.right
            elif T.right is None:
                T = T.left    
            else: # T has two chldren. Replace T by its successor, delete successor
                m = Smallest(T.right)
                T.item = m.item
                T.right = Delete(T.right,m.item)
    return T
         
def InOrder(T):
    # Prints items in BST in ascending order
    if T is not None:
        InOrder(T.left)
        print(T.item,end = ' ')
        InOrder(T.right)
  
def InOrderD(T,space):
    # Prints items and structure of BST
    if T is not None:
        InOrderD(T.right,space+'   ')
        print(space,T.item)
        InOrderD(T.left,space+'   ')
  
def SmallestL(T):
    # Returns smallest item in BST. Returns None if T is None
    if T is None:
        return None
    while T.left is not None:
        T = T.left
    return T   
 
def Smallest(T):
    # Returns smallest item in BST. Error if T is None
    if T.left is None:
        return T
    else:
        return Smallest(T.left)

def Largest(T):
    if T.right is None:
        return T
    else:
        return Largest(T.right)   

def Find(T,k):
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or T.item == k:
        return T
    if T.item<k:
        return Find(T.right,k)
    return Find(T.left,k)

#The iterative version of find, the while serves the function of the recursive call
def searchIt(T,k):
    if T is None or T.item == k:
        return T
    while T is not None:
        if k > T.item:
            T = T.right
        if k < T.item:
            T = T.left
        else:
            return T

#This method traverse the list until K is zero and prints all on that level         
def printD(T,k):  
    if T is None: 
        return None
    if k == 0: 
        print(T.item, ' ') 
    else: 
        printD(T.left, k-1) 
        printD(T.right, k-1) 

def FindAndPrint(T,k):
    t = searchIt(T,k)
    
    if t is not None:
        print(t.item,'found')
    else:
        print(k,'not found')
    
# Code to test the functions above

T = None
A = [70, 50, 90, 130, 150, 40, 10, 30, 100, 180, 45, 60, 140, 42]
for a in A:
    T = Insert(T,a)
    
InOrder(T)
print()
InOrderD(T,'')
print()
FindAndPrint(T,10)
print()
FindAndPrint(T,5)
print()
print('Keys at depth:', 0)
printD(T,0)
print('Keys at depth:', 1)
printD(T,1)
print('Keys at depth:', 2)
printD(T,2)
print('Keys at depth:', 3)
printD(T,3)
print('Keys at depth:', 4)
printD(T,4)
