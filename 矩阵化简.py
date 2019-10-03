from fractions import Fraction

#输入行数和列数
rows=int(input('请输入基变量个数:'))
clos=int(input('请输入单纯形表有效区列数:'))

#定义系数矩阵
matrix=[[0]*clos for i in range(rows)]
y0j=[0 for i in range(clos)]
#存放基变量所在列
base_vec_index=[0 for i in range(rows)]
#存放基变量对应系数
temp=[0 for i in range(rows)]
################################################

def get_index():
    'base_vec_index[i]=x 表示原矩阵第i+1行的基变量是Xa'
    global base_vec_index
    for i in range(0,rows):
        a=int(input('输入第{}行基变量是X几'.format(i+1)))-1
        base_vec_index[i]=a
    #print('base_vec_index:',base_vec_index)


def input_():
    '输入系数矩阵'
    global matrix
    get_index()
    for j in range(0,clos):
        y0j[j]=input('y0{}='.format(j+1))
        
    for j in range(0,clos):
        for  i in range(0,rows):
            matrix[i][j]=input('a{}{}='.format(i+1,j+1))
    matrix.append(y0j)
    
        
def to_fraction():
    global matrix
    for j in range(0,clos):
        for  i in range(0,rows+1):
            matrix[i][j]=Fraction(matrix[i][j])
            
def process(base_vec_index):
    '找出基变量所在列的系数'
    global temp
    global matrix
    for i in range(rows):
        temp[i]=matrix[i][base_vec_index[i]]
    #print('process_temp',temp)



def to_one(row):
    '将某行除以此行的基变量的系数'
    global temp
    global matrix
    global base_vec_index
    process(base_vec_index)
    for i in range(clos):
        matrix[row][i]=Fraction(matrix[row][i],temp[row])
        
        

def minus_to_zero(row1,row2):
    'row1=row1-row2:两行相减,'
    global matrix
    factor=matrix[row1][base_vec_index[row2]]
    for i in range(clos):
        matrix[row1][i]=matrix[row1][i]-matrix[row2][i]*factor
        

def get_result():
    '得到结果：基变量所在列只有一个1'
    for i in range(rows):
        to_one(i)
        for j in range(rows+1):
            if i!=j:
                minus_to_zero(j,i)
def out_():
    '输出矩阵，以分数的形式输出'
    for i in range(0,clos):
        if i==clos-1:
            print()
        else:
            print(' X{} '.format(i+1),end='')
    for i in range(0,rows):
        for  j in range(0,clos):
            if j==clos-2:
                print(' {} '.format(matrix[i][j]),end='||')
            else:
                print(' {} '.format(matrix[i][j]),end='  ')
            
        print()
    print('检验数行：')
    for  j in range(0,clos):
        if j==clos-2:
            print(' {} '.format(matrix[rows][j]),end='||')
        else:
            print(' {} '.format(matrix[rows][j]),end='  ')
################################################

input_()
to_fraction()
get_result()
out_()
while True:
    print('\n换基：按clrl+c停止运行')
    get_index()
    get_result()
    out_()

