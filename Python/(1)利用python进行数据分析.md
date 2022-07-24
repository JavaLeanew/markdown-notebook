# NumPy

NumPy（ Numerical Python的简称） 是Python数值计算最重要的基础包。 大多数提供科学计算的包都是用NumPy的数组作为构建基础。

## NumPy的ndarray： 一种多维数组对象

NumPy 最重要的一个特点是其 N 维数组对象 ndarray，它是一系列同类型数据的集合，以 0 下标为开始进行集合中元素的索引。
ndarray 对象是用于存放同类型元素的多维数组。
ndarray 中的每个元素在内存中都有相同存储大小的区域。

你可以利用ndarray对整块数据执行一些数学运算， 其语法跟标量元素之间的运算一样。

```python
In [1]: import numpy as np

In [2]: #generate some random data

In [3]: data=np.random.randn(2,3)    #产生一个2行三列的随机数组成的数组

In [4]: data
Out[4]:
array([[ 1.25038332,  0.69018631,  0.12264871],
       [ 0.26272941, -0.68111954,  0.94721243]])

In [5]: #进行数学运算

In [6]: data*10    #数组每个元素*10
Out[6]:
array([[12.50383319,  6.90186311,  1.22648712],
       [ 2.62729412, -6.81119539,  9.47212431]])

In [7]: data+data    #数组对应元素相加
Out[7]:
array([[ 2.50076664,  1.38037262,  0.24529742],
       [ 0.52545882, -1.36223908,  1.89442486]])
```

每个数组都有一个shape（一个表示各维度大小的元组） 和一个dtype（一个用于说明数组数据类型的对象） ：

```python
In [8]: data.shape    
Out[8]: (2, 3)        #表示data有两行三列

In [9]: data.dtype
Out[9]: dtype('float64')    #表示data中元素的类型为float64
```

> 当你看到“数组”、 “NumPy数组”、 "ndarray"时， 基本上都指的是同一样东西， 即ndarray对象。

### 创建ndarray

创建一个 ndarray 只需调用 NumPy 的 array 函数即可：

```python
numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
```

参数说明:

| 名称 | 描述 |
| - | - |
| object | 数组或嵌套的数列 |
| dtype | 数组元素的数据类型，可选 |
| copy | 对象是否需要复制，可选 |
| order | 创建数组的样式，C为行方向，F为列方向，A为任意方向（默认） |
| subok | 默认返回一个与基类类型一致的数组 |
| ndmin | 指定生成数组的最小维度 |




```python
In [10]: data1=[6,7.5,8,0,1]

In [11]: arr1=np.array(data1)   #array可接受一切序列类型的对象，并产生一个对应的ndarray

In [12]: arr1
Out[12]: array([6. , 7.5, 8. , 0. , 1. ])
```

嵌套序列将会被转化为一个多维数组：

```python
In [13]: data2=[[1,2,3,4],[5,6,7,8]]

In [14]: arr2=np.array(data2)

In [15]: arr2
Out[15]:
array([[1, 2, 3, 4],
       [5, 6, 7, 8]])
In [16]: arr2.ndim    #arr2的最小维度
Out[16]: 2

In [17]: arr2.shape
Out[17]: (2, 4)
```

除非特别说明（稍后将会详细介绍） ， np.array会尝试为新建的这个数组推断出一个较为合适的数
据类型。 数据类型保存在一个特殊的dtype对象中。

```python
In [18]: arr1.dtype
Out[18]: dtype('float64')

In [19]: arr2.dtype
Out[19]: dtype('int32')
```

其他创建数组的方法：

- zeros和ones分别创建指定长度或形状的全0或全1数组

- empty创建一个没有任何具体值的数组

```python
numpy.zeros(shape, dtype = float, order = 'C')#创建指定大小的数组，数组元素以 0 来填充：
```

```python
numpy.ones(shape, dtype = None, order = 'C')#创建指定形状的数组，数组元素以 1 来填充：
```

```python
numpy.empty(shape, dtype = float, order = 'C')#numpy.empty 方法用来创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组：
```

以上三个函数的参数说明

| 参数 | 描述 |
| - | - |
| shape | 数组形状 |
| dtype | 数据类型，可选 |
| order | 'C' 用于 C 的行数组，或者 'F' 用于 FORTRAN 的列数组 |




```python
In [2]: np.zeros(10)
Out[2]: array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])

In [3]: np.zeros((3,6))
Out[3]:
array([[0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0.]])

In [4]: np.empty((2,3,2))
Out[4]:
array([[[ 1.22854110e-311,  1.22853690e-311],
        [-1.30560842e-162,  1.22854110e-311],
        [ 1.22854105e-311, -8.93857919e+245]],

       [[ 1.22854110e-311,  1.22853690e-311],
        [ 1.04831218e+026,  1.22854110e-311],
        [ 1.22854105e-311,  7.16982928e+049]]])
```

注意： 认为np.empty会返回全0数组的想法是不安全的。 很多情况下（如前所示） ， 它返回
的都是一些未初始化的垃圾值。

```python
numpy.arange(start, stop, step, dtype)#numpy 包中的使用 arange 函数创建数值范围并返回 ndarray 对象
```

参数说明:

| 参数 | 描述 |
| - | - |
| start | 起始值，默认为0 |
| stop | 终止值(不包含) |
| step | 步长，默认为1 |
| dtype | 返回ndarray的数据类型，如果没有提供，则会使用输入数据的类型。 |


示例：

```python
In [5]: np.arange(10)
Out[5]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```

### ndarray的数据类型

dtype（数据类型） 是一个特殊的对象， 它含有ndarray将一块内存解释为特定数据类型所需的信息：

```python

In [6]: arr1=np.array([1,2,3],dtype=np.float64)

In [7]: arr2=np.array([1,2,3],dtype=np.int32)

In [8]: arr1.dtype
Out[8]: dtype('float64')
In [9]: arr2.dtype
Out[9]: dtype('int32')
```

NumPy的数据类型:

![](D:\home\markdown-notebook\assets\WEBRESOURCE280de3d2cc8415e3ff1ea2f2c2d17926.png)


![](D:\home\markdown-notebook\assets\WEBRESOURCE57fd5996862ccb0f6fa64814a2d5bec7.png)
可以通过ndarray的astype方法明确地将一个数组从一个dtype转换成另一个dtype：

```python
In [11]: arr=np.array([1,2,3,4,5])
In [12]: arr.dtype
Out[12]: dtype('int32')

In [13]: float_arr=arr.astype(np.float64)
In [14]: float_arr.dtype
Out[14]: dtype('float64')
 #将浮点数转化为整数

In [15]: arr=np.array([3,7,-1.2,-2.6,0.5,12.9,10.1])

In [16]: arr
Out[16]: array([ 3. ,  7. , -1.2, -2.6,  0.5, 12.9, 10.1])

In [17]: arr.astype(np.int32)
Out[17]: array([ 3,  7, -1, -2,  0, 12, 10])
#数字字符串转化为数字 

In [18]: numeric_strings=np.array(['1.25','-9.6','42'],dtype=np.string_)

In [19]: numeric_strings.astype(float)    #NumPy将python数据类型映射到dtype上
Out[19]: array([ 1.25, -9.6 , 42.  ])
 

In [20]: int_arr=np.arange(10)

In [21]: calibers=np.array([.22,.270,.375,.380,.44,.50],dtype=np.float64)

In [22]: int_arr.astype(calibers.dtype)
Out[22]: array([0., 1., 2., 3., 4., 5., 6., 7., 8., 9.])
#使用简洁的类型代码表示dtype 

In [23]: empty_unit32=np.empty(8,dtype='u4')
In [24]: empty_unit32
Out[24]:
array([         0,          0, 2628182096,      32767,          1,
                0, 4294967295, 4294967295], dtype=uint32)
```

调用astype总会创建一个新的数组（一个数据的备份） ， 即使新的dtype与旧的dtype相同。

### NumPy数组的运算

大小相等的数组之间的任何算术运算都会将运算应用到元素级：

```python
In [25]: arr=np.array([[1.,2.,3.],[4.,5.,6.]])

In [26]: arr
Out[26]:
array([[1., 2., 3.],
       [4., 5., 6.]])

In [27]: arr*arr
Out[27]:
array([[ 1.,  4.,  9.],
       [16., 25., 36.]])

In [28]: arr-arr
Out[28]:
array([[0., 0., 0.],
       [0., 0., 0.]])
#数组与标量的算术运算会将标量值传播到各个元素：
In [29]: 1/arr
Out[29]:
array([[1.        , 0.5       , 0.33333333],
       [0.25      , 0.2       , 0.16666667]])

In [30]: arr*0.5
Out[30]:
array([[0.5, 1. , 1.5],
       [2. , 2.5, 3. ]])
#大小相同的数组之间的比较会生成布尔值数组
In [31]: arr2=np.array([[0.,4.,1.],[7.,2.,12.]])

In [32]: arr2
Out[32]:
array([[ 0.,  4.,  1.],
       [ 7.,  2., 12.]])

In [33]: arr2>arr
Out[33]:
array([[False,  True, False],
       [ True, False,  True]])
```

### 基本的索引和切片

```python
In [37]: arr=np.arange(10)

In [38]: arr
Out[38]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In [39]: arr[5]
Out[39]: 5

In [40]: arr[5:8]
Out[40]: array([5, 6, 7])

In [41]: arr[5:8]=12    #切片赋值

In [42]: arr
Out[42]: array([ 0,  1,  2,  3,  4, 12, 12, 12,  8,  9])
#数组切片是原始数组的视图。 这意味着数据不会被复制， 视图上的任何修改都会直接反映到源数组上

In [43]: arr_slice=arr[5:8]

In [44]: arr_slice
Out[44]: array([12, 12, 12])

In [45]: arr_slice[1]=12345

In [46]: arr
Out[46]:
array([    0,     1,     2,     3,     4,    12, 12345,    12,     8,
           9])
#切片[:]会给数组中的所有值赋值                                             

In [47]: arr_slice[:]=64

In [48]: arr
Out[48]: array([ 0,  1,  2,  3,  4, 64, 64, 64,  8,  9])
#在一个二维数组中， 各索引位置上的元素不再是标量而是一维数组： 

In [49]: arr2d=np.array([[1,2,3],[4,5,6],[7,8,9]])

In [50]: arr2d[2]
Out[50]: array([7, 8, 9])

In [51]: arr2d[0][2]
Out[51]: 3

In [52]: arr2d[0,2]    #这种表示与上面是等价的
Out[52]: 3
```

注意： 如果你想要得到的是ndarray切片的一份副本而非视图， 就需要明确地进行复制操作，
例如 arr[5:8].copy() 。

在多维数组中， 如果省略了后面的索引， 则返回对象会是一个维度低一点的ndarray（它含有高一级维度上的所有数据） 。

```python
#arr3d是一个2X2X3的数组
In [53]: arr3d=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

In [54]: arr3d
Out[54]:
array([[[ 1,  2,  3],
        [ 4,  5,  6]],

       [[ 7,  8,  9],
        [10, 11, 12]]])

In [55]: arr3d[0]    #arr3d[0]是一个2x3数组
Out[55]:
array([[1, 2, 3],
       [4, 5, 6]])

In [56]: old_values=arr3d[0].copy()    #标量值和数组都可以被赋值给arr3d[0]

In [57]: arr3d[0]=42

In [58]: arr3d
Out[58]:
array([[[42, 42, 42],
        [42, 42, 42]],

       [[ 7,  8,  9],
        [10, 11, 12]]])

In [59]: arr3d[0]=old_values

In [60]: arr3d
Out[60]:
array([[[ 1,  2,  3],
        [ 4,  5,  6]],

       [[ 7,  8,  9],
        [10, 11, 12]]])
In [62]: arr3d[1,0]
Out[62]: array([7, 8, 9])
```

注意， 在上面所有这些选取数组子集的例子中， 返回的数组都是视图。

### 切片索引

```python
#对于一维数组
In [69]: arr
Out[69]: array([ 0,  1,  2,  3,  4, 64, 64, 64,  8,  9])

In [70]: arr[1:6]
Out[70]: array([ 1,  2,  3,  4, 64])
#对于二维数组 

In [71]: arr2d
Out[71]:
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])

In [72]: arr2d[:2]
Out[72]:
array([[1, 2, 3],
       [4, 5, 6]])

In [73]: arr2d[:2,1:]
Out[73]:
array([[2, 3],
       [5, 6]])

In [74]: arr2d[1,:2]
Out[74]: array([4, 5])

In [75]: arr2d[:2,2]
Out[75]: array([3, 6])

In [76]: arr2d[:,:1]
Out[76]:
array([[1],
       [4],
       [7]])

In [77]: arr2d[:2,1:]=0

In [78]: arr2d
Out[78]:
array([[1, 0, 0],
       [4, 0, 0],
       [7, 8, 9]])
```

### 布尔型索引

假设我们有一个用于存储数据的数组以及一个存储姓名的数组（含有重复
项） 。 在这里， 我将使用numpy.random中的randn函数生成一些正态分布的随机数据：

