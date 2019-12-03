import jieba
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler,StandardScaler,Imputer
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA

def textvec():
    '''
    从文本中提取特征值,及每个特征值在不同文本中的出现次数
    :return:
    '''
    vector = CountVectorizer()
    res = vector.fit_transform(["life is too short,i like python too","life is too long,i dislike python"])

    # 获取特征值的名称
    print(vector.get_feature_names())
    # 将特征值转换为二维数组方式
    print(res.toarray())
    '''
    ['dislike', 'is', 'life', 'like', 'long', 'python', 'short', 'too']
    [[0 1 1 1 0 1 1 2]
     [1 1 1 0 1 1 0 1]]
    '''
    return None

def cutword():
    '''
    将中文句子进行分词操作
    :return:
    '''
    con1 = jieba.cut("今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。")
    con2 = jieba.cut("我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去。")
    con3 = jieba.cut("如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。")

    # 将分词结果转换成列表
    content1 = list(con1)
    content2 = list(con2)
    content3 = list(con3)

    # 把列表转换成用空格连接的字符串
    c1 = ' '.join(content1)
    c2 = ' '.join(content2)
    c3 = ' '.join(content3)
    c_li = [c1, c2, c3]

    return c_li

def cncvec():
    '''
    对中文内容抽取特征值
    :return:
    '''
    # 抽取中文特征值,及特征值在每个样本中的出现次数
    vector = CountVectorizer()
    data = vector.fit_transform(cutword())

    print(vector.get_feature_names())
    print(data.toarray())
    '''
    ['一种', '不会', '不要', '之前', '了解', '事物', '今天', '光是在', '几百万年', 
    '发出', '取决于', '只用', '后天', '含义', '大部分', '如何', '如果', '宇宙', '我们', 
    '所以', '放弃', '方式', '明天', '星系', '晚上', '某样', '残酷', '每个', '看到', '真正', 
    '秘密', '绝对', '美好', '联系', '过去', '这样']
    [[0 0 1 0 0 0 2 0 0 0 0 0 1 0 1 0 0 0 0 1 1 0 2 0 1 0 2 1 0 0 0 1 1 0 0 0]
     [0 0 0 1 0 0 0 1 1 1 0 0 0 0 0 0 0 1 3 0 0 0 0 1 0 0 0 0 2 0 0 0 0 0 1 1]
     [1 1 0 0 4 3 0 0 0 0 1 1 0 1 0 1 1 0 1 0 0 1 0 0 0 1 0 0 0 2 1 0 0 1 0 0]]
    '''
    return None

def cntfidfvec():
    '''
    抽取特征值,但是不是统计每个样本中特征值出现的次数,
    而是统计某个特征在某个文本中出现的次数,
    和其在所有文本中出现的次数和文本个数的商的log值的乘积,
    即重要性.从而去除出现次数很多但是无关的词,如连接词,感叹词等
    :return:
    '''
    vector = TfidfVectorizer()
    data = vector.fit_transform(cutword())

    print(vector.get_feature_names())
    print(data.toarray())
    '''
    ['一种', '不会', '不要', '之前', '了解', '事物', '今天', '光是在', '几百万年', 
    '发出', '取决于', '只用', '后天', '含义', '大部分', '如何', '如果', '宇宙', '我们', 
    '所以', '放弃', '方式', '明天', '星系', '晚上', '某样', '残酷', '每个', '看到', '真正',
     '秘密', '绝对', '美好', '联系', '过去', '这样']
     
    [[0.         0.         0.21821789 0.         0.         0.
      0.43643578 0.         0.         0.         0.         0.
      0.21821789 0.         0.21821789 0.         0.         0.
      0.         0.21821789 0.21821789 0.         0.43643578 0.
      0.21821789 0.         0.43643578 0.21821789 0.         0.
      0.         0.21821789 0.21821789 0.         0.         0. ]
    ...]
    '''
    return None

