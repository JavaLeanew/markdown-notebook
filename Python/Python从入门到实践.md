# 变量和简单数据类型





## 1.变量的命名

- 变量名只能包含字母、 数字和下划线。变量名可以字母或下划线打头，但不能以数字打头， 例如，可将变量命名为message_1,但不能将其命名为1_message.

- 变量名不能包含空格，但可使用下划线来分隔其中的单词。例如，变量名greeting_message可行，但变量名greting message会引发错误。

- 不要将Python关键字和函数名用作变量名，即不要使用Python保留用于特殊用途的单词，如print。

- 变量名应既简短又具有描述性。例如，name比n好， student name比s_ n好，name_ lenght比lengh_of_persons_name好。

- 慎用小写字母l和大写字母O,因为它们可能被人错看成数字1和0。

## 2.字符串

字符串就是一系列字符。 在Python中， 用引号括起的都是字符串， 其中的引号可以是单引号， 也可以是双引号。

```python
"thsi is a string"
'this is a string'
#这种灵活性让你能够在字符串中包含引号和撇号
'I told my friend,"python" is my favorite language!'
"the language 'python' is named after monty python"
```

### 2.1修改字符串大小写

方法 是Python可对数据执行的操作。在name.title() 中， name 后面的句点（. ） 让Python对变量name 执行方法title() 指定的操作。 

title() 以首字母大写的方式显示每个单词， 即将每个单词的首字母都改为大写。 

```python
name="wang zhi yuan"
print(name.title())
#输出#
Wang Zhi Yuan
```

方法lower() 将字符串转化为小写，方法upper将字符串转化为大写。

### 2.2合并(拼接)字符串

Python使用加号（+ ）来合并字符串。

```python
 first_name="wang "
 last_name="zhi yuan"
 full_name=first_name+last_name
 print(full_name)
 #输出#
 wang zhi yuan
```

### 2.3使用制表符或换行符来添加空白

在字符串中添加制表符使用\t,添加换行符使用\n

```python
print('\tpython\n\tjava')
#输出#
        python
        java
```

### 2.4删除空白

Python能够找出字符串开头和末尾多余的空白。 

1.要确保字符串末尾没有空白， 可使用方法rstrip() 。

```python
>>>string='python '
>>>string
'python '
>>>string.rstrip()
'python'
#要永久删除这个字符串中的空白， 必须将删除操作的结果存回到变量中：
>>>string=string.rstrip()
```

2.剔除字符串开头的空白使用方法lstrip() 

3. 同时剔除字符串两端的空白使用方法和strip() 

## 3.数字

### 1.整数

在Python中， 可对整数执行加（+ ） 减（- ） 乘（* ） 除（/ ） 运算。也可以使用括号改变优先级。

```python
>>>3/2
1.5
```

### 2.浮点数

Python将带小数点的数字都称为浮点数 。 小数位数可能是不确定的。

```python
>>>0.2+0.1
0.30000000000000004
```

### 3.使用函数str()避免类型错误

```python
age=23
message="Happy"+age+"rd Birthday"
print(message)
"错误信息"
Traceback (most recent call last):
  File "D:\temp\demo.py", line 2, in <module>
    message="Happy"+age+"rd Birthday"
TypeError: can only concatenate str (not "int") to str
```

这是一个类型错误 ， 意味着Python无法识别你使用的信息。 在这个示例中， Python发现你使用了一个值为整数（int ） 的变量， 但它不知道该如何解读这个值。

```python
age=23
message="Happy"+str(age)+"rd Birthday"
print(message)
#输出#
Happy23rd Birthday
```

## 4.注释

在Python中， 注释用井号（# ） 标识。 井号后面的内容都会被Python解释器忽略

# 列表简介

列表 由一系列按特定顺序排列的元素组成。 你可以创建包含字母表中所有字母、 数字0~9或所有家庭成员姓名的列表； 也可以将任何东西加入列表中， 其中的元素之间可以没有任何关系。 类似于数组，但元素可以不是同一类型。







在Python中， 用方括号（[] ） 来表示列表， 并用逗号来分隔其中的元素。 

```python
>>>names=['小张','小王',23]
>>> names
['小张', '小王', 23]
```

## 1.访问列表元素

列表是有序集合， 因此要访问列表的任何元素， 只需将该元素的位置或索引告诉Python即可。

```python
>>>bicycles = [ 'trek', ' cannondale', ' redline', ' specialized']
>>>print (bicycles [0])    #列表的下标从0开始
trek
```

## 2.修改，添加和删除元素



### 2.1修改列表元素

指定列表名和要修改的元素的索引， 再指定该元素的新值。

```python
motorcycles=['honda','yamaha','suzuki']
motorcycles[0]='ducati'
```

### 2.2在列表中添加元素

1.在列表末添加元素。方法append() 将元素添加到列表末尾 ， 而不影响列表中的其他所有元素。

```python
mmotorcycles=[]
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
```

2.在列表中插入元素。使用方法insert() 可在列表的任何位置添加新元素。 为此， 你需要指定新元素的索引和值。

```python
motorcycles.inser(0,'ducati')    #在第0个元素后面添加新元素
```

### 2.3从列表中删除元素

1.使用del语句删除元素。如果知道要删除的元素在列表中的位置， 可使用del 语句。

```python
motorcycles=['honda','yamaha','suzuki']
del motorcycles[0]        #注意语法，删除之后就不好再使用这个元素了
```



2.使用pop()删除元素。有时候， 你要将元素从列表中删除， 并接着使用它的值。方法pop() 可删除列表末尾的元素， 并让你能够接着使用它。 

```python
motorcycles=['honda','yamaha','suzuki']
poped_cycle=motorcycles.pop()
print(motorcycles)
print(poped_cycle)
#输出#
['honda','yamaha']
suzuki
```



3.弹出列表中任何位置处的元素。实际上， 你可以使用pop() 来删除列表中任何位置的元素， 只需在括号中指定要删除的元素的索引即可。

```python
motorcycles=['honda','yamaha','suzuki']
poped_cycle=motorcycles.pop(1)
print(motorcycles)
print(poped_cycle)
#输出#
['honda','suzuki']
yamaha
```

每当你使用pop() 时， 被弹出的元素就不再在列表中了。

如果你要从列表中删除一个元素， 且不再以任何方式使用它， 就使用del 语句； 如果你要在删除元素后还能继续使用它， 就使用方法pop()

4.根据值删除元素

有时候， 你不知道要从列表中删除的值所处的位置。 如果你只知道要删除的元素的值， 可使用方法remove()。

```python
motorcycles=['honda','yamaha','suzuki']
too_expensive=motorcycles.remove('honda')    #类似pop方法，删除后可继续使用
print(motorcycles)
#输出#
['yamaha', 'suzuki']
```

方法remove() 只删除第一个指定的值。 如果要删除的值可能在列表中出现多次， 就需要使用循环来判断是否删除了所有这样的值。

### 2.4组织列表

有时候， 你希望保留列表元素最初的排列顺序， 而有时候又需要调整排列顺序。 Python提供了很多组织列表的方式， 可根据具体情况选用。

1.使用方法sort() 对列表进行永久性排序

```python
cars=['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
#输出#
['audi', 'bmw', 'subaru', 'toyota']
```

你还可以按与字母顺序相反的顺序排列列表元素， 为此， 只需向sort() 方法传递参数reverse=True 。 

```python
cars=['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)
#输出#
['toyota', 'subaru', 'bmw', 'audi']
```

2.使用函数sorted() 对列表进行临时排序

要保留列表元素原来的排列顺序， 同时以特定的顺序呈现它们， 可使用函数sorted() 。 函数sorted() 让你能够按特定顺序显示列表元素， 同时不影响它们在列表中的原始排列顺序。

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
#输出#
Here is the original list:
['bmw', 'audi', 'toyota', 'subaru']
Here is the sorted list:['audi', 'bmw', 'subaru', 'toyota']
Here is the original list again:
['bmw', 'audi', 'toyota', 'subaru']
```

调用函数sorted() 后， 列表元素的排列顺序并没有变 。 如果你要按与字母顺序相反的顺序显示列表， 也可向函数sorted() 传递参数reverse=True 。

3.倒着打印列表

要反转列表元素的排列顺序， 可使用方法reverse() 。 

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
#输出#
['bmw', 'audi', 'toyota', 'subaru']
['subaru', 'toyota', 'audi', 'bmw']
```

reverse() 不是指按与字母顺序相反的顺序排列列表元素， 而只是反转列表元素的排列顺序。方法reverse() 永久性地修改列表元素的排列顺序， 但可随时恢复到原来的排列顺序， 为此只需对列表再次调用reverse() 即可。