```python

In [80]: names=np.array(['Bob','Joe','Will','Boe','Will','Joe','Joe'])

In [81]: data=np.random.randn(7,4)

In [82]: names
Out[82]: array(['Bob', 'Joe', 'Will', 'Boe', 'Will', 'Joe', 'Joe'], dtype='<U4')

In [83]: data
Out[83]:
array([[-0.05517176,  1.53418707,  0.67846194, -0.78404911],
       [ 1.2158384 ,  0.06003841, -0.80189338,  0.36935571],
       [ 1.05387103, -0.44968939, -0.16742806,  0.69887068],
       [ 0.08282935,  0.43926446, -0.06406279,  0.06529691],
       [ 0.55245129,  1.63069078, -0.37199503, -0.9038578 ],
       [ 0.35621459, -0.90444116,  0.71776159,  0.18855562],
       [-0.05203564,  0.26097501, -0.50396423, -0.99435599]])
#跟算术运算一样， 数组的比较运算（如==） 也是矢量化的。 因此， 对names和字符串"Bob"的比较运算将会产生一个布尔型数组：              

In [84]: names=='Bob'
Out[84]: array([ True, False, False, False, False, False, False])
#这个布尔类型的数组可用于数组索引,布尔型数组的长度必须跟被索引的轴长度一致。

In [85]: data[names=='Bob']
Out[85]: array([[-0.05517176,  1.53418707,  0.67846194, -0.78404911]])

#取names=='Bob'的行，并索引了列
In [86]: data[names=='Bob',2:]
Out[86]: array([[ 0.67846194, -0.78404911]])

In [87]: data[names=='Bob',3]
Out[87]: array([-0.78404911])
#要选择除"Bob"以外的其他值， 既可以使用不等于符号（!=） ， 也可以通过~对条件进行否定： 

In [88]: names!='Bob'
Out[88]: array([False,  True,  True,  True,  True,  True,  True])

In [89]: data[~(names=='Bob')]
Out[89]:
array([[ 1.2158384 ,  0.06003841, -0.80189338,  0.36935571],
       [ 1.05387103, -0.44968939, -0.16742806,  0.69887068],
       [ 0.08282935,  0.43926446, -0.06406279,  0.06529691],
       [ 0.55245129,  1.63069078, -0.37199503, -0.9038578 ],
       [ 0.35621459, -0.90444116,  0.71776159,  0.18855562],
       [-0.05203564,  0.26097501, -0.50396423, -0.99435599]])

In [90]: cond=names=='Bob'

In [91]: data[~cond]
Out[91]:
array([[ 1.2158384 ,  0.06003841, -0.80189338,  0.36935571],
       [ 1.05387103, -0.44968939, -0.16742806,  0.69887068],
       [ 0.08282935,  0.43926446, -0.06406279,  0.06529691],
       [ 0.55245129,  1.63069078, -0.37199503, -0.9038578 ],
       [ 0.35621459, -0.90444116,  0.71776159,  0.18855562],
       [-0.05203564,  0.26097501, -0.50396423, -0.99435599]])
 #选取这三个名字中的两个需要组合应用多个布尔条件， 使用&（和） 、 |（或） 之类的布尔算术运算符即可：             

In [92]: mask=(names=='Bob')|(names=='Will')

In [93]: mask
Out[93]: array([ True, False,  True, False,  True, False, False])

In [94]: data[mask]
Out[94]:
array([[-0.05517176,  1.53418707,  0.67846194, -0.78404911],
       [ 1.05387103, -0.44968939, -0.16742806,  0.69887068],
       [ 0.55245129,  1.63069078, -0.37199503, -0.9038578 ]])       
#通过布尔型数组设置值是一种经常用到的手段。 为了将data中的所有负值都设置为0， 我们只需：       

In [95]: data[data<0]
Out[95]:
array([-0.05517176, -0.78404911, -0.80189338, -0.44968939, -0.16742806,
       -0.06406279, -0.37199503, -0.9038578 , -0.90444116, -0.05203564,
       -0.50396423, -0.99435599])

In [96]: data[data<0]=0

In [97]: data
Out[97]:
array([[0.        , 1.53418707, 0.67846194, 0.        ],
       [1.2158384 , 0.06003841, 0.        , 0.36935571],
       [1.05387103, 0.        , 0.        , 0.69887068],
       [0.08282935, 0.43926446, 0.        , 0.06529691],
       [0.55245129, 1.63069078, 0.        , 0.        ],
       [0.35621459, 0.        , 0.71776159, 0.18855562],
       [0.        , 0.26097501, 0.        , 0.        ]])
#通过一维布尔数组设置整行或列的值也很简单:              

In [98]: data[names!='Joe']=7

In [99]: data
Out[99]:
array([[7.        , 7.        , 7.        , 7.        ],
       [1.2158384 , 0.06003841, 0.        , 0.36935571],
       [7.        , 7.        , 7.        , 7.        ],
       [7.        , 7.        , 7.        , 7.        ],
       [7.        , 7.        , 7.        , 7.        ],
       [0.35621459, 0.        , 0.71776159, 0.18855562],
       [0.        , 0.26097501, 0.        , 0.        ]])
```

通过布尔型索引选取数组中的数据， 将总是创建数据的副本， 即使返回一模一样的数组也是如此。

### 花式索引

花式索引（Fancy indexing） 是一个NumPy术语， 它指的是利用整数数组进行索引。

```python
#生成一个8x4的数组
In [112]: arr=np.empty((8,4))

In [113]: for i in range(8):
     ...:     arr[i]=i
     ...:

In [114]: arr
Out[114]:
array([[0., 0., 0., 0.],
       [1., 1., 1., 1.],
       [2., 2., 2., 2.],
       [3., 3., 3., 3.],
       [4., 4., 4., 4.],
       [5., 5., 5., 5.],
       [6., 6., 6., 6.],
       [7., 7., 7., 7.]])
#为了以特定顺序选取行子集， 只需传入一个用于指定顺序的整数列表或ndarray即可:              

In [115]: arr[[4,3,0,6]]
Out[115]:
array([[4., 4., 4., 4.],
       [3., 3., 3., 3.],
       [0., 0., 0., 0.],
       [6., 6., 6., 6.]])
#使用负数索引将会从末尾开始选取行：              

In [116]: arr[[-3,-5,-7]]
Out[116]:
array([[5., 5., 5., 5.],
       [3., 3., 3., 3.],
       [1., 1., 1., 1.]])
#一次传入多个索引数组会有一点特别。 它返回的是一个一维数组， 其中的元素对应各个索引元组：       

In [117]: arr=np.arange(32).reshape((8,4))

In [118]: arr
Out[118]:
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15],
       [16, 17, 18, 19],
       [20, 21, 22, 23],
       [24, 25, 26, 27],
       [28, 29, 30, 31]])

In [119]: arr[[1,5,7,2],[0,3,1,2]]
Out[119]: array([ 4, 23, 29, 10])    #最终选出的是元素(1,0)、 (5,3)、 (7,1)和(2,2)。 无论数组是多少维的， 花式索引总是一维的。
#下面是选择数组的矩形区域，不是花式索引，注意区别。


In [120]: arr[[1,5,7,2]][:,[0,3,1,2]]
Out[120]:
array([[ 4,  7,  5,  6],
       [20, 23, 21, 22],
       [28, 31, 29, 30],
       [ 8, 11,  9, 10]])
```

记住， 花式索引跟切片不一样， 它总是将数据复制到新数组中。

### 数组转置和轴对换

转置是重塑的一种特殊形式， 它返回的是源数据的视图（不会进行任何复制操作） 。 数组不仅有transpose方法， 还有一个特殊的T属性：

```python
In [122]: arr=np.arange(15).reshape((3,5))

In [123]: arr
Out[123]:
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])

In [124]: arr.T
Out[124]:
array([[ 0,  5, 10],
       [ 1,  6, 11],
       [ 2,  7, 12],
       [ 3,  8, 13],
       [ 4,  9, 14]])
```

在进行矩阵计算时， 经常需要用到转置操作， 比如利用np.dot计算矩阵内积：

```python
In [126]: arr
Out[126]:
array([[ 2.27691372, -0.18733256, -0.08920677],
       [-0.78556533,  0.27117435,  0.27636969],
       [ 2.14357423,  1.29889209,  0.09506859],
       [ 1.67736885,  0.28793841, -0.17610893],
       [-0.54169009, -0.03598126,  0.23420932],
       [-0.61525871, -0.14746426, -0.88233737]])

In [127]: np.dot(arr.T,arr)
Out[127]:
array([[13.88189714,  2.73790466, -0.09583873],
       [ 2.73790466,  1.90169857,  0.28611709],
       [-0.09583873,  0.28611709,  0.95776368]])
```

对于高维数组， transpose需要得到一个由轴编号组成的元组才能对这些轴进行转置（比较费脑
子） ：

```python
In [129]: arr=np.arange(16).reshape((2,2,4))

In [130]: arr
Out[130]:
array([[[ 0,  1,  2,  3],
        [ 4,  5,  6,  7]],

       [[ 8,  9, 10, 11],
        [12, 13, 14, 15]]])

In [131]: arr.transpose((1,0,2))
Out[131]:
array([[[ 0,  1,  2,  3],
        [ 8,  9, 10, 11]],

       [[ 4,  5,  6,  7],
        [12, 13, 14, 15]]])
#第一个轴被换成了第二个， 第二个轴被换成了第一个， 最后一个轴不变。
```

简单的转置可以使用.T， 它其实就是进行轴对换而已。 ndarray还有一个swapaxes方法， 它需要接
受一对轴编号。

```python
In [132]: arr
Out[132]:
array([[[ 0,  1,  2,  3],
        [ 4,  5,  6,  7]],

       [[ 8,  9, 10, 11],
        [12, 13, 14, 15]]])

In [133]: arr.swapaxes(1,2)
Out[133]:
array([[[ 0,  4],
        [ 1,  5],
        [ 2,  6],
        [ 3,  7]],

       [[ 8, 12],
        [ 9, 13],
        [10, 14],
        [11, 15]]])
```

swapaxes也是返回源数据的视图（不会进行任何复制操作） 。

## 通用函数： 快速的元素级数组函数

通用函数（即ufunc） 是一种对ndarray中的数据执行元素级运算的函数。 你可以将其看做简单函数
（接受一个或多个标量值， 并产生一个或多个标量值） 的矢量化包装器。

```python
#这些都是一元（unary） ufunc。 
In [3]: arr=np.arange(10)

In [4]: arr
Out[4]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In [5]: np.sqrt(arr)
Out[5]:
array([0.        , 1.        , 1.41421356, 1.73205081, 2.        ,
       2.23606798, 2.44948974, 2.64575131, 2.82842712, 3.        ])

In [6]: np.exp(arr)
Out[6]:
array([1.00000000e+00, 2.71828183e+00, 7.38905610e+00, 2.00855369e+01,
       5.45981500e+01, 1.48413159e+02, 4.03428793e+02, 1.09663316e+03,
       2.98095799e+03, 8.10308393e+03])
```



```python
In [7]: x=np.random.randn(8)

In [8]: y=np.random.randn(8)

In [9]: x
Out[9]:
array([-0.46015928, -0.01221277,  0.38587877,  0.98157063, -0.46874868,
       -0.89677461,  0.28431179,  0.07348369])

In [10]: y
Out[10]:
array([-1.07514799,  0.18428925, -0.3501127 , -0.30169029,  0.13132063,
        3.11252567,  0.47883429, -0.02678514])

In [11]: np.maximum(x,y)    #numpy.maximum计算了x和y中元素级别最大的元素

Out[11]:
array([-0.46015928,  0.18428925,  0.38587877,  0.98157063,  0.13132063,
        3.11252567,  0.47883429,  0.07348369])
```

有些ufunc的确可以返回多个数组。 modf就是一个例子， 它是Python内置函数
divmod的矢量化版本， 它会返回浮点数数组的小数和整数部分：

```python
In [12]: arr=np.random.randn(7)*5

In [13]: arr
Out[13]:
array([-0.76313303, -0.88089947, -1.06063889, -0.88330023,  5.13801558,
        3.40602431,  5.21358423])

In [14]: remainder,whole_part=np.modf(arr)

In [15]: remainder
Out[15]:
array([-0.76313303, -0.88089947, -0.06063889, -0.88330023,  0.13801558,
        0.40602431,  0.21358423])

In [16]: whole_part
Out[16]: array([-0., -0., -1., -0.,  5.,  3.,  5.])
```

Ufuncs可以接受一个out可选参数， 这样就能在数组原地进行操作：

```python
In [17]: arr
Out[17]:
array([-0.76313303, -0.88089947, -1.06063889, -0.88330023,  5.13801558,
        3.40602431,  5.21358423])

In [18]: np.sqrt(arr)
<ipython-input-18-b58949107b3d>:1: RuntimeWarning: invalid value encountered in sqrt
  np.sqrt(arr)
Out[18]:
array([       nan,        nan,        nan,        nan, 2.26671912,
       1.84554174, 2.28332745])

In [19]: arr
Out[19]:
array([-0.76313303, -0.88089947, -1.06063889, -0.88330023,  5.13801558,
        3.40602431,  5.21358423])

In [20]: np.sqrt(arr,arr)
<ipython-input-20-e3ca18b15869>:1: RuntimeWarning: invalid value encountered in sqrt
  np.sqrt(arr,arr)
Out[20]:
array([       nan,        nan,        nan,        nan, 2.26671912,
       1.84554174, 2.28332745])

In [21]: arr
Out[21]:
array([       nan,        nan,        nan,        nan, 2.26671912,
       1.84554174, 2.28332745])
```

下面是一些一元和二元ufunc:



![](D:\home\markdown-notebook\assets\WEBRESOURCE0434a353a7ef856ea954287682074317.png)


![](D:\home\markdown-notebook\assets\WEBRESOURCE57303225b58c9ffd878e6ac2253643e7.png)


![](D:\home\markdown-notebook\assets\WEBRESOURCE024e53946f5509431c6665ef802af9fc.png)


## 利用数组进行数据处理

NumPy数组使你可以将许多种数据处理任务表述为简洁的数组表达式（否则需要编写循环） 。 用
数组表达式代替循环的做法， 通常被称为矢量化。 

作为简单的例子， 假设我们想要在一组值（网格型） 上计算函数 sqrt(x^2+y^2) 。

```python
In [1]: import numpy as np

In [2]: points=np.arange(-5,5,1)
# np.meshgrid函
数接受两个一维数组， 并产生两个二维矩阵（对应于两个数组中所有的(x,y)对）

In [3]: xs,ys=np.meshgrid(points,points)    

In [4]: ys
Out[4]:
array([[-5, -5, -5, -5, -5, -5, -5, -5, -5, -5],
       [-4, -4, -4, -4, -4, -4, -4, -4, -4, -4],
       [-3, -3, -3, -3, -3, -3, -3, -3, -3, -3],
       [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
       [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
       [ 1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
       [ 2,  2,  2,  2,  2,  2,  2,  2,  2,  2],
       [ 3,  3,  3,  3,  3,  3,  3,  3,  3,  3],
       [ 4,  4,  4,  4,  4,  4,  4,  4,  4,  4]])
       In [5]: z=np.sqrt(xs**2+ys**2)

In [6]: z
Out[6]:
array([[7.07106781, 6.40312424, 5.83095189, 5.38516481, 5.09901951,
        5.        , 5.09901951, 5.38516481, 5.83095189, 6.40312424],
       [6.40312424, 5.65685425, 5.        , 4.47213595, 4.12310563,
        4.        , 4.12310563, 4.47213595, 5.        , 5.65685425],
       [5.83095189, 5.        , 4.24264069, 3.60555128, 3.16227766,
        3.        , 3.16227766, 3.60555128, 4.24264069, 5.        ],
       [5.38516481, 4.47213595, 3.60555128, 2.82842712, 2.23606798,
        2.        , 2.23606798, 2.82842712, 3.60555128, 4.47213595],
       [5.09901951, 4.12310563, 3.16227766, 2.23606798, 1.41421356,
        1.        , 1.41421356, 2.23606798, 3.16227766, 4.12310563],
       [5.        , 4.        , 3.        , 2.        , 1.        ,
        0.        , 1.        , 2.        , 3.        , 4.        ],
       [5.09901951, 4.12310563, 3.16227766, 2.23606798, 1.41421356,
        1.        , 1.41421356, 2.23606798, 3.16227766, 4.12310563],
       [5.38516481, 4.47213595, 3.60555128, 2.82842712, 2.23606798,
        2.        , 2.23606798, 2.82842712, 3.60555128, 4.47213595],
       [5.83095189, 5.        , 4.24264069, 3.60555128, 3.16227766,
        3.        , 3.16227766, 3.60555128, 4.24264069, 5.        ],
       [6.40312424, 5.65685425, 5.        , 4.47213595, 4.12310563,
        4.        , 4.12310563, 4.47213595, 5.        , 5.65685425]])
```

### 将条件逻辑表述为数组运算

numpy.where函数是三元表达式x if condition else y的矢量化版本。 假设我们有一个布尔数组和两
个值数组：

```python
In [7]: xarr=np.array([1.1,1.2,1.3,1.4,1.5])

In [8]: yarr=np.array([2.1,2.2,2.3,2.4,2.5])

In [9]: cond=np.array([True,False,True,True,False])
#假设我们想要根据cond中的值选取xarr和yarr的值： 当cond中的值为True时， 选取xarr的值， 否则
从yarr中选取。 
#列表推导式的写法应该如下所示： 

In [10]: result=[(x if c else y) for x,y,c in zip(xarr,yarr,cond)]

In [11]: result
Out[11]: [1.1, 2.2, 1.3, 1.4, 2.5]
#这有几个问题。 第一， 它对大数组的处理速度不是很快（因为所有工作都是由纯Python完成
的） 。
#第二， 无法用于多维数组。 若使用np.where， 则可以将该功能写得非常简洁： 

In [12]: result=np.where(cond,xarr,yarr)

In [13]: result
Out[13]: array([1.1, 2.2, 1.3, 1.4, 2.5])
```