def dictvec():
    '''
    从字典中抽取数据
    :return:
    '''
    # 从字典中提取数据,并且输出为二位数组格式
    mydict = DictVectorizer(sparse=False)
    data = mydict.fit_transform([
        {'city': '北京','temperature': 100},
        {'city': '上海','temperature':60},
        {'city': '深圳','temperature': 30}])

    # 获取特征的名字,就是列名
    print(mydict.get_feature_names())
    print(data)
    # 将二位数组重新转换为字典格式
    print(mydict.inverse_transform(data))
    '''
    ['city=上海', 'city=北京', 'city=深圳', 'temperature']
    [[  0.   1.   0. 100.]
     [  1.   0.   0.  60.]
     [  0.   0.   1.  30.]]
    [{'city=北京': 1.0, 'temperature': 100.0}, 
    {'city=上海': 1.0, 'temperature': 60.0}, 
    {'city=深圳': 1.0, 'temperature': 30.0}]
    '''
    return None

def mm():
    '''
    对建立的样本数据进行归一化处理,使其数值在某个固定的区间之内,默认为0到1之间
    :return:
    '''
    mm = MinMaxScaler(feature_range=(1,2))
    data = mm.fit_transform([[90,2,10,40],[60,4,15,45],[75,3,13,46]])

    print(data)
    '''
    [[2.         1.         1.         1.        ]
     [1.         2.         2.         1.83333333]
     [1.5        1.5        1.6        2.        ]]
    '''
    return None

def stand():
    '''
    对样本数据进行标准化处理,
    该处理在正常样本数据充足的情况下
    对极值样本可以起到免疫的作用
    :return:
    '''
    std = StandardScaler()
    data = std.fit_transform([[ 1., -1., 3.],[ 2., 4., 2.],[ 4., 6., -1.]])
    data1 = std.fit_transform([[90, 2, 10, 40], [60, 4, 15, 45], [75, 3, 13, 46]])
    print(data)
    print(data1)
    '''
    [[-1.06904497 -1.35873244  0.98058068]
     [-0.26726124  0.33968311  0.39223227]
     [ 1.33630621  1.01904933 -1.37281295]]
     
    [[ 1.22474487 -1.22474487 -1.29777137 -1.3970014 ]
     [-1.22474487  1.22474487  1.13554995  0.50800051]
     [ 0.          0.          0.16222142  0.88900089]]
    '''
    return None

def im():
    '''
    处理缺失值
    :return:
    '''
    # 定义什么是缺失值,并且定义如何处理缺失值,定义按列处理缺失值
    im = Imputer(missing_values='NaN', strategy='mean', axis=0)
    data = im.fit_transform([[1, 2], [np.nan, 3], [7, 6]])
    print(data)
    '''
    [[1. 2.]
     [4. 3.]
     [7. 6.]]
    '''
    return None

def var():
    '''
    处理特征项,如果某列的方差值小于给定的threshold定义的值,就去掉那一列特征
    :return:
    '''
    var = VarianceThreshold(threshold=0)
    data = var.fit_transform([[0, 2, 0, 3], [0, 1, 4, 3], [0, 1, 1, 3]])
    print(data)
    '''
    [[2 0]
     [1 4]
     [1 1]]
    '''
    return None

def pca():
    '''
    主成分分析进行特征降维
    :return:
    '''
    # 对样本的特征值进行降维处理,并保证数据的准确性,为元数据集的95%
    pca = PCA(n_components=0.95)
    data = pca.fit_transform([[2,8,4,5],[6,3,0,8],[5,4,9,1]])
    print(data)
    '''
    [[ 1.28620952e-15  3.82970843e+00]
     [ 5.74456265e+00 -1.91485422e+00]
     [-5.74456265e+00 -1.91485422e+00]]
    '''
    return None


if __name__ == '__main__':
    # dictvec()
    # cncvec()
    # cntfidfvec()
    # mm()
    # stand()
    # im()
    # var()
    pca()