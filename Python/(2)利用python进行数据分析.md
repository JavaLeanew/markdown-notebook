# 数据清洗和准备

## 处理缺失数据

在许多数据分析工作中， 缺失数据是经常发生的。 pandas的目标之一就是尽量轻松地处理缺失数
据。 例如， pandas对象的所有描述性统计默认都不包括缺失数据。

缺失数据在pandas中呈现的方式有些不完美， 但对于大多数用户可以保证功能正常。 对于数值数
据， pandas使用浮点值NaN（Not a Number） 表示缺失数据。 我们称其为哨兵值， 可以方便的检
测出来：

```python
In [10]: string_data=pd.Series(['aardvark','artichoke',np.nan
    ...: ,'avocado'])

In [11]: string_data
Out[11]:
0     aardvark
1    artichoke
2          NaN
3      avocado
dtype: object

In [12]: string_data.isnull()
Out[12]:
0    False
1    False
2     True
3    False
dtype: bool
```

Python内置的None值在对象数组中也可以作为NA：


```python
In [14]: string_data[0]=None

In [15]: string_data.isnull()
Out[15]:
0     True
1    False
2     True
3    False
dtype: bool
```

pandas项目中还在不断优化内部细节以更好处理缺失数据， 像用户API功能， 例如pandas.isnull：

![](D:\home\markdown-notebook\assets\WEBRESOURCE579ea3a7e6c3759c3146792fada9bd00.png)
### 滤除缺失数据

过滤掉缺失数据的办法有很多种。 你可以通过pandas.isnull或布尔索引的手工方法， 但dropna可能
会更实用一些。 对于一个Series， dropna返回一个仅含非空数据和索引值的Series：


```python
In [16]: from numpy import nan as NA

In [17]: data=pd.Series([1,NA,3.5,NA,7])

In [18]: data.dropna()
Out[18]:
0    1.0
2    3.5
4    7.0
dtype: float64
#等价于 

In [19]: data[data.notnull()]
Out[19]:
0    1.0
2    3.5
4    7.0
dtype: float64
```

而对于DataFrame对象， 事情就有点复杂了。 你可能希望丢弃全NA或含有NA的行或列。 dropna默
认丢弃任何含有缺失值的行：

```python
In [20]: data=pd.DataFrame([[1.,6.5,3.],[1.,NA,NA],[NA,NA,NA]
    ...: ,[NA,6.5,3.]])

In [22]: cleaned=data.dropna()

In [23]: data
Out[23]:
     0    1    2
0  1.0  6.5  3.0
1  1.0  NaN  NaN
2  NaN  NaN  NaN
3  NaN  6.5  3.0

In [24]: cleaned
Out[24]:
     0    1    2
0  1.0  6.5  3.0
#传入how='all'将只丢弃全为NA的那些行 

In [25]: data.dropna(how='all')
Out[25]:
     0    1    2
0  1.0  6.5  3.0
1  1.0  NaN  NaN
3  NaN  6.5  3.0

In [26]: data[4]=NA

In [27]: data
Out[27]:
     0    1    2   4
0  1.0  6.5  3.0 NaN
1  1.0  NaN  NaN NaN
2  NaN  NaN  NaN NaN
3  NaN  6.5  3.0 NaN
#传入axis=1丢弃列 

In [28]: data.dropna(axis=1,how='all')
Out[28]:
     0    1    2
0  1.0  6.5  3.0
1  1.0  NaN  NaN
2  NaN  NaN  NaN
3  NaN  6.5  3.0
```

### 填充缺失数据

你可能不想滤除缺失数据（有可能会丢弃跟它有关的其他数据） ， 而是希望通过其他方式填补那
些“空洞”。 对于大多数情况而言， fillna方法是最主要的函数。 通过一个常数调用fillna就会将缺失值
替换为那个常数值：

