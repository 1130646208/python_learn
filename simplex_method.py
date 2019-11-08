
# -*- coding: utf-8 -*-
# @Time(v1): 2019/10/2 13:09 完成初版，单纯形法。
# @Time(v2): 2019/11/6 21:49 增加了自动换基功能。
# @Author  : 王双星
# @Site    : 北京科技大学
# @File    : simplex_method.py
# @Software: PyCharm

from fractions import Fraction
#######################以下是变量声明##########################

# 输入行数和列数
rows = int(input('请输入基变量个数:'))
cols = int(input('请输入变量个数:'))+1

# 定义系数矩阵
matrix = [[0] * cols for i in range(rows)]
y0j = [0 for i in range(cols)]

# 存放基变量所在列
base_vec_index = [0 for i in range(rows)]
# 存放基变量对应系数
temp = [0 for i in range(rows)]


#######################以下是函数声明############################

def get_index():
    """base_vec_index[i]=x 表示原矩阵第i+1行的基变量是Xa"""
    global base_vec_index
    for i in range(0, rows):
        a = int(input('输入第{}行基变量是X几'.format(i + 1))) - 1
        base_vec_index[i] = a


def input_():
    """
    输入系数矩阵和检验数行。
    如果有4个变量，X1~X4，那么a15代表y10；
    y05代表y00，依次类推。
    """
    global matrix
    get_index()
    for i in range(0, rows):
        for j in range(0, cols):
            matrix[i][j] = input('a{}{}='.format(i + 1, j + 1))

    for j in range(0, cols):
        y0j[j] = input('y0{}='.format(j + 1))
    matrix.append(y0j)


def to_fraction():
    """
    将输入矩阵转化为分数Fraction（）格式。
    1/2=Fraction（1，2）
    """
    global matrix
    for j in range(0, cols):
        for i in range(0, rows + 1):
            matrix[i][j] = Fraction(matrix[i][j])


def process(base_vec_index):
    """
    找出基变量所在列的系数存放到temp[i]
    """
    global temp
    global matrix
    for i in range(rows):
        temp[i] = matrix[i][base_vec_index[i]]


def to_one(row):
    """
    将某行除以此行的基变量的系数，即归一化基变量系数。
    """
    global temp
    global matrix
    global base_vec_index
    process(base_vec_index)
    for i in range(cols):
        matrix[row][i] = Fraction(matrix[row][i], temp[row])


def minus_to_zero(row1, row2):
    """
    两行相减，row1=row1-row2
    第一行减去第二行并赋值给第一行。
    """
    global matrix
    factor = matrix[row1][base_vec_index[row2]]
    for i in range(cols):
        matrix[row1][i] = matrix[row1][i] - matrix[row2][i] * factor


def get_result():
    """
    基变量所在列只有一个1，即是将单纯形表化成典式。
    """
    for i in range(rows):
        to_one(i)
        for j in range(rows + 1):
            if i != j:
                minus_to_zero(j, i)


def out_():
    """
    输出矩阵，以分数的形式输出。
    输出格式控制，尽量输出成为一个易读的表格。
    """
    for i in range(0, cols):
        if i == cols - 1:
            print('|XB')
        else:
            print('X{}\t'.format(i + 1), end='')
    for i in range(0, rows):
        for j in range(0, cols):
            if j == cols - 2:
                print('{}\t'.format(matrix[i][j]), end='|')
            else:
                print('{}\t'.format(matrix[i][j]), end='')
        print()
    print('检验数行：')
    for j in range(0, cols):
        if j == cols - 2:
             print('{}\t'.format(matrix[rows][j]), end='|')
        else:
             print('{}\t'.format(matrix[rows][j]), end='')
    print()


def change_base():
    """
    确定离基变量，并完成换基
    """
    global base_vec_index
    yi0_div_yiq=[-1 for i in range(rows)]
    if check_best() == -1:
        pass
    else:
        vec_to_in = check_best()
        print('进基变量：X{}'.format(vec_to_in+1))
        for i in range(0,rows):
            if matrix[i][vec_to_in]>0:
                yi0_div_yiq[i]=matrix[i][cols-1]/matrix[i][vec_to_in]
        print('离基变量：X{}'.format(base_vec_index[yi0_div_yiq.index(my_min(yi0_div_yiq))]+1))
            #换基
        base_vec_index[yi0_div_yiq.index(my_min(yi0_div_yiq))]=vec_to_in


def check_best():
    """
    此函数检验是否最优表并确定进基变量(Bland规则)。
    检验是否最优表,最优表返回-1，非最优表返回检验数下标，即确定离基变量。
    """
    global matrix
    for temp_y0j in matrix[rows]:
        if temp_y0j < 0 and matrix[rows].index(temp_y0j) !=cols - 1:
            #print('进基变量:X{}'.format(matrix[rows].index(temp_y0j)+1))
            return matrix[rows].index(temp_y0j)
            break
        else:
            pass
    return -1


def my_min(liss):
    """
    求一个LIST的非零最小值，用来确定离基变量。
    """
    min_val=-1
    flag=0
    for lis in liss:
        if 0 < lis and flag == 0:
            min_val = lis
            flag=1
        if 0 < lis < min_val and flag==1:
            min_val = lis
    return min_val

######################以下是处理部分##########################

input_()
to_fraction()
print('典式：')
get_result()
out_()
iter_times=0
while check_best() != -1 and iter_times<100:
    iter_times +=1
    print('*************************************************')
    print('第{}次换基。'.format(iter_times))
    change_base()
    for i in range(rows):
        print('当前基变量：', end='')
        print (' X{} '.format(base_vec_index[i]+1), end='')
    print()
    get_result()
    out_()
print('换基完成。')