4.确定列表的长度

使用函数len() 可快速获悉列表的长度。

```python
>>> cars = ['bmw', 'audi', 'toyota', 'subaru']
>>> len(cars)
4
```

Python计算列表元素数时从1开始。 

### 2.5使用列表时避免索引错误

1. 列表元素从0开始编号

1. 不可越界

1. 每当需要访问最后一个列表元素时， 都可使用索引-1 。在列表为空时会出错

# 操作列表



## 1.遍历整个列表

使用for循环

```python
magicians = ['alice', 'david', 'carolina']
#使用缩进来区分作用域，在for循环作用域内的语句需要缩进。
#for循环外的语句不需要缩进
for magician in magicians:
    print(magician)
#输出#
alice
david
carolina
```

这行代码让Python从列表magicians 中取出一个名字， 并将其存储在变量magician 中。 最后， 我们让Python打印前面存储到变量magician 中的名字 。

## 2.创建数值列表

1.使用函数range()。Python函数range() 让你能够轻松地生成一系列的数字。

```python
for value in range(1,5)
    print(value)
#输出#
1
2
3
4
```

range() 只是打印数字1~4。 函数range() 让Python从你指定的第一个值开始数， 并在到达你指定的第二个值后停止， 因此输出不包含第二个值（这里为5） 。要打印数字1~5， 需要使用range(1,6) 

2.使用range() 创建数字列表。要创建数字列表， 可使用函数list() 将range() 的结果直接转换为列表。

```python
numbers = list(range(1,6))
print(numbers)
#输出#
[1,2,3,4,5]
```

使用函数range() 时， 还可指定步长。 例如， 下面的代码打印1~10内的偶数：

```python
even_numbers = list(range(2,11,2))
print(even_numbers)
#输出#
[2,4,6,8,10]
```

使用函数range() 几乎能够创建任何需要的数字集。例如， 如何创建一个列表， 其中包含前10个整数（即1~10） 的平方。

```python
squares = []
for value in range(1,11): 
    square = value**2        #在Python中， 两个星号（** ） 表示乘方运算
    squares.append(square)
print(squares)
#输出#
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

3.对数字列表执行简单的统计计算

有几个专门用于处理数字列表的Python函数。 例如， 你可以轻松地找出数字列表的最大值、 最小值和总和：

```python
>>> digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
>>> min(digits)
0
>>> max(digits)
9
>>> sum(digits)
45
```

4.列表解析

列表解析 将for 循环和创建新元素的代码合并成一行， 并自动附加新元素。

```python
squares = [value**2 for value in range(1,11)]
print(squares)
#输出#
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

首先指定一个描述性的列表名， 如squares ； 然后， 指定一个左方括号， 并定义一个表达式， 用于生成你要存储到列表中的值。 在这个示例中， 表达式为value**2 ， 它计算平方值。 接下来， 编写一个for 循环， 用于给表达式提供值， 再加上右方括号。 在这个示例中， for 循环为for value in range(1,11) ， 它将值1~10提供给表达式value**2 。 请注意， 这里的for 语句末尾没有冒号。

## 3.使用列表的一部分



1.切片，就是获取列表的一部分。要创建切片， 可指定要使用的第一个元素和最后一个元素的索引。

你可以生成列表的任何子集。

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
#输出#
['charles', 'martina', 'michael']
```

如果你没有指定第一个索引， Python将自动从列表开头开始。要让切片终止于列表末尾， 也可使用类似的语法。

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])
#输出#
['charles', 'martina', 'michael', 'florence']
```



```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])
#输出#
['michael', 'florence','eli']
```

负数索引返回离列表末尾相应距离的元素， 因此你可以输出列表末尾的任何切片。

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])    #获取后三个元素
```

2.遍历切片

如果要遍历列表的部分元素， 可在for 循环中使用切片。 在下面的示例中， 我们遍历前三名队员， 并打印他们的名字：

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
#输出#
Here are the first three players on my team:
Charles
Martina
Michael
```

3.复制列表

要复制列表， 可创建一个包含整个列表的切片， 方法是同时省略起始索引和终止索引（[:] ） 。 这让Python创建一个始于第一个元素， 终止于最后一个元素的切片， 即复制整个列表。

```python
#这两个列表是独立的，互不影响。不能通过简单的赋值运算复制列表。
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
```

## 4.元组

列表非常适合用于存储在程序运行期间可能变化的数据集，列表是可以修改的。 然而， 有时候你需要创建一系列不可修改的元素， 元组可以满足这种需求。 Python将不能修改的值称为不可变的 ， 而不可变的列表被称为元组 。

1.定义元组

元组看起来犹如列表， 但使用圆括号而不是方括号来标识。 定义元组后， 就可以使用索引来访问其元素， 就像访问列表元素一样。

```python
dimensions = (200, 50)        #元组不行修改值
print(dimensions[0])
print(dimensions[1])
#输出#
200
50
```

2.遍历元组中的所有值。像列表一样， 也可以使用for 循环来遍历元组中的所有值。

```python
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)
```

3.修改元组变量

虽然不能修改元组的元素， 但可以给存储元组的变量赋值。 因此， 如果要修改前述矩形的尺寸， 可重新定义整个元组：

```python
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
    
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
#输出#
Original dimensions:
200
50

Modified dimensions:
400
100
```

# if 语句

## 1.条件测试

每条if 语句的核心都是一个值为True 或False 的表达式， 这种表达式被称为条件测试 。 Python根据条件测试的值为True 还是False 来决定是否执行if 语句中的代码。 如果条件测试的值为True ， Python就执行紧跟在if 语句后面的代码； 如果为False ， Python就忽略这些代码。

```python
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
#输出#
Audi
BMW
Subaru
Toyota
```

### 1.检查多个条件

有时候你需要在两个条件都为True 时才执行相应的操作， 而有时候你只要求一个条件为True 时就执行相应的操作。 在这些情况下， 关键字and 和or 可助你一臂之力

1. 使用and 检查多个条件。要检查是否两个条件都为True ， 可使用关键字and 将两个条件测试合而为一； 如果每个测试都通过了， 整个表达式就为True ； 如果至少有一个测试没有通过， 整个表达式就为False 。

```python
>>> age_0 = 22
>>> age_1 = 18
>>> age_0 >= 21 or age_1 >= 21
True
>>> age_0 = 18
>>> age_0 >= 21 or age_1 >= 21
False
```

2.使用or 检查多个条件。关键字or 也能够让你检查多个条件， 但只要至少有一个条件满足， 就能通过整个测试。 仅当两个测试都没有通过时， 使用or 的表达式才为False 。

```python
>>> age_0 = 22
>>> age_1 = 18
>>> age_0 >= 21 or age_1 >= 21
True
>>> age_0 = 18
>>> age_0 >= 21 or age_1 >= 21
False
```

### 2.检查特定值是否包含在列表中

要判断特定的值是否已包含在列表中， 可使用关键字in

```python
>>> requested_toppings = ['mushrooms', 'onions', 'pineapple']
>>> 'mushrooms' in requested_toppings
True
>>> 'pepperoni' in requested_toppings
False
```

### 3.检查特定值是否不包含在列表中

还有些时候， 确定特定的值未包含在列表中很重要； 在这种情况下， 可使用关键字not in 

```python
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
#输出#
Marie, you can post a response if you wish.
```

## 2.if语句

### 1.简单的if语句

最简单的if 语句只有一个测试和一个操作：

```python
if conditional_test:
    do something
```

在第1行中， 可包含任何条件测试， 而在紧跟在测试后面的缩进代码块中， 可执行任何操作。 如果条件测试的结果为True ， Python就会执行紧跟在if 语句后面的代码； 否则Python将忽略这些代码。

### 2.if-else 语句

经常需要在条件测试通过了时执行一个操作， 并在没有通过时执行另一个操作； 在这种情况下， 可使用Python提供的if-else 语句。 if-else 语句块类似于简单的if 语句， 但其中的else 语句让你能够指定条件测试未通过时要执行的操作。

```python
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
 else:
     print("Sorry, you are too young to vote.")
     print("Please register to vote as soon as you turn 18!")
```

### 3.if-elif-else 结构

经常需要检查超过两个的情形， 为此可使用Python提供的if-elif-else 结构。

```python
age = 12
if age < 4:
    print("Your admission cost is $0.")
 elif age < 18:
     print("Your admission cost is $5.")
 else:
     print("Your admission cost is $10.")
```

## 3.使用if语句处理列表

通过结合使用if 语句和列表，可完成一些有趣的任务： 对列表中特定的值做特殊处理； 

### 1.检查特殊元素