np.where的第二个和第三个参数不必是数组， 它们都可以是标量值。 在数据分析工作中， where通
常用于根据另一个数组而产生一个新的数组。 假设有一个由随机数据组成的矩阵， 你希望将所有正
值替换为2， 将所有负值替换为－2。 若利用np.where， 则会非常简单：

```python
In [14]: arr=np.random.randn(4,4)

In [15]: arr
Out[15]:
array([[-0.61149449, -0.99413917,  1.58234606, -0.74720651],
       [ 0.60278374,  1.96381039,  0.40885644,  0.49408553],
       [-2.45861749,  0.46854309,  0.3389395 ,  1.10144475],
       [-1.32180763, -0.92659561, -1.64363139,  0.5897704 ]])

In [16]: arr>0
Out[16]:
array([[False, False,  True, False],
       [ True,  True,  True,  True],
       [False,  True,  True,  True],
       [False, False, False,  True]])

In [17]: np.where(arr>0,0,-2)
Out[17]:
array([[-2, -2,  0, -2],
       [ 0,  0,  0,  0],
       [-2,  0,  0,  0],
       [-2, -2, -2,  0]])
```

使用np.where， 可以将标量和数组结合起来。 例如， 我可用常数2替换arr中所有正的值：

```python
In [18]: np.where(arr>0,0,arr)
Out[18]:
array([[-0.61149449, -0.99413917,  0.        , -0.74720651],
       [ 0.        ,  0.        ,  0.        ,  0.        ],
       [-2.45861749,  0.        ,  0.        ,  0.        ],
       [-1.32180763, -0.92659561, -1.64363139,  0.        ]])
```

传递给where的数组大小可以不相等， 甚至可以是标量值。

### 数学和统计方法

可以通过数组上的一组数学函数对整个数组或某个轴向的数据进行统计计算。 sum、 mean以及标
准差std等聚合计算（aggregation， 通常叫做约简（reduction） ） 既可以当做数组的实例方法调
用， 也可以当做顶级NumPy函数使用。

```python
In [2]: arr=np.random.randn(5,4)

In [3]: arr
Out[3]:
array([[-0.36589919,  0.21280561, -0.71043604,  0.70197317],
       [-0.48661596, -0.68844445, -1.32865229, -1.07141896],
       [ 0.14730929,  0.00455724,  0.72172257, -0.11212237],
       [-0.33126416, -0.73579026, -1.26233255, -0.85113856],
       [ 1.18076491,  0.2248318 , -0.93145207, -0.35545303]])

In [4]: arr.mean()
Out[4]: -0.3018527646983594

In [5]: np.mean(arr)
Out[5]: -0.3018527646983594

In [6]: arr.sum()
Out[6]: -6.037055293967189
```

mean和sum这类的函数可以接受一个axis选项参数， 用于计算该轴向上的统计值， 最终结果是一
个少一维的数组：

```python
#这里， arr.mean(1)是“计算行的平均值”， arr.sum(0)是“计算每列的和”。
In [7]: arr.mean(axis=1)
Out[7]: array([-0.04038911, -0.89378292,  0.19036668, -0.79513138,  0.0296729 ])

In [8]: arr.sum(axis=0)
Out[8]: array([ 0.14429489, -0.98204006, -3.51115037, -1.68815975])
```

其他如cumsum和cumprod之类的方法则不聚合， 而是产生一个由中间结果组成的数组：

```python
In [9]: arr=np.array([0,1,2,3,4,5,6,7])

In [10]: arr.cumsum()
Out[10]: array([ 0,  1,  3,  6, 10, 15, 21, 28], dtype=int32)
```

在多维数组中， 累加函数（如cumsum） 返回的是同样大小的数组， 但是会根据每个低维的切片沿
着标记轴计算部分聚类：

```python
In [12]: arr=np.array([[0,1,2],[3,4,5],[6,7,8]])

In [13]: arr
Out[13]:
array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])

In [14]: arr.cumsum(axis=0)
Out[14]:
array([[ 0,  1,  2],
       [ 3,  5,  7],
       [ 9, 12, 15]], dtype=int32)

In [15]: arr.cumsum(axis=1)
Out[15]:
array([[ 0,  1,  3],
       [ 3,  7, 12],
       [ 6, 13, 21]], dtype=int32)
```

下面列出了全部的基本数组统计方法:

 

![](D:\home\markdown-notebook\assets\WEBRESOURCE944fd24894c9a20e8a2bb49ec9d2eb03.png)
### 用于布尔型数组的方法

在上面这些方法中， 布尔值会被强制转换为1（True） 和0（False） 。 因此， sum经常被用来对布
尔型数组中的True值计数:

```python
In [16]: arr=np.random.randn(100)

In [17]: (arr>0).sum()
Out[17]: 35
```

另外还有两个方法any和all， 它们对布尔型数组非常有用。 any用于测试数组中是否存在一个或多
个True， 而all则检查数组中所有值是否都是True：

```python
In [20]: bools=np.array([False,False,True,False])

In [21]: bools.any()
Out[21]: True

In [22]: bools.all()
Out[22]: False
```

### 排序

跟Python内置的列表类型一样， NumPy数组也可以通过sort方法就地排序：

```python
In [25]: arr=np.random.randn(6)

In [26]: arr
Out[26]:
array([ 0.46413187, -0.59390426, -1.23406556, -1.23479226, -0.41383296,
        1.51315531])

In [27]: arr.sort()

In [28]: arr
Out[28]:
array([-1.23479226, -1.23406556, -0.59390426, -0.41383296,  0.46413187,
        1.51315531])
```

多维数组可以在任何一个轴向上进行排序， 只需将轴编号传给sort即可：

```python
In [29]: arr=np.random.randn(5,3)

In [30]: arr
Out[30]:
array([[-0.09617414, -0.05429359, -1.18233771],
       [-0.79094214, -0.1882165 ,  0.32617118],
       [ 0.85984985,  1.03497693, -0.60374401],
       [-0.59215488,  0.82834005, -0.58499392],
       [-1.79085977, -0.28642247,  0.33099811]])

In [31]: arr.sort(1)

In [32]: arr
Out[32]:
array([[-1.18233771, -0.09617414, -0.05429359],
       [-0.79094214, -0.1882165 ,  0.32617118],
       [-0.60374401,  0.85984985,  1.03497693],
       [-0.59215488, -0.58499392,  0.82834005],
       [-1.79085977, -0.28642247,  0.33099811]])
```

顶级方法np.sort返回的是数组的已排序副本， 而就地排序则会修改数组本身。 计算数组分位数最
简单的办法是对其进行排序， 然后选取特定位置的值：

```python
In [33]: large_arr=np.random.randn(1000)

In [34]: large_arr.sort()

In [35]: large_arr[int(0.05*len(large_arr))]
Out[35]: -1.6843930699015017
```

### 唯一化以及其它的集合逻辑

NumPy提供了一些针对一维ndarray的基本集合运算。 最常用的可能要数np.unique了， 它用于找
出数组中的唯一值并返回已排序的结果：

```python
In [36]: names=np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])

In [37]: np.unique(names)
Out[37]: array(['Bob', 'Joe', 'Will'], dtype='<U4')

In [38]: ints=np.array([3,3,3,2,2,1,1,4,4])

In [39]: np.unique(ints)
Out[39]: array([1, 2, 3, 4])

In [40]: #跟np.unique等价的纯python代码比较

In [41]: sorted(set(names))
Out[41]: ['Bob', 'Joe', 'Will']
```

另一个函数np.in1d用于测试一个数组中的值在另一个数组中的成员资格， 返回一个布尔型数组:

```python
In [42]: values=np.array([6,0,0,3,2,5,6])

In [43]: np.in1d(values,[2,3,6])
Out[43]: array([ True, False, False,  True,  True, False,  True])
```

NumPy中的集合函数:



![](D:\home\markdown-notebook\assets\WEBRESOURCEdedde46e7a7e08d344303bcb070b2935.png)
## 用于数组的文件输入输出

NumPy能够读写磁盘上的文本数据或二进制数据。 这一小节只讨论NumPy的内置二进制格式， 因
为更多的用户会使用pandas或其它工具加载文本或表格数据。

np.save和np.load是读写磁盘数组数据的两个主要函数。 默认情况下， 数组是以未压缩的原始二进
制格式保存在扩展名为.npy的文件中的：

```python
In [45]: arr=np.arange(10)

In [46]: np.save('some_array',arr)

In [47]: np.load('some_array.npy')
Out[47]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```

通过np.savez可以将多个数组保存到一个未压缩文件中， 将数组以关键字参数的形式传入即可：

```python
In [49]: np.savez('array_archive.npz',a=arr,b=arr)

In [50]: arch=np.load('array_archive.npz')

In [51]: arch['b']
Out[51]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```

如果要将数据压缩， 可以使用numpy.savez_compressed：

```python
In [52]: np.savez_compressed('arrays_compressed',a=arr,b=arr)

In [53]: arch=np.load('array_archive.npz')
```

## 线性代数

线性代数（如矩阵乘法、 矩阵分解、 行列式以及其他方阵数学等） 是任何数组库的重要组成部分。 NumPy提供了一个用于矩阵乘法的dot函数（既是一个数组方法也是numpy命名
空间中的一个函数） ：

```python
In [57]: x=np.array([[1.,2.,3.],[4.,5.,6.]])

In [58]: y=np.array([[6.,23.],[-1,7],[8,9]])

In [59]: x
Out[59]:
array([[1., 2., 3.],
       [4., 5., 6.]])

In [60]: y
Out[60]:
array([[ 6., 23.],
       [-1.,  7.],
       [ 8.,  9.]])

In [61]: x.dot(y)
Out[61]:
array([[ 28.,  64.],
       [ 67., 181.]])

In [62]: #x.dot(x,y)等价于np.dot(x,y)

In [63]: np.dot(x,y)
Out[63]:
array([[ 28.,  64.],
       [ 67., 181.]])
#个二维数组跟一个大小合适的一维数组的矩阵点积运算之后将会得到一个一维数组：        

In [64]: np.dot(x,np.ones(3))    #把一维数组看作列向量
Out[64]: array([ 6., 15.])
```

@符（类似Python 3.5） 也可以用作中缀运算符， 进行矩阵乘法：

```python
In [70]: x @ np.ones(3)
Out[70]: array([ 6., 15.])
```

numpy.linalg中有一组标准的矩阵分解运算以及诸如求逆和行列式之类的东西。 它们跟MATLAB和
R等语言所使用的是相同的行业标准线性代数库， 如BLAS、 LAPACK、 Intel MKL（Math Kernel
 Library， 可能有， 取决于你的NumPy版本） 等：

```python
In [81]: X=np.array([[1,0,0],[0,7,9],[0,0,13]])

In [82]: mat=X.T.dot(X)

In [83]: mat
Out[83]:
array([[  1,   0,   0],
       [  0,  49,  63],
       [  0,  63, 250]])

In [84]: mat.dot(inv(mat))       #这里是.乘，不是X乘
Out[84]:
array([[ 1.00000000e+00,  0.00000000e+00,  0.00000000e+00],
       [ 0.00000000e+00,  1.00000000e+00,  3.03576608e-17],
       [ 0.00000000e+00, -4.68375339e-17,  1.00000000e+00]])
```

矩阵·乘和x乘



![](D:\home\markdown-notebook\assets\WEBRESOURCE5f24cd07367953a5de4863b6b31548fa.png)
## 伪随机数生成

numpy.random模块对Python内置的random进行了补充， 增加了一些用于高效生成多种概率分布
的样本值的函数。 例如， 你可以用normal来得到一个标准正态分布的4×4样本数组：

```python
In [101]: samples=np.random.normal(size=(4,4))

In [102]: samples
Out[102]:
array([[ 0.52707931, -1.32193274, -1.28999059, -0.48263648],
       [-1.26947425,  0.17033616, -0.07303791,  0.14696383],
       [-0.18325403, -0.81138684, -0.68140743, -0.28935683],
       [ 0.50921353,  0.04385858, -0.087448  , -0.13253761]])
```

而Python内置的random模块则只能一次生成一个样本值。如果需
要产生大量样本值， numpy.random快了不止一个数量级。

我们说这些都是伪随机数， 是因为它们都是通过算法基于随机数生成器种子， 在确定性的条件下生
成的。 你可以用NumPy的np.random.seed更改随机数生成种子：

```python
In [103]: np.random.seed(1234)
#numpy.random的数据生成函数使用了全局的随机种子。 要避免全局状态， 你可以使用
numpy.random.RandomState， 创建一个与其它隔离的随机数生成器： 

In [104]: rng=np.random.RandomState(1234)

In [105]: rng.randn(10)
Out[105]:
array([ 0.47143516, -1.19097569,  1.43270697, -0.3126519 , -0.72058873,
        0.88716294,  0.85958841, -0.6365235 ,  0.01569637, -2.24268495])

```



![](D:\home\markdown-notebook\assets\WEBRESOURCE426687b14b2a053b52645bd5b37c8d6b.png)


![](D:\home\markdown-notebook\assets\WEBRESOURCE0b39f31a1f6643e859e5b97a98a86b64.png)
## 示例：随机漫步

我们通过模拟随机漫步来说明如何运用数组运算。 先来看一个简单的随机漫步的例子： 从0开始，
步长1和－1出现的概率相等。

下面是一个通过内置的random模块以纯Python的方式实现1000步的随机漫步：

```python
In [106]: import random

In [107]: position=0

In [108]: walk=[position]

In [109]: steps=1000

In [110]: for i in range(steps):
     ...:     step=1 if random.randint(0,1) else -1
     ...:     position+=step
     ...:     walk.append(position)
     ...:
```

可以用
np.random模块一次性随机产生1000个“掷硬币”结果（即两个数中任选一个） ， 将其分别设置为1
或－1， 然后计算累计和：

```python
In [115]: draws=np.random.randint(0,2,size=nsteps)

In [116]: steps=np.where(draws>0,1,-1)

In [117]: walk=steps.cumsum()
#有了这些数据之后， 我们就可以沿着漫步路径做一些统计工作了， 比如求取最大值和最小值： 

In [118]: walk.min()
Out[118]: 1

In [119]: walk.max()
Out[119]: 47
```

现在来看一个复杂点的统计任务——首次穿越时间， 即随机漫步过程中第一次到达某个特定值的时
间。 假设我们想要知道本次随机漫步需要多久才能距离初始0点至少10步远（任一方向均可） 。
np.abs(walk)>=10可以得到一个布尔型数组， 它表示的是距离是否达到或超过10， 而我们想要知
道的是第一个10或－10的索引。 可以用argmax来解决这个问题， 它返回的是该布尔型数组第一个
最大值的索引（True就是最大值） ：

```python
In [120]: (np.abs(walk)>=10).argmax()
Out[120]: 21
```

注意， 这里使用argmax并不是很高效， 因为它无论如何都会对数组进行完全扫描。 在本例中， 只
要发现了一个True， 那我们就知道它是个最大值了。

### 一次模拟多个随机漫步

如果你希望模拟多个随机漫步过程（比如5000个） ， 只需对上面的代码做一点点修改即可生成所
有的随机漫步过程。 只要给numpy.random的函数传入一个二元元组就可以产生一个二维数组， 然
后我们就可以一次性计算5000个随机漫步过程（一行一个） 的累计和了：

