from sklearn.datasets import load_iris,fetch_20newsgroups,load_boston
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier,export_graphviz
from sklearn.ensemble import RandomForestClassifier
import pandas as pd


def dectree():
    '''
    决策树和随机森林
    :return:
    '''
    titan = pd.read_csv("data_source/titanic.txt")
    # print(titan.info())
    titan.drop(labels=titan[titan["embarked"].isna()].index,axis=0,inplace=True)
    # print(titan.info())

    # 从所有特征中抽取自己人为重要的特征值
    feat = titan.loc[:,['pclass', 'age', 'sex','embarked']]
    # print(feat)
    '''
         pclass      age     sex
    0       1st  29.0000  female
    1       1st   2.0000  female
    2       1st  30.0000    male
    '''
    # 获取目标值,必须是series类型，dataframe会报错
    targ = titan.loc[:,['survived']]
    # targ = targ.values
    targ = pd.Series(targ['survived'].values)
    # targ = titan['survived']
    # print(type(targ))
    '''
              survived
    0            1
    1            0
    2            0
    '''
    # 处理空数据
    feat.loc[:,"age"].fillna(feat.loc[:,"age"].mean(),inplace=True)

    # 分割训练集和测试集
    feat_train,feat_test,targ_train,targ_test = train_test_split(feat,targ,test_size=0.25)
    # 进行处理（特征工程）特征-》类别-》one_hot编码
    # 就是先将带有字符串特征的样本转化为字典，然后利用字典特征值标准化，
    # 把所有类别提取出来，变成数字值
    mydict = DictVectorizer(sparse=False)
    feat_train = mydict.fit_transform(feat_train.to_dict(orient="records"))
    feat_test = mydict.transform(feat_test.to_dict(orient="records"))
    # print(mydict.get_feature_names())
    # print(feat_train)
    '''
    ['age', 'embarked=Cherbourg', 'embarked=Queenstown', 'embarked=Southampton',
     'pclass=1st', 'pclass=2nd', 'pclass=3rd', 'sex=female', 'sex=male']
     
    [[31.0349547  0.         0.        ...  0.         0.         1.       ]
     [46.         1.         0.        ...  0.         0.         1.       ]
     [22.         0.         0.        ...  0.         0.         1.       ]
    '''

    # 实例化决策树对象，训练对象，并测试预测的准确率
    # dec = DecisionTreeClassifier()
    # dec.fit(feat_train,targ_train)
    # test_res = dec.score(feat_test,targ_test)
    # print('准确率：',test_res)
    '''
    准确率： 0.8058252427184466
    '''

    # # 导出决策树的结构,转换命令：dot -Tpng tree.dot -o output.png
    # export_graphviz(dec, out_file="./tree.dot", feature_names=['年龄', 'pclass=1st', 'pclass=2nd', 'pclass=3rd', '女性', '男性'])

    # 使用随机森林和网格搜索，进行预测并查找最佳超参数
    rf = RandomForestClassifier(n_jobs=-1)
    # n_estimators 表示建立多少棵树的森林，max_depth 表示每棵树的最大深度
    param = {"n_estimators": [120, 200, 300, 500, 800, 1200], "max_depth": [5, 8, 15, 25, 30]}

    # 网格搜索与交叉验证
    gc = GridSearchCV(rf, param_grid=param, cv=5)
    gc.fit(feat_train, targ_train)

    print("准确率：", gc.score(feat_test, targ_test))
    print("查看选择的参数模型：", gc.best_params_)
    '''
    准确率： 0.8349514563106796
    查看选择的参数模型： {'max_depth': 5, 'n_estimators': 200}  
    '''
    return None


def decision():
    """
    决策树对泰坦尼克号进行预测生死
    :return: None
    """
    # 获取数据
    titan = pd.read_csv("data_source/titanic.txt")

    # 处理数据，找出特征值和目标值
    x = titan[['pclass', 'age', 'sex']]

    y = titan['survived']

    # print(x)
    # 缺失值处理
    x['age'].fillna(x['age'].mean(), inplace=True)

    # 分割数据集到训练集合测试集
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

    # 进行处理（特征工程）特征-》类别-》one_hot编码
    dict = DictVectorizer(sparse=False)

    x_train = dict.fit_transform(x_train.to_dict(orient="records"))

    # print(dict.get_feature_names())

    x_test = dict.transform(x_test.to_dict(orient="records"))

    # print(x_train)
    # 用决策树进行预测
    # dec = DecisionTreeClassifier()
    #
    # dec.fit(x_train, y_train)
    #
    # # 预测准确率
    # print("预测的准确率：", dec.score(x_test, y_test))
    #
    # # 导出决策树的结构
    # export_graphviz(dec, out_file="./tree.dot", feature_names=['年龄', 'pclass=1st', 'pclass=2nd', 'pclass=3rd', '女性', '男性'])

    # 随机森林进行预测 （超参数调优）
    rf = RandomForestClassifier(n_jobs=-1)

    param = {"n_estimators": [120, 200, 300, 500, 800, 1200], "max_depth": [5, 8, 15, 25, 30]}

    # 网格搜索与交叉验证
    gc = GridSearchCV(rf, param_grid=param, cv=5)

    gc.fit(x_train, y_train)

    print("准确率：", gc.score(x_test, y_test))

    print("查看选择的参数模型：", gc.best_params_)

    return None


if __name__ == '__main__':
    dectree()
    '''
    准确率： 0.8786407766990292
    查看选择的参数模型： {'max_depth': 5, 'n_estimators': 120}
    '''

    # decision()
    '''
    准确率： 0.8358662613981763
    查看选择的参数模型： {'max_depth': 5, 'n_estimators': 300}
    '''