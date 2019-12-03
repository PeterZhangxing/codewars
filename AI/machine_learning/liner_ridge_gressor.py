from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression,SGDRegressor,Ridge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error


def mylinear():
    '''
    使用线性回归和岭回归预测房价
    :return:
    '''
    # 获取数据
    lb = load_boston()

    # 分割训练集和测试集
    feat_train,feat_test,targ_train,targ_test = train_test_split(lb.data,lb.target,test_size=0.25)

    # 分别对特征值和目标值进行标准化
    std_train = StandardScaler()
    feat_train = std_train.fit_transform(feat_train)
    feat_test = std_train.transform(feat_test)

    std_targ = StandardScaler()
    targ_train = std_targ.fit_transform(targ_train.reshape(-1, 1))
    targ_test = std_targ.transform(targ_test.reshape(-1, 1))

    # 正规方程求解方式预测结果(波士顿房价)
    lr = LinearRegression()
    lr.fit(feat_train,targ_train)
    # 获取最优权重值
    print("正规方程最优权重值",lr.coef_)
    # 预测测试集的房子价格
    targ_lr_predict = std_targ.inverse_transform(lr.predict(feat_test))
    print("正规方程测试集里面每个房子的预测价格：", targ_lr_predict)
    print("正规方程的均方误差：", mean_squared_error(std_targ.inverse_transform(targ_test), targ_lr_predict))

    # 梯度下降方式预测结果(波士顿房价)
    sgd = SGDRegressor()
    sgd.fit(feat_train,targ_train)
    # 获取最优权重值
    print("梯度下降最优权重值",sgd.coef_)
    targ_sgd_predict = std_targ.inverse_transform(sgd.predict(feat_test))
    print("梯度下降测试集里面每个房子的预测价格：", targ_sgd_predict)
    print("梯度下降的均方误差：", mean_squared_error(std_targ.inverse_transform(targ_test), targ_sgd_predict))

    # 岭回归方式预测结果(波士顿房价)
    rd = Ridge()
    rd.fit(feat_train,targ_train)
    # 获取最优权重值
    print("岭回归最优权重值",rd.coef_)
    targ_rd_predict = std_targ.inverse_transform(rd.predict(feat_test))
    print("岭回归测试集里面每个房子的预测价格：", targ_rd_predict)
    print("岭回归的均方误差：", mean_squared_error(std_targ.inverse_transform(targ_test), targ_rd_predict))

    return None


if __name__ == '__main__':
    mylinear()
    '''
    正规方程的均方误差： 15.436923356401147
    梯度下降的均方误差： 16.462147250909908
    岭回归的均方误差： 15.45119428749679
    '''