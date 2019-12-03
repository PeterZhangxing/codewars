import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
from sklearn.metrics import silhouette_score

# read data from 4 different csv files
prior = pd.read_csv("data_source/order_products__prior.csv")
products = pd.read_csv("data_source/products.csv")
orders = pd.read_csv("data_source/orders.csv")
aisles = pd.read_csv("data_source/aisles.csv")

# merge 4 csv files into one file
mged_pri_pro = pd.merge(prior,products,left_on="product_id",right_on="product_id")
mged_pri_pro_ord = pd.merge(mged_pri_pro,orders,on=['order_id', 'order_id'])
mged_table = pd.merge(mged_pri_pro_ord,aisles,on=['aisle_id','aisle_id'])

# build cross table based on aisle per user
cross_table = pd.crosstab(mged_table['user_id'],mged_table['aisle'])

# do decomposition to cross_table with PCA
pca_obj = PCA(n_components=0.95)
data = pca_obj.fit_transform(cross_table)

# get some data from the big table
x = data[:1000]
# print(x.shape)
# (1000, 44)

# classify x to 7 differnt classes with k-means
km_obj = KMeans(n_clusters=7)
km_obj.fit(x)
predict = km_obj.predict(x)
# print(predict)
'''
[5 0 5 5 5 5 0 5 5 0 5 5 5 0 5 5 0 5 5 5 0 5 5 5 5 5 3 0 5 5 5 5 5 5 0 5 4
 0 0 5 5 5 0 5 5 0 5 0 5 1 5 5 5 1 5 0 5 5 5 5 5 5 4 0 0 5 5 5 5 5 4 5 5 5
 4 5 0 5 0 0 5 0 5 5 5 4 0 5 4 3 0 5 5 5 0 5 5 5 0 5 0 0 5 5 5 5 5 5 5 4 5
 0 5 0 5 5 5 0 5 5 5 5 5 0 5 0 5 5 5 5 5 5 0 5 5 5 5 5 5 2 5 4 0 5 5 4 5 5
 0 5 0 3 4 0 0 5 5 5 5 0 4 5 5 5 5 5 5 5 5 5 5 5 4 0 5 5 5 5 5 4 5 0 5 5 5
 5 5 5 5 0 5 5 5 5 0 5 4 5 5 0 5 4 5 4 5 0 5 5 3 1 5 5 5 1 5 0 5 5 0 0 0 0
 2 5 5 0 1 5 0 5 5 1 4 4 0 4 5 5 5 5 5 5 1 5 5 5 5 1 5 5 5 5 5 5 0 0 0 0 5
 5 5 0 5 2 5 5 0 5 5 5 5 5 5 5 0 5 5 4 0 2 4 5 5 0 5 5 5 5 1 3 5 5 5 0 0 5
 5 5 5 0 5 5 5 0 5 0 5 5 4 5 0 5 1 5 5 0 5 5 5 0 1 0 2 5 5 5 2 5 5 5 5 0 5
 1 5 5 0 5 5 5 0 5 5 5 5 5 5 0 5 0 0 0 5 5 0 5 0 5 0 5 5 0 0 0 5 5 5 5 5 0
 5 5 1 5 5 5 5 5 0 5 4 0 0 5 5 5 5 5 0 4 0 5 0 0 5 0 5 1 5 5 5 5 4 5 5 5 5
 5 2 0 5 5 0 5 5 5 5 0 5 5 5 0 5 5 0 5 5 5 5 5 5 4 5 5 5 5 5 0 5 5 5 0 0 6
 5 5 5 4 5 0 0 4 5 4 5 5 5 5 0 5 5 2 5 4 4 1 5 5 5 5 5 5 0 5 5 0 5 5 0 0 1
 5 5 5 0 4 4 0 0 5 5 5 5 0 0 2 0 5 5 5 5 0 4 5 5 5 5 0 0 5 5 5 5 5 5 2 5 5
 5 0 5 5 5 5 0 5 5 4 4 5 0 5 5 5 0 5 5 0 0 5 5 5 0 5 5 5 5 5 5 0 5 0 5 5 0
 5 5 0 4 0 5 5 5 0 5 5 0 5 5 5 5 5 5 0 5 5 5 5 5 0 5 4 1 5 5 5 5 0 5 5 5 5
 5 5 5 1 5 5 5 0 5 5 5 4 5 0 5 5 5 5 5 1 0 5 5 4 5 0 5 5 5 5 0 5 5 4 5 5 5
 0 5 5 5 5 5 5 5 5 5 5 4 5 0 5 0 1 5 5 2 0 0 0 4 5 2 5 0 2 5 0 5 5 5 5 5 5
 3 0 0 5 5 4 5 5 5 5 5 0 5 5 5 5 5 5 5 5 4 3 5 2 5 5 5 5 5 4 5 0 2 0 5 5 5
 5 5 0 5 5 5 0 5 5 5 5 5 5 5 5 1 0 0 5 4 5 0 5 0 0 0 5 5 5 5 0 0 5 5 0 5 5
 4 5 5 5 5 5 5 5 5 5 5 0 5 5 5 0 5 0 5 5 0 1 5 5 5 5 0 4 5 5 5 5 5 0 5 5 0
 0 0 5 5 5 5 5 5 2 5 5 5 5 5 5 5 5 5 5 5 5 5 0 5 0 0 5 5 5 5 5 0 5 5 2 5 5
 5 0 0 4 5 5 5 5 5 5 5 5 5 5 5 0 5 5 0 0 5 5 5 5 4 5 0 0 5 0 0 5 1 0 0 5 5
 1 0 1 0 5 4 5 5 0 5 5 0 0 5 4 5 4 5 1 5 5 5 0 5 5 0 5 4 4 0 5 5 5 0 0 5 0
 5 4 0 0 0 1 5 4 5 4 0 0 5 5 5 5 5 5 4 0 5 5 1 5 5 0 5 5 0 5 0 5 5 5 5 0 5
 5 5 5 5 5 5 0 4 5 0 5 5 5 5 5 0 5 5 5 0 0 4 5 5 5 5 5 5 5 5 5 4 2 5 0 4 4
 0 2 5 0 5 4 0 5 5 0 1 5 0 5 0 0 5 4 5 4 5 0 5 5 5 5 5 5 5 5 5 5 4 5 0 0 2
 0]
'''

# drawing scatter picture
plt.figure(figsize=(50,50),dpi=80)

colors = ['orange', 'green', 'blue', 'purple','red','yellow','black']
pre_color = [ colors[i] for i in predict ]

plt.scatter(x[:,3],x[:,7],color=pre_color)
plt.show()

# using silhouette_samples to judge the result of k-means
res = silhouette_score(x,predict)
# print(res)
'''
0.4332456196844815
'''