```python
In [121]: nwalks=5000

In [122]: nsteps=1000

In [123]: draws=np.random.randint(0,2,size=(nwalks,nsteps))

In [124]: draws.shape
Out[124]: (5000, 1000)
In [126]: steps=np.where(draws>0,1,-1)

In [127]: walks=steps.cumsum(1)

In [128]: walks
Out[128]:
array([[  1,   0,   1, ...,  40,  41,  42],
       [  1,   2,   3, ..., -26, -27, -28],
       [ -1,  -2,  -3, ..., -12, -13, -12],
       ...,
       [  1,   2,   1, ...,   2,   1,   0],
#计算所有随机漫步中的最大值和最小值
In [129]: walks.max()
Out[129]: 122

In [130]: walks.min()
Out[130]: -128
```

得到这些数据之后， 我们来计算30或－30的最小穿越时间。 这里稍微复杂些， 因为不是5000个过
程都到达了30。 我们可以用any方法来对此进行检查：

```python
In [131]: hits30=(np.abs(walks)>=30)

In [132]: hits30
Out[132]:
array([[False, False, False, ...,  True,  True,  True],
       [False, False, False, ..., False, False, False],
       [False, False, False, ..., False, False, False],
       ...,
       [False, False, False, ..., False, False, False],
       [False, False, False, ...,  True,  True,  True],
       [False, False, False, ..., False, False, False]])

In [133]: hits30.any(1)
Out[133]: array([ True,  True,  True, ..., False,  True, False])

In [134]: hits30=hits30.any(1)

In [135]: hits30
Out[135]: array([ True,  True,  True, ..., False,  True, False])

In [136]: hits30.sum()#number that hit 30 or not
Out[136]: 3367
```

然后我们利用这个布尔型数组选出那些穿越了30（绝对值） 的随机漫步（行） ， 并调用argmax在
轴1上获取穿越时间：

```python
In [137]: crossing_times=(np.abs(walks[hits30])>30).argmax(1)

In [138]: crossing_times.mean()
Out[138]: 495.26106326106327
```

> numpy.argmax() 和 numpy.argmin()函数分别沿给定轴返回最大和最小元素的索引。

# pandas

## pandas的数据结构介绍

要使用pandas， 你首先就得熟悉它的两个主要数据结构： Series和DataFrame。 虽然它们并不能
解决所有问题， 但它们为大多数应用提供了一种可靠的、 易于使用的基础。

### Series

Series是一种类似于一维数组的对象， 它由一组数据（各种NumPy数据类型） 以及一组与之相关
的数据标签（即索引） 组成。 仅由一组数据即可产生最简单的Series：

```python
In [3]: obj=pd.Series([4,7,-5,3])

In [4]: obj
Out[4]:
0    4
1    7
2   -5
3    3
dtype: int64
```

Series的字符串表现形式为： 索引在左边， 值在右边。 由于我们没有为数据指定索引， 于是会自动
创建一个0到N-1（N为数据的长度） 的整数型索引。 你可以通过Series 的values和index属性获取
其数组表示形式和索引对象：

```python
In [5]: obj.values
Out[5]: array([ 4,  7, -5,  3], dtype=int64)

In [6]: obj.index
Out[6]: RangeIndex(start=0, stop=4, step=1)
```

通常， 我们希望所创建的Series带有一个可以对各个数据点进行标记的索引：

```python
In [7]: obj2=pd.Series([4,7,-5,3],index=['d','b','a','c'])

In [8]: obj2
Out[8]:
d    4
b    7
a   -5
c    3
dtype: int64

In [9]: obj2.index
Out[9]: Index(['d', 'b', 'a', 'c'], dtype='object')
```

与普通NumPy数组相比， 你可以通过索引的方式选取Series中的单个或一组值：

```python
In [14]: obj2['a']
Out[14]: -5

In [15]: obj2['d']
Out[15]: 4

In [16]: obj2[['c','a','d']]
Out[16]:
c    3
a   -5
d    4
dtype: int64
```

使用NumPy函数或类似NumPy的运算（如根据布尔型数组进行过滤、 标量乘法、 应用数学函数
等） 都会保留索引值的链接：

```python
In [10]: obj2[obj2>0]
Out[10]:
d    4
b    7
c    3
dtype: int64

In [11]: obj2*2
Out[11]:
d     8
b    14
a   -10
c     6
dtype: int64

In [12]: np.exp(obj2)
Out[12]:
d      54.598150
b    1096.633158
a       0.006738
c      20.085537
dtype: float64
```

还可以将Series看成是一个定长的有序字典， 因为它是索引值到数据值的一个映射。 它可以用在许
多原本需要字典参数的函数中：

```python
In [17]: 'b' in obj2
Out[17]: True

In [18]: 'e' in obj2
Out[18]: False
```

如果数据被存放在一个Python字典中， 也可以直接通过这个字典来创建Series：

```python
In [22]: sdata={'Ohio':3500,'Texas':7100,'Oregon':16000,'Utah':5000}

In [23]: obj3=pd.Series(sdata)

In [24]: obj3
Out[24]:
Ohio       3500
Texas      7100
Oregon    16000
Utah       5000
dtype: int64
```

如果只传入一个字典， 则结果Series中的索引就是原字典的键（有序排列） 。 你可以传入排好序的
字典的键以改变顺序：

```python
In [25]: states=['California','Ohio','Oregon','Texas']

In [26]: obj4=pd.Series(sdata,states)

In [27]: obj4
Out[27]:
California        NaN
Ohio           3500.0
Oregon        16000.0
Texas          7100.0
dtype: float64
```

在这个例子中， sdata中跟states索引相匹配的那3个值会被找出来并放到相应的位置上， 但由
于"California"所对应的sdata值找不到， 所以其结果就为NaN（即“非数字”（not a number） ， 在
pandas中， 它用于表示缺失或NA值） 。 因为‘Utah’不在states中， 它被从结果中除去。

pandas的isnull和notnull函数可用于检测缺失数
据：

```python
In [31]: pd.isnull(obj4)
Out[31]:
California     True
Ohio          False
Oregon        False
Texas         False
dtype: bool

In [32]: pd.notnull(obj4)
Out[32]:
California    False
Ohio           True
Oregon         True
Texas          True
dtype: bool
#Series也有类似的实例方法
In [33]: obj4.isnull()
Out[33]:
California     True
Ohio          False
Oregon        False
Texas         False
dtype: bool
```

对于许多应用而言， Series最重要的一个功能是， 它会根据运算的索引标签自动对齐数据：

```python
In [34]: obj3
Out[34]:
Ohio       3500
Texas      7100
Oregon    16000
Utah       5000
dtype: int64

In [35]: obj4
Out[35]:
California        NaN
Ohio           3500.0
Oregon        16000.0
Texas          7100.0
dtype: float64

In [36]: obj3+obj4
Out[36]:
California        NaN
Ohio           7000.0
Oregon        32000.0
Texas         14200.0
Utah              NaN
dtype: float64
```

Series对象本身及其索引都有一个name属性， 该属性跟pandas其他的关键功能关系非常密切：

```python
In [37]: obj4.name='population'

In [39]: obj4.index.name='state'

In [40]: obj4
Out[40]:
state
California        NaN
Ohio           3500.0
Oregon        16000.0
Texas          7100.0
Name: population, dtype: float64

In [41]:
```

Series的索引可以通过赋值的方式就地修改：

```python
In [41]: obj
Out[41]:
0    4
1    7
2   -5
3    3
dtype: int64

In [42]: obj.index=['Bob','Steve','Jeff','Ryan']

In [43]: obj
Out[43]:
Bob      4
Steve    7
Jeff    -5
Ryan     3
dtype: int64
```

### DataFrame

DataFrame是一个表格型的数据结构， 它含有一组有序的列， 每列可以是不同的值类型（数值、 字
符串、 布尔值等） 。 DataFrame既有行索引也有列索引， 它可以被看做由Series组成的字典（共用
同一个索引） 。 DataFrame中的数据是以一个或多个二维块存放的（而不是列表、 字典或别的一维
数据结构） 。

建DataFrame的办法有很多， 最常用的一种是直接传入一个由等长列表或NumPy数组组成的字
典：

```python
In [53]: data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada','Nevada'],'year':[2000,2001,
    ...: 2002,2001,2002,2003],'pop':[1.5,1.7,3.6,2.4,2.9,3.2]}

In [54]: fram=pd.DataFrame(data)

In [55]: fram
#结果DataFrame会自动加上索引（跟Series一样） ， 且全部列会被有序排列： 
Out[55]:
    state  year  pop
0    Ohio  2000  1.5
1    Ohio  2001  1.7
2    Ohio  2002  3.6
3  Nevada  2001  2.4
4  Nevada  2002  2.9
5  Nevada  2003  3.2
```

```python
#对于特别大的DataFrame， head方法会选取前五行：
In [56]: fram.head()
Out[56]:
    state  year  pop
0    Ohio  2000  1.5
1    Ohio  2001  1.7
2    Ohio  2002  3.6
3  Nevada  2001  2.4
4  Nevada  2002  2.9
#如果指定了列序列， 则DataFrame的列就会按照指定顺序进行排列： 

In [57]: pd.DataFrame(data,columns=['year','state','pop'])
Out[57]:
   year   state  pop
0  2000    Ohio  1.5
1  2001    Ohio  1.7
2  2002    Ohio  3.6
3  2001  Nevada  2.4
4  2002  Nevada  2.9
5  2003  Nevada  3.2
#如果传入的列在数据中找不到， 就会在结果中产生缺失值： 

In [58]: fram2=pd.DataFrame(data,columns=['year','state','pop','debt'],index=['one','two','
    ...: tree','four','five','six'])

In [59]: fram2
Out[59]:
      year   state  pop debt
one   2000    Ohio  1.5  NaN
two   2001    Ohio  1.7  NaN
tree  2002    Ohio  3.6  NaN
four  2001  Nevada  2.4  NaN
five  2002  Nevada  2.9  NaN
six   2003  Nevada  3.2  NaN
```

通过类似字典标记的方式或属性的方式， 可以将DataFrame的列获取为一个Series：

```python
In [61]: fram2['state']
Out[61]:
one       Ohio
two       Ohio
tree      Ohio
four    Nevada
five    Nevada
six     Nevada
Name: state, dtype: object

In [62]: fram2.year
Out[62]:
one     2000
two     2001
tree    2002
four    2001
five    2002
six     2003
Name: year, dtype: int64
```

笔记： IPython提供了类似属性的访问（即frame2.year） 和tab补全。 frame2[column]适用于
任何列的名， 但是frame2.column只有在列名是一个合理的Python变量名时才适用。

注意， 返回的Series拥有原DataFrame相同的索引， 且其name属性也已经被相应地设置好了。

行也可以通过位置或名称的方式进行获取， 比如用loc属性（稍后将对此进行详细讲解） ：

```python
In [64]: fram2.loc['tree']
Out[64]:
year     2002
state    Ohio
pop       3.6
debt      NaN
Name: tree, dtype: object
```

列可以通过赋值的方式进行修改。 例如， 我们可以给那个空的"debt"列赋上一个标量值或一组值：

```python
In [69]: fram2['debt']=16.5

In [70]: fram2
Out[70]:
      year   state  pop  debt
one   2000    Ohio  1.5  16.5
two   2001    Ohio  1.7  16.5
tree  2002    Ohio  3.6  16.5
four  2001  Nevada  2.4  16.5
five  2002  Nevada  2.9  16.5
six   2003  Nevada  3.2  16.5

In [71]: fram2['debt']=np.arange(6.)

In [72]: fram2
Out[72]:
      year   state  pop  debt
one   2000    Ohio  1.5   0.0
two   2001    Ohio  1.7   1.0
tree  2002    Ohio  3.6   2.0
four  2001  Nevada  2.4   3.0
five  2002  Nevada  2.9   4.0
six   2003  Nevada  3.2   5.0
```

将列表或数组赋值给某个列时， 其长度必须跟DataFrame的长度相匹配。 如果赋值的是一个
Series， 就会精确匹配DataFrame的索引， 所有的空位都将被填上缺失值：

```python
In [73]: val=pd.Series([-1.2,-1.5,-1.7],index=['two','four','five'])

In [74]: fram2['debt']=val

In [75]: fram2
Out[75]:
      year   state  pop  debt
one   2000    Ohio  1.5   NaN
two   2001    Ohio  1.7  -1.2
tree  2002    Ohio  3.6   NaN
four  2001  Nevada  2.4  -1.5
five  2002  Nevada  2.9  -1.7
six   2003  Nevada  3.2   NaN
#为不存在的列赋值会创建出一个新列。 
```

关键字del用于删除列:

```python
#创建一个新列
In [76]: fram2['eastern']=fram2.state=='Ohio'

In [77]: fram2
Out[77]:
      year   state  pop  debt  eastern
one   2000    Ohio  1.5   NaN     True
two   2001    Ohio  1.7  -1.2     True
tree  2002    Ohio  3.6   NaN     True
four  2001  Nevada  2.4  -1.5    False
five  2002  Nevada  2.9  -1.7    False
six   2003  Nevada  3.2   NaN    False
#使用del删除列
In [79]: del fram2['eastern']

In [80]: fram2.columns
Out[80]: Index(['year', 'state', 'pop', 'debt'], dtype='object')
```

注意： 通过索引方式返回的列只是相应数据的视图而已， 并不是副本。 因此， 对返回的
Series所做的任何就地修改全都会反映到源DataFrame上。 通过Series的copy方法即可指定
复制列。

另一种常见的数据形式是嵌套字典：

```python
In [81]: pop={'Nevada':{2001:2.4,2002:2.9},'Ohio':{2000:1.5,2001:1.7,2002:3.6}}

In [82]: fram3=pd.DataFrame(pop)
#如果嵌套字典传给DataFrame， pandas就会被解释为： 外层字典的键作为列， 内层键则作为行索
引： 

In [83]: fram3
Out[83]:
      Nevada  Ohio
2001     2.4   1.7
2002     2.9   3.6
2000     NaN   1.5
```

你也可以使用类似NumPy数组的方法， 对DataFrame进行转置（交换行和列） ：

```python
In [84]: fram3.T
Out[84]:
        2001  2002  2000
Nevada   2.4   2.9   NaN
Ohio     1.7   3.6   1.5
```

内层字典的键会被合并、 排序以形成最终的索引。 如果明确指定了索引， 则不会这样:

```python
In [85]: pd.DataFrame(pop,index=[2001,2002,2003])
Out[85]:
      Nevada  Ohio
2001     2.4   1.7
2002     2.9   3.6
2003     NaN   NaN
```

由Series组成的字典差不多也是一样的用法：

```python
In [88]: pdata={'Ohio':fram3['Ohio'][:-1],'Nevada':fram3['Nevada'][:2]}

In [89]: pd.DataFrame(pdata)
Out[89]:
      Ohio  Nevada
2001   1.7     2.4
2002   3.6     2.9
```

下面列出了DataFrame构造函数所能接受的各种数据:



![](D:\home\markdown-notebook\assets\WEBRESOURCEdac743189541c0a9d5091975c9e54e42.png)
如果设置了DataFrame的index和columns的name属性， 则这些信息也会被显示出来：

```python
In [90]: fram3.index.name='year';fram3.columns.name='state'

In [91]: fram3
Out[91]:
state  Nevada  Ohio
year
2001      2.4   1.7
2002      2.9   3.6
2000      NaN   1.5
```

如果DataFrame各列的数据类型不同， 则值数组的dtype就会选用能兼容所有列的数据类型：

