from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import jieba
import numpy as np

from sklearn.preprocessing import MinMaxScaler,StandardScaler,Imputer
from sklearn.decomposition import PCA
from sklearn.feature_selection import VarianceThreshold


def dictvec():
    d_vec = DictVectorizer(sparse=False)
    test_dic_li = [
        {'city': '北京','temperature':100},
        {'city': '上海','temperature':60},
        {'city': '深圳','temperature': 30}
    ]
    data = d_vec.fit_transform(test_dic_li)
    feature_name = d_vec.get_feature_names()

    print(feature_name)
    print(data)
    '''
    ['city=上海', 'city=北京', 'city=深圳', 'temperature']
    [[  0.   1.   0. 100.]
     [  1.   0.   0.  60.]
     [  0.   0.   1.  30.]]
    '''
    return


def countvec():
    c_vec = CountVectorizer()
    text_data_li = ["人生 苦短，我 喜欢 python 人生", "人生漫长，不用 python 不用"]
    data = c_vec.fit_transform(text_data_li)
    feature_name = c_vec.get_feature_names()

    print(feature_name)
    print(data.toarray())
    '''
    ['python', '不用', '人生', '人生漫长', '喜欢', '苦短']
    [[1 0 2 0 1 1]
     [1 2 0 1 0 0]]
    '''
    return


def get_rawtext(cn_list):
    tmp_li = []
    for sentence in cn_list:
        res = list(jieba.cut(sentence))
        res_str = " ".join(res)
        tmp_li.append(res_str)
    return tmp_li


def tfidfvec(rawtext):
    td_vec = TfidfVectorizer()
    data = td_vec.fit_transform(rawtext)
    feature_name = td_vec.get_feature_names()

    print(feature_name)
    print(data.toarray())
    '''
    ['一种', '不会', '不要', '之前', '了解', '事物', '今天', '光是在', '几百万年', '发出', '取决于', '只用', '后天', '含义', '大部分', '如何', '如果', '宇宙', '我们', '所以', '放弃', '方式', '明天', '星系', '晚上', '某样', '残酷', '每个', '看到', '真正', '秘密', '绝对', '美好', '联系', '过去', '这样']
    [[0.         0.         0.21821789 0.         0.         0.
      0.43643578 0.         0.         0.         0.         0.
      0.21821789 0.         0.21821789 0.         0.         0.
      0.         0.21821789 0.21821789 0.         0.43643578 0.
      0.21821789 0.         0.43643578 0.21821789 0.         0.
      0.         0.21821789 0.21821789 0.         0.         0.        ]
     [0.         0.         0.         0.2410822  0.         0.
      0.         0.2410822  0.2410822  0.2410822  0.         0.
      0.         0.         0.         0.         0.         0.2410822
      0.55004769 0.         0.         0.         0.         0.2410822
      0.         0.         0.         0.         0.48216441 0.
      0.         0.         0.         0.         0.2410822  0.2410822 ]
     [0.15698297 0.15698297 0.         0.         0.62793188 0.47094891
      0.         0.         0.         0.         0.15698297 0.15698297
      0.         0.15698297 0.         0.15698297 0.15698297 0.
      0.1193896  0.         0.         0.15698297 0.         0.
      0.         0.15698297 0.         0.         0.         0.31396594
      0.15698297 0.         0.         0.15698297 0.         0.        ]]
    '''
    return

def my_imp(data):
    myimp = Imputer(missing_values="NaN",strategy="mean",axis=0)
    res = myimp.fit_transform(data)
    print(res)
    '''
    [[ 3. -1.  3.]
     [ 2.  4.  2.]
     [ 4.  6. -1.]]
    '''
    return

def my_std(data):
    mystd = StandardScaler()
    res = mystd.fit_transform(data)
    print(res)
    '''
    [[-1.06904497 -1.35873244  0.98058068]
     [-0.26726124  0.33968311  0.39223227]
     [ 1.33630621  1.01904933 -1.37281295]]
    '''
    return

def myvarians(data):
    '''
    方差小于指定数值的特征列将会被删除
    :param data:
    :return:
    '''
    myv = VarianceThreshold(threshold=1)
    res = myv.fit_transform(data)
    print(res)
    '''
    [[ 1. -1.  3.]
     [ 2.  4.  2.]
     [ 4.  6. -1.]]
    '''
    return

def mypcas(data):
    '''
    减少特征值的维度,并且还改变特征的值,但是可以保证信息损失可控
    :param data:
    :return:
    '''
    mypca = PCA(n_components=0.9)
    res= mypca.fit_transform(data)
    print(res)
    '''
    [[-1.20031604  4.68892333]
     [-2.07446332 -0.15072132]
     [-2.48409503 -3.81542837]
     [ 5.75887438 -0.72277364]]
    '''
    return


if __name__ == '__main__':
    # dictvec()
    # countvec()
    # cn_list = ["今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。",]
    # cn_list.append("我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去。")
    # cn_list.append("如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。")
    # rawtext = get_rawtext(cn_list)
    # tfidfvec(rawtext)
    data = [[ 1., -1., 3.,1.],
            [ 2., 4., 2.,1.],
            [ 4., 6., -1.,1.],
            [ -4., 3., -3., 2.]]

    data1 = [[ np.nan, -1., 3.],
            [ 2., 4., 2.],
            [ 4., 6., -1.]]

    # my_imp(data1)
    #
    # my_std(data)
    # myvarians(data)
    mypcas(data)