```python
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
     else:
         print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")
```



### 2.确认列表不是空的

```python
requested_toppings = []
if requested_toppings:                                #确认列表是否为空
    for requested_topping in requested_toppings:      #若列表不为空，执行for代码
        print("Adding " + requested_topping + ".")
     print("\nFinished making your pizza!")
 else:                                                #若列表为空，执行print代码
     print("Are you sure you want a plain pizza?")

```

### 3.使用多个列表

```python
available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")

```

# 字典

## 1.使用字典

字典是一系列键—值对 。 每个键 都与一个值相关联， 你可以使用键来访问与之相关联的值。 与键相关联的值可以是数字、 字符串、 列表乃至字典。 事实上， 可将任何Python对象用作字典中的值。

在Python中， 字典用放在花括号{} 中的一系列键—值对表示， 

```python
alien_0 = {'color': 'green', 'points': 5}
```

键—值 对是两个相关联的值。 指定键时， Python将返回与之相关联的值。 键和值之间用冒号分隔， 而键—值对之间用逗号分隔。 在字典中， 你想存储多少个键—值对都可以

### 1.访问字典中的值

要获取与键相关联的值， 可依次指定字典名和放在方括号内的键， 

```python
alien_0 = {'color': 'green'}
print(alien_0['color'])
#输出#
green
```

### 2.添加键——值对

字典是一种动态结构， 可随时在其中添加键—值对。 要添加键—值对， 可依次指定字典名、 用方括号括起的键和相关联的值。

```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
#输出#
{'color': 'green', 'points': 5}
{'color': 'green', 'points': 5, 'y_position': 25, 'x_position': 0}
```

### 3.创建一个空字典

有时候， 在空字典中添加键—值对是为了方便， 而有时候必须这样做。 为此， 可先使用一对空的花括号定义一个字典， 再分行添加各个键—值对。 

```python
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
#输出#
{'color': 'green', 'points': 5}
```

### 4.修改字典中的值

要修改字典中的值， 可依次指定字典名、 用方括号括起的键以及与该键相关联的新值。

```python
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")
#输出#
The alien is green.
The alien is now yellow.
```

### 5.删除键—值对

对于字典中不再需要的信息， 可使用del 语句将相应的键—值对彻底删除。 使用del 语句时， 必须指定字典名和要删除的键。

```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)
#输出#
{'color': 'green', 'points': 5}
{'color': 'green'}
```

## 2.遍历字典



可遍历字典的所有键—值对、 键或值。

```python
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items(): 
    print("\nKey: " + key)
    print("Value: " + value)
#输出#
Key: last
Value: fermi

Key: first
Value: enrico

Key: username
Value: efermi
    
```

要编写用于遍历字典的for 循环， 可声明两个变量， 用于存储键—值对中的键和值。 对于这两个变量， 可使用任何名称。

for 语句的第二部分包含字典名和方法items()  ， 它返回一个键—值对列表。 接下来， for 循环依次将每个键—值对存储到指定的两个变量中。 

即便遍历字典时， 键—值对的返回顺序也与存储顺序不同。 Python不关心键—值对的存储顺序， 而只跟踪键和值之间的关联关系

### 1.遍历字典中的所有键

在不需要使用字典中的值时， 方法keys() 很有用

```python
favorite_languages = {'jen': 'python','sarah': 'c','edward': 'ruby','phil': 'python',}
for name in favorite_languages.keys():
    print(name.title())
#输出#
Jen
Sarah
Phil
Edward
```

遍历字典时， 会默认遍历所有的键， 因此， 如果将上述代码中的for name in favorite_languages.keys(): 替换为for name in favorite_languages: ， 输出将不变。如果显式地使用方法keys() 可让代码更容易理解。

### 2.按顺序遍历字典中的所有键

字典总是明确地记录键和值之间的关联关系， 但获取字典的元素时， 获取顺序是不可预测的。 要以特定的顺序返回元素， 一种办法是在for 循环中对返回的键进行排序。 为此， 可使用函数sorted() 来获得按特定顺序排列的键列表的副本。

```python
favorite_languages = {'jen': 'python','sarah': 'c','edward': 'ruby','phil': 'python',}
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
#输出#
Edward, thank you for taking the poll.
Jen, thank you for taking the poll.
Phil, thank you for taking the poll.
Sarah, thank you for taking the poll.
```

### 3.遍历字典中的所有值

如果你感兴趣的主要是字典包含的值， 可使用方法values() ， 它返回一个值列表， 而不包含任何键。

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
#输出#
The following languages have been mentioned:
Python
C
Python
Ruby
```

这种做法提取字典中所有的值， 而没有考虑是否重复。为剔除重复项， 可使用集合（set） 。 集合 类似于列表， 但每个元素都必须是独一无二的。

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c','edward': 'ruby',
    'phil': 'python',
}
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
#输出#
The following languages have been mentioned:
Python
C
Ruby
```

通过对包含重复元素的列表调用set() ， 可让Python找出列表中独一无二的元素， 并使用这些元素来创建一个集合。

## 3.嵌套

需要将一系列字典存储在列表中， 或将列表作为值存储在字典中， 这称为嵌套 。 你可以在列表中嵌套字典、 在字典中嵌套列表甚至在字典中嵌套字典。 

### 1.字典列表

```python
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
#输出#
{'color': 'green', 'points': 5}
{'color': 'yellow', 'points': 10}
{'color': 'red', 'points': 15}
```

使用range()生成多个字典列表。

```python
# 创建一个用于存储外星人的空列表aliens = []
# 创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# 显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print("...")
# 显示创建了多少个外星人
print("Total number of aliens: " + str(len(aliens)))
#输出#
{'speed': 'slow', 'color': 'green', 'points': 5}
{'speed': 'slow', 'color': 'green', 'points': 5}
{'speed': 'slow', 'color': 'green', 'points': 5}
{'speed': 'slow', 'color': 'green', 'points': 5}
{'speed': 'slow', 'color': 'green', 'points': 5}
...
Total number of aliens: 30
```

### 2.在字典中存储列表

需要将列表存储在字典中， 而不是将字典存储在列表中。

```python
# 存储所点比萨的信息
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
# 概述所点的比萨
print("You ordered a " + pizza['crust'] + "-crust pizza " +"with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)
#输出#
You ordered a thick-crust pizza with the following toppings:
    mushrooms
    extra cheese

```

每当需要在字典中将一个键关联到多个值时， 都可以在字典中嵌套一个列表。 

### 3.在字典中存储字典

可在字典中嵌套字典， 但这样做时， 代码可能很快复杂起来。 

```python
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
        
     'mcurie': {
         'first': 'marie',
         'last': 'curie',
         'location': 'paris',
         },
       }
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
#输出#
Username: aeinstein
    Full name: Albert Einstein
    Location: Princeton
Username: mcurie
    Full name: Marie Curie
    Location: Paris
```

# 用户输入和while循环

## 1.函数input() 的工作原理

函数input() 让程序暂停运行， 等待用户输入一些文本。 获取用户输入后， Python将其存储在一个变量中， 以方便你使用。

函数input() 接受一个参数： 即要向用户显示的提示 或说明， 让用户知道该如何做。

```python
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
#输出#
Tell me something, and I will repeat it back to you: Hello everyone!
Hello everyone!
```

有时候， 提示可能超过一行， 例如， 你可能需要指出获取特定输入的原因。 在这种情况下， 可将提示存储在一个变量中， 再将该变量传递给函数input() 。

```python
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")
#输出#
If you tell us who you are, we can personalize the messages you see.
What is your first name? Eric

Hello, Eric!
```

使用int() 来获取数值输入。使用函数input() 时， Python将用户输入解读为字符串。 

```python
height = input("How tall are you, in inches? ")
height = int(height)                                #将字符串类型转换为数值类型
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
    
#输出#
How tall are you, in inches? 71

You're tall enough to ride!
```

处理数值信息时， 求模运算符 （%） 是一个很有用的工具， 它将两个数相除并返回余数：

## 2.while循环简介

for 循环用于针对集合中的每个元素都一个代码块， 而while 循环不断地运行， 直到指定的条件不满足为止。

### 1.使用while循环

```python
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
#输出#
1
2
3
4
5
```

在第1行， 我们将current_number 设置为1， 从而指定从1开始数。 接下来的while 循环被设置成这样： 只要current_number 小于或等于5， 就接着运行这个循环。 循环中的代码打印current_number 的值， 再使用代码current_number += 1 （代码current_number = current_number + 1 的简写） 将其值加1。

### 2.让用户选择何时退出