```python
In [30]: df=pd.DataFrame(np.random.randn(7,3))

In [31]: df.iloc[:4,1]=NA

In [32]: df.iloc[:2,2]=NA

In [33]: df
Out[33]:
          0         1         2
0  0.369981       NaN       NaN
1  1.582608       NaN       NaN
2 -0.308759       NaN  1.047090
3  0.069015       NaN  0.027606
4  0.403965  0.305350 -0.800660
5 -0.290466  1.365380 -0.361180
6  0.840956  0.457553 -0.027806

In [34]: df.fillna(0)
Out[34]:
          0         1         2
0  0.369981  0.000000  0.000000
1  1.582608  0.000000  0.000000
2 -0.308759  0.000000  1.047090
3  0.069015  0.000000  0.027606
4  0.403965  0.305350 -0.800660
5 -0.290466  1.365380 -0.361180
6  0.840956  0.457553 -0.027806
#若是通过一个字典调用fillna， 就可以实现对不同的列填充不同的值：
 

In [35]: df.fillna({1:0.5,2:0})
Out[35]:
          0         1         2
0  0.369981  0.500000  0.000000
1  1.582608  0.500000  0.000000
2 -0.308759  0.500000  1.047090
3  0.069015  0.500000  0.027606
4  0.403965  0.305350 -0.800660
5 -0.290466  1.365380 -0.361180
6  0.840956  0.457553 -0.027806
#fillna默认会返回新对象， 但也可以对现有对象进行就地修改：
 

In [36]: _=df.fillna(0,inplace=True)

In [37]: df
Out[37]:
          0         1         2
0  0.369981  0.000000  0.000000
1  1.582608  0.000000  0.000000
2 -0.308759  0.000000  1.047090
3  0.069015  0.000000  0.027606
4  0.403965  0.305350 -0.800660
5 -0.290466  1.365380 -0.361180
6  0.840956  0.457553 -0.027806
```

对reindexing有效的那些插值方法也可用于fillna：


```python
In [39]: df=pd.DataFrame(np.random.randn(6,3))

In [40]: df.iloc[2:,1]=NA

In [41]: df.iloc[4:,2]=NA

In [42]: df
Out[42]:
          0         1         2
0  0.447311 -1.562021  0.148839
1  2.152282 -0.270072  1.816863
2  0.109245       NaN  1.343202
3  0.261636       NaN -0.886285
4  0.205601       NaN       NaN
5 -0.415160       NaN       NaN

In [43]: df.fillna(method='ffill')
Out[43]:
          0         1         2
0  0.447311 -1.562021  0.148839
1  2.152282 -0.270072  1.816863
2  0.109245 -0.270072  1.343202
3  0.261636 -0.270072 -0.886285
4  0.205601 -0.270072 -0.886285
5 -0.415160 -0.270072 -0.886285

In [44]: df.fillna(method='ffill',limit=2)
Out[44]:
          0         1         2
0  0.447311 -1.562021  0.148839
1  2.152282 -0.270072  1.816863
2  0.109245 -0.270072  1.343202
3  0.261636 -0.270072 -0.886285
4  0.205601       NaN -0.886285
5 -0.415160       NaN -0.886285
```

只要有些创新， 你就可以利用fillna实现许多别的功能。 比如说， 你可以传入Series的平均值或中位
数：

```python
In [45]: data=pd.Series([1,NA,3.5,NA,7])

In [46]: data.fillna(data.mean())
Out[46]:
0    1.000000
1    3.833333
2    3.500000
3    3.833333
4    7.000000
dtype: float64
```

fillna的参考：

![](D:\home\markdown-notebook\assets\WEBRESOURCE64c537cd5a2b58e97e30d5c5e8d35d20.png)
![](D:\home\markdown-notebook\assets\WEBRESOURCE783bad940cff5b3c442f5d91f9493326.png)
## 数据转换

另一类重要操作则是过滤、 清理以及其他的转换工作。

### 移除重复数据


```python
In [48]: data=pd.DataFrame({'k1':['one','two']*3+['two'],'k2'
    ...: :[1,1,2,3,3,4,4]})

In [49]: data
Out[49]:
    k1  k2
0  one   1
1  two   1
2  one   2
3  two   3
4  one   3
5  two   4
6  two   4
#DataFrame的duplicated方法返回一个布尔型Series， 表示各行是否是重复行（前面出现过的
行） ： 

In [50]: data.duplicated()
Out[50]:
0    False
1    False
2    False
3    False
4    False
5    False
6     True
dtype: bool
#还有一个与此相关的drop_duplicates方法， 它会返回一个DataFrame， 重复的数组会被删除：
 

In [51]: data.drop_duplicates()
Out[51]:
    k1  k2
0  one   1
1  two   1
2  one   2
3  two   3
4  one   3
5  two   4
#这两个方法默认会判断全部列， 你也可以指定部分列进行重复项判断。 假设我们还有一列值， 且只
希望根据k1列过滤重复项： 

In [52]: data['v1']=range(7)

In [53]: data.drop_duplicates(['k1'])
Out[53]:
    k1  k2  v1
0  one   1   0
1  two   1   1
#duplicated和drop_duplicates默认保留的是第一个出现的值组合。 传入keep='last'则保留最后一
个 

In [54]: data.drop_duplicates(['k1','k2'],keep='last')
Out[54]:
    k1  k2  v1
0  one   1   0
1  two   1   1
2  one   2   2
3  two   3   3
4  one   3   4
6  two   4   6
```

