# 获取自带数据集
from sklearn.datasets import load_iris,load_boston,fetch_20newsgroups

# 特征工程
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import StandardScaler

# 分割数据集
from sklearn.model_selection import train_test_split

# 网格搜索，获取较优超参数
from sklearn.model_selection import GridSearchCV

# 机器学习算法
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression,Ridge,LogisticRegression

# 评估预测结果
from sklearn.metrics import classification_report,mean_squared_error

# 保存训练好的模型
from sklearn.externals import joblib

import pandas as pd
import numpy as np


class SimpleMachineLearning(object):

    def __init__(self,data=None,data_path=None,function=None):
        self.data = data
        self.data_path = data_path
        self.func = self.get_function(function)

    def get_function(self,function):
        if hasattr(self,function):
            func = getattr(self,function)
            return func
        raise Exception("no such function")

    def run_function(self):
        res = self.func()
        return res

    def knncls(self):
        df = pd.read_csv(self.data_path)
        df.query("x > 1.0 &  x < 1.25 & y > 2.5 & y < 2.75")

        time_value = pd.to_datetime(df['time'], unit="s")
        time_obj = pd.DatetimeIndex(time_value)
        df['day'] = time_obj.day
        df['hour'] = time_obj.hour
        df['weekday'] = time_obj.weekday
        df = df.drop(["time",],axis=1)

        places_count = df.groupby(by="place_id").count()
        selected_places = places_count.loc[places_count["row_id"]>2].reset_index()
        df = df.loc[df["place_id"].isin(selected_places["place_id"])]

        targ = df['place_id']
        feat = df.drop(['place_id'], axis=1)

        x_train, x_test, y_train, y_test = train_test_split(feat, targ, test_size=0.2)

        std_obj = StandardScaler()
        x_train = std_obj.fit_transform(x_train)
        x_test = std_obj.transform(x_test)

        knn = KNeighborsClassifier()
        param = {"n_neighbors": [2, 5, 10]}

        gs_obj = GridSearchCV(knn,param,cv=5)
        gs_obj.fit(x_train,y_train)

        accuracy = gs_obj.score(x_test, y_test)
        best_score = gs_obj.best_score_
        best_estimator = gs_obj.best_estimator_
        cv_res = gs_obj.cv_results_

        res = {"accuracy":accuracy,"best_score":best_score,"best_estimator":best_estimator,"cv_res":cv_res,"type":"classifier"}
        return res

    def naviebayes(self):
        news = fetch_20newsgroups(subset='all')

        # tf = TfidfVectorizer()
        # data = tf.fit_transform(news.data).toarray()
        # print(type(list(data)))
        # print(len(data),len(data[0]))
        # print(len(news.data),len(news.data[0]))
        # x_train, x_test, y_train, y_test = train_test_split(list(data), news.target, test_size=0.2)

        x_train, x_test, y_train, y_test = train_test_split(news.data, news.target, test_size=0.2)
        # print("news_type: ",type(x_train),type(y_train))

        tf = TfidfVectorizer()
        x_train = tf.fit_transform(x_train)
        x_test = tf.transform(x_test)

        mlt = MultinomialNB(alpha=1.0)
        mlt.fit(x_train, y_train)
        y_predict = mlt.predict(x_test)

        accuracy = mlt.score(x_test,y_test)
        c_rep = classification_report(y_test,y_predict,target_names=news.target_names)

        res = {"accuracy":accuracy,"c_rep":c_rep,"type":"classifier"}

        return res

    def d_tree(self):
        df = pd.read_csv("data_source/titanic.txt")
        # 删除没有在哪里登船的样本
        df.drop(labels=df[df["embarked"].isna()].index,axis=0,inplace=True)
        # 将年龄为空的样本，设置为平均年龄
        df["age"].fillna(df["age"].mean(),inplace=True)
        # 获取特征值和目标值
        feat = df[['pclass', 'age', 'sex','embarked']]
        targ = df['survived']
        # 分割测试集和训练集
        x_train,x_test,y_train,y_test = train_test_split(feat,targ,test_size=0.2)
        # 将特征值变成onehot编码
        dict_vec = DictVectorizer(sparse=False)
        x_train = dict_vec.fit_transform(x_train.to_dict(orient="records"))
        x_test = dict_vec.transform(x_test.to_dict(orient="records"))
        # 使用决策树进行预测
        d_tree_obj = DecisionTreeClassifier(max_depth=10)
        d_tree_obj.fit(x_train,y_train)

        y_predict = d_tree_obj.predict(x_test)
        accuracy = d_tree_obj.score(x_test,y_test)
        c_rep = classification_report(y_test,y_predict,target_names=["死翘翘","活下来"])

        res = {"accuracy":accuracy,"c_rep":c_rep,"type":"classifier"}
        return res

    def rf_pre(self):
        df = pd.read_csv("data_source/titanic.txt")
        # 删除没有在哪里登船的样本
        df.drop(labels=df[df["embarked"].isna()].index,axis=0,inplace=True)
        # 将年龄为空的样本，设置为平均年龄
        df["age"].fillna(df["age"].mean(),inplace=True)
        # 获取特征值和目标值
        feat = df[['pclass', 'age', 'sex','embarked']]
        targ = df['survived']
        # 分割测试集和训练集
        x_train,x_test,y_train,y_test = train_test_split(feat,targ,test_size=0.2)
        # 将特征值变成onehot编码
        dict_vec = DictVectorizer(sparse=False)
        x_train = dict_vec.fit_transform(x_train.to_dict(orient="records"))
        x_test = dict_vec.transform(x_test.to_dict(orient="records"))

        rf_obj = RandomForestClassifier(n_jobs=-1)
        params = {"n_estimators": [120, 200, 300, 500, 800, 1200], "max_depth": [5, 8, 15, 25, 30]}

        gs = GridSearchCV(estimator=rf_obj,param_grid=params,cv=5)
        gs.fit(x_train,y_train)

        y_predict = gs.predict(x_test)
        accuracy = gs.score(x_test,y_test)
        c_rep = classification_report(y_test,y_predict,target_names=["死翘翘","活下来"])

        # print("最好超参数：",gs.best_params_)
        # print("最好得分：",gs.best_score_)
        '''
        最好超参数： {'max_depth': 5, 'n_estimators': 800}
        最好得分： 0.8185975609756098
        '''
        res = {"accuracy":accuracy,"c_rep":c_rep,"type":"classifier"}
        return res

    def my_linear(self):
        hp = load_boston()
        x_train,x_test,y_train,y_test = train_test_split(hp.data,hp.target,test_size=0.2)
        # print(y_test)

        x_std = StandardScaler()
        y_std = StandardScaler()

        x_train = x_std.fit_transform(x_train)
        x_test = x_std.transform(x_test)

        y_train = y_std.fit_transform(y_train.reshape(-1,1))
        y_test = y_std.transform(y_test.reshape(-1,1))

        lr_obj = LinearRegression()
        lr_obj.fit(x_train,y_train)
        lr_pre = y_std.inverse_transform(lr_obj.predict(x_test))

        msr = mean_squared_error(y_std.inverse_transform(y_test),lr_pre)
        mycoef = lr_obj.coef_

        res = {"pre":lr_pre,"msr":msr,"mycoef":mycoef,"type":"Regression"}
        '''
        27.601277917691508
        ****************************************************************************************************
        [[-0.10995107  0.11950577  0.00806897  0.08103766 -0.18413522  0.3481043
          -0.05114878 -0.34999744  0.26324756 -0.23371828 -0.21594368  0.08605247
          -0.34542951]]
        '''
        return res

    def my_ridge(self):
        hp = load_boston()
        x_train,x_test,y_train,y_test = train_test_split(hp.data,hp.target,test_size=0.2)
        # print(y_test)

        x_std = StandardScaler()
        y_std = StandardScaler()

        x_train = x_std.fit_transform(x_train)
        x_test = x_std.transform(x_test)

        y_train = y_std.fit_transform(y_train.reshape(-1,1))
        y_test = y_std.transform(y_test.reshape(-1,1))

        rd_obj = Ridge()
        rd_obj.fit(x_train,y_train)
        rd_pre = y_std.inverse_transform(rd_obj.predict(x_test))

        msr = mean_squared_error(y_std.inverse_transform(y_test),rd_pre)
        mycoef = rd_obj.coef_

        res = {"pre":rd_pre,"msr":msr,"mycoef":mycoef,"type":"Regression"}
        '''
        23.374692941047943
        ****************************************************************************************************
        [[-0.12411777  0.08261566 -0.00672291  0.10267077 -0.19931229  0.34224458
          -0.03708516 -0.30653053  0.26792711 -0.19554446 -0.21336845  0.07825969
          -0.34234288]]
        '''
        return res

    def my_logistic(self):
        bc = pd.read_csv(
            "data_source/breast-cancer-wisconsin.data",
            names=[
                'Sample code number','Clump Thickness','Uniformity of Cell Size',
                'Uniformity of Cell Shape','Marginal Adhesion',
                'Single Epithelial Cell Size','Bare Nuclei','Bland Chromatin',
                'Normal Nucleoli','Mitoses','Class'
            ])
        # print(bc)
        bc.replace(to_replace="?",value=np.nan,inplace=True)
        bc.dropna(inplace=True)

        target = pd.Series(bc.iloc[:,10])
        x_train,x_test,y_train,y_test = train_test_split(bc.iloc[:,1:10],target,test_size=0.2)
        # print(x_test)
        # print(y_test)

        st_obj = StandardScaler()
        x_train = st_obj.fit_transform(x_train)
        x_test = st_obj.transform(x_test)

        # lr_obj = LogisticRegression(C=1.0)
        # lr_obj.fit(x_train,y_train)

        # joblib.dump(lr_obj,"model_results/lrobj.pkl")
        # 读取训练好的模型进行预测，不需要每次预测前都进行训练了
        lr_obj = joblib.load('model_results/lrobj.pkl')

        lr_pre = lr_obj.predict(x_test)
        accuracy = lr_obj.score(x_test,y_test)
        bset_weights = lr_obj.coef_
        c_rep = classification_report(y_test,lr_pre,labels=[2,4],target_names=["良性", "恶性"])

        res = {"accuracy":accuracy,"c_rep":c_rep,"bset_weights":bset_weights,"type":"classifier"}
        '''
        0.9927007299270073
        ****************************************************************************************************
                      precision    recall  f1-score   support
        
                  良性       1.00      0.99      0.99        93
                  恶性       0.98      1.00      0.99        44
        
           micro avg       0.99      0.99      0.99       137
           macro avg       0.99      0.99      0.99       137
        weighted avg       0.99      0.99      0.99       137
        '''
        return res


if __name__ == '__main__':
    sml_obj = SimpleMachineLearning(function="my_logistic")
    res = sml_obj.run_function()

    if res.get("type") == "classifier":
        print(res.get("accuracy"))
        print("*"*100)
        print(res.get("c_rep"))
    elif res.get("type") == "Regression":
        print(res.get("msr"))
        print("*"*100)
        print(res.get("mycoef"))
        print("*"*100)
        print(res.get("pre"))