可使用while 循环让程序在用户愿意时不断地运行

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
```

### 3.使用标志

在要求很多条件都满足才继续运行的程序中， 可定义一个变量， 用于判断整个程序是否处于活动状态。 这个变量被称为标志 ， 充当了程序的交通信号灯。 

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
```

### 4.使用break退出循环

要立即退出while 循环， 不再运行循环中余下的代码， 也不管条件测试的结果如何， 可使用break 语句。 

```python
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
```

### 5.在循环中使用continue

要返回到循环开头， 并根据条件测试结果决定是否继续执行循环， 可使用continue 语句， 它不像break 语句那样不再执行余下的代码并退出整个循环。 

```python
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
```

## 3.使用while 循环来处理列表和字典

for 循环是一种遍历列表的有效方式， 但在for 循环中不应修改列表， 否则将导致Python难以跟踪其中的元素。 要在遍历列表的同时对其进行修改， 可使用while 循环。 通过将while 循环同列表和字典结合起来使用， 可收集、 存储并组织大量输入， 供以后查看和显示。

### 1.在列表之间移动元素

```python
#假设有一个列表， 其中包含新注册但还未验证的网站用户； 验证这些用户后， 如何将他们移到另一个已验证用户列表中呢？ 

# 首先， 创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# 验证每个用户， 直到没有未验证用户为止
# 将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
    
# 显示所有已验证的用户print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
```

### 2.删除包含特定值的所有列表元素

我们使用函数remove() 来删除列表中的特定值， 这之所以可行， 是因为要删除的值在列表中只出现了一次。如果要删除列表中所有包含特定值的元素，使用循环。

```python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
    
print(pets) 
```

### 3.使用用户输入来填充字典

下面来创建一个调查程序， 其中的循环每次执行时都提示输入被调查者的名字和回答。 我们将收集的数据存储在一个字典中， 以便将回答同被调查者关联起来。

```python
responses = {}
# 设置一个标志， 指出调查是否继续
polling_active = True
while polling_active:
    # 提示输入被调查者的名字和回答
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    
    # 将答卷存储在字典中
    responses[name] = response
    
    # 看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
        
   # 调查结束， 显示结果
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")

```

# 函数

## 1.定义函数

```python
def greet_user():
    """显示简单的问候语"""
    print("hello")

greet_user()
```

- 第一行的代码行使用关键字def 来告诉Python你要定义一个函数。 这是函数定义 ， 向Python指出了函数名， 还可能在括号内指出函数为完成其数名为greet_user() ， 它不需要任	何信息就能完成其工作， 因此括号是空的（即便如此， 括号也必不可少） 。 最后， 定义以冒号结尾。

- 紧跟在def greet_user(): 后面的所有缩进行构成了函数体。 第2行的文本是被称为文档字符串 （docstring） 的注释， 描述了函数是做什么的。 文档字符串用三引号括起， Python用他们来生成有关程序中函数的文档。

- 代码行print("Hello!")  是函数体内的唯一一行代码， greet_user() 只做一项工作： 打印Hello! 。

函数调用让Python执行函数的代码。 要调用 函数，可依次指定函数名以及用括号括起的必要信息。

### 1.1向函数传递信息

```python
def greet_user(username):
    """显示简单的问候语"""
    print("hello,"+username.title()+"!")

greet_user('jesse')
```

代码greet_user('jesse') 调用函数greet_user() ， 并向它提供执行print 语句所需的信息。 这个函数接受你传递给它的名字， 并向这个人发出问候。

### 1.2实参和形参

变量username 是一个形参 ——函数完成其工作所需的一项信息。 在代码greet_user('jesse') 中， 值'jesse' 是一个实参 。 实参是调用函数时传递给函数的信息。 我们调用函数时， 将要让函数使用的信息放在括号内。 在greet_user('jesse') 中， 将实参'jesse' 传递给了函数greet_user() ， 这个值被存储在形参username 中。

## 2传递实参



鉴于函数定义中可能包含多个形参， 因此函数调用中也可能包含多个实参。 向函数传递实参的方式很多， 可使用位置实参 ， 这要求实参的顺序与形参的顺序相同； 也可使用关键字实参 ， 其中每个实参都由变量名和值组成； 还可使用列表和字典。

### 2.1位置实参

你调用函数时， Python必须将函数调用中的每个实参都关联到函数定义中的一个形参。 为此， 最简单的关联方式是基于实参的顺序。 这种关联方式被称为位置实参 。

```python
def describe_pet(animal_type,pet_name):
    """显示宠物信息"""
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
   
describe_pet('hamster','harry') 
```

调用describe_pet() 时， 需要按顺序提供一种动物类型和一个名字。 例如， 在前面的函数调用中， 实参'hamster' 存储在形参animal_type 中， 而实参'harry' 存储在形参pet_name 中。

### 2.2关键字实参

关键字实参是传递给函数的名称—值对。 你直接在实参中将名称和值关联起来了， 因此向函数传递实参时不会混淆 。 关键字实参让你无需考虑函数调用中的实参顺序， 还清楚地指出了函数调用中各个值的用途。

```python
def describe_pet(animal_type,pet_name):
    """显示宠物信息"""
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
   
describe_pet(animal_type='hamster',pet_name='harry') 
```

关键字实参的顺序无关紧要， 因为Python知道各个值该存储到哪个形参中。

### 2.3默认值

编写函数时， 可给每个形参指定默认值 。 在调用函数中给形参提供了实参时， Python将使用指定的实参值； 否则， 将使用形参的默认值。 因此， 给形参指定默认值后， 可在函数调用中省略相应的实参。 使用默认值可简化函数调用， 还可清楚地指出函数的典型用法。

```python
def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
   
describe_pet(pet_name='willie')
describe_pet('willie')
```

默认形参只能放在函数参数的后面位置。

## 3返回值

函数并非总是直接显示输出， 相反， 它可以处理一些数据， 并返回一个或一组值。 函数返回的值被称为返回值 。 在函数中， 可使用return 语句将值返回到调用函数的代码行。

### 3.1返回简单值

```python
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
```

函数get_formatted_name() 的定义通过形参接受名和姓 。 它将姓和名合而为一， 在它们之间加上一个空格， 并将结果存储在变量full_name 中 。 然后，将full_name 的值转换为首字母大写格式， 并将结果返回到函数调用行。

### 3.2让实参变为可选的

有时候， 需要让实参变成可选的， 这样使用函数的人就只需在必要时才提供额外的信息。 可使用默认值来让实参变成可选的。

```python
def get_formatted_name(first_name,last_name,middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name=first_name+" "+middle_name+" "+last_name
    else:
        full_name=first_name+" "+last_name
    return full_name.title()

musician=get_formatted_name('john','hooker','lee')
print(musician)
```

在这个示例中， 姓名是根据三个可能提供的部分创建的。 由于人都有名和姓， 因此在函数定义中首先列出了这两个形参。 中间名是可选的， 因此在函数定义中最后列出该形参，并将其默认值设置为空字符串。 

如果还要指定中间名， 就必须确保它是最后一个实参， 这样Python才能正确地将位置实参关联到形参。

### 3.3返回字典

函数可返回任何类型的值， 包括列表和字典等较复杂的数据结构。

```python
def build_person(first_name, last_name):
    """返回一个字典， 其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)
#输出#
{'first': 'jimi', 'last': 'hendrix'}
```

函数build_person() 接受名和姓， 并将这些值封装到字典中 。 存储first_name 的值时， 使用的键为'first' ， 而存储last_name 的值时， 使用的键为'last' 。 最后， 返回表示人的整个字典 。 在第7行， 打印这个返回的值， 此时原来的两项文本信息存储在一个字典中。

### 3.4结合使用函数和while循环

可将函数同本书前面介绍的任何Python结构结合起来使用。

```python
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
    
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_n
ame = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
```

## 4传递列表

假设有一个用户列表， 我们要问候其中的每位用户。 下面的示例将一个名字列表传递给一个名为greet_users() 的函数， 这个函数问候列表中的每个人。

```python
def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
    msg = "Hello, " + name.title() + "!"
    print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
```

### 4.1在函数中修改列表

将列表传递给函数后， 函数就可对其进行修改。 在函数中对这个列表所做的任何修改都是永久性的， 这让你能够高效地处理大量的数据。

```python
#来看一家为用户提交的设计制作3D打印模型的公司。 需要打印的设计存储在一个列表中， 打印后移到另一个列表中。 
#下面是在不使用函数的情况下模拟这个过程的代码：

# 首先创建一个列表， 其中包含一些要打印的设计
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# 模拟打印每个设计， 直到没有未打印的设计为止
# 打印每个设计后， 都将其移到列表completed_models中
while unprinted_designs:
    current_design = unprinted_designs.pop()
    #模拟根据设计制作3D打印模型的过程
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# 显示打印好的所有模型
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

```

