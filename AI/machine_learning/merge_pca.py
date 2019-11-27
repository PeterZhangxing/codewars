from sklearn.decomposition import PCA
import pandas as pd

# 读取四张表的数据
prior = pd.read_csv("data_source/order_products_prior.csv")
products = pd.read_csv("data_source/products.csv")
orders = pd.read_csv("data_source/orders.csv")
aisles = pd.read_csv("data_source/aisles.csv")

# 按照两张表共有的某列，将四张表合成为一张大表
_mg_table = pd.merge(prior,products,on=['product_id','product_id'])
_mg_table =pd.merge(_mg_table,orders,on=['order_id','order_id'])
mtab = pd.merge(_mg_table,aisles,on=['aisle_id','aisle_id'])

# 查看合并后的表的前三行数据
print(mtab.head(3))

# 使用交叉表，统计每个客户所购买的所有产品的个数
cli_pro_cross = pd.crosstab(mtab['user_id'],mtab['aisle'])
print(cli_pro_cross.head(3))

# 对上面的描述每个客户各类商品分别买了多少的表，进行降维处理
pca = PCA(n_components=0.95)
data = pca.fit_transform(cli_pro_cross)

print(data)