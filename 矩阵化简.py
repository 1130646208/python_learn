from fractions import Fraction
#输入行数和列数
rows=int(input('请输入行数:'))
clos=int(input('请输入列数:'))
#创建系数矩阵
matrix=[[0]*clos for k in range(rows)]
#输入系数矩阵
for j in range(0,clos):
    for  i in range(0,rows):
        matrix[i][j]=float(input('a{}{}='.format(i+1,j+1)))
print('输入的矩阵：',matrix)

################################################

#存放基变量所在列
base_vec_index=[0 for i in range(clos)]


for i in range(0,rows):
    x=int(input('输入第{}行基变量是X几'.format(i+1)))-1
    base_vec_index[i]=x
print('base_vec_index:',base_vec_index)

temp=[0 for i in range(rows)]
################################################

def process(base_vec_index):
    '找出基变量所在列的系数'
    global temp
    global matrix
    for i in range(rows):
        temp[i]=matrix[i][base_vec_index[i]]
    print('process_temp',temp)



def to_one(row):
    '将某行除以此行的基变量'
    global temp
    global matrix
    global base_vec_index
    for i in range(clos):
        matrix[row][i]=Fraction(int(matrix[row][i]),int(temp[row]))
        
        

def minus_to_zero(row1,row2):
    'row1=row1-row2:两行相减,'
    global matrix
    factor=matrix[row1][base_vec_index[row2]]
    for i in range(clos):
        matrix[row1][i]=matrix[row1][i]-matrix[row2][i]*factor
        

def get_result():
    for i in range(rows):
        to_one(i)
        for j in range(rows):
            if i!=j:
                minus_to_zero(j,i)
################################################

process(base_vec_index)

get_result()

for i in range(0,rows):
    for  j in range(0,clos):
        print(' {} '.format(matrix[i][j]),end='')
    print()
