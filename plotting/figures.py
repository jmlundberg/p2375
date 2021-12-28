# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 10:19:54 2021

@author: johan
"""

# -*- coding: utf-8 -*-
"""
Example of how partition
that is range-of-nth nth_element 
can be used to equalize data

@author: johan
"""


import numpy
import numpy as np
from PIL import Image
nan=np.nan
from matplotlib import pyplot as plt 
import matplotlib
import matplotlib.cm as cm
import math
from matplotlib.patches import Rectangle
from matplotlib.patches import Rectangle

def saveFig(fg,name):
    bbox_inches='tight'
    bbox = fig.get_tightbbox(fig.canvas.get_renderer())
    bbox
    bbox_inches=bbox
    fg.savefig("figs/"+name, dpi=1600,transparent=True, bbox_inches=bbox_inches)
    fg.savefig("figs/"+name.replace(".png",".pdf"), dpi=1600,transparent=True, bbox_inches=bbox_inches)

def swap(l,i1,i2):
    v=l[i1]
    l[i1]=l[i2]
    l[i2]=v

for case in ("rnd","sort","1a","1b","2","3","p","pend","qs"):
    exampleV=list(range(0,26))    
    np.random.seed(42)
    exampleV=np.random.permutation(exampleV)
    nths=[]
    if case == "rnd":
        np.random.seed(221)
        exampleV[8:]=np.random.permutation(range(8,26))
        exampleV[:8]=np.random.permutation(range(0,8))
    if case == "sort":
        exampleV=np.sort(exampleV)
    if case == "1a":
        nths=[7]
        np.random.seed(11)
        exampleV=np.partition(exampleV,nths)
        exampleV[8:]=np.random.permutation(range(8,26))
        exampleV[8:20]=np.random.permutation(range(8,20))
        exampleV[8:20]=np.random.permutation(range(8,20))
    if case == "1b":
        nths=[20]
        exampleV=np.partition(exampleV,nths)
        swap(exampleV,5,16)
        swap(exampleV,2,14)
        swap(exampleV,8,17)
        exampleV[21:]=[23,22,24,25,21]
        exampleV[8:20]=np.random.permutation(range(8,20))
        exampleV[8:20]=np.random.permutation(range(8,20))
    if case == "2":
        nths=[7,20]
        exampleV=np.partition(exampleV,nths)
        swap(exampleV,3,6)
        swap(exampleV,9,13)
        swap(exampleV,8,17)
        exampleV[21:]=[23,22,24,25,21]
        exampleV[8:20]=np.random.permutation(range(8,20))
        exampleV[8:20]=np.random.permutation(range(8,20))


    if case == "3":
        nths=[7,12,20]
        exampleV=np.partition(exampleV,nths)
        swap(exampleV,3,6)
        swap(exampleV,8,9)
        swap(exampleV,13,16)
        swap(exampleV,14,18)
        exampleV[21:]=[23,22,24,25,21]
        exampleV[13:20]=np.random.permutation(range(13,20))


    if case == "p":
        nths=[0,1,2,3,4,5,6,7]
        exampleV[:8]=nths
        np.random.seed(22)
        exampleV[8:]=np.random.permutation(range(8,26))

    if case == "pend":
        nths=list(range(20,26))
        exampleV[20:]=nths
        np.random.seed(22)
        exampleV[:20]=np.random.permutation(range(20))

    if case == "qs":
        exampleV=np.sort(exampleV)
        np.random.seed(17)
        exampleV[0:5]=np.random.permutation(range(0,5))
        np.random.seed(17)
        exampleV[7:14]=np.random.permutation(range(7,14))
        np.random.seed(22)
        exampleV[16:]=np.random.permutation(range(16,26))
        nths=[5,6,14,15]
        
    fig, ax1 = plt.subplots() 
    plt.tight_layout(pad=0, h_pad=None, w_pad=None, rect=None)
    fig.set_figwidth(4)
    fig.set_figheight(4)
    ax1.grid(color='#aaaaaa', linestyle='-', linewidth=0.37)
    ax1.set_aspect(1)
    plt.axis('off')
    plt.grid(False)
    #plt.rcParams.update({'font.size': 6})
    plt.rcParams.update({'font.size': 4})
    ax1.set_ylim([-0.1,1.95])
    ax1.set_xlim([-len(exampleV)*0.005,len(exampleV)*1.005])

    #t1 = plt.Rectangle([-0.5/2,-3],height=5,width=len(exampleV)+1.5,color="gray",ec="black",linewidth=1)
    #ax1.add_patch(t1)

    for i in nths:
        xofs=-0.01
        hofs=0.5
        t1 = plt.Circle([i+0.5+xofs,1+hofs],radius=0.35,color="#dddddd",ec="black",linewidth=0.5)
        ax1.add_patch(t1)
    
    for i,v in enumerate(exampleV):
        valcol=(v/len(exampleV))**0.9
        ax1.add_patch(Rectangle((i, 0), 1, 1,ec="black",fc=cm.hot(valcol)))
        col=0.99 if v/len(exampleV)<0.25 else 0
        tc=cm.gray(col)
        txt=v+100 #chr(65+v)
        ax1.text(i+0.5-0.01,0.5-0.05,txt,  ha='center', va='center',color=tc,fontsize=3.5)

    for i,v in enumerate(exampleV):
        txt=str(i)
        h=2.2+0.5
        if not nths:
            h=2
        h=2
        ax1.text(i+0.5-0.01,0.5-0.05-1+h,txt,  ha='center', va='center',color="black")
           
    if 0:
        for i in nths:
            h=0.6
            w=h/1.5
            xofs=0
            hofs=0.1
            t1 = plt.Polygon([[i-w+0.5,1+h+hofs],[i+0.5,1+hofs],[i+0.5+w,1+h+hofs]],color="black",ec="black",linewidth=0)
            ax1.add_patch(t1)



    fig.show() 
        
        # approximate equalize using 2,3 or 5 partition points to
        
    #saveFig(fig,"sorted.pdf")
    saveFig(fig,case+".png")
        
