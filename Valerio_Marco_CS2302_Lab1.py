# -*- coding: utf-8 -*-
"""
Lab 1

@author: Marco Valerio
"""
import math
import numpy as np
import matplotlib.pyplot as plt
"""
Slicing the array and plotting the ponits
For this one I was not able to make the four corner squares, but I was able to shrink the 
square properly
"""
def draw_squares(ax,n,p,w):
    if n>0:
        q = p*w 
        ax.plot(p[:,0],p[:,1],Linewidth=1,color='k') 
        draw_squares(ax,n-1,q,w/2)

plt.close("all") 
orig_size = 800
q1_size = 1000
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
draw_squares(ax,6,p,.5)
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('squares.png')

plt.close("all") 
orig_size = 800
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
draw_squares(ax,6,p,.7)
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('squares1.png')

def binary_tree(ax,t,n):
    if n>0:
        t1 = t/2
        ax.plot(t[:,0],t[:,1],Linewidth=1,color='k')
        binary_tree(ax,t1,n-1)
        
"""For the binary tree I plotted the first two branches of the binary tree using np.array
    This bit of code goes through binary_tree() one time to show the code can produce the shape
"""
plt.close("all") 
orig_size = 50
t = np.array([[0,0],[orig_size*.5,orig_size*.5],[orig_size,0],[orig_size*.5,orig_size*.5],[orig_size,orig_size],[orig_size*1.5,orig_size*.5],[orig_size*1.25,0],[orig_size*1.5,orig_size*.5],[orig_size*2,0]])
fig, ax = plt.subplots()
binary_tree(ax,t,1)
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('binary1.png')

"""
This section of calls binary_tree() multiple times to show it will work under the recursive calls
As you can see in the result the tree only grows on the left side of the tree and decreases in
size by 2
I used the same format for the squares on to plot the base of the tree
"""
plt.close("all") 
orig_size = 50
t = np.array([[0,0],[orig_size*.5,orig_size*.5],[orig_size,0],[orig_size*.5,orig_size*.5],[orig_size,orig_size],[orig_size*1.5,orig_size*.5],[orig_size*1.25,0],[orig_size*1.5,orig_size*.5],[orig_size*2,0]])
fig, ax = plt.subplots()
binary_tree(ax,t,10)
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('binary2.png')

"""
Using the provided code for circles I modded them to attempt the new patterns
I was able to get the one which shifted the center of the circle to the left
"""
def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y
"""
In order to shift the center of the circle to the left, I add the radius to the x 
coordinate every time it runs through draw_circles()
"""
def draw_circles(ax,n,center,radius,w):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x+radius,y,color='k')
        draw_circles(ax,n-1,center,radius*w,w)
      
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 5, [100,0], 100,.9)
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('circles_single.png')

plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 50, [100,0], 100,.9)
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('circles.png')

def circle1(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y
"""
draw_circles1() was my attempt on the tri-nested circles, I modified the x,y coordinates
by dividing the radius by 3 and plotting the circle 4 times
I was able to get one of the cirlces in the correct design, but it had extra circles

"""

def draw_circles1(ax,n,center,radius,w):
    if n>0:
        x,y = circle1(center,radius/3)
        ax.plot(x,y,color='k')
        ax.plot(x+radius,y,color='k')
        ax.plot(x-radius,y,color='k')
        ax.plot(x,y+radius,color='k')
        ax.plot(x,y-radius,color='k')
        draw_circles1(ax,n-1,center,radius*w,w)
    
plt.close("all")    
fig, ax = plt.subplots() 
draw_circles1(ax, 2, [100,0], 50,.3)
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('circles1_single.png')

plt.close("all")    
fig, ax = plt.subplots() 
draw_circles1(ax, 5, [100,0], 50,.3)
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('circles1.png')



