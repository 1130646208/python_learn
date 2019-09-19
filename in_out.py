table = {'Google':1,'Runoob':2,'Taobao':3}
for name,number in table.items():
   print('{0:10}  {1:10}'.format(name,number))


#字符串 后面不带d，数字后面带不带都可以
print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))
print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))
print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))
print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))
print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))



str=input('请输入：')
print('输入的是：{}'.format(str))
