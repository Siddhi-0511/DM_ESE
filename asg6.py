from logging import PlaceHolder
import math
from multiprocessing import Value
import streamlit as st
import pylab as pl
import numpy as np
import numpy.random as random
from  numpy.core.fromnumeric import *
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import math as m
from sklearn.datasets import make_blobs 
import plotly.figure_factory as ff
from scipy.cluster import hierarchy
from scipy.cluster.hierarchy import dendrogram, linkage


def app(data):
    st.title("Assignment 6")
    def printf(url):
         st.markdown(f'<p style="color:#000;font:lucida;font-size:25px;">{url}</p>', unsafe_allow_html=True)

    operation = st.selectbox("Operation", ["AGNES",'DBSCAN','K-MEANS', 'K-MEDOIDE'])
    if operation == "AGNES":
        # data = """1,0.697,0.46,2,0.774,0.376,3,0.634,0.264,4,0.608,0.318,5,0.556,0.215,6,0.403,0.237,7,0.481,0.149,8,0.437,0.211,9,0.666,0.091,10,0.243,0.267,11,0.245,0.057,12,0.343,0.099,13,0.639,0.161,14,0.657,0.198,15,0.36,0.37,16,0.593,0.042,17,0.719,0.103,18,0.359,0.188,19,0.339,0.241,20,0.282,0.257,21,0.748,0.232,22,0.714,0.346,23,0.483,0.312,24,0.478,0.437,25,0.525,0.369,26,0.751,0.489,27,0.532,0.472,28,0.473,0.376,29,0.725,0.445,30,0.446,0.459"""
        cols = []
        for i in data.columns[:-1]:
            cols.append(i)
        atr1, atr2 = st.columns(2)
        attribute1 = atr1.selectbox("Select Attribute 1", cols)
        attribute2 = atr2.selectbox("Select Attribute 2", cols, index=1)
        dataset = []
        arr1 = []
        arr2 = []
        for i in range(len(data)):
                arr1.append(data.loc[i, attribute1])
        for i in range(len(data)):
                arr2.append(data.loc[i, attribute2])
        for i in range(len(arr1)):
            tmp = []
            tmp.append(arr1[i])
            tmp.append(arr2[i])
            dataset.append(tmp)
        st.write(dataset)

        def dist(a, b):
            return math.sqrt(math.pow(a[0]-b[0], 2)+math.pow(a[1]-b[1], 2))

#dist_min
        def dist_min(Ci, Cj):
            return min(dist(i, j) for i in Ci for j in Cj)
#dist_max
        def dist_max(Ci, Cj):
            return max(dist(i, j) for i in Ci for j in Cj)
    #dist_avg
        def dist_avg(Ci, Cj):
            return sum(dist(i, j) for i in Ci for j in Cj)/(len(Ci)*len(Cj))

        def find_Min(M):
            min = 1000
            x = 0
            y = 0
            for i in range(len(M)):
                for j in range(len(M[i])):
                    if i != j and M[i][j] < min:
                        min = M[i][j];
                        x = i; 
                        y = j
            return (x, y, min)

        def AGNES(dataset, dist, k):
            C = []
            M = []
            for i in dataset:
                Ci = []
                Ci.append(i)
                C.append(Ci)
#     print(C)
            for i in C:
                Mi = []
                for j in C:
#             print(Mi)
                    Mi.append(dist(i, j))
                M.append(Mi)
#     print(len(M))
            q = len(dataset)
#     print(q)
            while q > k:
                x, y, min = find_Min(M)
#         print(find_Min(M))
                C[x].extend(C[y])
                C.remove(C[y])
                M = []
                for i in C:
                    Mi = []
                    for j in C:
                        Mi.append(dist(i, j))
                    M.append(Mi)
                q -= 1
            return C
        def draw(C):
            st.subheader("Plot of cluster using AGNES")
            colValue = ['r', 'y', 'g', 'b', 'c', 'k', 'm']
            c = ["Setosa","Versicolor","Virginica"]
            for i in range(len(C)):
                coo_X = []    
                coo_Y = []    
                for j in range(len(C[i])):
                    coo_X.append(C[i][j][0])
                    coo_Y.append(C[i][j][1])
                pl.xlabel(attribute1)
                pl.ylabel(attribute2)
                pl.scatter(coo_X, coo_Y, marker='x', color=colValue[i%len(colValue)], label=i)

            pl.legend(loc='upper right')
            st.pyplot()
        n = st.number_input('Insert value for K',step = 1 , min_value = 1)