### 4.2禁止函数修改列表

为解决这个问题， 可向函数传递列表的副本而不是原件； 这样函数所做的任何修改都只影响副本， 而丝毫不影响原件。

要将列表的副本传递给函数， 可以像下面这样做：

```python
function_name(list_name[:])    #切片表示法[:] 创建列表的副本。 
```

虽然向函数传递列表的副本可保留原始列表的内容， 但除非有充分的理由需要传递副本， 否则还是应该将原始列表传递给函数， 因为让函数使用现成列表可避免花时间和内存创建副本， 从而提高效率， 在处理大型列表时尤其如此。

## 5传递任意数量的实参

有时候， 你预先不知道函数需要接受多少个实参， 好在Python允许函数从调用语句中收集任意数量的实参。

```python
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)
    
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
#输出#
('pepperoni',)
('mushrooms', 'green peppers', 'extra cheese')
```

形参名*toppings 中的星号让Python创建一个名为toppings 的空元组， 并将收到的所有值都封装到这个元组中。 函数体内的print 语句通过生成输出来证明Python能够处理使用一个值调用函数的情形， 也能处理使用三个值来调用函数的情形。 它以类似的方式处理不同的调用， 注意， Python将实参封装到一个元组中， 即便函数只收到一个值也如此。

### 5.1结合使用位置实参和任意数量实参

如果要让函数接受不同类型的实参， 必须在函数定义中将接纳任意数量实参的形参放在最后。 Python先匹配位置实参和关键字实参， 再将余下的实参都收集到最后一个形参中。

```python
def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) +"-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
        
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#输出#
Making a 16-inch pizza with the following toppings:
- pepperoni

Making a 12-inch pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese
```

### 5.2使用任意数量的关键字实参

有时候， 需要接受任意数量的实参， 但预先不知道传递给函数的会是什么样的信息。 在这种情况下， 可将函数编写成能够接受任意数量的键—值对——调用语句提供了多少就接受多少。 

```python
def build_profile(first, last, **user_info):
    """创建一个字典， 其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
    
user_profile = build_profile('albert', 'einstein',location='princeton',field='physics')
print(user_profile)
#输出#
{'first_name': 'albert', 'last_name': 'einstein','location': 'princeton', 'field': 'physics'}
```

函数build_profile() 的定义要求提供名和姓， 同时允许用户根据需要提供任意数量的名称—值对。 形参**user_info 中的两个星号让Python创建一个名为user_info 的空字典， 并将收到的所有名称—值对都封装到这个字典中。 在这个函数中， 可以像访问其他字典那样访问user_info 中的名称—值对。

## 6将函数存储在模块中

函数的优点之一是， 使用它们可将代码块与主程序分离。 通过给函数指定描述性名称， 可让主程序容易理解得多。 你还可以更进一步， 将函数存储在被称为模块 的独立文件中，再将模块导入 到主程序中。 import 语句允许在当前运行的程序文件中使用模块中的代码。

### 6.1导入整个模块

要让函数是可导入的， 得先创建模块。 模块 是扩展名为.py的文件， 包含要导入到程序中的代码。

pizza.py

```python
def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) +"-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
```

making_pizzas.py

```python
import pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

Python读取这个文件时， 代码行import pizza 让Python打开文件pizza.py， 并将其中的所有函数都复制到这个程序中。 要调用被导入的模块中的函数， 可指定导入的模块的名称pizza 和函数名make_pizza() ， 并用句点分隔它们。

### 6.2导入特定的函数

```python
from module_name import function_name
#通过用逗号分隔函数名， 可根据需要从模块中导入任意数量的函数
from module_name import function_0, function_1, function_2
```

若使用这种语法， 调用函数时就无需使用句点。 由于我们在import 语句中显式地导入了函数make_pizza() ， 因此调用它时只需指定其名称。

```python
from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

### 6.3使用as 给函数指定别名

如果要导入的函数的名称可能与程序中现有的名称冲突， 或者函数的名称太长， 可指定简短而独一无二的别名 ——函数的另一个名称， 类似于外号。 要给函数指定这种特殊外号， 需要在导入它时这样做。

```python
from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
```

### 6.4使用as给模块指定别名

```python
import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

### 6.5导入模块中的所有函数

使用星号（* ） 运算符可让Python导入模块中的所有函数。

```python
from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

import 语句中的星号让Python将模块pizza 中的每个函数都复制到这个程序文件中。 由于导入了每个函数， 可通过名称来调用每个函数， 而无需使用句点表示法。 然而， 使用并非自己编写的大型模块时， 最好不要采用这种导入方法： 如果模块中有函数的名称与你的项目中使用的名称相同， 可能导致意想不到的结果： Python可能遇到多个名称相同的函数或变量， 进而覆盖函数， 而不是分别导入所有的函数。

最佳的做法是， 要么只导入你需要使用的函数， 要么导入整个模块并使用句点表示法。 这能让代码更清晰， 更容易阅读和理解。

### 7函数编写指南

- 应给函数指定描述性名称， 且只在其中使用小写字母和下划线。 描述性名称可帮助你和别人明白代码想要做什么。 给模块命名时也应遵循上述约定。

- 每个函数都应包含简要地阐述其功能的注释， 该注释应紧跟在函数定义后面， 并采用文档字符串格式。 文档良好的函数让其他程序员只需阅读文档字符串中的描述就能够使用它： 

- 给形参指定默认值时， 等号两边不要有空格。

- 如果程序或模块包含多个函数， 可使用两个空行将相邻的函数分开， 这样将更容易知道前一个函数在什么地方结束， 下一个函数从什么地方开始。

- 所有的import 语句都应放在文件开头， 唯一例外的情形是， 在文件开头使用了注释来描述整个程序。

# 类

## 1 创建和使用类

1. 创建Dog类

```python
class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self, name, age):
    """初始化属性name和age"""
    self.name = name
    self.age = age

    def sit(self):
    """模拟小狗被命令时蹲下"""
    print(self.name.title() + " is now sitting.")
    
    def roll_over(self):
    """模拟小狗被命令时打滚"""
    print(self.name.title() + " rolled over!")
```

根据约定， 在Python中， 首字母大写的名称指的是类。 这个类定义中的括号是空的， 因为我们要从空白创建这个类。 在第2行， 我们编写了一个文档字符串， 对这个类的功能作了描述。

方法__init__()：

类中的函数称为方法 ； 你前面学到的有关函数的一切都适用于方法， 就目前而言， 唯一重要的差别是调用方法的方式。 第3行的方法__init__() 是一个特殊的方法， 每当你根据Dog 类创建新实例时， Python都会自动运行它。 在这个方法的名称中， 开头和末尾各有两个下划线， 这是一种约定， 旨在避免Python默认方法与普通方法发生名称冲突。

我们将方法__init__() 定义成了包含三个形参： self 、 name 和age 。 在这个方法的定义中， 形参self 必不可少， 还必须位于其他形参的前面。因为Python调用这个__init__() 方法来创建Dog 实例时， 将自动传入实参self 。 每个与类相关联的方法调用都自动传递实参self ， 它是一个指向实例本身的引用， 让实例能够访问类中的属性和方法。 我们创建Dog 实例时， Python将调用Dog 类的方法__init__() 。 我们将通过实参向Dog() 传递名字和年龄； self 会自动传递，因此我们不需要传递它。 每当我们根据Dog 类创建实例时， 都只需给最后两个形参（name 和age ） 提供值。

1. 根据类创建实例

可将类视为有关如何创建实例的说明。 Dog 类是一系列说明， 让Python知道如何创建表示特定小狗的实例。

```python
class Dog():
    --snip--

my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
```

在第4行处， 我们让Python创建一条名字为'willie' 、 年龄为6 的小狗。 遇到这行代码时， Python使用实参'willie' 和6 调用Dog 类中的方法__init__() 。 方法__init__() 创建一个表示特定小狗的示例， 并使用我们提供的值来设置属性name 和age 。 方法__init__() 并未显式地包含return 语句，但Python自动返回一个表示这条小狗的实例。 

访问属性：

```python
my_dog.name
```

在这里， Python先找到实例my_dog ， 再查找与这个实例相关联的属性name 。 在Dog 类中引用这个属性时， 使用的是self.name 。

调用方法：

```python
class Dog():
    --snip--
my_dog = Dog('willie', 6)
my_dog.sit()
my_dog.roll_over()
```

