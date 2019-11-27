import pandas as pd
from sklearn.decomposition import PCA

# 读取数据文件
prior = pd.read_csv("data_source/order_products__prior.csv")
products = pd.read_csv("data_source/products.csv")
orders = pd.read_csv("data_source/orders.csv")
aisles = pd.read_csv("data_source/aisles.csv")

# print(prior.info())
# print(products.info())
# print(orders.info())
# print(aisles.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 32434489 entries, 0 to 32434488
Data columns (total 4 columns):
order_id             int64
product_id           int64
add_to_cart_order    int64
reordered            int64
dtypes: int64(4)
memory usage: 989.8 MB
None

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 49688 entries, 0 to 49687
Data columns (total 4 columns):
product_id       49688 non-null int64
product_name     49688 non-null object
aisle_id         49688 non-null int64
department_id    49688 non-null int64
dtypes: int64(3), object(1)
memory usage: 1.5+ MB
None

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3421083 entries, 0 to 3421082
Data columns (total 7 columns):
order_id                  int64
user_id                   int64
eval_set                  object
order_number              int64
order_dow                 int64
order_hour_of_day         int64
days_since_prior_order    float64
dtypes: float64(1), int64(5), object(1)
memory usage: 182.7+ MB
None

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 134 entries, 0 to 133
Data columns (total 2 columns):
aisle_id    134 non-null int64
aisle       134 non-null object
dtypes: int64(1), object(1)
memory usage: 2.2+ KB
None
'''

# 将客户信息和购买的商品合并到一张表中
_mg = pd.merge(prior, products, on=['product_id', 'product_id'])
_mg = pd.merge(_mg, orders, on=['order_id', 'order_id'])
mt = pd.merge(_mg, aisles, on=['aisle_id', 'aisle_id'])

# 用客户id分组数据,并且客户id为行,列是每种商品
cross = pd.crosstab(mt['user_id'], mt['aisle'])
# print(cross.shape)

# 使用PCA完成数据的降维操作,大幅减小特征值列数
pca = PCA(n_components=0.9)
data = pca.fit_transform(cross)
# print(data.shape)