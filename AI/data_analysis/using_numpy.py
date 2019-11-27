import numpy as np


def repalce_nan(t1):
    '''
    去掉一个二维数组中的所有nan，用这一列的平均值替换nan
    :param t1:
    :return:
    '''
    for i in range(t1.shape[1]):
        tmp_col = t1[:,i] # 获取每一列数据
        # 计算当前列中包含的nan个数
        nan_num = np.count_nonzero(tmp_col!=tmp_col)
        # 如果有nan存在当前列中，用该列中的非nan值的平均值代替该列中的所有nan
        if nan_num:
            # 获取该列中的非nan值
            tmp_nnan_col = tmp_col[tmp_col==tmp_col]
            # 用该列中的非nan值的平均值代替该列中的所有nan
            tmp_col[np.isnan(tmp_col)] = tmp_nnan_col.mean()
    return t1


if __name__ == '__main__':
    t1 = np.arange(12).reshape(3, 4).astype("float")
    t1[1, 2:] = np.nan
    t1 = repalce_nan(t1)
    # print(t1)