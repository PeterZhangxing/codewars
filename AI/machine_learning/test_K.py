from sklearn.datasets import load_iris,fetch_20newsgroups,load_boston
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
import pandas as pd


def knncls():
    '''
    使用K-近邻算法，预测用户的签到位置
    :return:
    '''
    # 从文件中读取数据
    data = pd.read_csv("data_source/train.csv")
    # print(data.head(3))

    # 设定根据样本的x和y特征取值范围，减少样本数据量，值留下符合要求的样本
    data = data.query("x > 1.0 &  x < 1.25 & y > 2.5 & y < 2.75")

    # 将样本中的时间字符串转化为时间对象
    time_value = pd.to_datetime(data['time'],unit="s")
    # print(time_value)
    # 将时间对象转化为结构化时间，从而可以取得时间的不同部分
    time_value = pd.DatetimeIndex(time_value)
    # print(time_value)

    # 为样本数据添加新的特征
    data['day'] = time_value.day
    data['hour'] = time_value.hour
    data['weekday'] = time_value.weekday

    # 删除原来的时间戳特征
    data = data.drop(['time'],axis=1)
    # print(data)

    # 把签到数量少于n的目标位置的样本删除
    place_count = data.groupby(by='place_id').count()
    tf = place_count[place_count.row_id>3].reset_index()
    data = data[data['place_id'].isin(tf.place_id)]

    # 取出特征值和目标值
    targ = data['place_id']
    feat = data.drop(['place_id'],axis=1)

    # 分割测试集和训练集,指明测试集的大小
    feat_train,feat_test,targ_train,targ_test = train_test_split(feat,targ,test_size=0.25)

    # 特征工程，标准化特征集
    std = StandardScaler()
    feat_train = std.fit_transform(feat_train)
    feat_test = std.transform(feat_test)

    # # 实例化K-邻居算法
    # knn = KNeighborsClassifier(n_neighbors=3)
    #
    # # 根据训练数据，计算出最邻近的3个样本，后面根据他们来对测试集进行预测
    # knn.fit(feat_train, targ_train)
    #
    # # 得出预测结果
    # feat_predict = knn.predict(feat_test)
    # print("预测的目标签到位置为：", feat_predict)
    #
    # # 得出准确率
    # print("预测的准确率:", knn.score(feat_test, targ_test))

    knn = KNeighborsClassifier()
    param = {"n_neighbors":[2,5,10]}
    # 生成网格搜索对象，指定要进行网格搜索的算法，参数集，和训练集折叠次数
    gc = GridSearchCV(knn,param_grid=param,cv=10)
    # 在训练集上进行网格搜索算法，确定最佳参数
    gc.fit(feat_train,targ_train)

    # 预测准确率
    print("在测试集上准确率：", gc.score(feat_test, targ_test))
    print("在交叉验证当中最好的结果：", gc.best_score_)
    print("选择最好的模型是：", gc.best_estimator_) # 此结果中有选择哪个参数获得的准确率最高
    print("每个超参数每次交叉验证的结果：", gc.cv_results_)

    return None


def naviebayes():
    '''
    利用朴素贝叶斯算法完成文章的分类
    :return:
    '''
    news = fetch_20newsgroups(subset='all')
    print("*"*20)

    # 将样本数据分为训练集和测试集
    feat_train,feat_test,targ_train,targ_test = train_test_split(news.data,news.target,test_size=0.25)

    # 对数据进行特征抽取
    tf = TfidfVectorizer()
    # 以训练集当中的词的列表进行每篇文章重要性统计
    feat_train = tf.fit_transform(feat_train)
    feat_test = tf.transform(feat_test)

    # print(tf.get_feature_names())
    # print(feat_test.toarray())

    # 进行朴素贝叶斯算法的预测
    mlt = MultinomialNB(alpha=1.0)
    # 用训练集建立预测模型
    mlt.fit(feat_train,targ_train)
    # 用建立的模型，预测测试集中文章的分类
    targ_predict = mlt.predict(feat_test)

    print("预测的文章类别为：", targ_predict)
    print("准确率为：", mlt.score(feat_test, targ_test))
    print("每个类别的精确率和召回率：\n", classification_report(targ_test, targ_predict, target_names=news.target_names))

    return None


if __name__ == '__main__':
    naviebayes()