```python
In [92]: fram2.values
Out[92]:
array([[2000, 'Ohio', 1.5, nan],
       [2001, 'Ohio', 1.7, -1.2],
       [2002, 'Ohio', 3.6, nan],
       [2001, 'Nevada', 2.4, -1.5],
       [2002, 'Nevada', 2.9, -1.7],
       [2003, 'Nevada', 3.2, nan]], dtype=object)
```

### 索引对象

pandas的索引对象负责管理轴标签和其他元数据（比如轴名称等） 。 构建Series或DataFrame
时， 所用到的任何数组或其他序列的标签都会被转换成一个Index：

```python
In [93]: obj=pd.Series(range(3),index=['a','b','c'])

In [94]: index=obj.index

In [95]: index
Out[95]: Index(['a', 'b', 'c'], dtype='object')

In [96]: index[1:]
Out[96]: Index(['b', 'c'], dtype='object')

In [97]: #index对象是不可变的，因此用户不能对其进行修改

In [98]: index[1]='d'
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Input In [98], in <cell line: 1>()
----> 1 index[1]='d'

File ~\anaconda3\lib\site-packages\pandas\core\indexes\base.py:5021, in Index.__setitem__(self, key, value)
   5019 @final
   5020 def __setitem__(self, key, value):
-> 5021     raise TypeError("Index does not support mutable operations")

TypeError: Index does not support mutable operations

In [99]: #不可变可以使index对象在多个数据结构之间安全共享

In [100]: labels=pd.Index(np.arange(3))

In [101]: labels
Out[101]: Int64Index([0, 1, 2], dtype='int64')

In [102]: obj2=pd.Series([1.5,-2.5,0],index=labels)

In [103]: obj2
Out[103]:
0    1.5
1   -2.5
2    0.0
dtype: float64

In [104]: obj2.index is labels
Out[104]: True
```

除了类似于数组， Index的功能也类似一个固定大小的集合：

```python
In [105]: fram3
Out[105]:
state  Nevada  Ohio
year
2001      2.4   1.7
2002      2.9   3.6
2000      NaN   1.5

In [106]: fram3.columns
Out[106]: Index(['Nevada', 'Ohio'], dtype='object', name='state')

In [107]: 'Ohio' in fram3.columns
Out[107]: True

In [108]: 2003 in fram3.index
Out[108]: False

In [109]: #与python的集合不同，pandas的Index可以包含重复的标签

In [110]: dup_labels=pd.Index(['foo','foo','bar','bar'])

In [111]: dup_labels
Out[111]: Index(['foo', 'foo', 'bar', 'bar'], dtype='object')
#选择重复的标签， 会显示所有的结果。
```

每个索引都有一些方法和属性， 它们可用于设置逻辑并回答有关该索引所包含的数据的常见问题。



![](D:\home\markdown-notebook\assets\WEBRESOURCEa23833f5d6de120bc6f49342681df461.png)
## 基本功能

下面介绍操作Series和DataFrame中的数据的基本手段。

### 重新索引

pandas对象的一个重要方法是reindex， 其作用是创建一个新对象， 它的数据符合新的索引。 看下
面的例子：

```python
In [5]: obj=pd.Series([4.5,7.2,-5.3,3.6],index=['d','b','a','c'])

In [6]: obj
Out[6]:
d    4.5
b    7.2
a   -5.3
c    3.6
dtype: float64
#用该Series的reindex将会根据新索引进行重排。 如果某个索引值当前不存在， 就引入缺失值 

In [7]: obj2=obj.reindex(['a','b','c','d','e'])

In [8]: obj2
Out[8]:
a   -5.3
b    7.2
c    3.6
d    4.5
e    NaN
dtype: float64
```

对于时间序列这样的有序数据， 重新索引时可能需要做一些插值处理。 method选项即可达到此目
的， 例如， 使用ffill可以实现前向值填充：

```python
In [9]: obj3=pd.Series(['blue','purple','yellow'],index=[0,2,4])

In [10]: obj3
Out[10]:
0      blue
2    purple
4    yellow
dtype: object

In [11]: obj3.reindex(range(6),method='ffill')    #在索引中间插入了项
Out[11]:
0      blue
1      blue
2    purple
3    purple
4    yellow
5    yellow
dtype: object
```

借助DataFrame， reindex可以修改（行） 索引和列。 只传递一个序列时， 会重新索引结果的行：

```python
In [17]: frame=pd.DataFrame(np.arange(9).reshape((3,3)),index=['a','b','d'],columns=['O
    ...: hio','Texas','California'])

In [18]: frame
Out[18]:
   Ohio  Texas  California
a     0      1           2
b     3      4           5
d     6      7           8

In [19]: frame2=frame.reindex(['a','b','c','d'])

In [20]: frame2
Out[20]:
   Ohio  Texas  California
a   0.0    1.0         2.0
b   3.0    4.0         5.0
c   NaN    NaN         NaN
d   6.0    7.0         8.0

In [21]: #列可以用columns关键字重新索引

In [22]: states=['Texas','Utah','California']

In [23]: frame.reindex(columns=states)
Out[23]:
   Texas  Utah  California
a      1   NaN           2
b      4   NaN           5
d      7   NaN           8
```



![](D:\home\markdown-notebook\assets\WEBRESOURCE7909ee038f262c94e9b5c575b64ef708.png)
### 丢弃指定轴上的项

丢弃某条轴上的一个或多个项很简单， 只要有一个索引数组或列表即可。 由于需要执行一些数据整
理和集合逻辑， 所以drop方法返回的是一个在指定轴上删除了指定值的新对象：

```python
In [24]: obj=pd.Series(np.arange(5.),index=['a','b','c','d','e'])

In [25]: obj
Out[25]:
a    0.0
b    1.0
c    2.0
d    3.0
e    4.0
dtype: float64

In [26]: new_obj=obj.drop('c')

In [27]: new_obj
Out[27]:
a    0.0
b    1.0
d    3.0
e    4.0
dtype: float64

In [28]: obj.drop(['d','c'])
Out[28]:
a    0.0
b    1.0
e    4.0
dtype: float64
```

对于DataFrame， 可以删除任意轴上的索引值。 

```python
In [29]: data=pd.DataFrame(np.arange(16).reshape((4,4)),index=['Ohio','Colorado','Utah'
    ...: ,'New York'],columns=['one','two','three','four'])

In [30]: data
Out[30]:
          one  two  three  four
Ohio        0    1      2     3
Colorado    4    5      6     7
Utah        8    9     10    11
New York   12   13     14    15

In [31]: #用标签调用drop会从行标签(axis0)删除值

In [32]: data.drop(['Colorado','Ohio'])
Out[32]:
          one  two  three  four
Utah        8    9     10    11
New York   12   13     14    15

In [33]: #通过传递axis=1或axis='columns'可以删除列的值

In [34]: data.drop('two',axis=1)
Out[34]:
          one  three  four
Ohio        0      2     3
Colorado    4      6     7
Utah        8     10    11
New York   12     14    15

In [35]: data.drop(['two','four'],axis='columns')
Out[35]:
          one  three
Ohio        0      2
Colorado    4      6
Utah        8     10
New York   12     14

In [36]: #许多函数，如drop，会修改Series或DataFrame的大小或形状，可以就地修改对象，不会
    ...: 返回新的对象

In [37]: obj.drop('c',inplace=True)

In [38]: obj
Out[38]:
a    0.0
b    1.0
d    3.0
e    4.0
dtype: float64
```

小心使用inplace， 它会销毁所有被删除的数据。

### 索引、 选取和过滤

Series索引（obj[...]） 的工作方式类似于NumPy数组的索引， 只不过Series的索引值不只是整数。
下面是几个例子：

```python
In [3]: obj=pd.Series(np.arange(4.),index=['a','b','c','d'])

In [4]: obj
Out[4]:
a    0.0
b    1.0
c    2.0
d    3.0
dtype: float64

In [5]: obj['b']
Out[5]: 1.0

In [6]: obj[1]
Out[6]: 1.0

In [7]: obj[2:4]
Out[7]:
c    2.0
d    3.0
dtype: float64

In [8]: obj[['b','a','d']]
Out[8]:
b    1.0
a    0.0
d    3.0
dtype: float64

In [9]: obj[[1,3]]
Out[9]:
b    1.0
d    3.0
dtype: float64

In [10]: obj[obj>2]
Out[10]:
d    3.0
dtype: float64

In [11]: #利用标签的切片运算与普通的python切片运算不同，其末端是包含的

In [12]: obj['b':'c']
Out[12]:
b    1.0
c    2.0
dtype: float64

In [13]: #用切片可以对Series的相应部分进行设置

In [14]: obj['b':'c']=5

In [15]: obj
Out[15]:
a    0.0
b    5.0
c    5.0
d    3.0
dtype: float64
```

用一个值或序列对DataFrame进行索引其实就是获取一个或多个列：

```python
In [17]: data=pd.DataFrame(np.arange(16).reshape((4,4)),index=['Ohio','Colorado','U
    ...: tah','New York'],columns=['one','two','three','four'])

In [18]: data
Out[18]:
          one  two  three  four
Ohio        0    1      2     3
Colorado    4    5      6     7
Utah        8    9     10    11
New York   12   13     14    15

In [19]: data['two']
Out[19]:
Ohio         1
Colorado     5
Utah         9
New York    13
Name: two, dtype: int32
In [23]: data[['three','one']]
Out[23]:
          three  one
Ohio          2    0
Colorado      6    4
Utah         10    8
New York     14   12

In [24]: #特殊情况：通过切片或布尔型数组选取数据

In [25]: data[:2]
Out[25]:
          one  two  three  four
Ohio        0    1      2     3
Colorado    4    5      6     7

In [26]: data[data['three']>5]
Out[26]:
          one  two  three  four
Colorado    4    5      6     7
Utah        8    9     10    11
New York   12   13     14    15

In [27]: #选取行的语法data[:2]十分方便，向[]传递单一的元素或列表，就可选择列
```

另一种用法是通过布尔型DataFrame（比如下面这个由标量比较运算得出的） 进行索引：

```python
In [30]: data<5
Out[30]:
            one    two  three   four
Ohio       True   True   True   True
Colorado   True  False  False  False
Utah      False  False  False  False
New York  False  False  False  False

In [31]: data[data<5]=0

In [32]: data
Out[32]:
          one  two  three  four
Ohio        0    0      0     0
Colorado    0    5      6     7
Utah        8    9     10    11
New York   12   13     14    15
```

### 用loc和iloc进行选取

对于DataFrame的行的标签索引， 我引入了特殊的标签运算符loc和iloc。 它们可以让你用类似
NumPy的标记， 使用轴标签（loc） 或整数索引（iloc） ， 从DataFrame选择行和列的子集。

```python
In [34]: data.loc['Colorado',['two','three']]
Out[34]:
two      5
three    6
Name: Colorado, dtype: int32

In [35]: #用iloc和整数进行选取

In [36]: data.iloc[2,[3,0,1]]
Out[36]:
four    11
one      8
two      9
Name: Utah, dtype: int32

In [37]: data.iloc[2]
Out[37]:
one       8
two       9
three    10
four     11
Name: Utah, dtype: int32

In [38]: data.iloc[[1,2],[3,0,1]]
Out[38]:
          four  one  two
Colorado     7    0    5
Utah        11    8    9
```



![](D:\home\markdown-notebook\assets\WEBRESOURCEd71dc6f02251c6f4f410e201beba237e.png)
### 整数索引

在pandas对象中使用整数索引容易出错

```python
In [39]: ser=pd.Series(np.arange(3.))

In [40]: ser
Out[40]:
0    0.0
1    1.0
2    2.0
dtype: float64

In [41]: ser[-1]    #ser是整数索引，此代码引发错误
#######
In [43]: ser=pd.Series(np.arange(3.),index=['a','b','c'])

In [44]: ser[-1]    #此时ser不是整数索引，此代码正确
Out[44]: 2.0
```

为了进行统一， 如果轴索引含有整数， 数据选取总会使用标签。 为了更准确， 请使用loc（标签）
或iloc（整数） ：

```python
In [46]: ser=pd.Series(np.arange(3.))

In [47]: ser[:1]
Out[47]:
0    0.0
dtype: float64

In [48]: ser.loc[:1]
Out[48]:
0    0.0
1    1.0
dtype: float64

In [49]: ser.iloc[:1]
Out[49]:
0    0.0
dtype: float64
```

### 算术运算和数据对齐

pandas最重要的一个功能是， 它可以对不同索引的对象进行算术运算。 在将对象相加时， 如果存
在不同的索引对， 则结果的索引就是该索引对的并集。 

```python
In [3]: s1=pd.Series([7.3,-2.5,3.4,1.5],index=['a','c','d','e'])
In [5]: s2=pd.Series([-2.1,3.6,-1.5,4,3.1],index=['a','c','e','f','g'])
In [6]: s1
Out[6]:
a    7.3
c   -2.5
d    3.4
e    1.5
dtype: float64

In [7]: s2
Out[7]:
a   -2.1
c    3.6
e   -1.5
f    4.0
g    3.1
dtype: float64

In [8]: s1+s2
Out[8]:
a    5.2
c    1.1
d    NaN
e    0.0
f    NaN
g    NaN
dtype: float64
```

自动的数据对齐操作在不重叠的索引处引入了NA值。 缺失值会在算术运算过程中传播。


对于DataFrame， 对齐操作会同时发生在行和列上：

```python
In [9]: df1=pd.DataFrame(np.arange(9.).reshape((3,3)),columns=list('bcd'),index=['Ohio','Texas','Colorado'])

In [10]: df2=pd.DataFrame(np.arange(12.).reshape((4,3)),columns=list('bde'),index=['Utah','Ohio','Texas','Oregon'])

In [11]: df1
Out[11]:
            b    c    d
Ohio      0.0  1.0  2.0
Texas     3.0  4.0  5.0
Colorado  6.0  7.0  8.0

In [12]: df2
Out[12]:
          b     d     e
Utah    0.0   1.0   2.0
Ohio    3.0   4.0   5.0
Texas   6.0   7.0   8.0
Oregon  9.0  10.0  11.0

In [13]: #将df1与df2相加，结果的索引和列是原来的并集

In [14]: df1+df2
Out[14]:
            b   c     d   e
Colorado  NaN NaN   NaN NaN
Ohio      3.0 NaN   6.0 NaN
Oregon    NaN NaN   NaN NaN
Texas     9.0 NaN  12.0 NaN
Utah      NaN NaN   NaN NaN
```

如果DataFrame对象相加， 没有共用的列或行标签， 结果都会是空：

```python
In [15]: df1=pd.DataFrame({'A':[1,2]})

In [16]: df2=pd.DataFrame({'B':[3,4]})

In [17]: df1
Out[17]:
   A
0  1
1  2

In [18]: df2
Out[18]:
   B
0  3
1  4

In [19]: df1-df2
Out[19]:
    A   B
0 NaN NaN
1 NaN NaN
```

### 在算术方法中填充值

在对不同索引的对象进行算术运算时， 你可能希望当一个对象中某个轴标签在另一个对象中找不到
时填充一个特殊值（比如0） ：