# st.write('The current number is ', number)
        C = AGNES(dataset, dist_avg,n)
        draw(C)
        # C = np.array(C,dtype=np.double)
        # st.write(C)
        # Z = hierarchy.linkage(C, method='average')
        # plt.figure()
        # plt.title("Dendrograms")
        # dendrogram = hierarchy.dendrogram(Z)
    if operation == "DBSCAN":

        def calDist(X1 , X2 ):
            sum = 0
            for x1 , x2 in zip(X1 , X2):
                sum += (x1 - x2) ** 2
            return sum ** 0.5
            return (((X1[0]-X2[0])**2)+(X1[1]-X2[1])**2)**0.5


        def getNeibor(data , dataSet , e):
            res = []
            for i in range(len(dataSet)):
                if calDist(data , dataSet[i])<e:
                    res.append(i)
            return res


        def DBSCAN(dataSet , e , minPts):
            coreObjs = {}
            C = {}
            n = dataset 
            for i in range(len(dataSet)):
                neibor = getNeibor(dataSet[i] , dataSet , e)
                if len(neibor)>=minPts:
                    coreObjs[i] = neibor
            oldCoreObjs = coreObjs.copy()
            k = 0
            notAccess = list(range(len(dataset)))
            while len(coreObjs)>0:
                OldNotAccess = []
                OldNotAccess.extend(notAccess)
                cores = coreObjs.keys()
                randNum = random.randint(0,len(cores))
                cores=list(cores)
                core = cores[randNum]
                queue = []
                queue.append(core)
                notAccess.remove(core)
                while len(queue)>0:
                    q = queue[0]
                    del queue[0]
                    if q in oldCoreObjs.keys() :
                        delte = [val for val in oldCoreObjs[q] if val in notAccess]
                        queue.extend(delte)
                        notAccess = [val for val in notAccess if val not in delte]
                k += 1
                C[k] = [val for val in OldNotAccess if val not in notAccess]
                for x in C[k]:
                    if x in coreObjs.keys():
                        del coreObjs[x]
            return C


        def draw(C , dataSet):
            color = ['r', 'y', 'g', 'b', 'c', 'k', 'm']
            vis = set()
            for i in C.keys():
                X = []
                Y = []
                datas = C[i]
                for k in datas:
                    vis.add(k)
                for j in range(len(datas)):
                    X.append(dataSet[datas[j]][0])
                    Y.append(dataSet[datas[j]][1])
                plt.scatter(X, Y, marker='o', color=color[i % len(color)], label=i)
            vis = list(vis)
            unvis1 = []
            unvis2 = []
            for i in range(len(dataSet)):
                if i not in vis:
                    unvis1.append(dataSet[i][0])
                    unvis2.append(dataSet[i][1])
            st.subheader("Plot of cluster's after DBSCAN ")
            plt.xlabel(attribute1)
            plt.ylabel(attribute2)
            plt.scatter(unvis1,unvis2,marker='o',color = 'black')
            plt.legend(loc='lower right')
            plt.show()
            st.pyplot()


        cols = []
        for i in data.columns[:-1]:
            cols.append(i)
        atr1, atr2 = st.columns(2)
        attribute1 = atr1.selectbox("Select Attribute 1", cols)
        attribute2 = atr2.selectbox("Select Attribute 2", cols, index=1)
        dataset = []
        arr1 = []
        arr2 = []
        for i in range(len(data)):
                arr1.append(data.loc[i, attribute1])
        for i in range(len(data)):
                arr2.append(data.loc[i, attribute2])
        for i in range(len(arr1)):
            tmp = []
            tmp.append(arr1[i]);
            tmp.append(arr2[i])
            dataset.append(tmp)
        r =  st.number_input('Insert value for eps',)
        mnp =  st.number_input('Insert mimimum number of points in cluster',step = 1)        
        C = DBSCAN(dataset,1,12)
        draw(C, dataset)

    if operation == "K-MEANS":
        cols = []
        for i in data.columns[:-1]:
            cols.append(i)
        atr1, atr2 = st.columns(2)
        attribute1 = atr1.selectbox("Select Attribute 1", cols)
        attribute2 = atr2.selectbox("Select Attribute 2", cols, index=1)
        # print(attribute1)
        # print(attribute2)
        class color:
            PURPLE = '\033[95m'
            CYAN = '\033[96m'
            DARKCYAN = '\033[36m'
            BLUE = '\033[94m'
            GREEN = '\033[92m'
            YELLOW = '\033[93m'
            RED = '\033[91m'
            BOLD = '\033[1m'
            UNDERLNE = '\033[4m'
            END = '\033[0m'
        def plot_data(X):
            plt.figure(figsize=(7.5,6))
            for i in range(len(X)):
                plt.scatter(X[i][0],X[i][1],color='k')   
        
        def random_centroid(X,k):
            random_idx=[np.random.randint(len(X)) for i in range(k)]
            centroids=[]
            for i in random_idx:
                centroids.append(X[i])
            return centroids

        def assign_cluster(X,ini_centroids,k):
            cluster=[] 
            for i in range(len(X)):
                euc_dist=[] 
                for j in range(k):
                    euc_dist.append(np.linalg.norm(np.subtract(X[i],ini_centroids[j]))) 
                idx=np.argmin(euc_dist) 
                cluster.append(idx) 
            return np.asarray(cluster)

        def compute_centroid(X,clusters,k):
            centroid = [] 
            for i in range(k):
                temp_arr=[]
                for j in range(len(X)):
                    if clusters[j]==i:
                        temp_arr.append(X[j])
                centroid.append(np.mean(temp_arr,axis=0))
            return np.asarray(centroid)

        def difference(prev,nxt):
            diff=0
            for i in range(len(prev)):
                diff+=np.linalg.norm(prev[i]-nxt[i])
            return diff

        def show_clusters(X,clusters,centroids,ini_centroids,mark_centroid=True,show_ini_centroid=True,show_plots=True):
            cols={0:'r',1:'b',2:'g',3:'coral',4:'c',5:'lime'}
            fig,ax=plt.subplots(figsize=(7.5,6));
            for i in range(len(clusters)):
                ax.scatter(X[i][0],X[i][1],color=cols[clusters[i]])
            for j in range(len(centroids)):
                ax.scatter(centroids[j][0],centroids[j][1],marker='*',color=cols[j])
                if show_ini_centroid==True:
                    ax.scatter(ini_centroids[j][0],ini_centroids[j][1],marker="+",s=150,color=cols[j])
            if mark_centroid==True:
                for i in range(len(centroids)):
                    ax.add_artist(plt.Circle((centroids[i][0],centroids[i][1]),0.4,linewidth=2,fill=False))
                    if show_ini_centroid==True:
                        ax.add_artist(plt.Circle((ini_centroids[i][0],ini_centroids[i][1]),0.4,linewidth=2,color='y',fill=False))
            ax.set_xlabel(attribute1)
            ax.set_ylabel(attribute2)
            ax.set_title("K-means Clustering")
            if show_plots==True:
                plt.show()
                st.pyplot()
            if show_plots==True:
                plt.show()
                st.pyplot()

        
        def k_means(X,k,show_type='all',show_plots=True):
            c_prev = random_centroid(X,k)
            cluster=assign_cluster(X,c_prev,k) 
            diff = 10 
            ini_centroid = c_prev;     
            st.write("NOTE:\n +  Yellow Circle -> Initial Centroid\n * Black Circle -> Final Centroid")
            if show_plots:
                st.write("Initial Plot:")
                show_clusters(X,cluster,c_prev,ini_centroid,show_plots=show_plots)
            while diff>0.0001:
                cluster = assign_cluster(X,c_prev,k) 
                if show_type=='all' and show_plots:
                    show_clusters(X,cluster,c_prev,ini_centroid,False,False,show_plots=show_plots)
                    mark_centroid=False 
                    show_ini_centroid=False 
                c_new = compute_centroid(X,cluster,k) 
                diff = difference(c_prev,c_new) 
                c_prev=c_new 
        
            if show_plots:
                st.write("Initial Cluster Centers:")
                st.write(ini_centroid)
                st.write("Final Cluster Centers:")
                st.write(c_prev)
                st.write("Final Plot:") 
                show_clusters(X,cluster,c_prev,ini_centroid,mark_centroid=True,show_ini_centroid=True)    
            return cluster,c_prev
        def validate(original_clus,my_clus,k):
            ori_grp=[]
            my_grp=[]
            for i in range(k):
                temp=[]
                temp1=[]
                for j in range(len(my_clus)):
                    if my_clus[j]==i:
                        temp.append(j)
                    if original_clus[j]==i:
                        temp1.append(j)
                my_grp.append(temp)
                ori_grp.append(temp1)
            same_bool=True
            for f in range(len(ori_grp)):
                if my_grp[f] not in ori_grp:
                    st.write("Not Same")
                    same_bool=False
                    break;
            if same_bool:
                st.write("Both the clusters are equal")
        k = st.number_input("Enter value for K",step=1,value=1)
        X,original_clus = make_blobs(n_samples=50, centers=3, n_features=2, random_state=len(attribute1))
        datat = []
        arr1 = []
        arr2 = []
        for i in range(len(data)):
                arr1.append(data.loc[i, attribute1])
        for i in range(len(data)):
                arr2.append(data.loc[i, attribute2])
        for i in range(len(arr1)):
            tmp = []
            tmp.append(arr1[i]);
            tmp.append(arr2[i])
            datat.append(tmp)
        cluster,centroid = k_means(datat,k,show_type='ini_fin')


    if operation == "K-MEDOIDE":
        cols = []
        for i in data.columns[:-1]:
            cols.append(i)
        atr1, atr2 = st.columns(2)
        attribute1 = atr1.selectbox("Select Attribute 1", cols)
        attribute2 = atr2.selectbox("Select Attribute 2", cols, index=1)
        class KMedoidsClass:
            def __init__(self,data,k,iters):
                self.data= data
                self.k = k
                self.iters = iters
                self.medoids = np.array([data[i] for i in range(self.k)])
                self.colors = np.array(np.random.randint(0, 255, size =(self.k, 4)))/255
                self.colors[:,3]=1

            def manhattan(self,p1, p2):
                return np.abs((p1[0]-p2[0])) + np.abs((p1[1]-p2[1]))

            def get_costs(self, medoids, data):
                tmp_clusters = {i:[] for i in range(len(medoids))}
                cst = 0
                for d in data:
                    dst = np.array([self.manhattan(d, md) for md in medoids])
                    c = dst.argmin()
                    tmp_clusters[c].append(d)
                    cst+=dst.min()

                tmp_clusters = {k:np.array(v) for k,v in tmp_clusters.items()}
                return tmp_clusters, cst

            def fit(self):

                self.datanp = np.asarray(data)
                samples,_ = self.datanp.shape

                self.clusters, cost = self.get_costs(data=self.data, medoids=self.medoids)
                count = 0

                colors =  np.array(np.random.randint(0, 255, size =(self.k, 4)))/255
                colors[:,3]=1

                st.subheader("Step : 0")
                plt.xlabel(attribute1)
                plt.ylabel(attribute2)
                [plt.scatter(self.clusters[t][:, 0], self.clusters[t][:, 1], marker="*", s=100,
                                        color = colors[t]) for t in range(self.k)]
                plt.scatter(self.medoids[:, 0], self.medoids[:, 1], s=200, color=colors)
                # plt.show()
                st.pyplot()

                while True:
                    swap = False
                    for i in range(samples):
                        if not i in self.medoids:
                            for j in range(self.k):
                                tmp_meds = self.medoids.copy()
                                tmp_meds[j] = i
                                clusters_, cost_ = self.get_costs(data=self.data, medoids=tmp_meds)

                                if cost_<cost:
                                    self.medoids = tmp_meds
                                    cost = cost_
                                    swap = True
                                    self.clusters = clusters_
                                    st.write(f"Medoids Changed to: {self.medoids}.")
                                    st.subheader(f"Step :{count+1}") 
                                    # count += 1  
                                    plt.xlabel(attribute1)
                                    plt.ylabel(attribute2)
                                    [plt.scatter(self.clusters[t][:, 0], self.clusters[t][:, 1], marker="*", s=100,
                                            color = colors[t]) for t in range(self.k)]
                                    plt.scatter(self.medoids[:, 0], self.medoids[:, 1], s=200, color=colors)
                                    # plt.show()
                                    st.pyplot()
                    count+=1

                    if count>=self.iters:
                        st.write("End of the iterations.")
                        break
                    if not swap:
                        st.write("End.")
                        break
        # dt = np.random.randint(0,100, (100,2))
        datat = []
        arr1 = []
        arr2 = []
        for i in range(len(data)):
                arr1.append(data.loc[i, attribute1])
        for i in range(len(data)):
                arr2.append(data.loc[i, attribute2])
        for i in range(len(arr1)):
            tmp = []
            tmp.append(arr1[i]);
            tmp.append(arr2[i])
            datat.append(tmp)
        k = st.number_input("Enter value fot k",step=1,min_value=1)
        kmedoid = KMedoidsClass(datat,k,10)
        kmedoid.fit()