要调用方法， 可指定实例的名称（这里是my_dog ） 和要调用的方法， 并用句点分隔它们。 遇到代码my_dog.sit() 时， Python在类Dog 中查找方法sit() 并运行其代码。Python以同样的方式解读代码my_dog.roll_over() 。

## 2使用类和实例

下面来编写一个表示汽车的类， 它存储了有关汽车的信息， 还有一个汇总这些信息的方法：

```python
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
    """初始化描述汽车的属性"""
    self.make = make
    self.model = model
    self.year = year
    
def get_descriptive_name(self):
    """返回整洁的描述性信息"""
    long_name = str(self.year) + ' ' + self.make + ' ' + self.model
    return long_name.title()

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
```

给属性指定默认值：类中的每个属性都必须有初始值， 哪怕这个值是0或空字符串。 在有些情况下， 如设置默认值时， 在方法__init__() 内指定这种初始值是可行的； 如果你对某个属性这样做了， 就无需包含为它提供初始值的形参。

下面来添加一个名为odometer_reading 的属性， 其初始值总是为0。 我们还添加了一个名为read_odometer() 的方法， 用于读取汽车的里程表：

```python
class Car():
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        --snip--
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
```

修改属性的值：可以以三种不同的方式修改属性的值： 直接通过实例进行修改； 通过方法进行设置； 通过方法进行递增（增加特定的值） 。

1.直接修改属性的值

```python
class Car():
    --snip--
    
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
```

2.通过方法修改属性的值

如果有替你更新属性的方法， 将大有裨益。 这样， 你就无需直接访问属性， 而可将值传递给一个方法， 由它在内部进行更新。

```python
class Car():
    --snip--
    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值"""
        self.odometer_reading = mileage
        
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()
```

3. 通过方法对属性的值进行递增

```python
class Car():
    --snip--
    def update_odometer(self, mileage):
        --snip--
    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles

my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
```

## 3继承

如果你要编写的类是另一个现成类的特殊版本， 可使用继承 。 一个类继承 另一个类时， 它将自动获得另一个类的所有属性和方法； 原有的类称为父类 ， 而新类称为子类 。 子类继承了其父类的所有属性和方法， 同时还可以定义自己的属性和方法

### 3.1子类的方法__init__()

创建子类的实例时， Python首先需要完成的任务是给父类的所有属性赋值。 为此， 子类的方法__init__() 需要父类施以援手。

```python
class Car():
    """一次模拟汽车的简单尝试"""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
        
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        self.odometer_reading += miles
        
class ElectricCar(Car):
    """电动汽车的独特之处"""
    
    def __init__(self, make, model, year):
    """初始化父类的属性"""
    super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name()
```

创建子类时， 父类必须包含在当前文件中， 且位于子类前面。定义子类时， 必须在括号内指定父类的名称。 方法__init__() 接受创建Car 实例所需的信息。

super() 是一个特殊函数， 帮助Python将父类和子类关联起来。 这行代码让Python调用ElectricCar 的父类的方法__init__() ， 让ElectricCar 实例包含父类的所有属性。 父类也称为超类 （superclass） ， 名称super因此而得名。

### 3.2给子类定义属性和方法

让一个类继承另一个类后， 可添加区分子类和父类所需的新属性和方法。

```python
class Car():
    --snip--

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """电动汽车的独特之处初始化父类的属性， 再初始化电动汽车特有的属性"""
        super().__init__(make, model, year)
        self.battery_size = 70
    
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
        
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
```

### 3.3重写父类的方法

对于父类的方法， 只要它不符合子类模拟的实物的行为， 都可对其进行重写。 为此， 可在子类中定义一个这样的方法， 即它与要重写的父类方法同名。 这样， Python将不会考虑这个父类方法， 而只关注你在子类中定义的相应方法。

假设Car 类有一个名为fill_gas_tank() 的方法， 它对全电动汽车来说毫无意义， 因此你可能想重写它。 下面演示了一种重写方式：

```python
def ElectricCar(Car):
    --snip--
    
def fill_gas_tank():
    """电动汽车没有油箱"""
    print("This car doesn't need a gas tank!")
```

现在， 如果有人对电动汽车调用方法fill_gas_tank() ， Python将忽略Car 类中的方法fill_gas_tank() ， 转而运行上述代码。 使用继承时， 可让子类保留从父类那里继承而来的精华， 并剔除不需要的糟粕。

### 3.4将实例用作属性

使用代码模拟实物时， 你可能会发现自己给类添加的细节越来越多： 属性和方法清单以及文件都越来越长。 在这种情况下， 可能需要将类的一部分作为一个独立的类提取出来。你可以将大型类拆分成多个协同工作的小类。

例如， 不断给ElectricCar 类添加细节时， 我们可能会发现其中包含很多专门针对汽车电瓶的属性和方法。 在这种情况下， 我们可将这些属性和方法提取出来， 放到另一个名为Battery 的类中， 并将一个Battery 实例用作ElectricCar 类的一个属性：

```python
class Car():
    --snip--

class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size
        
    def describe_battery(self):
    """打印一条描述电瓶容量的消息"""
    print("This car has a " + str(self.battery_size) + "-kWh battery.")
    
class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性， 再初始化电动汽车特有的属性"""
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
```

## 4导入类

随着你不断地给类添加功能， 文件可能变得很长， 即便你妥善地使用了继承亦如此。 为遵循Python的总体理念， 应让文件尽可能整洁。 为在这方面提供帮助， Python允许你将类存储在模块中， 然后在主程序中导入所需的模块。

### 4.1导入单个类

Car.py

```python
 """一个可用于表示汽车的类"""
class Car():
    """一次模拟汽车的简单尝试"""
    
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """返回整洁的描述性名称"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条消息， 指出汽车的里程"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        拒绝将里程表往回拨
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles
```

在第一行， 我们包含了一个模块级文档字符串， 对该模块的内容做了简要的描述。 你应为自己创建的每个模块都编写文档字符串。

my_car.py

```python
from car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
```

第一行处的import 语句让Python打开模块car ， 并导入其中的Car 类。 这样我们就可以使用Car 类了。

### 4.2从一个模块中导入多个类

```python
from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
```

### 4.3导入整个模块

你还可以导入整个模块， 再使用句点表示法访问需要的类。 这种导入方法很简单， 代码也易于阅读。 由于创建类实例的代码都包含模块名， 因此不会与当前文件使用的任何名称发生冲突。

```python
import car

my_beetle = car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
```

### 4.4导入模块中的所有类

```python
from module_name import *
```

不推荐使用这种导入方式， 其原因有二。 首先， 如果只要看一下文件开头的import 语句， 就能清楚地知道程序使用了哪些类， 将大有裨益； 但这种导入方式没有明确地指出你使用了模块中的哪些类。 这种导入方式还可能引发名称方面的困惑。 如果你不小心导入了一个与程序文件中其他东西同名的类， 将引发难以诊断的错误。 这里之所以介绍这种导入方式， 是因为虽然不推荐使用这种方式， 但你可能会在别人编写的代码中见到它。

需要从一个模块中导入很多类时， 最好导入整个模块， 并使用 module_name.class_name 语法来访问类。 这样做时， 虽然文件开头并没有列出用到的所有类， 但你清楚地知道在程序的哪些地方使用了导入的模块； 你还避免了导入模块中的每个类可能引发的名称冲突。

### 4.5Python标准库

Python标准库 是一组模块， 安装的Python都包含它。 你现在对类的工作原理已有大致的了解， 可以开始使用其他程序员编写好的模块了。 可使用标准库中的任何函数和类， 为此只需在程序开头包含一条简单的import 语句。 

### 4.6类编码风格

- 类名应采用驼峰命名法 ， 即将类名中的每个单词的首字母都大写， 而不使用下划线。 实例名和模块名都采用小写格式， 并在单词之间加上下划线。

- 对于每个类， 都应紧跟在类定义后面包含一个文档字符串。 这种文档字符串简要地描述类的功能， 并遵循编写函数的文档字符串时采用的格式约定。 每个模块也都应包含一个文档字符串， 对其中的类可用于做什么进行描述。

- 可使用空行来组织代码， 但不要滥用。 在类中， 可使用一个空行来分隔方法； 而在模块中， 可使用两个空行来分隔类。

- 需要同时导入标准库中的模块和你编写的模块时， 先编写导入标准库模块的import 语句， 再添加一个空行， 然后编写导入你自己编写的模块的import 语句。 在包含多条import 语句的程序中， 这种做法让人更容易明白程序使用的各个模块都来自何方。

# 文件和异常

## 1.从文件中读取数据

要使用文本文件中的信息， 首先需要将信息读取到内存中。 为此， 你可以一次性读取文件的全部内容， 也可以以每次一行的方式逐步读取。