```python
In [20]: df1=pd.DataFrame(np.arange(12.).reshape((3,4)),columns
    ...: =list('abcd'))

In [21]: df2=pd.DataFrame(np.arange(20.).reshape((4,5)),columns
    ...: =list('abcde'))

In [22]: df2.loc[1,'b']=np.nan

In [23]: df1
Out[23]:
     a    b     c     d
0  0.0  1.0   2.0   3.0
1  4.0  5.0   6.0   7.0
2  8.0  9.0  10.0  11.0

In [24]: df2
Out[24]:
      a     b     c     d     e
0   0.0   1.0   2.0   3.0   4.0
1   5.0   NaN   7.0   8.0   9.0
2  10.0  11.0  12.0  13.0  14.0
3  15.0  16.0  17.0  18.0  19.0

In [25]: df1+df2#没有重叠的位置会产生NA值
Out[25]:
      a     b     c     d   e
0   0.0   2.0   4.0   6.0 NaN
1   9.0   NaN  13.0  15.0 NaN
2  18.0  20.0  22.0  24.0 NaN
3   NaN   NaN   NaN   NaN NaN


In [27]: #使用df1的add方法，传入df2以及一个fill_value参数

In [28]: df1.add(df2,fill_value=0)
Out[28]:
      a     b     c     d     e
0   0.0   2.0   4.0   6.0   4.0
1   9.0   5.0  13.0  15.0   9.0
2  18.0  20.0  22.0  24.0  14.0
3  15.0  16.0  17.0  18.0  19.0
```

下表列出了Series和DataFrame的算术方法。 它们每个都有一个副本， 以字母r开头， 它会翻转参
数。 因此这两个语句是等价的：

```python
In [29]: 1/df1
Out[29]:
       a         b         c         d
0    inf  1.000000  0.500000  0.333333
1  0.250  0.200000  0.166667  0.142857
2  0.125  0.111111  0.100000  0.090909

In [30]: df1.rdiv(1)
Out[30]:
       a         b         c         d
0    inf  1.000000  0.500000  0.333333
1  0.250  0.200000  0.166667  0.142857
2  0.125  0.111111  0.100000  0.090909
```

![](D:\home\markdown-notebook\assets\WEBRESOURCE3268c8db46f6c3c0ec2e9ca08c817ac3.png)
与此类似， 在对Series或DataFrame重新索引时， 也可以指定一个填充值：

```python
In [31]: df1.reindex(columns=df2.columns,fill_val
    ...: ue=0)
Out[31]:
     a    b     c     d  e
0  0.0  1.0   2.0   3.0  0
1  4.0  5.0   6.0   7.0  0
2  8.0  9.0  10.0  11.0  0
```

### DataFrame和Series之间的运算

跟不同维度的NumPy数组一样， DataFrame和Series之间算术运算也是有明确规定的。 先来看一
个具有启发性的例子， 计算一个二维数组与其某行之间的差：

```python
In [32]: arr=np.arange(12.).reshape((3,4))

In [33]: arr
Out[33]:
array([[ 0.,  1.,  2.,  3.],
       [ 4.,  5.,  6.,  7.],
       [ 8.,  9., 10., 11.]])

In [34]: arr[0]
Out[34]: array([0., 1., 2., 3.])

In [35]: arr-arr[0]
Out[35]:
array([[0., 0., 0., 0.],
       [4., 4., 4., 4.],
       [8., 8., 8., 8.]])
```

当我们从arr减去arr[0]， 每一行都会执行这个操作。 

 DataFrame和Series之间的运算差不多也是如此：

```python
In [37]: frame=pd.DataFrame(np.arange(12.).reshape((4,3)),columns=list('
    ...: bde'),index=['Utah','Ohio','Texas','Oregon'])

In [38]: series=frame.iloc[0]

In [39]: frame
Out[39]:
          b     d     e
Utah    0.0   1.0   2.0
Ohio    3.0   4.0   5.0
Texas   6.0   7.0   8.0
Oregon  9.0  10.0  11.0

In [40]: series
Out[40]:
b    0.0
d    1.0
e    2.0
Name: Utah, dtype: float64

In [41]: #默认情况下，DataFrame和Series之间的算术运算会将Series的索引匹
    ...: 配到DataFrame的列，然后沿着行一直向下广播

In [42]: frame-series
Out[42]:
          b    d    e
Utah    0.0  0.0  0.0
Ohio    3.0  3.0  3.0
Texas   6.0  6.0  6.0
Oregon  9.0  9.0  9.0

In [43]: #如果某个索引值在DataFrame的列或Series的索引中找不到，则参与运
    ...: 算的两个对象就会被重新索引以形成并集

In [44]: series2=pd.Series(range(3),index=['b','e','f'])

In [45]: frame+series2    #元素级操作
Out[45]:
          b   d     e   f
Utah    0.0 NaN   3.0 NaN
Ohio    3.0 NaN   6.0 NaN
Texas   6.0 NaN   9.0 NaN
Oregon  9.0 NaN  12.0 NaN
```

如果你希望匹配行且在列上广播， 则必须使用算术运算方法。

```python
In [46]: series3=frame['d']

In [47]: frame
Out[47]:
          b     d     e
Utah    0.0   1.0   2.0
Ohio    3.0   4.0   5.0
Texas   6.0   7.0   8.0
Oregon  9.0  10.0  11.0

In [48]: series3
Out[48]:
Utah       1.0
Ohio       4.0
Texas      7.0
Oregon    10.0
Name: d, dtype: float64

In [49]: frame.sub(series3,axis='index')
Out[49]:
          b    d    e
Utah   -1.0  0.0  1.0
Ohio   -1.0  0.0  1.0
Texas  -1.0  0.0  1.0
Oregon -1.0  0.0  1.0
```

### 函数应用和映射

NumPy的ufuncs（元素级数组方法） 也可用于操作pandas对象：

```python
In [51]: frame=pd.DataFrame(np.random.randn(4,3),columns=list('bde'),ind
    ...: ex=['Utah','Ohio','Texas','Oregon'])

In [52]: frame
Out[52]:
               b         d         e
Utah    0.270258 -0.391507  0.803101
Ohio   -0.387573 -1.335139 -0.212660
Texas   0.671690  0.112527  0.807778
Oregon -0.525290 -0.391070 -0.128506

In [53]: np.abs(frame)
Out[53]:
               b         d         e
Utah    0.270258  0.391507  0.803101
Ohio    0.387573  1.335139  0.212660
Texas   0.671690  0.112527  0.807778
Oregon  0.525290  0.391070  0.128506
```

另一个常见的操作是， 将函数应用到由各列或行所形成的一维数组上。 DataFrame的apply方法即
可实现此功能：

```python
In [54]: f=lambda x:x.max()-x.min()

In [55]: frame.apply(f)
Out[55]:
b    1.196980
d    1.447666
e    1.020438
dtype: float64
```

这里的函数f， 计算了一个Series的最大值和最小值的差， 在frame的每列都执行了一次。 结果是一
个Series， 使用frame的列作为索引。

如果传递axis='columns'到apply， 这个函数会在每行执行：

```python
In [56]: frame.apply(f,axis='columns')
Out[56]:
Utah      1.194608
Ohio      1.122479
Texas     0.695251
Oregon    0.396784
dtype: float64
```

许多最为常见的数组统计功能都被实现成DataFrame的方法（如sum和mean） ， 因此无需使用
apply方法。

传递到apply的函数不是必须返回一个标量， 还可以返回由多个值组成的Series：

```python
In [57]: def f(x):
    ...:     return pd.Series([x.min(),x.max()],index=['min','max'])
    ...:

In [58]: frame.apply(f)
Out[58]:
           b         d         e
min -0.52529 -1.335139 -0.212660
max  0.67169  0.112527  0.807778
```

元素级的Python函数也是可以用的。 假如你想得到frame中各个浮点值的格式化字符串， 使用
applymap即可：

```python
In [60]: format1=lambda x:'%.2f' %x

In [61]: frame.applymap(format1)
Out[61]:
            b      d      e
Utah     0.27  -0.39   0.80
Ohio    -0.39  -1.34  -0.21
Texas    0.67   0.11   0.81
Oregon  -0.53  -0.39  -0.13
```

之所以叫做applymap， 是因为Series有一个用于应用元素级函数的map方法：

```python
In [64]: frame['e'].map(format1)
Out[64]:
Utah       0.80
Ohio      -0.21
Texas      0.81
Oregon    -0.13
Name: e, dtype: object
```

### 排序和排名

根据条件对数据集排序（sorting） 也是一种重要的内置运算。 要对行或列索引进行排序（按字典顺
序） ， 可使用sort_index方法， 它将返回一个已排序的新对象：

```python
In [67]: obj=pd.Series(range(4),index=['d','a','b','c'])

In [68]: obj.sort_index()
Out[68]:
a    1
b    2
c    3
d    0
dtype: int64
```

对于DataFrame， 则可以根据任意一个轴上的索引进行排序：

```python
In [71]: frame=pd.DataFrame(np.arange(8).reshape((2,4)),index=['three','
    ...: one'],columns=['d','a','b','c'])

In [72]: frame.sort_index()
Out[72]:
       d  a  b  c
one    4  5  6  7
three  0  1  2  3

In [73]: frame.sort_index(axis=1)
Out[73]:
       a  b  c  d
three  1  2  3  0
one    5  6  7  4

In [74]: #数据默认按升序排序，但也可以降序排序

In [75]: frame.sort_index(axis=1,ascending=False)
Out[75]:
       d  c  b  a
three  0  3  2  1
one    4  7  6  5
```

若要按值对Series进行排序， 可使用其sort_values方法：

```python
In [76]: obj=pd.Series([4,7,-3,2])

In [78]: obj.sort_values()
Out[78]:
2   -3
3    2
0    4
1    7
dtype: int64
```

在排序时， 任何缺失值默认都会被放到Series的末尾：

```python
In [79]: obj=pd.Series([4,np.nan,7,np.nan,-3,2])

In [80]: obj.sort_values()
Out[80]:
4   -3.0
5    2.0
0    4.0
2    7.0
1    NaN
3    NaN
dtype: float64
```

当排序一个DataFrame时， 你可能希望根据一个或多个列中的值进行排序。 将一个或多个列的名字
传递给sort_values的by选项即可达到该目的：

```python
In [81]: frame=pd.DataFrame({'b':[4,7,-3,2],'a':[0,1,0,1]})

In [82]: frame
Out[82]:
   b  a
0  4  0
1  7  1
2 -3  0
3  2  1

In [83]: frame.sort_values(by='b')
Out[83]:
   b  a
2 -3  0
3  2  1
0  4  0
1  7  1

In [84]: #要根据多个列进行排序，传入名称的列表即可

In [85]: frame.sort_values(by=['a','b'])
Out[85]:
   b  a
2 -3  0
0  4  0
3  2  1
1  7  1
#排名会从1开始一直到数组中有效数据的数量。 
```

接下来介绍Series和DataFrame的rank方法。 默认
情况下， rank是通过“为各组分配一个平均排名”的方式破坏平级关系的：

```python
In [86]: obj=pd.Series([7,-5,7,4,2,0,4])

In [87]: obj.rank()
Out[87]:
0    6.5
1    1.0
2    6.5
3    4.5
4    3.0
5    2.0
6    4.5
dtype: float64
```

也可以根据值在原数据中出现的顺序给出排名：

```python
In [89]: obj.rank(method='first')
Out[89]:
0    6.0
1    1.0
2    7.0
3    4.0
4    3.0
5    2.0
6    5.0
dtype: float64
```

这里， 条目0和2没有使用平均排名6.5， 它们被设成了6和7， 因为数据中标签0位于标签2的前面。

按降序进行排名：

```python
In [90]: #assign tie values the maximum rank in the group

In [91]: obj.rank(ascending=False,method='max')
Out[91]:
0    2.0
1    7.0
2    2.0
3    4.0
4    5.0
5    6.0
6    4.0
dtype: float64
```

DataFrame可以在行或列上计算排名：

```python
In [92]: frame=pd.DataFrame({'b':[4.3,7,-3,2],'a':[0,1,0,1],'c':[-2,5,8,
    ...: -2.5]})

In [93]: frame
Out[93]:
     b  a    c
0  4.3  0 -2.0
1  7.0  1  5.0
2 -3.0  0  8.0
3  2.0  1 -2.5

In [94]: frame.rank(axis='columns')
Out[94]:
     b    a    c
0  3.0  2.0  1.0
1  3.0  1.0  2.0
2  1.0  2.0  3.0
3  3.0  2.0  1.0
```



![](D:\home\markdown-notebook\assets\WEBRESOURCE5c320029c8580a5cc2856758fad77ff9.png)
### 带有重复标签的轴索引

直到目前为止， 我所介绍的所有范例都有着唯一的轴标签（索引值） 。 虽然许多pandas函数（如
reindex） 都要求标签唯一， 但这并不是强制性的。 我们来看看下面这个简单的带有重复索引值的
Series：

```python
In [95]: obj=pd.Series(range(5),index=['a','a','b','b','c'])

In [96]: obj
Out[96]:
a    0
a    1
b    2
b    3
c    4
dtype: int64

In [97]: #索引的is_unique属性可以告诉你它的值是否唯一

In [98]: obj.index.is_unique
Out[98]: False

In [99]: #对于带有重复值的索引，数据选取的行为将会有所不同。如果某个索引
    ...: 对应多个值，则返回一个Series;而对应单个值的，则返回一个标量值。
    ...:

In [100]: obj['a']
Out[100]:
a    0
a    1
dtype: int64

In [101]: obj['c']
Out[101]: 4
```

对DataFrame的行进行索引时也是如此：

```python
In [102]: df=pd.DataFrame(np.random.randn(4,3),index=['a','a','b','b'])

In [103]: df
Out[103]:
          0         1         2
a -1.509219 -0.136720  0.594205
a -0.598141 -1.025076  1.353398
b  0.331016 -1.458925  0.174889
b -1.533776  0.624465  2.085446

In [104]: df.loc['b']
Out[104]:
          0         1         2
b  0.331016 -1.458925  0.174889
b -1.533776  0.624465  2.085446
```

## 汇总和计算描述统计

pandas对象拥有一组常用的数学和统计方法。 它们大部分都属于约简和汇总统计， 用于从Series
中提取单个值（如sum或mean） 或从DataFrame的行或列中提取一个Series。 跟对应的NumPy数
组方法相比， 它们都是基于没有缺失数据的假设而构建的。 

```
In [4]: df=pd.DataFrame([[1.4,np.nan],[7.1,-4.5],[np.nan,np.nan]
   ...: ,[0.75,-1.3]],index=['a','b','c','d'],columns=['one','tw
   ...: o'])

In [5]: df
Out[5]:
    one  two
a  1.40  NaN
b  7.10 -4.5
c   NaN  NaN
d  0.75 -1.3

In [6]: #调用DataFrame的sum方法将会返回一个含有列的和的Series

In [7]: df.sum()
Out[7]:
one    9.25
two   -5.80
dtype: float64

In [8]: #传入axis='columns'或axis=1将会按行进行求和运算

In [9]: df.sum(axis=1)
Out[9]:
a    1.40
b    2.60
c    0.00
d   -0.55
dtype: float64

In [10]: #NA值将会自动被排除，除非整个切片都是NA。通过skipna选项
    ...: 可以禁用该功能

In [11]: df.mean(axis='columns',skipna=False)
Out[11]:
a      NaN
b    1.300
c      NaN
d   -0.275
dtype: float64
```

![](D:\home\markdown-notebook\assets\WEBRESOURCEd03e4cf37d819943832600aa4d56dccb.png)
有些方法（如idxmin和idxmax） 返回的是间接统计（比如达到最小值或最大值的索引） ：

```python
In [12]: df
Out[12]:
    one  two
a  1.40  NaN
b  7.10 -4.5
c   NaN  NaN
d  0.75 -1.3

In [13]: df.idxmax()
Out[13]:
one    b
two    d
dtype: object
```

