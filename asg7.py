from logging import PlaceHolder
import math
from multiprocessing import Value
import streamlit as st
from itertools import combinations
import pylab as pl
import numpy as np
import numpy.random as random
from  numpy.core.fromnumeric import *
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import math as m
import plotly.figure_factory as ff
from collections import Counter

def app(Data):
    st.title("Assignment 7")
    def printf(url):
         st.markdown(f'<p style="color:#000;font:lucida;font-size:25px;">{url}</p>', unsafe_allow_html=True)
    operation = st.selectbox("Operation", ["Apriori"])
    if operation == "Apriori":
        def Apriori():
            data = []
            cols = []
            for i in Data.columns[:-1]:
                cols.append(i)
            # atr1, atr2 = st.columns(2)
            # attribute1 = atr1.selectbox("Select Attribute 1", cols)
            # attribute2 = atr2.selectbox("Select Attribute 2", cols, index=1)
            k = 1
            for i in range(len(Data)):
                arr = []
                tm = []
                tm.append("T"+str(k))
                k+=1
                for j in cols:
                    arr.append((Data.loc[i,j]))
                
                tm.append(arr)
                data.append(tm)
            print("data:",data)
            # atr1, atr2 = st.columns(2)
            # attribute1 = atr1.selectbox("Select Attribute 1", cols)
            # attribute2 = atr2.selectbox("Select Attribute 2", cols, index=1)
            # for i in range(len(data)):
            #         arr1.append(data.loc[i, attribute1])
            # for i in range(len(data)):
            #         arr2.append(data.loc[i, attribute2])
            data = [
            ['T100',['I1','I2','I5']],
            ['T200',['I2','I4']],
            ['T300',['I2','I3']],
            ['T400',['I1','I2','I4']],
            ['T500',['I1','I3']],
            ['T600',['I2','I3']],
            ['T700',['I1','I3']],
            ['T800',['I1','I2','I3','I5']],
            ['T900',['I1','I2','I3']]
            ]

            init = []
            for i in data:
                for q in i[1]:
                    res = isinstance(q,str)
                    if(q not in init and res):
                        init.append(q)
            init = sorted(init)
            # print(init)
            # st.write(tg)
            # print(len(init))
            s = int(sp*len(init))



            c = Counter()
            for i in init:
                for d in data:
                    if(i in d[1]):
                        c[i]+=1
            # print("C1:")
            st.write(c)
            for i in c:
                pass
    # print(str([i])+": "+str(c[i]))
            l = Counter()
            for i in c:
                if(c[i] >= s):
                    l[frozenset([i])]+=c[i]
            st.write(l)
# print("L1:")
            for i in l:
                pass
    # print(str(list(i))+": "+str(l[i]))
            # print()
            pl = l
            pos = 1
            for count in range(2,100000):
                nc = set()
                temp = list(l)
                for i in range(0,len(temp)):
                    for j in range(i+1,len(temp)):
                        t = temp[i].union(temp[j])
                        if(len(t) == count):
                            nc.add(temp[i].union(temp[j]))
                nc = list(nc)
                c = Counter()
                for i in nc:
                    c[i] = 0
                    for q in data:
                        temp = set(q[1])
                        if(i.issubset(temp)):
                            c[i]+=1
    # print("C"+str(count)+":")
                for i in c:
        # print(str(list(i))+": "+str(c[i]))
                    pass
                # print()\
                # st.write("s",s)
                l = Counter()
                for i in c:
                    if(c[i] >= s):
                        l[i]+=c[i]
    # print("L"+str(count)+":")
                for i in l:
        # print(str(list(i))+": "+str(l[i]))
                    pass
                print()
                if(len(l) == 0):
                    break
                pl = l
                pos = count
            # print("Result: ")
            st.write("Result: ")
# print("L"+str(pos)+":")
            for i in pl:
    # print(str(list(i))+": "+str(pl[i]))
                pass
# print()

            from itertools import combinations
            for l in pl:
                c = [frozenset(q) for q in combinations(l,len(l)-1)]
                mmax = 0
                for a in c:
                    b = l-a
                    ab = l
                    sab = 0
                    sa = 0
                    sb = 0
                    for q in data:
                        temp = set(q[1])
                        if(a.issubset(temp)):
                            sa+=1
                        if(b.issubset(temp)):
                            sb+=1
                        if(ab.issubset(temp)):
                            sab+=1
                    temp = sab/sa*100
                    if(temp == mmax):
                        mmax = temp
                    temp = sab/sb*100
                    if(temp > confidance):
                        mmax = temp
                        st.write(str(list(a))+" -> "+str(list(b))+" = "+str(sab/sa*100)+"%")
                        st.write(str(list(b))+" -> "+str(list(a))+" = "+str(sab/sb*100)+"%")
                curr = 1
                st.write("choosing:", end=' ')
                for a in c:
                    b = l-a
                    ab = l
                    sab = 0
                    sa = 0
                    sb = 0
                    for q in data:
                        temp = set(q[1])
                        if(a.issubset(temp)):
                            sa+=1
                        if(b.issubset(temp)):
                            sb+=1
                        if(ab.issubset(temp)):
                            sab+=1
                    temp = sab/sa*100
                    if(temp == mmax):
                        st.write(curr, end = ' ')
                    curr += 1
                    temp = sab/sb*100
                    if(temp == mmax):
                        st.write(curr, end = ' ')
                    curr += 1
                # print()
                # print()
        
        sp =  st.number_input('Insert value for Support',)
        confidance  =  st.number_input('Insert value for confidance',step=1)
        Apriori()