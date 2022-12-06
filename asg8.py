from logging import PlaceHolder
import math
from multiprocessing import Value
from itertools import combinations
import pylab as pl
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import numpy as np
import numpy.random as random
from  numpy.core.fromnumeric import *
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import math as m
import plotly.figure_factory as ff
from collections import Counter
import streamlit as st

def app(Data):
    st.title("Assignment 8")
    def printf(url):
         st.markdown(f'<p style="color:#000;font:lucida;font-size:25px;">{url}</p>', unsafe_allow_html=True)
    operation = st.selectbox("Operation", ["Crawler_bfs","Crawler_dfs","Page_Rank_Algo"])
    if operation == "Crawler_bfs":
        vis = dict()
        sst = set()
        q = []
        def bfs():
            while(len(q)>0):
                nxt_url = q[0] 
                q.pop(0)
                try:
                    st.write("*************************level: ",vis[nxt_url],"*******************************")
                    # if(vis[link.get('href')])>6:
                        # return 
                except KeyError:
                    pass
                try:
                    req = Request(nxt_url)
                    html_page = urlopen(req)
                    soup = BeautifulSoup(html_page, "lxml")
                except Exception:
                    pass
                cnt = 0 ;
                for link in soup.findAll('a'):
                    st.write(link.get('href'))
                    # if(vis[link.get('href')]==0):
                    if(link.get('href') not in sst):
                        q.append(link.get('href'))
                        sst.add(link.get('href'))
                    try:
                        vis[link.get('href')] = vis[nxt_url] + 1
                        if(vis[link.get('href')])>5:
                            return  
                    except KeyError:
                        pass
                    cnt = cnt + 1 ;
                    if(cnt>20):
                        break 
            
                # for link in links:
                    # print(link) 
                if(len(sst)>10000):
                    return 

        seed_url = "http://google.com"
        # req = Request("http://google.com")
        # html_page = urlopen(req)

        # soup = BeautifulSoup(html_page, "lxml")

        # links = []
        # for link in soup.findAll('a'):
        #     links.append(link.get('href'))
        vis[seed_url] = 0  
        q.append(seed_url)
        bfs()

        # for link in st: 
            # print(link)
        # for link in links:
        #     print(link)
    if operation == "Crawler_dfs":
        q = []
        # vis = dict()
        sst = set()
        def dfs():
            while(len(q)>0):
                nxt_url = q[-1] 
                q.pop(-1)
                try:
                    req = Request(nxt_url)
                    html_page = urlopen(req)

                    soup = BeautifulSoup(html_page, "lxml")
                except Exception:
                    pass
                cnt = 0 ;
                for link in soup.findAll('a'):
                    if(link is not None):
                        st.write(link.get('href'))
                    # if(vis[link.get('href')]==0):
                    if(link.get('href') not in sst):
                        q.append(link.get('href'))
                        sst.add(link.get('href'))
                    try:
                        pass
                        # vis[link.get('href')] = vis[nxt_url] + 1
                        # if(vis[link.get('href')])>5:
                            # return  
                    except KeyError:
                        pass
                    cnt = cnt + 1 ;
                    if(cnt>20):
                        break 
            
                # for link in links:
                    # print(link) 
                if(len(sst)>10000):
                    return 

        seed_url = "http://google.com"
        # req = Request("http://google.com")
        # html_page = urlopen(req)

        # soup = BeautifulSoup(html_page, "lxml")

        # links = []
        # for link in soup.findAll('a'):
        #     links.append(link.get('href'))
        # vis[seed_url] = 0  
        q.append(seed_url)
        dfs()

        # for link in st: 
            # print(link)
        # for link in links:
        #     print(link)

    if operation == "Page_Rank_Algo":
        # file = open("C:\\Users\\Akash\\Downloads\\data mining\\Assignment8\\stnfordgraph.txt", "r")
        flg = 0 ;
        # content = file.readlines()
        # l = str(Data.loc[0])
        # print(l)
        # l = l.split(' ')
        # print("Data row : " , l[0],"***",l[1])
        # print("Data col 1 : ", Data.loc[0][0])
        # print("Data col 2 : ", Data.loc[0][1])
        # print("Data type : ", type(Data.loc[0]))
        adj_mat = {}
        print(len(Data))
        for i in range(0,len(Data)):
            # print(line)
            if(flg==0):
                l = str(Data.loc[i])
                # print(l)
                l = l.split(' ')
                # lin = line.split(' ')
                vertex = int(l[0])
                edges = int(l[1])
                print("Vertex :",vertex)
                print("Edges :",edges)
                # print(edges)
                flg = 1
                adj_mat = {new_list: [] for new_list in range(vertex+1)}
                in_deg = [0]*(vertex+1)
                out_deg = [0]*(vertex+1)
                # print(adj_mat)
            else:
                # lin = line.split(' ')
                # tmp = lin[0].split('\t')
                # print(tmp)  
                l = str(Data.loc[3,str(vertex)])
                # print(l)
                l = l.split(' ')
                print(l)
                # lin = line.split(' ')
                # vertex = int(l[0])
                # edges = int(l[1])
                adj_mat[int(l[1])].append(int(l[0])) 
                # adj_mat[int(tmp[1][:-1])].append(int(tmp[0]))
                # in_deg[int(tmp[1][:-1])] += 1
                in_deg[int(l[1])] += 1
                # out_deg[int(tmp[0])] += 1
                out_deg[int(l[0])] += 1
        # file = open('geek.txt','w')
        # print(out_deg)
        def calclute_pagerank():
            cnt = 0
            itr = 1
            while(cnt<=vertex+1):
                # file.write(str("******Iteration" +str(itr)+" ******"))
                for i in range(1,vertex+1):
                    tmp_prnk[i] = 0 ;
                    for no in adj_mat[i]:
                        tmp_prnk[i] += (page_Rank[no]/out_deg[no])
                    if((abs(tmp_prnk[i]-page_Rank[i])/(page_Rank[i]))*100<=0.0001):
                        cnt += 1
                    if(tmp_prnk[i]):
                        page_Rank[i] = tmp_prnk[i]
                    # file.write(str(page_Rank[i])+" ")
                itr+=1 
        
        # vertex = 6
        # adj_mat = {1:[3],2:[1,3],3:[1],4:[6,5],5:[3,4],6:[5,4]}
        page_Rank = [1/(vertex)]*(vertex+1)
        tmp_prnk = [0]*(vertex+1) 
        page_Rank[0] = 0
        # out_deg = [0,2,0,3,2,2,1]
        # file.write(str(page_Rank))
        calclute_pagerank()
        index = {}
        for i in range(1,vertex+1):
            index[page_Rank[i]] = i ;
        page_Rank.sort()
        for i in range(1,11):
            st.write("Top ",i, "web page number is ", index[page_Rank[-i]] , "page rank is ",page_Rank[-i]);
        # st.write("Web and their Page rank")
        # for i in range(1,vertex+1):
            # st.write(i," page their ",page_Rank[-i])





        