另一些方法则是累计型的：

```python
In [14]: df
Out[14]:
    one  two
a  1.40  NaN
b  7.10 -4.5
c   NaN  NaN
d  0.75 -1.3

In [15]: df.cumsum()
Out[15]:
    one  two
a  1.40  NaN
b  8.50 -4.5
c   NaN  NaN
d  9.25 -5.8
```

还有一种方法， 它既不是约简型也不是累计型。 describe就是一个例子， 它用于一次性产生多个汇
总统计：

```python
In [16]: df
Out[16]:
    one  two
a  1.40  NaN
b  7.10 -4.5
c   NaN  NaN
d  0.75 -1.3

In [17]: df.describe()
Out[17]:
            one       two
count  3.000000  2.000000
mean   3.083333 -2.900000
std    3.493685  2.262742
min    0.750000 -4.500000
25%    1.075000 -3.700000
50%    1.400000 -2.900000
75%    4.250000 -2.100000
max    7.100000 -1.300000
In [18]: #对于非数值型数据，describe会产生另外一种汇总统计

In [19]: obj=pd.Series(['a','a','b','c']*4)

In [20]: obj.describe()
Out[20]:
count     16
unique     3
top        a
freq       8
dtype: object
```

![](D:\home\markdown-notebook\assets\WEBRESOURCE202c3489818b9fabe7be6584ced640bb.png)
### 相关系数与协方差(略)

### 唯一值、 值计数以及成员资格

还有一类方法可以从一维Series的值中抽取信息。 看下面的例子：

```python
In [11]: obj=pd.Series(['c','a','d','a','a','b','b','c''c']
    ...: )

In [12]: uniques=obj.unique()

In [13]: uniques
Out[13]: array(['c', 'a', 'd', 'b', 'cc'], dtype=object)
```

返回的唯一值是未排序的， 如果需要的话， 可以对结果再次进行排序（uniques.sort()） 。 相似
的， value_counts用于计算一个Series中各值出现的频率：

```python
In [16]: obj.value_counts()
Out[16]:
a     3
b     2
c     1
d     1
cc    1
dtype: int64
```

为了便于查看， 结果Series是按值频率降序排列的。 value_counts还是一个顶级pandas方法， 可
用于任何数组或序列：

```python
In [18]: pd.value_counts(obj.values,sort=False)
Out[18]:
c     1
a     3
d     1
b     2
cc    1
dtype: int64
```

isin用于判断矢量化集合的成员资格， 可用于过滤Series中或DataFrame列中数据的子集：

```python
In [19]: obj
Out[19]:
0     c
1     a
2     d
3     a
4     a
5     b
6     b
7    cc
dtype: object


In [21]: mask=obj.isin(['b','c'])

In [22]: mask
Out[22]:
0     True
1    False
2    False
3    False
4    False
5     True
6     True
7    False
dtype: bool

In [23]: obj[mask]
Out[23]:
0    c
5    b
6    b
dtype: object
```

与isin类似的是Index.get_indexer方法， 它可以给你一个索引数组， 从可能包含重复值的数组到另
一个不同值的数组：

```python
In [24]: to_match=pd.Series(['c','a','b','b','c','a'])

In [25]: unique_vals=pd.Series(['c','b','a'])

In [26]: pd.Index(unique_vals).get_indexer(to_match)
Out[26]: array([0, 2, 1, 1, 0, 2], dtype=int64)
```



![](D:\home\markdown-notebook\assets\WEBRESOURCEfeca2f9fa246004d4cb1a790520cc7be.png)
有时， 你可能希望得到DataFrame中多个相关列的一张柱状图。 例如：

```python
In [28]: data
Out[28]:
   Qu1  Qu2  Qu3
0    1    2    1
1    3    3    5
2    4    1    2
3    3    2    4
4    4    3    4

In [29]: result=data.apply(pd.value_counts).fillna(0)

In [30]: result
Out[30]:
   Qu1  Qu2  Qu3
1  1.0  1.0  1.0
2  0.0  2.0  1.0
3  2.0  2.0  0.0
4  2.0  0.0  2.0
5  0.0  0.0  1.0
```

这里， 结果中的行标签是所有列的唯一值。 后面的频率值是每个列中这些值的相应计数。

# 数据加载，存储与文件格式

## 读写文本格式的数据

pandas提供了一些用于将表格型数据读取为DataFrame对象的函数。 表6-1对它们进行了总结， 其
中read_csv和read_table可能会是你今后用得最多的。



![](D:\home\markdown-notebook\assets\WEBRESOURCEc305fee5db149e00158e42241d63d9c1.png)
这些函数的选项
可以划分为以下几个大类：

- 索引： 将一个或多个列当做返回的DataFrame处理， 以及是否从文件、 用户获取列名。


- 类型推断和数据转换： 包括用户定义值的转换、 和自定义的缺失值标记列表等。


- 日期解析： 包括组合功能， 比如将分散在多个列中的日期时间信息组合成结果中的单个列。


- 迭代： 支持对大文件进行逐块迭代。


- 不规整数据问题： 跳过一些行、 页脚、 注释或其他一些不重要的东西（比如由成千上万个逗号
隔开的数值数据） 。

首先我们来看一个以逗号分隔的（CSV） 文
本文件：

```
test\ex1.csv
a,b,c,d,message
1,2,3,4,hello
5,6,7,8,world
9,10,11,12,foo
```

由于该文件以逗号分隔， 所以我们可以使用read_csv将其读入一个DataFrame:

```python
In [5]: df=pd.read_csv('test/ex1.csv')

In [6]: df
Out[6]:
   a   b   c   d message
0  1   2   3   4   hello
1  5   6   7   8   world
2  9  10  11  12     foo
```

我们还可以使用read_table， 并指定分隔符：

```python
In [9]: pd.read_table('test/ex1.csv',sep=',')
Out[9]:
   a   b   c   d message
0  1   2   3   4   hello
1  5   6   7   8   world
2  9  10  11  12     foo
```

可以控制读入文件的标题行：

```
 test\ex2.csv
 1,2,3,4,hello
5,6,7,8,world
9,10,11,12,foo
```

读入该文件的办法有两个。 你可以让pandas为其分配默认的列名， 也可以自己定义列名：

```python
In [12]: pd.read_csv('test/ex1.csv',header=None)
Out[12]:
   0   1   2   3        4
0  a   b   c   d  message
1  1   2   3   4    hello
2  5   6   7   8    world
3  9  10  11  12      foo

In [13]: pd.read_csv('test/ex1.csv',names=['a','b','c','d
    ...: ','message'])
Out[13]:
   a   b   c   d  message
0  a   b   c   d  message
1  1   2   3   4    hello
2  5   6   7   8    world
3  9  10  11  12      foo
```

假设你希望将message列做成DataFrame的索引。 你可以明确表示要将该列放到索引4的位置上，
也可以通过index_col参数指定"message"：

```python
In [14]: names=['a','b','c','d','message']

In [15]: pd.read_csv('test/ex2.csv',names=names,index_col
    ...: ='message')
Out[15]:
         a   b   c   d
message
hello    1   2   3   4
world    5   6   7   8
foo      9  10  11  12
```

如果希望将多个列做成一个层次化索引， 只需传入由列编号或列名组成的列表即可：

```python
test\csv.mindex.csv
key1,key2,value1,value2
one,a,1,2
one,b,3,4
one,c,5,6
one,d,7,8
two,a,9,10
two,b,11,12
two,c,13,14
two,d,15,16
```

```python
In [16]: parsed=pd.read_csv('test/csv_mindex.csv',index_col=['key1','k
    ...: ey2'])

In [17]: parsed
Out[17]:
           value1  value2
key1 key2
one  a          1       2
     b          3       4
     c          5       6
     d          7       8
two  a          9      10
     b         11      12
     c         13      14
     d         15      16
```

有些情况下， 有些表格可能不是用固定的分隔符去分隔字段的（比如空白符或其它模式） 。 看看下
面这个文本文件

```
A B C
aaa   -0.264438 -1.026059 -0.619500
bbb 0.927272 0.302904 -0.032399
ccc -0.264273 -0.386314 -0.217601
ddd   -0.871858 -0.348382 1.100491
```

虽然可以手动对数据进行规整， 这里的字段是被数量不同的空白字符间隔开的。 这种情况下， 你可
以传递一个正则表达式作为read_table的分隔符。 可以用正则表达式表达为\s+(表示多次匹配任意空白字符)， 于是有：

```python
In [20]: result=pd.read_table('test/ex3.csv',sep='\s+')

In [21]: result
Out[21]:
            A         B         C
aaa -0.264438 -1.026059 -0.619500
bbb  0.927272  0.302904 -0.032399
ccc -0.264273 -0.386314 -0.217601
ddd -0.871858 -0.348382  1.100491
```

由于列名比数据行的数量少， 所以read_table推断第一列应该是DataFrame的索引.

你可以用skiprows跳过文件的第一行、 第三行和第四行：

```python
test\ex4.csv
# hey!
a,b,c,d,messageskui
# just wanted to make things more difficult for you
# who reads CSV files with computers, anyway?
1,2,3,4,hello
5,6,7,8,world
9,10,11,12,foo
```

```python
In [22]: pd.read_csv('test/ex4.csv',skiprows=[0,2,3])
Out[22]:
   a   b   c   d message
0  1   2   3   4   hello
1  5   6   7   8   world
2  9  10  11  12     foo
```

缺失值处理是文件解析任务中的一个重要组成部分。 缺失数据经常是要么没有（空字符串） ， 要么
用某个标记值表示。 默认情况下， pandas会用一组经常出现的标记值进行识别， 比如NA及
NULL:

```
test\ex5.csv
something,a,b,c,d,message
one,1,2,3,4,NA
two,5,6,,8,world
three,9,10,11,12,foo
```



```python
In [23]: result=pd.read_csv('test/ex5.csv')

In [24]: result
Out[24]:
  something  a   b     c   d message
0       one  1   2   3.0   4     NaN
1       two  5   6   NaN   8   world
2     three  9  10  11.0  12     foo

In [25]: pd.isnull(result)
Out[25]:
   something      a      b      c      d  message
0      False  False  False  False  False     True
1      False  False  False   True  False    False
2      False  False  False  False  False    False
```

na_values可以用一个列表或集合的字符串表示缺失值：

```python
In [31]: result=pd.read_csv('test/ex5.csv',na_values=['world'])

In [32]: result
Out[32]:
  something  a   b     c   d message
0       one  1   2   3.0   4     NaN
1       two  5   6   NaN   8     NaN
2     three  9  10  11.0  12     foo
```

字典的各列可以使用不同的NA标记值：

```python
In [33]: sentinels={'message':['foo','NA'],'something':['two']}

In [34]: pd.read_csv('test/ex5.csv',na_values=sentinels)
Out[34]:
  something  a   b     c   d message
0       one  1   2   3.0   4     NaN
1       NaN  5   6   NaN   8   world
2     three  9  10  11.0  12     NaN
```

表6-2列出了pandas.read_csv和pandas.read_table常用的选项:

![](D:\home\markdown-notebook\assets\WEBRESOURCEd4541a5b863afeae7d7bcb0e54f075b3.png)
![](D:\home\markdown-notebook\assets\WEBRESOURCE93fa6fccded31c6000b7ee588d076355.png)
![](D:\home\markdown-notebook\assets\WEBRESOURCEde16aa0cb63d08a4180302d4942f8951.png)
## 逐块读取文本文件

在处理很大的文件时， 或找出大文件中的参数集以便于后续处理时， 你可能只想读取文件的一小部
分或逐块对文件进行迭代。

```python
#在看大文件之前， 我们先设置pandas显示地更紧些：
In [3]: pd.options.display.max_rows=10

In [4]: result=pd.read_csv("test/ex6.csv")

In [5]: result
Out[5]:
           one       two     three      four key
0     0.467976 -0.038649 -0.295344 -1.824726   L
1    -0.358893  1.404453  0.704965 -0.200638   B
2    -0.501840  0.659254 -0.421691 -0.057688   G
3     0.204886  1.074134  1.388361 -0.982404   R
4     0.354628 -0.133116  0.283763 -0.837063   Q
...        ...       ...       ...       ...  ..
9995  2.311896 -0.417070 -1.409599 -0.515821   L
9996 -0.479893 -0.650419  0.745152 -0.646038   E
9997  0.523331  0.787112  0.486066  1.093156   K
9998 -0.362559  0.598894 -1.843201  0.887292   G
9999 -0.096376 -1.012999 -0.657431 -0.573315   0

[10000 rows x 5 columns]
#如果只想读取几行（避免读取整个文件） ， 通过nrows进行指定即可：
In [6]: pd.read_csv('test/ex6.csv',nrows=5)
Out[6]:
        one       two     three      four key
0  0.467976 -0.038649 -0.295344 -1.824726   L
1 -0.358893  1.404453  0.704965 -0.200638   B
2 -0.501840  0.659254 -0.421691 -0.057688   G
3  0.204886  1.074134  1.388361 -0.982404   R
4  0.354628 -0.133116  0.283763 -0.837063   Q
#要逐块读取文件， 可以指定chunksize（行数） ：
In [7]: chunker=pd.read_csv('test/ex6.csv',chunksize=1000)

In [8]: chunker
Out[8]: <pandas.io.parsers.readers.TextFileReader at 0x1f048958730>
#read_csv所返回的这个TextParser对象使你可以根据chunksize对文件进行逐块迭代。 
#比如说， 我们可以迭代处理ex6.csv， 将值计数聚合到"key"列中， 如下所示：
In [9]: tot=pd.Series([])
<ipython-input-9-68aa5c24f913>:1: FutureWarning: The default dtype for empty Series will be 'object' instead of 'float64' in a future version. Specify a dtype explicitly to silence this warning.
  tot=pd.Series([])

In [10]: for piece in chunker:
    ...:     tot=tot.add(piece['key'].value_counts(),fill_va
    ...: lue=0)
    ...:

In [11]: tot=tot.sort_values(ascending=False)

In [12]: tot[:10]
Out[12]:
E    368.0
X    364.0
L    346.0
O    343.0
Q    340.0
M    338.0
J    337.0
F    335.0
K    334.0
H    330.0
dtype: float64
#TextParser还有一个get_chunk方法， 它使你可以读取任意大小的块
```

### 将数据写出到文本格式

数据也可以被输出为分隔符格式的文本。 我们再来看看之前读过的一个CSV文件：

```python
In [9]: #读取一个CSV文件

In [10]: data=pd.read_csv("test/ex5.csv")

In [11]: data
Out[11]:
  something  a   b     c   d message
0       one  1   2   3.0   4     NaN
1       two  5   6   NaN   8   world
2     three  9  10  11.0  12     foo
#利用DataFrame的to_csv方法，将数据写入到一个以逗号分隔的文件中 

In [12]: data.to_csv("test/out.csv")

In [13]: !type test\\out.csv
,something,a,b,c,d,message
0,one,1,2,3.0,4,
1,two,5,6,,8,world
2,three,9,10,11.0,12,foo
#也可以使用其他的分隔符 

In [14]: import sys

In [15]: data.to_csv(sys.stdout,sep='|')
|something|a|b|c|d|message
0|one|1|2|3.0|4|
1|two|5|6||8|world
2|three|9|10|11.0|12|foo
#缺失值在输出结果中会被表示为空字符，你可以希望将其表示为别的标记值 

In [16]: data.to_csv(sys.stdout,na_rep='NULL')
,something,a,b,c,d,message
0,one,1,2,3.0,4,NULL
1,two,5,6,NULL,8,world
2,three,9,10,11.0,12,foo
#如果没有设置其他选项，则会写出行和列的标签。也可以禁用: 

In [17]: data.to_csv(sys.stdout,index=False,header=False)
one,1,2,3.0,4,
two,5,6,,8,world
three,9,10,11.0,12,foo
#可以写出一部分的列，并以你指定的顺序排列 

In [18]: data.to_csv(sys.stdout,index=False,columns=['a','b','c'])
a,b,c
1,2,3.0
5,6,
9,10,11.0
```