### 1.1读取整个文件

```python
with open('pi.txt') as file_object:
    contents=file_object.read()
    print(contents)
```

要以任何方式使用文件——哪怕仅仅是打印其内容， 都得先打开 文件， 这样才能访问它。 函数open()接受一个参数： 要打开的文件的名称。 Python在当前执行的文件所在的目录中查找指定的文件。函数open() 返回一个表示文件的对象。 在这里， open('pi_digits.txt') 返回一个表示文件pi_digits.txt 的对象； Python将这个对象存储在我们将在后面使用的变量中。

 关键字with 在不再需要访问文件后将其关闭。 在这个程序中， 注意到我们调用了open() ， 但没有调用close() ； 你也可以调用open() 和close() 来打开和关闭文件， 但这样做时， 如果程序存在bug， 导致close() 语句未执行， 文件将不会关闭。 这看似微不足道， 但未妥善地关闭文件可能会导致数据丢失或受损。 如果在程序中过早地调用close() ， 你会发现需要使用文件时它已关闭 （无法访问） ， 这会导致更多的错误。 并非在任何情况下都能轻松确定关闭文件的恰当时机， 但通过使用前面所示的结构， 可让Python去确定： 你只管打开文件， 并在需要时使用它， Python自会在合适的时候自动将其关闭。

我们使用方法read()  读取这个文件的全部内容， 并将其作为一个长长的字符串存储在变量contents 中。 这样， 通过打印contents 的值， 就可将这个文本文件的全部内容显示出来。因为read() 到达文件末尾时返回一个空字符串， 所以读取的文本会多一个空行。

### 1.2文件路径

要让Python打开不与程序文件位于同一个目录中的文件， 需要提供文件路径 ， 它让Python到系统的特定位置去查找。

相对文件路径让Python到指定的位置去查找， 而该位置是相对于当前运行的程序所在目录的。 

你还可以将文件在计算机中的准确位置告诉Python， 这样就不用关心当前运行的程序存储在什么地方了。 这称为绝对文件路径 。 在相对路径行不通时， 可使用绝对路径。 

### 1.3逐行读取

```python
filename='pi.txt'

with open('pi.txt') as file_object:
    for line in file_object:
        print(line)
```

 在第1行处， 我们将要读取的文件的名称存储在变量filename 中， 这是使用文件时一种常见的做法。 由于变量filename 表示的并非实际文件——它只是一个让Python知道到哪里去查找文件的字符串， 因此可轻松地将'pi.txt' 替换为你要使用的另一个文件的名称。 调用open() 后， 将一个表示文件及其内容的对象存储到了变量file_object 中 。 这里也使用了关键字with ， 让Python负责妥善地打开和关闭文件。 为查看文件的内容， 我们通过对文件对象执行循环来遍历文件中的每一行 。

### 1.4创建一个包含文件各行内容的列表

使用关键字with 时， open() 返回的文件对象只在with 代码块内可用。 如果要在with 代码块外访问文件的内容， 可在with 代码块内将文件的各行存储在一个列表中， 并在with 代码块外使用该列表： 你可以立即处理文件的各个部分， 也可推迟到程序后面再处理。

```python
filename='pi.txt'

with open(filename) as file_object:
    lines=file_object.readlines()

for line in lines:
    print(line.rstrip())
```

方法readlines() 从文件中读取每一行， 并将其存储在一个列表中； 接下来， 该列表被存储到变量lines 中； 在with 代码块外， 我们依然可以使用这个变量。

读取文本文件时， Python将其中的所有文本都解读为字符串。 如果你读取的是数字， 并要将其作为数值使用， 就必须使用函数int() 将其转换为整数， 或使用函数float() 将其转换为浮点数。

## 2写入文件

保存数据的最简单的方式之一是将其写入到文件中。 通过将输出写入文件， 即便关闭包含程序输出的终端窗口， 这些输出也依然存在： 你可以在程序结束运行后查看这些输出，可与别人分享输出文件， 还可编写程序来将这些输出读取到内存中并进行处理。

### 2.1写入空文件

```python
filename='programing.txt'

with open(filename,'w') as file_object:
    file_object.write("I love programing.")
```

在这个示例中， 调用open() 时提供了两个实参 。 第一个实参也是要打开的文件的名称； 第二个实参（'w' ） 告诉Python， 我们要以写入模式 打开这个文件。 打开文件时， 可指定读取模式 （'r' ） 、 写入模式 （'w' ） 、 附加模式 （'a' ） 或让你能够读取和写入文件的模式（'r+' ） 。 如果你省略了模式实参， Python将以默认的只读模式打开文件。

如果你要写入的文件不存在， 函数open() 将自动创建它。 然而， 以写入（'w' ） 模式打开文件时千万要小心， 因为如果指定的文件已经存在， Python将在返回文件对象前清空该文件。

注意 Python只能将字符串写入文本文件。 要将数值数据存储到文本文件中， 必须先使用函数str() 将其转换为字符串格式。

### 2.2写入多行

函数write() 不会在你写入的文本末尾添加换行符， 因此如果你写入多行时没有指定换行符， 文件看起来可能不是你希望的那样。

```python
filename='programing.txt'

with open(filename,'w') as file_object:
    file_object.write("I love programing.\n")
    file_object.write("I love creating new games.\n")
```

### 2.3附加到文件

如果你要给文件添加内容， 而不是覆盖原有的内容， 可以附加模式 打开文件。 你以附加模式打开文件时， Python不会在返回文件对象前清空文件， 而你写入到文件的行都将添加到文件末尾。 如果指定的文件不存在， Python将为你创建一个空文件。

```python
filename = 'programming.txt'
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
```

### 3异常

Python使用被称为异常的特殊对象来管理程序执行期间发生的错误。 每当发生让Python不知所措的错误时， 它都会创建一个异常对象。 如果你编写了处理该异常的代码， 程序将继续运行； 如果你未对异常进行处理， 程序将停止， 并显示一个traceback， 其中包含有关异常的报告。

异常是使用try-except 代码块处理的。 try-except 代码块让Python执行指定的操作， 同时告诉Python发生异常时怎么办。 使用了try-except 代码块时， 即便出现异常，程序也将继续运行： 显示你编写的友好的错误消息， 而不是令用户迷惑的traceback。

### 3.1处理ZeroDivisonError异常

0不能做除数

```python
print(5/0)
#输出#
Traceback (most recent call last):
    File "division.py", line 1, in <module>
        print(5/0)
ZeroDivisionError: division by zero
```

### 3.2使用try-except代码块

处理ZeroDivisionError 异常的try-except 代码块类似于下面这样：

```python
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!'")
#输出#
You can't divide by zero!
```

我们将导致错误的代码行print(5/0) 放在了一个try 代码块中。 如果try 代码块中的代码运行起来没有问题， Python将跳过except 代码块； 如果try 代码块中的代码导致了错误， Python将查找这样的except 代码块， 并运行其中的代码， 即其中指定的错误与引发的错误相同。

### 3.3使用异常避免崩溃

未进行异常处理的除法程序，当除数为0时发生错误。

```python
print("Give me two numbers,and I will divide them.")
print("Enter 'q' to quit.")

while True:
    first_number=input("\nFirst number:")
    if first_number=='q':
        break
    second_number=input("second number:")
    if second_number=='q':
        break
    answer=int(first_number)/int(second_number)
    print(answer)
#除数为0时，发生错误#
Give me two numbers, and I'll divide them.
Enter 'q' to quit.

First number: 5
Second number: 0
Traceback (most recent call last):
    File "division.py", line 9, in <module>
        answer = int(first_number) / int(second_number)
ZeroDivisionError: division by zero
```

### 3.4else代码块

通过将可能引发错误的代码放在try-except 代码块中， 可提高这个程序抵御错误的能力。 错误是执行除法运算的代码行导致的， 因此我们需要将它放到try-except 代码块中。 这个示例还包含一个else 代码块； 依赖于try 代码块成功执行的代码都应放到else 代码块中。

```python
print("Give me two numbers,and I will divide them.")
print("Enter 'q' to quit.")

while True:
    first_number=input("\nFirst number:")
    if first_number=='q':
        break
    second_number=input("second number:")
    try:
        answer=int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("you can't divide by 0!'")
    else:
        print(answer)
```

我们让Python尝试执行try 代码块中的除法运算 ， 这个代码块只包含可能导致错误的代码。 依赖于try 代码块成功执行的代码都放在else 代码块中； 在这个示例中， 如果除法运算成功， 我们就使用else 代码块来打印结果 。

