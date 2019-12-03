import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, classification_report
from sklearn.externals import joblib


def logistisize():
    '''
    利用逻辑回归算法，实现二分类预测
    本函数利用逻辑回归做二分类进行癌症预测（根据细胞的属性特征）
    :return:
    '''
    # 因为样本数据没有特征名称，即每一列的名称，需要手动构造
    column = ['Sample code number','Clump Thickness',
              'Uniformity of Cell Size',
              'Uniformity of Cell Shape',
              'Marginal Adhesion',
              'Single Epithelial Cell Size',
              'Bare Nuclei','Bland Chromatin',
              'Normal Nucleoli','Mitoses','Class']

    # 读取样本数据
    data = pd.read_csv("data_source/breast-cancer-wisconsin.data",names=column)
    # print(data.head(3))
    '''
           Sample code number  Clump Thickness  ...  Mitoses  Class
    0             1000025                5  ...        1      2
    1             1002945                5  ...        1      2
    2             1015425                3  ...        1      2
    '''

    # 处理缺失值,删除有缺失值的样本
    data.replace(to_replace="?",value=np.nan,inplace=True)
    data.dropna(inplace=True)
    # print(data.info())

    # 分割训练集和测试集
    feat_train, feat_test, targ_train, targ_test = train_test_split(data[column[1:10]],data[column[10]],test_size=0.25)

    # 标准化样本数据
    std = StandardScaler()
    feat_train = std.fit_transform(feat_train)
    feat_test = std.transform(feat_test)

    # 生成模型对象，训练，并进行预测
    lg = LogisticRegression(C=1.0)
    lg.fit(feat_train,targ_train)
    targ_predict = lg.predict(feat_test)

    print("最佳权重参数：",lg.coef_)
    print("预测结果：",targ_predict)
    print("准确率：", lg.score(feat_test,targ_test))
    print("召回率：\n", classification_report(targ_test, targ_predict, labels=[2, 4], target_names=["良性", "恶性"]))
    '''
    最佳权重参数： [[ 1.44410608 -0.05644181  0.69862061  0.85237849  0.12443182  1.23704464
       1.34878466  0.73762794  0.85721309]]
    预测结果： [2 2 2 2 2 4 2 2 4 2 2 4 2 4 4 4 4 2 2 4 2 2 2 4 2 4 2 2 2 2 2 2 4 2 2 2 2
     4 4 2 2 4 4 4 4 4 2 2 4 2 2 2 2 4 4 2 2 2 2 2 2 2 4 2 4 2 2 2 2 2 2 2 4 2
     2 2 2 4 2 4 2 2 2 4 2 4 4 2 2 4 4 2 2 2 2 2 2 4 4 4 4 2 2 4 2 4 2 2 2 2 2
     4 2 2 2 2 4 2 4 2 2 2 2 4 2 4 2 2 2 2 4 2 4 4 2 4 2 4 2 4 2 2 2 2 4 4 4 2
     4 4 2 2 4 2 2 4 4 4 4 4 2 2 2 2 2 2 2 2 4 2 2]
    准确率： 0.9766081871345029
    召回率：
           precision    recall  f1-score   support
    良性       0.98      0.98      0.98       111
    恶性       0.97      0.97      0.97        60
    
       micro avg       0.98      0.98      0.98       171
       macro avg       0.97      0.97      0.97       171
    weighted avg       0.98      0.98      0.98       171
    '''

    # 保存训练好的模型
    # joblib.dump(lg, "model_results/test.pkl")

    # 利用保存的训练好的模型预测结果
    # model = joblib.load("model_results/test.pkl")
    # targ_predict = model.predict(feat_test))

    return None


if __name__ == '__main__':
    logistisize()