Series也有一个to_csv方法：

```python
In [19]: dates=pd.date_range('1/1/2000',periods=7)

In [20]: ts=pd.Series(np.arange(7),index=dates)

In [21]: ts.to_csv("test/tseries.csv")

In [22]: !type test\\tseries.csv
,0
2000-01-01,0
2000-01-02,1
2000-01-03,2
2000-01-04,3
2000-01-05,4
2000-01-06,5
2000-01-07,6
```

### 处理分隔符格式

大部分存储在磁盘上的表格型数据都能用pandas.read_table进行加载。 然而， 有时还是需要做一
些手工处理。 由于接收到含有畸形行的文件而使read_table出毛病的情况并不少见。 为了说明这些
基本工具， 看看下面这个简单的CSV文件：

```python
In [28]: !type test\\ex7.csv
"a","b","c"
"1","2","3"
"1","2","3"
```

对于任何单字符分隔符文件， 可以直接使用Python内置的csv模块。 将任意已打开的文件或文件型
的对象传给csv.reader：

```python
import csv 
f=open('ex7.csv')
reader=csv.reader(f)
#对这个reader进行迭代
将会为每行产生一个元组（并移除了所有的引号):
for line in reader:
    print(line)
['a', 'b', 'c']
['1', '2', '3']
['1', '2', '3']
#现在， 为了使数据格式合乎要求， 你需要对其做一些整理工作。 
#首先， 读取文
件到一个多行的列表中：
with open("ex7.csv") as f:
    lines=list(csv.reader(f))
#然后， 我们将这些行分为标题行和数据行:
header,values=lines[0],lines[1:]
#然后， 我们可以用字典构造式和zip(*values)， 后者将行转置为列， 创建数据列的字典：
data_dict={h:v for h,v in zip(header,zip(*values))}
data_dict
{'a': ('1', '1'), 'b': ('2', '2'), 'c': ('3', '3')}
```

CSV文件的形式有很多。 只需定义csv.Dialect的一个子类即可定义出新格式（如专门的分隔符、 字
符串引用约定、 行结束符等） ：

```python
class my_dialect(csv.Dialect):
    lineterminator='\n'
    delimiter=';'
    quotechar='"'
    quoting=csv.QUOTE_MINIMAL
reader=csv.reader(f,dialect=my_dialect)
```

各个CSV语支的参数也可以用关键字的形式提供给csv.reader， 而无需定义子类：


```python
reader = csv.reader(f, delimiter='|')
```

可用的选项（csv.Dialect的属性） 及其功能如表所示：

![](D:\home\markdown-notebook\assets\WEBRESOURCE45a10370110e16ecb139dfd860277df8.png)
对于那些使用复杂分隔符或多字符分隔符的文件， csv模块就无能为力了。 这种情况
下， 你就只能使用字符串的split方法或正则表达式方法re.split进行行拆分和其他整理工作
了

要手工输出分隔符文件， 你可以使用csv.writer。 它接受一个已打开且可写的文件对象以及跟
csv.reader相同的那些语支和格式化选项：

```python
with open('mydata.csv','w') as f:
    writer=csv.writer(f,dialect=my_dialect)
    writer.writerow(('one','two','three'))
    writer.writerow(('1','2','3'))
    writer.writerow(('4','5','6'))
```

### JSON数据

JSON（JavaScript Object Notation的简称） 已经成为通过HTTP请求在Web浏览器和其他应用程
序之间发送数据的标准格式之一。 它是一种比表格型文本格式（如CSV） 灵活得多的数据格式。


下面是一个例子：

```python
obj = """
{"name": "Wes",
"places_lived": ["United States", "Spain", "Germany"],
"pet": null,
"siblings": [{"name": "Scott", "age": 30, "pets": ["Zeus", "Zuko"]},
             {"name": "Katie", "age": 38,
             "pets": ["Sixes", "Stache", "Cisco"]}]
} "
""
```

除其空值null和一些其他的细微差别（如列表末尾不允许存在多余的逗号） 之外， JSON非常接近
于有效的Python代码。 基本类型有对象（字典） 、 数组（列表） 、 字符串、 数值、 布尔值以及
null。 对象中所有的键都必须是字符串。 许多Python库都可以读写JSON数据。 我将使用json， 因
为它是构建于Python标准库中的。 通过json.loads即可将JSON字符串转换成Python形式：

```python
import json
result=json.loads(obj)    #loads而不是load
result
{'name': 'Wes',
 'places_lived': ['United States', 'Spain', 'Germany'],
 'pet': None,
 'siblings': [{'name': 'Scott', 'age': 30, 'pets': ['Zeus', 'Zuko']},
  {'name': 'Katie', 'age': 38, 'pets': ['Sixes', 'Stache', 'Cisco']}]}
​
```

json.dumps则将Python对象转换成JSON格式：


```python
asjson=json.dumps(result)
```

如何将（一个或一组） JSON对象转换为DataFrame或其他便于分析的数据结构就由你决定了。 最
简单方便的方式是： 向DataFrame构造器传入一个字典的列表（就是原先的JSON对象） ， 并选取
数据字段的子集：

```python
siblings=pd.DataFrame(result['siblings'],columns=['name','age'])
siblings
	name	age
0	Scott	30
1	Katie	38
```

pandas.read_json可以自动将特别格式的JSON数据集转换为Series或DataFrame。 例如：


```python
!type example.json
[{"a": 1, "b": 2, "c": 3},
 {"a": 4, "b": 5, "c": 6},
 {"a": 7, "b": 8, "c": 9}]
#pandas.read_json的默认选项假设JSON数组中的每个对象是表格中的一行：
data=pd.read_json('example.json')
data
	a	b	c
0	1	2	3
1	4	5	6
2	7	8	9
```

如果你需要将数据从pandas输出到JSON， 可以使用to_json方法：


```python
print(data.to_json())
{"a":{"0":1,"1":4,"2":7},"b":{"0":2,"1":5,"2":8},"c":{"0":3,"1":6,"2":9}}
print(data.to_json(orient='records'))
[{"a":1,"b":2,"c":3},{"a":4,"b":5,"c":6},{"a":7,"b":8,"c":9}]
```

### 利用lxml.objectify解析XML

XML（Extensible Markup Language） 是另一种常见的支持分层、 嵌套数据以及元数据的结构化数
据格式。

前面， 我介绍了pandas.read_html函数， 它可以使用lxml或Beautiful Soup从HTML解析数据。
XML和HTML的结构很相似， 但XML更为通用。 这里， 我会用一个例子演示如何利用lxml从XML格
式解析数据:

```python
#我们先用lxml.objectify解析该文件， 然后通过getroot得到该XML文件的根节点的引用：
In [8]: from lxml import objectify

In [9]: path="test/datasets/mta_perf/Performance_MNR.xml"

In [10]: parsed=objectify.parse(open(path))

In [11]: root=parsed.getroot()
#root.INDICATOR返回一个用于产生各个XML元素的生成器。
#对于每条记录， 我们可以用标记名
（如YTD_ACTUAL） 和数据值填充一个字典（排除几个标记） ： 

In [12]: data=[]

In [13]: skip_fields=['PARENT_SEQ','INDICATOR_SEQ','DESIRED_CH
    ...: ANGE','DECIMAL_PLACES']

In [14]: for elt in root.INDICATOR:
    ...:     el_data={}
    ...:     for child in elt.getchildren():
    ...:         if child.tag in skip_fields:
    ...:             continue
    ...:         el_data[child.tag]=child.pyval
    ...:     data.append(el_data)
    ...:
#最后， 将这组字典转换为一个DataFrame：     

In [15]: perf=pd.DataFrame(data)

In [16]: perf.head()
Out[16]:
            AGENCY_NAME  ... MONTHLY_ACTUAL
0  Metro-North Railroad  ...           96.9
1  Metro-North Railroad  ...           95.0
2  Metro-North Railroad  ...           96.9
3  Metro-North Railroad  ...           98.3
4  Metro-North Railroad  ...           95.8

[5 rows x 12 columns]
```

## 二进制数据格式


实现数据的高效二进制格式存储最简单的办法之一是使用Python内置的pickle序列化。 pandas对象
都有一个用于将数据以pickle格式保存到磁盘上的to_pickle方法

```python
In [17]: frame=pd.read_csv("test/ex1.csv")

In [18]: frame
Out[18]:
   a   b   c   d message
0  1   2   3   4   hello
1  5   6   7   8   world
2  9  10  11  12     foo

In [19]: frame.to_pickle("test/frame_pickle")
#你可以通过pickle直接读取被pickle化的数据， 或是使用更为方便的pandas.read_pickle：
 

In [20]: pd.read_pickle("test/frame_pickle")
Out[20]:
   a   b   c   d message
0  1   2   3   4   hello
1  5   6   7   8   world
2  9  10  11  12     foo
"""
注意： pickle仅建议用于短期存储格式。 其原因是很难保证该格式永远是稳定的； 今天pickle
的对象可能无法被后续版本的库unpickle出来。 虽然我尽力保证这种事情不会发生在pandas
中， 但是今后的某个时候说不定还是得“打破”该pickle格式。
"""
```

pandas内置支持两个二进制数据格式： HDF5和MessagePack。 

### 使用HDF5格式

HDF5是一种存储大规模科学数组数据的非常好的文件格式。 它可以被作为C标准库， 带有许多语
言的接口， 如Java、 Python和MATLAB等。 HDF5中的HDF指的是层次型数据格式（hierarchical
 data format） 。 每个HDF5文件都含有一个文件系统式的节点结构， 它使你能够存储多个数据集并
支持元数据。 与其他简单格式相比， HDF5支持多种压缩器的即时压缩， 还能更高效地存储重复模
式数据。 对于那些非常大的无法直接放入内存的数据集， HDF5就是不错的选择， 因为它可以高效
地分块读写。

虽然可以用PyTables或h5py库直接访问HDF5文件， pandas提供了更为高级的接口， 可以简化存
储Series和DataFrame对象。 HDFStore类可以像字典一样， 处理低级的细节：

```python
In [21]: frame=pd.DataFrame({'a':np.random.randn(100)})

In [22]: store=pd.HDFStore("mydaya.h5")

In [23]: store['obj1']=frame

In [24]: store['obj1_col']=frame['a']

In [25]: store
Out[25]:
<class 'pandas.io.pytables.HDFStore'>
File path: mydaya.h5
#HDF5文件中的对象可以通过与字典一样的API进行获取： 

In [27]: store['obj1']
Out[27]:
           a
0  -1.898381
1   1.217265
2   0.686839
3   0.153487
4  -0.395246
..       ...
95 -1.297047
96 -0.351135
97 -0.374818
98 -0.978988
99 -0.443000

[100 rows x 1 columns]
#HDFStore支持两种存储模式， 'fixed'和'table'。 后者通常会更慢， 但是支持使用特殊语法进行查询
操作:
#put是store['obj2'] = frame方法的显示版本， 允许我们设置其它的选项， 比如格式。 

In [28]: store.put('obj2',frame,format='table')

In [29]: store.select('obj2',where=['index >= 10 and index <=
    ...: 15'])
Out[29]:
           a
10  0.382608
11  1.313928
12  1.076195
13  0.354589
14  1.332309
15  0.827173

In [30]: store.close()
#pandas.read_hdf函数可以快捷使用这些工具：
 

In [31]: frame.to_hdf("mydata.h5",'obj3',format='table')

In [32]: pd.read_hdf('mydata.h5','obj3',where=['index<5'])
Out[32]:
          a
0 -1.898381
1  1.217265
2  0.686839
3  0.153487
4 -0.395246
```

如果需要本地处理海量数据， 我建议你好好研究一下PyTables和h5py， 看看它们能满足你的哪些
需求。 。 由于许多数据分析问题都是IO密集型（而不是CPU密集型） ， 利用HDF5这样的工具能显
著提升应用程序的效率。

注意： HDF5不是数据库。 它最适合用作“一次写多次读”的数据集。 虽然数据可以在任何时候
被添加到文件中， 但如果同时发生多个写操作， 文件就可能会被破坏。

### 读取Microsoft Excel文件


pandas的ExcelFile类或pandas.read_excel函数支持读取存储在Excel 2003（或更高版本） 中的表
格型数据。 这两个工具分别使用扩展包xlrd和openpyxl读取XLS和XLSX文件。 你可以用pip或
conda安装它们。

```python
#读写大型文件时，使用ExceFile
In [37]: frame=pd.read_excel("test/ex1.xlsx",'Sheet1')

In [38]: frame
Out[38]:
   Unnamed: 0  a   b   c   d message
0           0  1   2   3   4   hello
1           1  5   6   7   8   world
2           2  9  10  11  12     foo
#如果要将pandas数据写入为Excel格式， 你必须首先创建一个ExcelWriter， 然后使用pandas对象
的to_excel方法将数据写入到其中 

In [39]: writer=pd.ExcelWriter("ex2.xlsx")

In [40]: frame.to_excel(writer,'Sheet1')

In [41]: writer.save()
#你还可以不使用ExcelWriter， 而是传递文件的路径到to_excel：
 

In [42]: frame.to_excel('ex2.xlsx')
```

### Web APIs交互


许多网站都有一些通过JSON或其他格式提供数据的公共API。 通过Python访问这些API的办法有不
少。 一个简单易用的办法（推荐） 是requests包 。


为了搜索最新的30个GitHub上的pandas主题， 我们可以发一个HTTP GET请求， 使用requests扩
展库：

```python
In [1]: import requests

In [2]: url='https://api.github.com/repos/pandas-dev/pandas/i
   ...: ssues'

In [3]: resp=requests.get(url)

In [4]: resp
Out[4]: <Response [200]>
#响应对象的json方法会返回一个包含被解析过的JSON字典， 加载到一个Python对象中：
 

In [5]: data=resp.json()

In [6]: data[0]['title']
Out[6]: 'ENH: '
#data中的每个元素都是一个包含所有GitHub主题页数据（不包含评论） 的字典。 我们可以直接传
递数据到DataFrame， 并提取感兴趣的字段： 

In [7]: import pandas as pd
   ...: import numpy as np

In [8]: issues=pd.DataFrame(data,columns=['number','title','l
   ...: abels','state'])

In [9]: issues
Out[9]:
    number  ... state
0    47815  ...  open
1    47814  ...  open
2    47813  ...  open
3    47812  ...  open
4    47811  ...  open
5    47810  ...  open
6    47809  ...  open
7    47808  ...  open
8    47807  ...  open
9    47806  ...  open
10   47805  ...  open
11   47804  ...  open
12   47803  ...  open
13   47802  ...  open
14   47801  ...  open
15   47800  ...  open
16   47799  ...  open
17   47798  ...  open
18   47797  ...  open
19   47796  ...  open
20   47794  ...  open
21   47793  ...  open
22   47791  ...  open
23   47790  ...  open
24   47789  ...  open
25   47787  ...  open
26   47786  ...  open
27   47785  ...  open
28   47782  ...  open
29   47781  ...  open

[30 rows x 4 columns]
```