try-except-else 代码块的工作原理大致如下： Python尝试执行try 代码块中的代码； 只有可能引发异常的代码才需要放在try 语句中。 有时候， 有一些仅在try 代码块成功执行时才需要运行的代码； 这些代码应放在else 代码块中。 except 代码块告诉Python， 如果它尝试运行try 代码块中的代码时引发了指定的异常， 该怎么办。

### 3.5处理FileNotFoundError异常

使用文件时， 一种常见的问题是找不到文件： 你要查找的文件可能在其他地方、 文件名可能不正确或者这个文件根本就不存在。 对于所有这些情形， 都可使用try-except 代码块以直观的方式进行处理。

```python
filename='alice.txt'

try:
    with open(filename) as f_obj:
        contents=f_obj.read()
except FileNotFoundError:
    msg="sorry,the file "+filename+" does not exist."
    print(msg)
```

## 4存储数据

很多程序都要求用户输入某种信息， 如让用户存储游戏首选项或提供要可视化的数据。 不管专注的是什么， 程序都把用户提供的信息存储在列表和字典等数据结构中。 用户关闭程序时， 你几乎总是要保存他们提供的信息； 一种简单的方式是使用模块json 来存储数据。

模块json 让你能够将简单的Python数据结构转储到文件中， 并在程序再次运行时加载该文件中的数据。 你还可以使用json 在Python程序之间分享数据。 更重要的是， JSON数据格式并非Python专用的， 这让你能够将以JSON格式存储的数据与使用其他编程语言的人分享。 这是一种轻便格式， 很有用， 也易于学习。

JSON（JavaScript Object Notation） 格式最初是为JavaScript开发的， 但随后成了一种常见格式， 被包括Python在内的众多语言采用。

### 4.1使用json.dump()和json.load()

函数json.dump() 接受两个实参： 要存储的数据以及可用于存储数据的文件对象。 下面演示了如何使用json.dump() 来存储数字列表：

```python
import json

numbers=[2,3,5,7,,11,13]

filename='numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)
```

我们先导入模块json ， 再创建一个数字列表。 在第5行处， 我们指定了要将该数字列表存储到其中的文件的名称。 通常使用文件扩展名.json来指出文件存储的数据为JSON格式。 接下来， 我们以写入模式打开这个文件， 让json 能够将数据写入其中 。 在第7行处， 我们使用函数json.dump() 将数字列表存储到文件numbers.json中。

```python
import json
filename='numbers.json'
with open(filename) as f_obj:
    numbers=json.load(f_obj)
print(numbers)
#输出#
[2, 3, 5, 7, 11, 13]
```

在第2行处， 我们确保读取的是前面写入的文件。 这次我们以读取方式打开这个文件， 因为Python只需读取这个文件 。 在第4行处， 我们使用函数json.load() 加载存储在numbers.json中的信息， 并将其存储到变量numbers 中。 最后， 我们打印恢复的数字列表， 看看它是否与number_writer.py中创建的数字列表相同。

# 测试代码



## 1.测试函数

Python标准库中的模块unittest 提供了代码测试工具。单元测试用于核实函数的某个方面没有问题；测试用例 是一组单元测试， 这些单元测试一起核实函数在各种情形下的行为都符合要求。 良好的测试用例考虑到了函数可能收到的各种输入， 包含针对所有这些情形的测试。全覆盖式测试用例包含一整套单元测试， 涵盖了各种可能的函数使用方式。 对于大型项目， 要实现全覆盖可能很难。 通常， 最初只要针对代码的重要行为编写测试即可， 等项目被广泛使用时再考虑全覆盖。

要为函数编写测试用例， 可先导入模块unittest 以及要测试的函数， 再创建一个继承unittest.TestCase 的类， 并编写一系列方法对函数行为的不同方面进行测试。

test_name_function.py

```python
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""
    
    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的名字吗?"""
        formatted_name=get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')
        
unittest.main()
```

首先， 我们导入了模块unittest 和要测试的函数get_formatted_name() 。 在第4行处， 我们创建了一个名为NamesTestCase 的类， 用于包含一系列针对get_formatted_name() 的单元测试。 你可随便给这个类命名， 但最好让它看起来与要测试的函数相关， 并包含字样Test。 这个类必须继承unittest.TestCase 类， 这样Python才知道如何运行你编写的测试。

NamesTestCase 只包含一个方法， 用于测试get_formatted_name() 的一个方面。 我们将这个方法命名为test_first_last_name() ， 因为我们要核实的是只有名和姓的姓名能否被正确地格式化。 我们运行testname_function.py时， 所有以test 打头的方法都将自动运行。 在这个方法中， 我们调用了要测试的函数， 并存储了要测试的返回值。在这个示例中， 我们使用实参'janis' 和'joplin' 调用get_formatted_name() ， 并将结果存储到变量formatted_name 中 。

在第10行处， 我们使用了unittest 类最有用的功能之一： 一个断言 方法。 断言方法用来核实得到的结果是否与期望的结果一致。 在这里， 我们知道get_formatted_name() 应返回这样的姓名， 即名和姓的首字母为大写， 且它们之间有一个空格， 因此我们期望formatted_name 的值为Janis Joplin 。 为检查是否确实如此， 我们调用unittest的方法assertEqual() ， 并向它传递formatted_name 和'Janis Joplin' 。 代码行self.assertEqual(formatted_name, 'Janis Joplin') 的意思是说： “将formatted_name 的值同字符串'Janis Joplin' 进行比较， 如果它们相等， 就万事大吉， 如果它们不相等， 跟我说一声！

## 2测试类

Python在unittest.TestCase 类中提供了很多断言方法。断言方法检查你认为应该满足的条件是否确实满足。 如果该条件确实满足， 你对程序行为的假设就得到了确认， 你就可以确信其中没有错误。 如果你认为应该满足的条件实际上并不满足， Python将引发异常。

### 2.1各种断言方法

| 方法 | 用途 |
| - | - |
| assertEqual(a,b) | 核实a==b |
| assertNotEqual(a,b) | 核实a!=b |
| assertTrue(x) | 核实x为True |
| assertFalse(x) | 核实x为False |
| assertIn(item,list) | 核实 item 在 list 中 |
| assertNotIn(item,list) | 核实 item 不在 list 中 |


使用这些方法可核实返回的值等于或不等于预期的值、 返回的值为True 或False 、 返回的值在列表中或不在列表中。 你只能在继承unittest.TestCase 的类中使用这些方法。 

### 2.2一个要测试的类

类的测试与函数的测试相似——你所做的大部分工作都是测试类中方法的行为， 但存在一些不同之处， 下面来编写一个类进行测试。 来看一个帮助管理匿名调查的类：

```python
class AnonymousSurvey():
    """收集匿名调查问卷的答案"""
    def __init__(self, question):
        """存储一个问题， 并为存储答案做准备"""
        self.question = question
        self.responses = []
        
    def show_question(self):
        """显示调查问卷"""
        print(question)
        
    def store_response(self, new_response):
        """存储单份调查答卷"""
        self.responses.append(new_response)

    def show_results(self):
        """显示收集到的所有答卷"""
        print("Survey results:")
        for response in responses:
            print('- ' + response)
```

这个类首先存储了一个你指定的调查问题 ， 并创建了一个空列表， 用于存储答案。 这个类包含打印调查问题的方法 、 在答案列表中添加新答案的方法以及将存储在列表中的答案都打印出来的方法 。 要创建这个类的实例， 只需提供一个问题即可。 有了表示调查的实例后， 就可使用show_question() 来显示其中的问题， 可使用store_response() 来存储答案， 并使用show_results() 来显示调查结果。

### 2.3测试AnonymousSurvey类

下面来编写一个测试， 对AnonymousSurvey 类的行为的一个方面进行验证： 如果用户面对调查问题时只提供了一个答案， 这个答案也能被妥善地存储。 为此， 我们将在这个答案被存储后， 使用方法assertIn() 来核实它包含在答案列表中：

```python
import unittest
from survey import AnonymousSurvey

class TestAnonmyousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""
    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        elf.assertIn('English', my_survey.responses)

unittest.main()
```

### 2.4方法setUp()

如果你在TestCase 类中包含了方法setUp() ， Python将先运行它， 再运行各个以test_打头的方法。 这样， 在你编写的每个测试方法中都可使用在方法setUp() 中创建的对象了。

```python
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""

    def setUp(self):
        """
创建一个调查对象和一组答案， 供使用的测试方法使用
"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
        
    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()
```

方法setUp() 做了两件事情： 创建一个调查对象 ； 创建一个答案列表 。 存储这两样东西的变量名包含前缀self （即存储在属性中） ， 因此可在这个类的任何地方使用。

