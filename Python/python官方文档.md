# python速览

## python用作计算器

### 数字

在解释器中，整数的类型是int，小数的类型是float。

除法运算（/）返回浮点数。用 // 运算符执行floor division 的结果是整数（忽略小数）；计算余数用 %；floor division -- 向下取整除法

Python 用 ** 运算符计算乘方。

```python
>>> 5 ** 2 # 5 squared
25
>>> 2 ** 7 # 2 to the power of 7
128
```

Python 全面支持浮点数；混合类型运算数的运算会把整数转换为浮点数：

交互模式下，上次输出的表达式会赋给变量 _。把 Python 当作计算器时，用该变量实现下一步计算更简单，例如：

```python
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
```

### 字符串

除了数字， Python 还可以操作字符串。字符串有多种表现形式，用单引号（'…… '）或双引号（"…… "）标注的结果相同。反斜杠 \ 用于转义。

如果不希望前置 \ 的字符转义成特殊字符，可以使用 原始字符串，在引号前添加 r 即可。

```python
>>> print('C:\some\name') # here \n means newline!
C:\some
ame
>>> print(r'C:\some\name') # note the r before the quote
C:\some\name
```

字符串字面值可以包含多行。一种实现方式是使用三重引号： """...""" 或 '''...'''。字符串中将自动包括行结束符，但也可以在换行的地方添加一个 \ 来避免此情况。参见以下示例：

```python
print("""\
Usage: thingy [OPTIONS]
-h Display this usage message
-H hostname Hostname to connect to
""")
```

输出如下（请注意开始的换行符没有被包括在内）：

```
Usage: thingy [OPTIONS]
-h Display this usage message
-H hostname Hostname to connect to
```

字符串可以用 + 合并（粘到一起），也可以用 * 重复:

```python
>>> # 3 times 'un', followed by 'ium'
>>> 3 * 'un' + 'ium'
'unununium'
```

相邻的两个或多个 字符串字面值（引号标注的字符）会自动合并：

```python
>>> 'Py' 'thon'
'Python'
```

字符串支持 索引（下标访问），第一个字符的索引是 0。单字符没有专用的类型，就是长度为一的字符串：

```python
>>> word = 'Python'
>>> word[0] # character in position 0
'P'
>>> word[5] # character in position 5
'n
```

索引还支持负数，用负数索引时，从右边开始计数：

```python
>>> word[-1] # last character
'n'
>>> word[-2] # second-last character
'o'
>>> word[-6]
'P'
```

注意， -0 和 0 一样，因此，负数索引从 -1 开始。


除了索引，字符串还支持 切片。索引可以提取单个字符， 切片则提取子字符串：

```python
>>> word[0:2] # characters from position 0 (included) to 2 (excluded)
'Py'
>>> word[2:5] # characters from position 2 (included) to 5 (excluded)
'tho'
```

切片索引的默认值很有用；省略开始索引时，默认值为 0，省略结束索引时，默认为到字符串的结尾：

```python
>>> word[:2] # character from the beginning to position 2 (excluded)
'Py'
>>> word[4:] # characters from position 4 (included) to the end
'on'
>>> word[-2:] # characters from the second-last (included) to the end
'on'
```

注意，输出结果包含切片开始，但不包含切片结束。因此， s[:i] + s[i:] 总是等于 s：

```python
>>> word[:2] + word[2:]
'Python'
>>> word[:4] + word[4:]
'Python'
```

切片会自动处理越界索引：

```python
>>> word[4:42]
'on'
>>> word[42:]
''
```

Python 字符串不能修改，是immutable 的。因此，为字符串中某个索引位置赋值会报错。要生成不同的字符串，应新建一个字符串：

```python
>>> 'J' + word[1:]
'Jython'
>>> word[:2] + 'py'
'Pypy'
```

内置函数 len() 返回字符串的长度。

### 列表

Python 支持多种 复合数据类型，可将不同值组合在一起。最常用的 列表，是用方括号标注，逗号分隔的一组值。 列表可以包含不同类型的元素，但一般情况下，各个元素的类型相同：

```python
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
```

和字符串（及其他内置sequence 类型）一样，列表也支持索引和切片。

切片操作返回包含请求元素的新列表。以下切片操作会返回列表的 浅拷贝：

```python
>>> squares[:]
[1, 4, 9, 16, 25]
```

列表还支持合并操作：

```python
>>> squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

与immutable 字符串不同, 列表是mutable 类型，其内容可以改变：

```python
>>> cubes = [1, 8, 27, 65, 125] # something's wrong here
>>> 4 ** 3 # the cube of 4 is 64, not 65!
64
>>> cubes[3] = 64 # replace the wrong value
>>> cubes
[1, 8, 27, 64, 125]
```

append() 方法可以在列表结尾添加新元素:

```python
>>> cubes.append(216) # add the cube of 6
>>> cubes.append(7 ** 3) # and the cube of 7
>>> cubes
[1, 8, 27, 64, 125, 216, 343]
```

为切片赋值可以改变列表大小，甚至清空整个列表：

```python
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> # replace some values
>>> letters[2:5] = ['C', 'D', 'E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> # now remove them
>>> letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
>>> # clear the list by replacing all the elements with an empty list
>>> letters[:] = []
>>> letters
[]
```

内置函数 len() 也支持列表。

还可以嵌套列表（创建包含其他列表的列表），例如：

```python
>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
```

### 走向编程第一步

```python
>>> # Fibonacci series:
... # the sum of two elements defines the next
... a, b = 0, 1
>>> while a < 10:
...     print(a)
...     a, b = b, a+b
...
0 
1
1 
2 
3 
5 
8
```

第一行中的 多重赋值：变量 a 和 b 同时获得新值 0 和 1。最后一行又用了一次多重赋值，这体现在右表达式在赋值前就已经求值了。右表达式求值顺序为从左到右。

```python
>>> i = 256*256
>>> print('The value of i is', i)
The value of i is 65536
```

关键字参数 end 可以取消输出后面的换行, 或用另一个字符串结尾：

```python
>>> a, b = 0, 1
>>> while a < 1000:
...     print(a, end=',')
...     a, b = b, a+b
...
0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
```

## 流程控制

### if语句

if 语句包含零个或多个 elif 子句及可选的 else 子句。

### for语句

Python 的 for 语句与 C 或 Pascal 中的不同。 Python 的 for 语句不迭代算术递增数值（如 Pascal），或是
给予用户定义迭代步骤和暂停条件的能力（如 C），而是迭代列表或字符串等任意序列，元素的迭代顺序
与在序列中出现的顺序一致。例如:

```python
>>> # Measure some strings:
... words = ['cat', 'window', 'defenestrate']
>>> for w in words:
...     print(w, len(w))
...
cat 3
window 6
defenestrate 12
```

遍历集合时修改集合的内容，会很容易生成错误的结果。因此不能直接进行循环，而是应遍历该集合的
副本或创建新的集合：

```python
# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy: Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
        
# Strategy: Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
```

### range()函数

内置函数 range() 常用于遍历数字序列，该函数可以生成算术级数：

```python
>>> for i in range(5):
...     print(i)
...
0 
1
2
3
4
```

生成的序列不包含给定的终止数值； range(10) 生成 10 个值，这是一个长度为 10 的序列，其中的元素
索引都是合法的。 range 可以不从 0 开始，还可以按指定幅度递增（递增幅度称为’ 步进’，支持负数）：

```python
>>> list(range(5, 10))
[5, 6, 7, 8, 9]
>>> list(range(0, 10, 3))
[0, 3, 6, 9]
>>> list(range(-10, -100, -30))
[-10, -40, -70]
```

range() 和 len() 组合在一起，可以按索引迭代序列：

```python
>>> a = ['Mary', 'had', 'a', 'little', 'lamb']
>>> for i in range(len(a)):
...     print(i, a[i])
...
0 Mary
1 had
2 a
3 little
4 lamb
```

如果只输出 range，会出现意想不到的结果：

```python
>>> range(10)
range(0, 10)
```

range() 返回对象的操作和列表很像，但其实这两种对象不是一回事。迭代时，该对象基于所需序列返
回连续项，并没有生成真正的列表，从而节省了空间。


这种对象称为可迭代对象iterable，函数或程序结构可通过该对象获取连续项，直到所有元素全部迭代完
毕。 for 语句就是这样的架构， sum() 是一种把可迭代对象作为参数的函数：

```python
>>> sum(range(4)) # 0 + 1 + 2 + 3
6
```

###  循环中的 break、 continue 语句及 else 子句

break 语句和 C 中的类似，用于跳出最近的 for 或 while 循环。


循环语句支持 else 子句； for 循环中，可迭代对象中的元素全部循环完毕，或 while 循环的条件为假
时，执行该子句； break 语句终止循环时，不执行该子句。请看下面这个查找素数的循环示例：

```python
>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print(n, 'equals', x, '*', n//x)
...             break
...     else:
...         # loop fell through without finding a factor
...         print(n, 'is a prime number')
...
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```

与 if 语句相比，循环的 else 子句更像 try 的 else 子句： try 的 else 子句在未触发异常时执行，循
环的 else 子句则在未运行 break 时执行。 

### pass语句

pass 语句不执行任何操作。语法上需要一个语句，但程序不实际执行任何动作时，可以使用该语句。例
如：

```python
>>> while True:
...     pass # Busy-wait for keyboard interrupt (Ctrl+C)
...
```

pass 还可以用作函数或条件子句的占位符，让开发者聚焦更抽象的层次。此时，程序直接忽略 pass：

```python
>>> def initlog(*args):
...     pass # Remember to implement this!
...
```

### match语句

match 语句接受一个表达式并将其值与作为一个或多个 case 块给出的连续模式进行比较。 这在表面上类似于 C、Java 或 JavaScript（以及许多其他语言）中的 switch 语句，但它更类似于 Rust 或 Haskell 等语言中的模式匹配。 只有匹配的第一个模式被执行，它还可以从值中提取组件（序列元素或对象属性）到变量中。

最简单的形式是将一个目标值与一个或多个字面值进行比较：

```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
    
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
```

注意最后一个代码块：“变量名” _ 被作为 通配符并必定会匹配成功。如果没有 case 语句匹配成功，则
不会执行任何分支。

使用 | （“or ”）在一个模式中可以组合多个字面值：

```python
case 401 | 403 | 404:
    return "Not allowed"
```

其他功能暂时省略。

### 定义函数

Python从入门到实践中函数章节

return 语句返回函数的值。 return 语句不带表达式参数时，返回 None。函数执行完毕退出也
返回 None。

默认值在 定义作用域里的函数定义中求值，所以：

```python
i = 5
def f(arg=i):
    print(arg)
    
i = 6
f()
#输出5
```

重要警告： 默认值只计算一次。默认值为列表、字典或类实例等可变对象时，会产生与该规则不同的结
果。例如，下面的函数会累积后续调用时传递的参数：

```python
def f(a, L=[]):
    L.append(a)
    return L
    
print(f(1))
print(f(2))
print(f(3))
```

输出如下:

```python
[1]
[1, 2]
[1, 2, 3]
```

不想在后续调用之间共享默认值时，应以如下方式编写函数：

```python
def f(a, L=None):
    if L is None:
        L = []        
L.append(a)
return L
```

默认情况下，参数可以按位置或显式关键字传递给 Python 函数。为了让代码易读、高效，最好限制参数
的传递方式，这样，开发者只需查看函数定义，即可确定参数项是仅按位置、按位置或关键字，还是仅
按关键字传递。

```python
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    -----------      ----------     ----------
            |             |               |
            |     Positional or keyword   |
            |                              - Keyword only
            -- Positional only
```

- 函数定义中未使用 / 和 * 时，参数可以按位置或关键字传递给函数。

- 仅限位置时，形参的顺序很重要，且这些形参不
能用关键字传递。仅限位置形参应放在 / （正斜杠）前。 / 用于在逻辑上分割仅限位置形参与其它形参。
如果函数定义中没有 /，则表示没有仅限位置形参。
/ 后可以是 位置或关键字或 仅限关键字形参。

- 把形参标记为 仅限关键字，表明必须以关键字参数形式传递该形参，应在参数列表中第一个 仅限关键字
形参前添加 *。

解包实参列表:

函数调用要求独立的位置参数，但实参在列表或元组里时，要执行相反的操作。例如，内置的 range()
函数要求独立的 start 和 stop 实参。如果这些参数不是独立的，则要在调用函数时，用 * 操作符把实参从
列表或元组解包出来：

```python
>>> list(range(3, 6)) # normal call with separate arguments
[3, 4, 5]
>>> args = [3, 6]
>>> list(range(*args)) # call with arguments unpacked from a list
[3, 4, 5]
```

同样，字典可以用 ** 操作符传递关键字参数：

```python
>>> def parrot(voltage, state='a stiff', action='voom'):
...     print("-- This parrot wouldn't", action, end=' ')
...     print("if you put", voltage, "volts through it.", end=' ')
...     print("E's", state, "!")
...
>>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
>>> parrot(**d)
-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin
,!' demised !
```



Lambda表达式:

略



文档字符串：

```python
>>> def my_function():
...     """Do nothing, but document it.
...
...     No, really, it doesn't do anything.
...     """
...     pass
...
>>> print(my_function.__doc__)
Do nothing, but document it.

    No, really, it doesn't do anything.
```



函数注解：

标注以字典的形式存放在函数的 __annotations__ 属性中，并且不会影响函数的任何其他部分。形
参标注的定义方式是在形参名后加冒号，后面跟一个表达式，该表达式会被求值为标注的值。返回值标
注的定义方式是加组合符号 ->，后面跟一个表达式，该标注位于形参列表和表示 def 语句结束的冒号
之间。下面的示例有一个必须的参数，一个可选的关键字参数以及返回值都带有相应的标注:

```python
>>> def f(ham: str, eggs: str = 'eggs') -> str:
...     print("Annotations:", f.__annotations__)
...     print("Arguments:", ham, eggs)
...     return ham + ' and ' + eggs
...
>>> f('spam')
Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
Arguments: spam eggs
'spam and eggs'
```

# 数据结构

## 列表详解

列表数据类型支持很多方法，列表对象的所有方法所示如下：

list.append(x)

在列表末尾添加一个元素，相当于 a[len(a):] = [x]

list.extend(iterable)


用可迭代对象的元素扩展列表。相当于 a[len(a):] = iterable 。

list.insert(i, x)


在指定位置插入元素。第一个参数是插入元素的索引，因此， a.insert(0, x) 在列表开头插入
元素， a.insert(len(a), x) 等同于 a.append(x) 。

list.remove(x)


从列表中删除第一个值为 x 的元素。未找到指定元素时，触发 ValueError 异常。

list.pop([i])
删除列表中指定位置的元素，并返回被删除的元素。未指定位置时， a.pop() 删除并返回列表的
最后一个元素。（方法签名中 i 两边的方括号表示该参数是可选的，不是要求输入方括号。这种表
示法常见于 Python 参考库）。

list.clear()


删除列表里的所有元素，相当于 del a[:] 。

list.index(x[, start[, end]])
返回列表中第一个值为 x 的元素的零基索引。未找到指定元素时，触发 ValueError 异常。
可选参数 start 和 end 是切片符号，用于将搜索限制为列表的特定子序列。返回的索引是相对于整
个序列的开始计算的，而不是 start 参数。

list.count(x)


返回列表中元素 x 出现的次数。

list.sort(*, key=None, reverse=False)

就地排序列表中的元素（要了解自定义排序参数，详见 sorted()）。

list.reverse()


翻转列表中的元素。

list.copy()


返回列表的浅拷贝。相当于 a[:] 。

```python
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> fruits.count('tangerine')
0
>>> fruits.index('banana')
3
>>> fruits.index('banana', 4) # Find next banana starting a position 4
6
>>> fruits.reverse()
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear
```

insert、 remove、 sort 等方法只修改列表，不输出返回值——返回的默认值为 None 。这是所有
Python 可变数据结构的设计原则。

还有，不是所有数据都可以排序或比较。例如， [None, 'hello', 10] 就不可排序，因为整数不能与字符串对比，而 None 不能与其他类型对比。有些类型根本就没有定义顺序关系，例如， 3+4j < 5+7j这种对比操作就是无效的。

### 用列表实现堆栈

使用列表方法实现堆栈非常容易，最后插入的最先取出（“后进先出”）。把元素添加到堆栈的顶端，使用
append() 。从堆栈顶部取出元素，使用 pop() ，不用指定索引。例如

```python
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]
```

### 用列表实现队列

列表也可以用作队列，最先加入的元素，最先取出（“先进先出”）；然而，列表作为队列的效率很低。因
为，在列表末尾添加和删除元素非常快，但在列表开头插入或移除元素却很慢（因为所有其他元素都必
须移动一位）。

实现队列最好用 collections.deque，可以快速从两端添加或删除元素。例如：

```python
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry") # Terry arrives
>>> queue.append("Graham") # Graham arrives
>>> queue.popleft() # The first to arrive now leaves
'Eric'
>>> queue.popleft() # The second to arrive now leaves
'John'
>>> queue # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```

### 列表推导式

列表推导式创建列表的方式更简洁。常见的用法为，对序列或可迭代对象中的每个元素应用某种操作，
用生成的结果创建新的列表；或用满足特定条件的元素创建子序列。

```python
>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

注意，这段代码创建（或覆盖）变量 x，该变量在循环结束后仍然存在。下述方法可以无副作用地计算
平方列表：

```python
squares = [x**2 for x in range(10)]
```

列表推导式的方括号内包含以下内容：一个表达式，后面为一个 for 子句，然后，是零个或多个 for 或
if 子句。结果是由表达式依据 for 和 if 子句求值计算而得出一个新列表。举例来说，以下列表推导式
将两个列表中不相等的元素组合起来：

```python
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

等价于：

```python
>>> combs = []
>>> for x in [1,2,3]:
...     for y in [3,1,4]:
...         if x != y:
...             combs.append((x, y))
...
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

表达式是元组（例如上例的 (x, y)）时，必须加上括号：

```python
>>> vec = [-4, -2, 0, 2, 4]
>>> # create a new list with the values doubled
>>> [x*2 for x in vec]
[-8, -4, 0, 4, 8]
>>> # filter the list to exclude negative numbers
>>> [x for x in vec if x >= 0]
[0, 2, 4]
>>> # apply a function to all the elements
>>> [abs(x) for x in vec]
[4, 2, 0, 2, 4]
>>> # call a method on each element
>>> freshfruit = [' banana', ' loganberry ', 'passion fruit ']
>>> [weapon.strip() for weapon in freshfruit]
['banana', 'loganberry', 'passion fruit']
>>> # create a list of 2-tuples like (number, square)
>>> [(x, x**2) for x in range(6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
>>> # the tuple must be parenthesized, otherwise an error is raised
>>> [x, x**2 for x in range(6)]
File "<stdin>", line 1, in <module>
[x, x**2 for x in range(6)]
^
SyntaxError: invalid syntax
>>> # flatten a list using a listcomp with two 'for'
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

列表推导式可以使用复杂的表达式和嵌套函数：

```python
>>> from math import pi
>>> [str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']
```

## del语句

del 语句按索引，而不是值从列表中移除元素。与返回值的 pop() 方法不同， del 语句也可以从列表中
移除切片，或清空整个列表（之前是将空列表赋值给切片）。例如：

```python
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
```

del 也可以用来删除整个变量：

```python
>>> del a
```

此后，再引用 a 就会报错（直到为它赋与另一个值）。后文会介绍 del 的其他用法。

## 元组和序列

列表和字符串有很多共性，例如，索引和切片操作。这两种数据类型是 序列（参见 typesseq）。随着 Python
语言的发展，其他的序列类型也被加入其中。本节介绍另一种标准序列类型： 元组。

元组由多个用逗号隔开的值组成，例如：

```python
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> # Tuples may be nested:
... u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> # Tuples are immutable:
... t[0] = 88888
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> # but they can contain mutable objects:
... v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])
```

输出时，元组都要由圆括号标注，这样才能正确地解释嵌套元组。输入时，圆括号可有可无，不过经常
是必须的（如果元组是更大的表达式的一部分）。不允许为元组中的单个元素赋值，当然，可以创建含列
表等可变对象的元组。

虽然，元组与列表很像，但使用场景不同，用途也不同。元组是immutable（不可变的），一般可包含异质
元素序列，通过解包（见本节下文）或索引访问（如果是 namedtuples，可以属性访问）。列表是mutable
（可变的），列表元素一般为同质类型，可迭代访问。

构造 0 个或 1 个元素的元组比较特殊：为了适应这种情况，对句法有一些额外的改变。用一对空圆括号
就可以创建空元组；只有一个元素的元组可以通过在这个元素后添加逗号来构建（圆括号里只有一个值
的话不够明确）。丑陋，但是有效。例如：

```python
>>> empty = ()
>>> singleton = 'hello', # <-- note trailing comma
>>> len(empty)
0
>>> len(singleton)
1
>>> singleton
('hello',)
```

语句 t = 12345, 54321, 'hello!' 是 元组打包的例子：值 12345, 54321 和 'hello!' 一起被打
包进元组。逆操作也可以：

```python
>>> x, y, z = t
```

称之为 序列解包也是妥妥的，适用于右侧的任何序列。序列解包时，左侧变量与右侧序列元素的数量应
相等。注意，多重赋值其实只是元组打包和序列解包的组合。

## 集合

Python 还支持 集合这种数据类型。集合是由不重复元素组成的无序容器。基本用法包括成员检测、消除
重复元素。集合对象支持合集、交集、差集、对称差分等数学运算。

创建集合用花括号或 set() 函数。注意，创建空集合只能用 set()，不能用 {}， {} 创建的是空字典，
下一小节介绍数据结构：字典。

```python
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket) # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket # fast membership testing
True
>>> 'crabgrass' in basket
False
>>> # Demonstrate set operations on unique letters from two words
...
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b # letters in both a and b
{'a', 'c'}
>>> a ^ b # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
```

与列表推导式 类似，集合也支持推导式：

```python
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}
```

## 字典

字典以 关键字为索引，关键字通常是字符串或数字，也可
以是其他任意不可变类型。只包含字符串、数字、元组的元组，也可以用作关键字。但如果元组直接或间
接地包含了可变对象，就不能用作关键字。列表不能当关键字，因为列表可以用索引、切片、 append()
、 extend() 等方法修改。

可以把字典理解为 键值对的集合，但字典的键必须是唯一的。花括号 {} 用于创建空字典。另一种初始
化字典的方式是，在花括号里输入逗号分隔的键值对，这也是字典的输出方式。

字典的主要用途是通过关键字存储、提取值。用 del 可以删除键值对。用已存在的关键字存储值，与该
关键字关联的旧值会被取代。通过不存在的键提取值，则会报错。

对字典执行 list(d) 操作，返回该字典中所有键的列表，按插入次序排列（如需排序，请使用
sorted(d)）。检查字典里是否存在某个键，使用关键字 in。

```python
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>> list(tel)
['jack', 'guido', 'irv']
>>> sorted(tel)
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False
```

dict() 构造函数可以直接用键值对序列创建字典：

```python
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

字典推导式可以用任意键值表达式创建字典：

```python
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
```

关键字是比较简单的字符串时，直接用关键字参数指定键值对更便捷：

```python
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

## 循环的技巧

在字典中循环时，用 items() 方法可同时取出键和对应的值：

```python
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
...
gallahad the pure
robin the brave
```

在序列中循环时，用 enumerate() 函数可以同时取出位置索引和对应的值：

```python
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe
```

同时循环两个或多个序列时，用 zip() 函数可以将其内的元素一一匹配：

```python
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}? It is {1}.'.format(q, a))
...
What is your name? It is lancelot.
What is your quest? It is the holy grail.
What is your favorite color? It is blue.
```

逆向循环序列时，先正向定位序列，然后调用 reversed() 函数：

```python
>>> for i in reversed(range(1, 10, 2)):
...     print(i)
...
9
7
5
3
1
```

按指定顺序循环序列，可以用 sorted() 函数，在不改动原序列的基础上，返回一个重新的序列：

```python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for i in sorted(basket):
...     print(i)
...
apple
apple
banana
orange
orange
pear
```

使用 set() 去除序列中的重复元素。使用 sorted() 加 set() 则按排序后的顺序，循环遍历序列中的
唯一元素：

```python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...     print(f)
...
apple
banana
orange
pear
```

一般来说，在循环中修改列表的内容时，创建新列表比较简单，且安全：

```python
>>> import math
>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> filtered_data = []
>>> for value in raw_data:
...     if not math.isnan(value):
...         filtered_data.append(value)
...
>>> filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]
```

## 深入条件控制

while 和 if 条件句不只可以进行比较，还可以使用任意运算符。


比较运算符 in 和 not in 用于执行确定一个值是否存在（或不存在）于某个容器中的成员检测。运算
符 is 和 is not 用于比较两个对象是否是同一个对象。所有比较运算符的优先级都一样，且低于任何
数值运算符。


比较操作支持链式操作。例如， a < b == c 校验 a 是否小于 b，且 b 是否等于 c。


比较操作可以用布尔运算符 and 和 or 组合，并且，比较操作（或其他布尔运算）的结果都可以用 not
取反。这些操作符的优先级低于比较操作符； not 的优先级最高， or 的优先级最低，因此， A and not
B or C 等价于 (A and (not B)) or C。与其他运算符操作一样，此处也可以用圆括号表示想要的
组合。


布尔运算符 and 和 or 也称为 短路运算符：其参数从左至右解析，一旦可以确定结果，解析就会停止。
例如，如果 A 和 C 为真， B 为假，那么 A and B and C 不会解析 C。用作普通值而不是布尔值时，短
路操作符返回的值通常是最后一个变量。
还可以把比较操作或逻辑表达式的结果赋值给变量，例如：

```python
>>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
>>> non_null = string1 or string2 or string3
>>> non_null
'Trondheim'
```

## 序列和其他类型的比较

序列对象可以与相同序列类型的其他对象比较。这种比较使用 字典式顺序：首先，比较前两个对应元素，
如果不相等，则可确定比较结果；如果相等，则比较之后的两个元素，以此类推，直到其中一个序列结
束。如果要比较的两个元素本身是相同类型的序列，则递归地执行字典式顺序比较。如果两个序列中所
有的对应元素都相等，则两个序列相等。如果一个序列是另一个的初始子序列，则较短的序列可被视为
较小（较少）的序列。对于字符串来说，字典式顺序使用 Unicode 码位序号排序单个字符。下面列出了
一些比较相同类型序列的例子：

```python
(1, 2, 3) < (1, 2, 4)
[1, 2, 3] < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4) < (1, 2, 4)
(1, 2) < (1, 2, -1)
(1, 2, 3) == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4)
```

注意，对不同类型的对象来说，只要待比较的对象提供了合适的比较方法，就可以使用 < 和 > 进行比较。
例如，混合数值类型通过数值进行比较，所以， 0 等于 0.0，等等。否则，解释器不会随便给出一个对比
结果，而是触发 TypeError 异常。

# 模块

Python 把各种定义存入一个文件，在脚本或解释器的交互式实例中使用。这个文件就
是 模块；模块中的定义可以 导入到其他模块或 主模块（在顶层和计算器模式下，执行脚本中可访问的
变量集）。

模块是包含 Python 定义和语句的文件。其文件名是模块名加后缀名 .py 。在模块内部，通过全局变量
__name__ 可以获取模块名（即字符串）。例如，用文本编辑器在当前目录下创建 fibo.py 文件，输入
以下内容：

```python
# Fibonacci numbers module
def fib(n): # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
    
def fib2(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```

现在，进入 Python 解释器，用以下命令导入该模块：

```python
>>> import fibo
```

这项操作不直接把 fibo 函数定义的名称导入到当前符号表，只导入模块名 fibo 。要使用模块名访问
函数：

```python
>>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibo.__name__
'fibo'
```

如果经常使用某个函数，可以把它赋值给局部变量：

```python
>>> fib = fibo.fib
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

## 模块详解

模块包含可执行语句及函数定义。这些语句用于初始化模块，且仅在 import 语句 第一次遇到模块名时执
行。 (文件作为脚本运行时，也会执行这些语句。 )

模块有自己的私有符号表，用作模块中所有函数的全局符号表。因此，在模块内使用全局变量时，不用
担心与用户定义的全局变量发生冲突。另一方面，可以用与访问模块函数一样的标记法，访问模块的全
局变量， modname.itemname。

可以把其他模块导入模块。按惯例，所有 import 语句都放在模块（或脚本）开头，但这不是必须的。
被导入的模块名存在导入方模块的全局符号表里。

import 语句有一个变体，可以直接把模块里的名称导入到另一个模块的符号表。例如：

```python
>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

还有一种变体可以导入模块内定义的所有名称：

```python
>>> from fibo import *
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

模块名后使用 as 时，直接把 as 后的名称与导入模块绑定。

```python
>>> from fibo import fib as fibonacci
>>> fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

### 以脚本方式运行模块

可以用以下方式运行 Python 模块：

```python
python fibo.py <arguments>
```

这项操作将执行模块里的代码，和导入模块一样，但会把 __name__ 赋值为 "__main__"。也就是需要把下
列代码添加到模块末尾：

```python
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```

既可以把这个文件当脚本使用，也可以用作导入的模块，因为，解析命令行的代码只有在模块以“main”
文件执行时才会运行：

```python
$ python fibo.py 50
0 1 1 2 3 5 8 13 21 34
```

导入模块时，不运行这些代码：

```python
>>>import fibo
>>>
```

这种操作常用于为模块提供便捷用户接口，或用于测试（把模块当作执行测试套件的脚本运行）。

### 模块搜索路径

当一个名为 spam 的模块被导入时，解释器首先搜索具有该名称的内置模块。这些模块的名字被列在
sys.buildin_module_names 中。如果没有找到，它就在变量 sys.path 给出的目录列表中搜索一
个名为 spam.py 的文件， sys.path 从这些位置初始化:

- 输入脚本的目录（或未指定文件时的当前目录）。


- PYTHONPATH （目录列表，与 shell 变量 PATH 的语法一样）。


- 依赖于安装的默认值（按照惯例包括一个 site-packages 目录，由 site 模块处理）

初始化后， Python 程序可以更改 sys.path。运行脚本的目录在标准库路径之前，置于搜索路径的开头。
即，加载的是该目录里的脚本，而不是标准库的同名模块。除非刻意替换，否则会报错。

## 标准模块

Python 自带一个标准模块的库，它在 Python 库参考（此处以下称为” 库参考” ）里另外描述。一些模块是
内嵌到编译器里面的，它们给一些虽并非语言核心但却内嵌的操作提供接口，要么是为了效率，要么是
给操作系统基础操作例如系统调入提供接口。这些模块集是一个配置选项，并且还依赖于底层的操作系
统。例如， winreg 模块只在 Windows 系统上提供。一个特别值得注意的模块 sys，它被内嵌到每一个
Python 编译器中。 sys.ps1 和 sys.ps2 变量定义了一些字符，它们可以用作主提示符和辅助提示符:

```python
>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
C>
```

只有解释器用于交互模式时，才定义这两个变量。

变量 sys.path 是字符串列表，用于确定解释器的模块搜索路径。该变量以环境变量 PYTHONPATH 提
取的默认路径进行初始化，如未设置 PYTHONPATH，则使用内置的默认路径。可以用标准列表操作修改
该变量：

```python
>>> import sys
>>> sys.path.append('/ufs/guido/lib/python')
```

## dir()函数

内置函数 dir() 用于查找模块定义的名称。返回结果是经过排序的字符串列表：

```python
>>> import fibo, sys
>>> dir(fibo)
['__name__', 'fib', 'fib2']
>>> dir(sys)
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__',
'__interactivehook__', '__loader__', '__name__', '__package__', '__spec__',
'__stderr__', '__stdin__', '__stdout__', '__unraisablehook__',
'_clear_type_cache', '_current_frames', '_debugmallocstats', '_framework',
'_getframe', '_git', '_home', '_xoptions', 'abiflags', 'addaudithook',
'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix',
'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing',
'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info',
'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info',
'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth',
'getallocatedblocks', 'getdefaultencoding', 'getdlopenflags',
'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile',
'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval',
'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value',
'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks',
'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'pycache_prefix',
'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setdlopenflags',
'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr',
'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info',
'warnoptions']
```

没有参数时， dir() 列出当前定义的名称：

```python
>>> a = [1, 2, 3, 4, 5]
>>> import fibo
>>> fib = fibo.fib
>>> dir()
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
```

注意，该函数列出所有类型的名称：变量、模块、函数等。

dir() 不会列出内置函数和变量的名称。这些内容的定义在标准模块 builtins 里。

## 包

包是一种用“点式模块名”构造 Python 模块命名空间的方法。例如，模块名 A.B 表示包 A 中名为 B 的
子模块。正如模块可以区分不同模块之间的全局变量名称一样，点式模块名可以区分 NumPy 或 Pillow 等
不同多模块包之间的模块名称。

假设要为统一处理声音文件与声音数据设计一个模块集（“包”）。声音文件的格式很多（通常以扩展名来
识别，例如： .wav， .aiff， .au），因此，为了不同文件格式之间的转换，需要创建和维护一个不断增
长的模块集合。为了实现对声音数据的不同处理（例如，混声、添加回声、均衡器功能、创造人工立体
声效果），还要编写无穷无尽的模块流。下面这个分级文件树展示了这个包的架构：

```python
sound/                                                             Top-level package
    __init__.py                                                    Initialize the sound package
    formats/                                                       Subpackage for file format conversions
        __init__.py
        wavread.py
        wavwrite.py
        aiffread.py
        aiffwrite.py
        auread.py
        auwrite.py
        ...
    effects/                                                       Subpackage for sound effects
        __init__.py
        echo.py
        surround.py
        reverse.py
        ...
    filters/                                                       Subpackage for filters
        __init__.py
        equalizer.py
        vocoder.py
        karaoke.py
        ...
```

导入包时， Python 搜索 sys.path 里的目录，查找包的子目录。

Python 只把含 __init__.py 文件的目录当成包。这样可以防止以 string 等通用名称命名的目录，无
意中屏蔽出现在后方模块搜索路径中的有效模块。最简情况下， __init__.py 只是一个空文件，但该
文件也可以执行包的初始化代码，或设置 __all__ 变量，详见下文。

还可以从包中导入单个模块，例如：

```python
import sound.effects.echo
```

这段代码加载子模块 sound.effects.echo ，但引用时必须使用子模块的全名：

```python
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
```

另一种导入子模块的方法是：

```python
from sound.effects import echo
```

这段代码还可以加载子模块 echo ，不加包前缀也可以使用。因此，可以按如下方式使用：

```python
echo.echofilter(input, output, delay=0.7, atten=4)
```

Import 语句的另一种变体是直接导入所需的函数或变量：

```python
from sound.effects.echo import echofilter
```

同样，这样也会加载子模块 echo，但可以直接使用函数 echofilter()：

```python
echofilter(input, output, delay=0.7, atten=4)
```

注意，使用 from package import item 时， item 可以是包的子模块（或子包），也可以是包中定义
的函数、类或变量等其他名称。 import 语句首先测试包中是否定义了 item；如果未在包中定义，则假
定 item 是模块，并尝试加载。如果找不到 item，则触发 ImportError 异常。

相反，使用 import item.subitem.subsubitem 句法时，除最后一项外，每个 item 都必须是包；最
后一项可以是模块或包，但不能是上一项中定义的类、函数或变量。

###  从包中导入 *

使用 from sound.effects import * 时会发生什么？理想情况下，该语句在文件系统查找并导入
包的所有子模块。这项操作花费的时间较长，并且导入子模块可能会产生不必要的副作用，这种副作用
只有在显式导入子模块时才会发生。

唯一的解决方案是提供包的显式索引。 import 语句使用如下惯例：如果包的 __init__.py 代码定义
了列表 __all__，运行 from package import * 时，它就是用于导入的模块名列表。发布包的新版
本时，包的作者应更新此列表。如果包的作者认为没有必要在包中执行导入 * 操作，也可以不提供此列
表。例如， sound/effects/__init__.py 文件包含以下代码：

```python
__all__ = ["echo", "surround", "reverse"]
```

这将意味着将 from sound.effects import * 导入 sound.effects 包的三个命名的子模块。

如果没有定义 __all__， from sound.effects import * 语句 不会把包 sound.effects 中所有
子模块都导入到当前命名空间；该语句只确保导入包 sound.effects （可能还会运行 __init__.py
中的初始化代码），然后，再导入包中定义的名称。这些名称包括 __init__.py 中定义的任何名称（以
及显式加载的子模块），还包括之前 import 语句显式加载的包里的子模块。请看以下代码：

```python
import sound.effects.echo
import sound.effects.surround
from sound.effects import *
```

本例中，执行 from...import 语句时，将把 echo 和 surround 模块导入至当前命名空间，因为，它
们是在 sound.effects 包里定义的。（该导入操作在定义了 __all__ 时也有效。）

虽然，可以把模块设计为用 import * 时只导出遵循指定模式的名称，但仍不提倡在生产代码中使用这
种做法。

### 子包参考

包中含有多个子包时（与示例中的 sound 包一样），可以使用绝对导入引用兄弟包中的子模块。例
如，要在模块 sound.filters.vocoder 中使用 sound.effects 包的 echo 模块时，可以用 from
 sound.effects import echo 导入。

还可以用 import 语句的 from module import name 形式执行相对导入。这些导入语句使用前导句点
表示相对导入中的当前包和父包。例如，相对于 surround 模块，可以使用：

```python
from . import echo
from .. import formats
from ..filters import equalizer
```

注意，相对导入基于当前模块名。因为主模块名是 "__main__" ，所以 Python 程序的主模块必须始终
使用绝对导入。

# 输入输出

## 更复杂的输出格式

至此，我们已学习了两种写入值的方法： 表达式语句和 print() 函数。第三种方法是使用文件对象的
write() 方法；标准输出文件称为 sys.stdout。详见标准库参考。

对输出格式的控制不只是打印空格分隔的值，还需要更多方式。格式化输出包括以下几种方法。

- 使用格式化字符串字面值 ，要在字符串开头的引号/三引号前添加 f 或 F 。在这种字符串中，可以
在 { 和 } 字符之间输入引用的变量，或字面值的 Python 表达式。

```python
>>> year = 2016
>>> event = 'Referendum'
>>> f'Results of the {year} {event}'
'Results of the 2016 Referendum'
```

- 字符串的 str.format() 方法需要更多手动操作。该方法也用 { 和 } 标记替换变量的位置，虽然
这种方法支持详细的格式化指令，但需要提供格式化信息。

```python
>>> yes_votes = 42_572_654
>>> no_votes = 43_132_495
>>> percentage = yes_votes / (yes_votes + no_votes)
>>> '{:-9} YES votes {:2.2%}'.format(yes_votes, percentage)
' 42572654 YES votes 49.67%'
```

format函数用法

- 最后，还可以用字符串切片和合并操作完成字符串处理操作，创建任何排版布局。字符串类型还支
持将字符串按给定列宽进行填充，这些方法也很有用。

str() 函数返回供人阅读的值， repr() 则生成适于解释器读取的值（如果没有等效的语法，则强制执
行 SyntaxError）。对于没有支持供人阅读展示结果的对象， str() 返回与 repr() 相同的值。一般情
况下，数字、列表或字典等结构的值，使用这两个函数输出的表现形式是一样的。字符串有两种不同的
表现形式。

```python
>>> s = 'Hello, world.'
>>> str(s)
'Hello, world.'
>>> repr(s)
"'Hello, world.'"
>>> str(1/7)
'0.14285714285714285'
>>> x = 10 * 3.25
>>> y = 200 * 200
>>> s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
>>> print(s)
The value of x is 32.5, and y is 40000...
>>> # The repr() of a string adds string quotes and backslashes:
... hello = 'hello, world\n'
>>> hellos = repr(hello)
>>> print(hellos)
'hello, world\n'
>>> # The argument to repr() may be any Python object:
... repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"
```

### 格式化字符串字面值

格式化字符串字面值（简称为 f-字符串）在字符串前加前缀 f 或 F，通过 {expression} 表达式，把
Python 表达式的值添加到字符串内。

格式说明符是可选的，写在表达式后面，可以更好地控制格式化值的方式。下例将 pi 舍入到小数点后三
位：

```python
>>> import math
>>> print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142.
```

在 ':' 后传递整数，为该字段设置最小字符宽度，常用于列对齐：

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
>>> for name, phone in table.items():
...     print(f'{name:10} ==> {phone:10d}')
...
Sjoerd ==> 4127
Jack ==> 4098
Dcab ==> 7678
```

还有一些修饰符可以在格式化前转换值。 '!a' 应用 ascii() ， '!s' 应用 str()， '!r' 应用 repr()：

```python
>>> animals = 'eels'
>>> print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
>>> print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'eels'.
```

### 字符串format方法

str.format() 方法的基本用法如下所示：

```python
>>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"
```

花括号及之内的字符（称为格式字段）被替换为传递给 str.format() 方法的对象。花括号中的数字表
示传递给 str.format() 方法的对象所在的位置。

```python
>>> print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
>>> print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam
```

str.format() 方法中使用关键字参数名引用值。

```python
>>> print('This {food} is {adjective}.'.format(
...     food='spam', adjective='absolutely horrible'))
This spam is absolutely horrible.
```

位置参数和关键字参数可以任意组合：

```python
>>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
other='Georg'))
The story of Bill, Manfred, and Georg
```

如果不想分拆较长的格式字符串，最好按名称引用变量进行格式化，不要按位置。这项操作可以通过传
递字典，并用方括号 '[]' 访问键来完成。

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
...         'Dcab: {0[Dcab]:d}'.format(table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

这也可以通过将表字典作为关键字参数传递到具有 ** 表示法来完成。

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

例如，下面的代码生成一组整齐的列，包含给定整数及其平方与立方：

```python
>>> for x in range(1, 11):
...     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
...
1 1 1
2 4 8
3 9 27
4 16 64
5 25 125
6 36 216
7 49 343
8 64 512
9 81 729
10 100 1000
```

### 手动格式化字符串

下面是使用手动格式化方式实现的同一个平方和立方的表：

```python
>>> for x in range(1, 11):
...     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
...     # Note use of 'end' on previous line
...     print(repr(x*x*x).rjust(4))
...
1 1 1
2 4 8
3 9 27
4 16 64
5 25 125
6 36 216
7 49 343
8 64 512
9 81 729
10 100 1000
```

字符串对象的 str.rjust() 方法通过在左侧填充空格，对给定宽度字段中的字符串进行右对齐。同类
方法还有 str.ljust() 和 str.center() 。这些方法不写入任何内容，只返回一个新字符串，如果
输入的字符串太长，它们不会截断字符串，而是原样返回；虽然这种方式会弄乱列布局，但也比另一种
方法好，后者在显示值时可能不准确（如果真的想截断字符串，可以使用 x.ljust(n)[:n] 这样的切
片操作。）

另一种方法是 str.zfill() ，该方法在数字字符串左边填充零，且能识别正负号：

```python
>>> '12'.zfill(5)
'00012'
>>> '-3.14'.zfill(7)
'-003.14'
>>> '3.14159265359'.zfill(5)
'3.14159265359'
```

### 旧式字符串格式方法

% 运算符（求余符）也可用于字符串格式化。给定 'string' % values，则 string 中的 % 实例会以
零个或多个 values 元素替换。此操作被称为字符串插值。例如：

```python
>>> import math
>>> print('The value of pi is approximately %5.3f.' % math.pi)
The value of pi is approximately 3.142.
```

## 读写文件

open() 返回一个file object ，最常使用的是两个位置参数和一个关键字参数： open(filename, mode,
encoding=None)

```python
>>> f = open('workfile', 'w', encoding="utf-8")
```

第一个实参是文件名字符串。第二个实参是包含描述文件使用方式字符的字符串。 mode 的值包括 'r' ，
表示文件只能读取； 'w' 表示只能写入（现有同名文件会被覆盖）； 'a' 表示打开文件并追加内容，任何
写入的数据会自动添加到文件末尾。 'r+' 表示打开文件进行读写。 mode 实参是可选的，省略时的默认
值为 'r'。

通常情况下，文件是以 text mode 打开的，也就是说，你从文件中读写字符串，这些字符串是以特定的
encoding 编码的。如果没有指定 encoding ，默认的是与平台有关的（见 open() ）。因为 UTF-8 是现代事
实上的标准，除非你知道你需要使用一个不同的编码，否则建议使用 encoding="utf-8" 。在模式后
面加上一个 'b' ，可以用 binary mode 打开文件。二进制模式的数据是以 bytes 对象的形式读写的。在
二进制模式下打开文件时，你不能指定 encoding 。

在文本模式下读取文件时，默认把平台特定的行结束符（Unix 上为 \n, Windows 上为 \r\n）转换为 \n。
在文本模式下写入数据时，默认把 \n 转换回平台特定结束符。这种操作方式在后台修改文件数据对文
本文件来说没有问题，但会破坏 JPEG 或 EXE 等二进制文件中的数据。注意，在读写此类文件时，一定
要使用二进制模式。

在处理文件对象时，最好使用 with 关键字。优点是，子句体结束后，文件会正确关闭，即便触发异常
也可以。而且，使用 with 相比等效的 try-finally 代码块要简短得多：

```python
>>> with open('workfile', encoding="utf-8") as f:
...     read_data = f.read()
>>> # We can check that the file has been automatically closed.
>>> f.closed
True
```

如果没有使用 with 关键字，则应调用 f.close() 关闭文件，即可释放文件占用的系统资源。

警告: 调用 f.write() 时，未使用 with 关键字，或未调用 f.close()，即使程序正常退出，也
** 可能 ** 导致 f.write() 的参数没有完全写入磁盘。

通过 with 语句，或调用 f.close() 关闭文件对象后，再次使用该文件对象将会失败。

### 文件对象的方法

下文中的例子假定已创建 f 文件对象。

f.read(size) 可用于读取文件内容，它会读取一些数据，并返回字符串（文本模式），或字节串对象
（在二进制模式下）。 size 是可选的数值参数。省略 size 或 size 为负数时，读取并返回整个文件的内容；文
件大小是内存的两倍时，会出现问题。 size 取其他值时，读取并返回最多 size 个字符（文本模式）或 size
个字节（二进制模式）。如已到达文件末尾， f.read() 返回空字符串（''）。

```python
>>> f.read()
'This is the entire file.\n'
>>> f.read()
''
```

f.readline() 从文件中读取单行数据；字符串末尾保留换行符（\n），只有在文件不以换行符结尾时，
文件的最后一行才会省略换行符。这种方式让返回值清晰明确；只要 f.readline() 返回空字符串，就
表示已经到达了文件末尾，空行使用 '\n' 表示，该字符串只包含一个换行符。

```python
>>> f.readline()
'This is the first line of the file.\n'
>>> f.readline()
'Second line of the file\n'
>>> f.readline()
''
```

从文件中读取多行时，可以用循环遍历整个文件对象。这种操作能高效利用内存，快速，且代码简单：

```python
>>> for line in f:
...     print(line, end='')
...
This is the first line of the file.
Second line of the file
```

如需以列表形式读取文件中的所有行，可以用 list(f) 或 f.readlines()。

f.write(string) 把 string 的内容写入文件，并返回写入的字符数。

```python
>>> f.write('This is a test\n')
15
```

写入其他类型的对象前，要先把它们转化为字符串（文本模式）或字节对象（二进制模式）：

```python
>>> value = ('the answer', 42)
>>> s = str(value) # convert the tuple to string
>>> f.write(s)
18
```

f.tell() 返回整数，给出文件对象在文件中的当前位置，表示为二进制模式下时从文件开始的字节数，
以及文本模式下的意义不明的数字。

f.seek(offset, whence) 可以改变文件对象的位置。通过向参考点添加 offset 计算位置；参考点由
whence 参数指定。 whence 值为 0 时，表示从文件开头计算， 1 表示使用当前文件位置， 2 表示使用文件
末尾作为参考点。省略 whence 时，其默认值为 0，即使用文件开头作为参考点。

```python
>>> f = open('workfile', 'rb+')
>>> f.write(b'0123456789abcdef')
16
>>> f.seek(5) # Go to the 6th byte in the file
5
>>> f.read(1)
b'5'
>>> f.seek(-3, 2) # Go to the 3rd byte before the end
13
>>> f.read(1)
b'd'
```

在文本文件（模式字符串未使用 b 时打开的文件）中，只允许相对于文件开头搜索（使用 seek(0, 2)
搜索到文件末尾是个例外），唯一有效的 offset 值是能从 f.tell() 中返回的，或 0。其他 offset 值都会产
生未定义的行为。

### 使用 json 保存结构化数据

从文件写入或读取字符串很简单，数字则稍显麻烦，因为 read() 方法只返回字符串，这些字符串必须
传递给 int() 这样的函数，接受 '123' 这样的字符串，并返回数字值 123。保存嵌套列表、字典等复
杂数据类型时，手动解析和序列化的操作非常复杂。

Python 支持 JSON (JavaScript Object Notation) 这种流行数据交换格式，用户无需没完没了地编写、调试代
码，才能把复杂的数据类型保存到文件。 json 标准模块采用 Python 数据层次结构，并将之转换为字符
串表示形式；这个过程称为 serializing （序列化）。从字符串表示中重建数据称为 deserializing （解序化）。
在序列化和解序化之间，表示对象的字符串可能已经存储在文件或数据中，或通过网络连接发送到远方
的机器。

只需一行简单的代码即可查看某个对象的 JSON 字符串表现形式：

```python
>>> import json
>>> x = [1, 'simple', 'list']
>>> json.dumps(x)
'[1, "simple", "list"]'
```

dumps() 函数还有一个变体， dump() ，它只将对象序列化为text file 。因此，如果 f 是text file 对象，可
以这样做：

```python
json.dump(x, f)
```

要再次解码对象，如果 f 是已打开、供读取的binary file 或text file 对象：

```python
x = json.load(f)
```

JSON 文件必须以 UTF-8 编码。当打开 JSON 文件作为一个text file 用于读写时，使用
encoding="utf-8" 。

# 错误和异常

## 句法错误

句法错误又称解析错误，是学习 Python 时最常见的错误：

```python
>>> while True print('Hello world')
    File "<stdin>", line 1
    while True print('Hello world')
                ^
SyntaxError: invalid syntax
```

解析器会复现出现句法错误的代码行，并用小“箭头”指向行里检测到的第一个错误。错误是由箭头 上
方的 token 触发的（至少是在这里检测出的）：本例中，在 print() 函数中检测到错误，因为，在它前
面缺少冒号（':'）。错误信息还输出文件名与行号，在使用脚本文件时，就可以知道去哪里查错。

## 异常

即使语句或表达式使用了正确的语法，执行时仍可能触发错误。执行时检测到的错误称为 异常，异常不
一定导致严重的后果：很快我们就能学会如何处理 Python 的异常。大多数异常不会被程序处理，而是显
示下列错误信息：

```python
>>> 10 * (1/0)
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

错误信息的最后一行说明程序遇到了什么类型的错误。异常有不同的类型，而类型名称会作为错误
信息的一部分中打印出来：上述示例中的异常类型依次是： ZeroDivisionError， NameError 和
TypeError。作为异常类型打印的字符串是发生的内置异常的名称。对于所有内置异常都是如此，但对
于用户定义的异常则不一定如此（虽然这种规范很有用）。标准的异常类型是内置的标识符（不是保留关
键字）。

## 异常的处理

可以编写程序处理选定的异常。下例会要求用户一直输入内容，直到输入有效的整数，但允许用户中断程
序（使用 Control-C 或操作系统支持的其他操作）；注意，用户中断程序会触发 KeyboardInterrupt
异常。

```python
>>> while True:
...     try:
...         x = int(input("Please enter a number: "))
...         break
...     except ValueError:
...     print("Oops! That was no valid number. Try again...")
...
```

try 语句的工作原理如下：


- 首先，执行 try 子句（try 和 except 关键字之间的（多行）语句）。


- 如果没有触发异常，则跳过 except 子句， try 语句执行完毕。


- 如果在执行 try 子句时发生了异常，则跳过该子句中剩下的部分。如果异常的类型与 except 关
键字后指定的异常相匹配，则会执行 except 子句，然后跳到 try/except 代码块之后继续执行。


- 如果发生的异常与 except 子句中指定的异常不匹配，则它会被传递到外部的 try 语句中；如果没
有找到处理程序，则它是一个 未处理异常且执行将终止并输出如上所示的消息。

try 语句可以有多个 except 子句来为不同的异常指定处理程序。但最多只有一个处理程序会被执行。处
理程序只处理对应的 try 子句中发生的异常，而不处理同一 try 语句内其他处理程序中的异常。 except 子
句可以用带圆括号的元组来指定多个异常，例如:

```python
... except (RuntimeError, TypeError, NameError):
...     pass
```

如果发生的异常与 except 子句中的类是同一个类或是它的基类时，则该类与该异常相兼容（反之则不
成立 --- 列出派生类的 except 子句与基类不兼容）。例如，下面的代码将依次打印 B, C, D:

```python
class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass
   
for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
```

请注意如果颠倒 except 子句的顺序（把 except B 放在最前），则会输出 B, B, B --- 即触发了第一个匹配
的 except 子句。

所有异常都继承自 BaseException，因此它可被用作通配符。但这种用法要非常谨慎小心，因为它很
容易掩盖真正的编程错误！它还可被用于打印错误消息然后重新引发异常（允许调用者再来处理该异常）
:

```python
import sys
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
```

可以选择让最后一个 except 子句省略异常名称，但在此之后异常值必须从 sys.exc_info()[1] 获取。

try ... except 语句具有可选的 else 子句，该子句如果存在，它必须放在所有 except 子句之后。它适用
于 try 子句没有引发异常但又必须要执行的代码。例如:

```python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```

使用 else 子句比向 try 子句添加额外的代码要好，可以避免意外捕获非 try ... except 语句保护的代
码触发的异常。

发生异常时，它可能具有关联值，即异常 参数。是否需要参数，以及参数的类型取决于异常的类型。

except 子句可以在异常名称后面指定一个变量。这个变量会绑定到一个异常实例并将参数存储在
instance.args 中。为了方便起见，该异常实例定义了 __str__() 以便能直接打印参数而无需
引用 .args。也可以在引发异常之前先实例化一个异常并根据需要向其添加任何属性。 :

```python
>>> try:
...     raise Exception('spam', 'eggs')
... except Exception as inst:
...     print(type(inst)) # the exception instance
...     print(inst.args) # arguments stored in .args
...     print(inst) # __str__ allows args to be printed directly,
...                 # but may be overridden in exception subclasses
...     x, y = inst.args # unpack args
...     print('x =', x)
...     print('y =', y)
...
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs
```

如果异常有参数，则它们将作为未处理异常的消息的最后一部分（’ 详细信息’）打印。

异常处理程序不仅会处理在 try 子句中发生的异常，还会处理在 try 子句中调用（包括间接调用）的函数。
例如:

```python
>>> def this_fails():
...     x = 1/0
...
>>> try:
...     this_fails()
... except ZeroDivisionError as err:
...     print('Handling run-time error:', err)
...
Handling run-time error: division by zero
```

## 触发异常

raise 语句支持强制触发指定的异常。例如：

```python
>>> raise NameError('HiThere')
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
NameError: HiThere
```

raise 唯一的参数就是要触发的异常。这个参数必须是异常实例或异常类（派生自 Exception 类）。如
果传递的是异常类，将通过调用没有参数的构造函数来隐式实例化：

```python
raise ValueError # shorthand for 'raise ValueError()'
```

如果只想判断是否触发了异常，但并不打算处理该异常，则可以使用更简单的 raise 语句重新触发异
常：

```python
>>> try:
...     raise NameError('HiThere')
... except NameError:
...     print('An exception flew by!')
...     raise
...
An exception flew by!
Traceback (most recent call last):
    File "<stdin>", line 2, in <module>
NameError: HiThere
```

## 异常链

raise 语句支持可选的 from 子句，该子句用于启用链式异常。例如：

```python
# exc must be exception instance or None.
raise RuntimeError from exc
```

转换异常时，这种方式很有用。例如：

```python
>>> def func():
...     raise ConnectionError
...
>>> try:
...     func()
... except ConnectionError as exc:
...     raise RuntimeError('Failed to open database') from exc
...
Traceback (most recent call last):
    File "<stdin>", line 2, in <module>
    File "<stdin>", line 2, in func
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
    File "<stdin>", line 4, in <module>
RuntimeError: Failed to open database
```

异常链会在 except 或 finally 子句内部引发异常时自动生成。这可以通过使用 from None 这样的
写法来禁用:

```python
>>> try:
...     open('database.sqlite')
... except OSError:
...     raise RuntimeError from None
...
Traceback (most recent call last):
    File "<stdin>", line 4, in <module>
RuntimeError
```

## 用户自定义异常

程序可以通过创建新的异常类命名自己的异常（Python 类的内容详见类）。不论是以直接还是间接的方
式，异常都应从 Exception 类派生。

异常类可以被定义成能做其他类所能做的任何事，但通常应当保持简单，它往往只提供一些属性，允许
相应的异常处理程序提取有关错误的信息。


大多数异常命名都以“Error”结尾，类似标准异常的命名。
许多标准模块都需要自定义异常，以报告由其定义的函数中出现的错误。有关类的说明，详见类。

## 定义清理操作

try 语句还有一个可选子句，用于定义在所有情况下都必须要执行的清理操作。例如：

```python
>>> try:
...     raise KeyboardInterrupt
... finally:
...     print('Goodbye, world!')
...
Goodbye, world!
KeyboardInterrupt
Traceback (most recent call last):
    File "<stdin>", line 2, in <module>
```

如果存在 finally 子句，则 finally 子句是 try 语句结束前执行的最后一项任务。不论 try 语句是
否触发异常，都会执行 finally 子句。以下内容介绍了几种比较复杂的触发异常情景：

• 如果执行 try 子句期间触发了某个异常，则某个 except 子句应处理该异常。如果该异常没有
except 子句处理，在 finally 子句执行后会被重新触发。


• except 或 else 子句执行期间也会触发异常。同样，该异常会在 finally 子句执行之后被重新
触发。


• 如果 finally 子句中包含 break、 continue 或 return 等语句，异常将不会被重新引发。


• 如果执行 try 语句时遇到 break,、 continue 或 return 语句，则 finally 子句在执行 break、
continue 或 return 语句之前执行。


• 如果 finally 子句中包含 return 语句，则返回值来自 finally 子句的某个 return 语句的返
回值，而不是来自 try 子句的 return 语句的返回值。

例如：

```python
>>> def bool_return():
...     try:
...         return True
...     finally:
...         return False
...
>>> bool_return()
False
```



```python
>>> def divide(x, y):
...     try:
...         result = x / y
...     except ZeroDivisionError:
...         print("division by zero!")
...     else:
...         print("result is", result)
...     finally:
...         print("executing finally clause")
...
>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```

如上所示，任何情况下都会执行 finally 子句。 except 子句不处理两个字符串相除触发的 TypeError，
因此会在 finally 子句执行后被重新触发。


在实际应用程序中， finally 子句对于释放外部资源（例如文件或者网络连接）非常有用，无论是否成
功使用资源

## 预定义的清理操作

某些对象定义了不需要该对象时要执行的标准清理操作。无论使用该对象的操作是否成功，都会执行清
理操作。比如，下例要打开一个文件，并输出文件内容：

```python
for line in open("myfile.txt"):
    print(line, end="")
```

这个代码的问题在于，执行完代码后，文件在一段不确定的时间内处于打开状态。在简单脚本中这没有
问题，但对于较大的应用程序来说可能会出问题。 with 语句支持以及时、正确的清理的方式使用文件对
象：

```python
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```

语句执行完毕后，即使在处理行时遇到问题，都会关闭文件 f。和文件一样，支持预定义清理操作的对
象会在文档中指出这一点。

# 类

类把数据与功能绑定在一起。创建新类就是创建新的对象类型，从而创建该类型的新实例。类实例支持
维持自身状态的属性，还支持（由类定义的）修改自身状态的方法。

##  名称和对象

对象之间相互独立，多个名称（在多个作用域内）可以绑定到同一个对象。其他语言称之为别名。 Python
初学者通常不容易理解这个概念，处理数字、字符串、元组等不可变基本类型时，可以不必理会。但是，
对涉及可变对象，如列表、字典等大多数其他类型的 Python 代码的语义，别名可能会产生意料之外的效
果。这样做，通常是为了让程序受益，因为别名在某些方面就像指针。例如，传递对象的代价很小，因
为实现只传递一个指针；如果函数修改了作为参数传递的对象，调用者就可以看到更改。

## python作用域和命名空间

在介绍类前，首先要介绍 Python 的作用域规则。类定义对命名空间有一些巧妙的技巧，了解作用域和命
名空间的工作机制有利于加强对类的理解。并且，即便对于高级 Python 程序员，这方面的知识也很有用。

namespace （命名空间）是映射到对象的名称。现在，大多数命名空间都使用 Python 字典实现，但除非
涉及到优化性能，我们一般不会关注这方面的事情，而且将来也可能会改变这种方式。命名空间的几个
常见示例： abs() 函数、内置异常等的内置函数集合；模块中的全局名称；函数调用中的局部名称。对
象的属性集合也算是一种命名空间。关于命名空间的一个重要知识点是，不同命名空间中的名称之间绝
对没有关系；例如，两个不同的模块都可以定义 maximize 函数，且不会造成混淆。用户使用函数时必
须要在函数名前面附加上模块名。

点号之后的名称是属性。例如，表达式 z.real 中， real 是对象 z 的属性。严格来说，对模块中名称的
引用是属性引用：表达式 modname.funcname 中， modname 是模块对象， funcname 是模块的属性。
模块属性和模块中定义的全局名称之间存在直接的映射：它们共享相同的命名空间！

属性可以是只读或者可写的。如果可写，则可对属性赋值。模块属性是可写时，可以使用 modname.
the_answer = 42 。 del 语句可以删除可写属性。例如， del modname.the_answer 会删除
modname 对象中的 the_answer 属性。

命名空间是在不同时刻创建的，且拥有不同的生命周期。内置名称的命名空间是在 Python 解释器启动时
创建的，永远不会被删除。模块的全局命名空间在读取模块定义时创建；通常，模块的命名空间也会持
续到解释器退出。从脚本文件读取或交互式读取的，由解释器顶层调用执行的语句是 __main__ 模块调
用的一部分，也拥有自己的全局命名空间。内置名称实际上也在模块里，即 builtins 。

函数的本地命名空间在调用该函数时创建，并在函数返回或抛出不在函数内部处理的错误时被删除。（实
际上，用“遗忘”来描述实际发生的情况会更好一些。）当然，每次递归调用都会有自己的本地命名空间。

作用域是命名空间可直接访问的 Python 程序的文本区域。“可直接访问”的意思是，对名称的非限定引
用会在命名空间中查找名称。

作用域虽然是静态确定的，但会被动态使用。执行期间的任何时刻，都会有 3 或 4 个命名空间可被直接
访问的嵌套作用域：

• 最内层作用域，包含局部名称，并首先在其中进行搜索


• 封闭函数的作用域，包含非局部名称和非全局名称，从最近的封闭作用域开始搜索


• 倒数第二个作用域，包含当前模块的全局名称


• 最外层的作用域，包含内置名称的命名空间，最后搜索

如果把名称声明为全局变量，则所有引用和赋值将直接指向包含该模块的全局名称的中间作用域。重新
绑定在最内层作用域以外找到的变量，使用 nonlocal 语句把该变量声明为非局部变量。未声明为非局
部变量的变量是只读的，（写入只读变量会在最内层作用域中创建一个 新的局部变量，而同名的外部变
量保持不变。）

通常，当前局部作用域将（按字面文本）引用当前函数的局部名称。在函数之外，局部作用域引用与全
局作用域一致的命名空间：模块的命名空间。类定义在局部命名空间内再放置另一个命名空间。

划重点，作用域是按字面文本确定的：模块内定义的函数的全局作用域就是该模块的命名空间，无论该
函数从什么地方或以什么别名被调用。另一方面，实际的名称搜索是在运行时动态完成的。但是， Python
正在朝着“编译时静态名称解析”的方向发展，因此不要过于依赖动态名称解析！（局部变量已经是被静
态确定了。）

Python 有一个特殊规定。如果不存在生效的 global 或 nonlocal 语句，则对名称的赋值总是会进入最
内层作用域。赋值不会复制数据，只是将名称绑定到对象。删除也是如此：语句 del x 从局部作用域引
用的命名空间中移除对 x 的绑定。所有引入新名称的操作都是使用局部作用域：尤其是 import 语句和
函数定义会在局部作用域中绑定模块或函数名称。

global 语句用于表明特定变量在全局作用域里，并应在全局作用域中重新绑定； nonlocal 语句表明
特定变量在外层作用域中，并应在外层作用域中重新绑定。

### 作用域和命名空间示例

```python
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)
    
scope_test()
print("In global scope:", spam)
```

实例代码输出:

```python
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
```

注意， 局部赋值（这是默认状态）不会改变 scope_test 对 spam 的绑定。 nonlocal 赋值会改变 scope_test
对 spam 的绑定，而 global 赋值会改变模块层级的绑定。
而且， global 赋值前没有 spam 的绑定。

## 初探类

### 类定义语法

```python
class ClassName:
    <statement-1>
    . 
    .
    .
    <
statement-N>
```

与函数定义 (def 语句) 一样，类定义必须先执行才能生效。把类定义放在 if 语句的分支里或函数内部
试试。

当进入类定义时，将创建一个新的命名空间，并将其用作局部作用域 --- 因此，所有对局部变量的赋值都
是在这个新命名空间之内。特别的，函数定义会绑定到这里的新函数名称。

当（从结尾处）正常离开类定义时，将创建一个 类对象。这基本上是一个包围在类定义所创建命名空
间内容周围的包装器；我们将在下一节了解有关类对象的更多信息。原始的（在进入类定义之前起作
用的）局部作用域将重新生效，类对象将在这里被绑定到类定义头所给出的类名称 (在这个示例中为
ClassName)。

### Class对象

类对象支持两种操作：属性引用和实例化。

属性引用使用 Python 中所有属性引用所使用的标准语法: obj.name。有效的属性名称是类对象被创建
时存在于类命名空间中的所有名称。因此，如果类定义是这样的:

```python
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
```

那么 MyClass.i 和 MyClass.f 就是有效的属性引用，将分别返回一个整数和一个函数对象。类属性
也可以被赋值，因此可以通过赋值来更改 MyClass.i 的值。 __doc__ 也是一个有效的属性，将返回所
属类的文档字符串: "A simple example class"。

类的 实例化使用函数表示法。可以把类对象视为是返回该类的一个新实例的不带参数的函数。举例来说
（假设使用上述的类） :

```python
x = MyClass()
```

创建类的新 实例并将此对象分配给局部变量 x。

实例化操作（“调用”类对象）会创建一个空对象。许多类喜欢创建带有特定初始状态的自定义实例。为
此类定义可能包含一个名为 __init__() 的特殊方法，就像这样:

```python
def __init__(self):
    self.data = []
```

当 一 个 类 定 义 了 __init__() 方 法 时， 类 的 实 例 化 操 作 会 自 动 为 新 创 建 的 类 实 例 发 起 调 用
__init__()。因此在这个示例中，可以通过以下语句获得一个经初始化的新实例:

```python
x = MyClass()
```

当然， __init__() 方法还可以有额外参数以实现更高灵活性。在这种情况下，提供给类实例化运算符
的参数将被传递给 __init__()。例如，:

```python
>>> class Complex:
...     def __init__(self, realpart, imagpart):
...         self.r = realpart
...         self.i = imagpart
...
>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)
```

### 实例对象

实例对象所能理解的唯一操作是属性引用。有两种有效的属性名称：数
据属性和方法。

数据属性对应于 Smalltalk 中的“实例变量”，以及 C++ 中的“数据成员”。数据属性不需要声明；像局部
变量一样，它们将在第一次被赋值时产生。例如，如果 x 是上面创建的 MyClass 的实例，则以下代码
段将打印数值 16，且不保留任何追踪信息:

```python
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
```

另一类实例属性引用称为 方法。方法是“从属于”对象的函数。（在 Python 中，方法这个术语并不是类
实例所特有的：其他对象也可以有方法。例如，列表对象具有 append, insert, remove, sort 等方法。然而，
在以下讨论中，我们使用方法一词将专指类实例对象的方法，除非另外显式地说明。）


实例对象的有效方法名称依赖于其所属的类。根据定义，一个类中所有是函数对象的属性都是定义了其
实例的相应方法。因此在我们的示例中， x.f 是有效的方法引用，因为 MyClass.f 是一个函数，而 x.i
不是方法，因为 MyClass.i 不是函数。但是 x.f 与 MyClass.f 并不是一回事 --- 它是一个 方法对象，
不是函数对象。

### 方法对象

通常，方法在绑定后立即被调用:

```python
x.f()
```

在 MyClass 示例中，这将返回字符串 'hello world'。但是，立即调用一个方法并不是必须的: x.f
是一个方法对象，它可以被保存起来以后再调用。例如:

```python
xf = x.f
while True:
    print(xf())
```

方法的特殊之处就在于实例对象会作为函数的第一个参数被传入。在
我们的示例中，调用 x.f() 其实就相当于 MyClass.f(x)。总之，调用一个具有 n 个参数的方法就相
当于调用再多一个参数的对应函数，这个参数值为方法所属实例对象，位置在其他参数之前。

### 类和实例变量

一般来说，实例变量用于每个实例的唯一数据，而类变量用于类的所有实例共享的属性和方法:

```python
class Dog:
    kind = 'canine'     # class variable shared by all instances

    def __init__(self, name):
        self.name = name     # instance variable unique to each instance
        
>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.kind     # shared by all dogs
'canine'
>>> e.kind     # shared by all dogs
'canine'
>>> d.name     # unique to d
'Fido'
>>> e.name     # unique to e
'Buddy'
```

正如名称和对象 中已讨论过的，共享数据可能在涉及mutable 对象例如列表和字典的时候导致令人惊讶
的结果。例如以下代码中的 tricks 列表不应该被用作类变量，因为所有的 Dog 实例将只共享一个单独的
列表:

```python
class Dog:

    tricks = []     # mistaken use of a class variable
    
    def __init__(self, name):
        self.name = name
        
    def add_trick(self, trick):
        self.tricks.append(trick)
        
>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks # unexpectedly shared by all dogs
['roll over', 'play dead']
```

正确的类设计应该使用实例变量:

```python
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []     # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)
        
>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']
```

## 补充说明

如果同样的属性名称同时出现在实例和类中，则属性查找会优先选择实例:

```python
>>> class Warehouse:
...     purpose = 'storage'
...     region = 'west'
...
>>> w1 = Warehouse()
>>> print(w1.purpose, w1.region)
storage west
>>> w2 = Warehouse()
>>> w2.region = 'east'
>>> print(w2.purpose, w2.region)
storage east
```

数据属性可以被方法以及一个对象的普通用户（“客户端”）所引用。换句话说，类不能用于实现纯抽象
数据类型。实际上，在 Python 中没有任何东西能强制隐藏数据 --- 它是完全基于约定的。（而在另一方面，
用 C 语言编写的 Python 实现则可以完全隐藏实现细节，并在必要时控制对象的访问；此特性可以通过用
C 编写 Python 扩展来使用。）

客户端应当谨慎地使用数据属性 --- 客户端可能通过直接操作数据属性的方式破坏由方法所维护的固定
变量。请注意客户端可以向一个实例对象添加他们自己的数据属性而不会影响方法的可用性，只要保证
避免名称冲突 --- 再次提醒，在此使用命名约定可以省去许多令人头痛的麻烦。

在方法内部引用数据属性（或其他方法！）并没有简便方式。我发现这实际上提升了方法的可读性：当浏
览一个方法代码时，不会存在混淆局部变量和实例变量的机会。

方法的第一个参数常常被命名为 self。这也不过就是一个约定: self 这一名称在 Python 中绝对没有特
殊含义。但是要注意，不遵循此约定会使得你的代码对其他 Python 程序员来说缺乏可读性，而且也可以
想像一个 类浏览器程序的编写可能会依赖于这样的约定。

任何一个作为类属性的函数都为该类的实例定义了一个相应方法。函数定义的文本并非必须包含于类定
义之内：将一个函数对象赋值给一个局部变量也是可以的。例如:

```python
# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)
    
class C:
    f = f1

    def g(self):
        return 'hello world'

h = g
```

现在 f, g 和 h 都是 C 类的引用函数对象的属性，因而它们就都是 C 的实例的方法 --- 其中 h 完全等同于
g。但请注意，本示例的做法通常只会令程序的阅读者感到迷惑。

方法可以通过使用 self 参数的方法属性调用其他方法:

```python
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
```

方法可以通过与普通函数相同的方式引用全局名称。与方法相关联的全局作用域就是包含其定义的模
块。（类永远不会被作为全局作用域。）

## 继承

当然，如果不支持继承，语言特性就不值得称为“类”。派生类定义的语法如下所示:

```python
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <
statement-N>
```

名称 BaseClassName 必须定义于包含派生类定义的作用域中。也允许用其他任意表达式代替基类名称
所在的位置。这有时也可能会用得上，例如，当基类定义在另一个模块中的时候:

```python
class DerivedClassName(modname.BaseClassName):
```

派生类定义的执行过程与基类相同。当构造类对象时，基类会被记住。此信息将被用来解析属性引用：
如果请求的属性在类中找不到，搜索将转往基类中进行查找。如果基类本身也派生自其他某个类，则此
规则将被递归地应用。

派生类的实例化没有任何特殊之处: DerivedClassName() 会创建该类的一个新实例。方法引用将按
以下方式解析：搜索相应的类属性，如有必要将按基类继承链逐步向下查找，如果产生了一个函数对象
则方法引用就生效。

派生类可能会重写其基类的方法。因为方法在调用同一对象的其他方法时没有特殊权限，所以调用同
一基类中定义的另一方法的基类方法最终可能会调用覆盖它的派生类的方法。

在派生类中的重载方法实际上可能想要扩展而非简单地替换同名的基类方法。有一种方式可以简单地直
接调用基类方法：即调用 BaseClassName.methodname(self, arguments)。有时这对客户端来
说也是有用的。（请注意仅当此基类可在全局作用域中以 BaseClassName 的名称被访问时方可使用此
方式。）

Python 有两个内置函数可被用于继承机制：

• 使 用 isinstance() 来 检 查 一 个 实 例 的 类 型: isinstance(obj, int) 仅 会 在 obj.
__class__ 为 int 或某个派生自 int 的类时为 True。

• 使用 issubclass() 来检查类的继承关系: issubclass(bool, int) 为 True，因为 bool 是
int 的子类。但是， issubclass(float, int) 为 False，因为 float 不是 int 的子类。

### 多重继承

Python 也支持一种多重继承。带有多个基类的类定义语句如下所示:

```python
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <
statement-N>
```

对于多数应用来说，在最简单的情况下，你可以认为搜索从父类所继承属性的操作是深度优先、从左至右
的，当层次结构中存在重叠时不会在同一个类中搜索两次。因此，如果某一属性在 DerivedClassName
中未找到，则会到 Base1 中搜索它，然后（递归地）到 Base1 的基类中搜索，如果在那里未找到，再
到 Base2 中搜索，依此类推。

真实情况比这个更复杂一些；方法解析顺序会动态改变以支持对 super() 的协同调用。这种方式在某
些其他多重继承型语言中被称为后续方法调用，它比单继承型语言中的 super 调用更强大。

## 私有变量

那种仅限从一个对象内部访问的“私有”实例变量在 Python 中并不存在。但是，大多数 Python 代码都遵
循这样一个约定：带有一个下划线的名称 (例如 _spam) 应该被当作是 API 的非公有部分 (无论它是函数、
方法或是数据成员)。这应当被视为一个实现细节，可能不经通知即加以改变。

由于存在对于类私有成员的有效使用场景（例如避免名称与子类所定义的名称相冲突），因此存在对此种
机制的有限支持，称为 名称改写。任何形式为 __spam 的标识符（至少带有两个前缀下划线，至多一个
后缀下划线）的文本将被替换为 _classname__spam，其中 classname 为去除了前缀下划线的当前
类名称。这种改写不考虑标识符的句法位置，只要它出现在类定义内部就会进行。

名称改写有助于让子类重载方法而不破坏类内方法调用。例如:

```python
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)
        
    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update     # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
```

上面的示例即使在 MappingSubclass 引入了一个 __update 标识符的情况下也不会出错，因
为它会在 Mapping 类中被替换为_Mapping__update 而在 MappingSubclass 类中被替换为
_MappingSubclass__update。

请注意，改写规则的设计主要是为了避免意外冲突；访问或修改被视为私有的变量仍然是可能的。这在
特殊情况下甚至会很有用，例如在调试器中。

## 杂项说明

有时会需要使用类似于 Pascal 的“record”或 C 的“struct”这样的数据类型，将一些命名数据项捆绑在
一起。这种情况适合定义一个空类:

```python
class Employee:
    pass

john = Employee() # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000
```

一段需要特定抽象数据类型的 Python 代码往往可以被传入一个模拟了该数据类型的方法的类作为替
代。例如，如果你有一个基于文件对象来格式化某些数据的函数，你可以定义一个带有 read() 和
readline() 方法从字符串缓存获取数据的类，并将其作为参数传入。

## 迭代器

到目前为止，您可能已经注意到大多数容器对象都可以使用 for 语句:

```python
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')
```

这种访问风格清晰、简洁又方便。迭代器的使用非常普遍并使得 Python 成为一个统一的整体。在幕后，
for 语句会在容器对象上调用 iter()。该函数返回一个定义了 __next__() 方法的迭代器对象，此方
法将逐一访问容器中的元素。当元素用尽时， __next__() 将引发 StopIteration 异常来通知终止
for 循环。你可以使用 next() 内置函数来调用 __next__() 方法；这个例子显示了它的运作方式:

```python
>>> s = 'abc'
>>> it = iter(s)
>>> it
<str_iterator object at 0x10c90e650>
>>> next(it)
'a'
>>> next(it)
'b'
>>> next(it)
'c'
>>> next(it)
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
        next(it)
StopIteration
```

看过迭代器协议的幕后机制，给你的类添加迭代器行为就很容易了。定义一个 __iter__() 方法来返回一个带有 __next__() 方法的对象。如果类已定义了 __next__()，则 __iter__() 可以简单地返回
self:

```python
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
```



```python
>>> rev = Reverse('spam')
>>> iter(rev)
<__main__.Reverse object at 0x00A1DB50>
>>> for char in rev:
...     print(char)
...
m
a
p
s
```

## 生成器

生成器 是一个用于创建迭代器的简单而强大的工具。它们的写法类似于标准的函数，但当它们要返回数
据时会使用 yield 语句。每次在生成器上调用 next() 时，它会从上次离开的位置恢复执行（它会记住
上次执行语句时的所有数据值）。一个显示如何非常容易地创建生成器的示例如下:

```python
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
```



```python
>>> for char in reverse('golf'):
...     print(char)
...
f
l
o
g
```

可以用生成器来完成的操作同样可以用前一节所描述的基于类的迭代器来完成。但生成器的写法更为紧
凑，因为它会自动创建 __iter__() 和 __next__() 方法。

另一个关键特性在于局部变量和执行状态会在每次调用之间自动保存。这使得该函数相比使用 self.
index 和 self.data 这种实例变量的方式更易编写且更为清晰。


除了会自动创建方法和保存程序状态，当生成器终结时，它们还会自动引发 StopIteration。这些特
性结合在一起，使得创建迭代器能与编写常规函数一样容易。

## 生成器表达式

某些简单的生成器可以写成简洁的表达式代码，所用语法类似列表推导式，但外层为圆括号而非方括号。
这种表达式被设计用于生成器将立即被外层函数所使用的情况。生成器表达式相比完整的生成器更紧凑
但较不灵活，相比等效的列表推导式则更为节省内存。

```python
>>> sum(i*i for i in range(10))     # sum of squares
285
>>> xvec = [10, 20, 30]
>>> yvec = [7, 5, 3]
>>> sum(x*y for x,y in zip(xvec, yvec)) # dot product
260
>>> unique_words = set(word for line in page for word in line.split())
>>> valedictorian = max((student.gpa, student.name) for student in graduates)
>>> data = 'golf'
>>> list(data[i] for i in range(len(data)-1, -1, -1))
['f', 'l', 'o', 'g']
```

# 标准库介绍

## 操作系统接口

os 模块提供了许多与操作系统交互的函数:

```python
>>> import os
>>> os.getcwd() # Return the current working directory
'C:\\Python310'
>>> os.chdir('/server/accesslogs') # Change current working directory
>>> os.system('mkdir today') # Run the command mkdir in the system shell
0
```

一定要使用 import os 而不是 from os import * 。这将避免内建的 open() 函数被 os.open()
隐式替换掉，因为它们的使用方式大不相同。

内置的 dir() 和 help() 函数可用作交互式辅助工具，用于处理大型模块，如 os:

```python
>>> import os
>>> dir(os)
<returns a list of all module functions>
>>> help(os)
<returns an extensive manual page created from the module's docstrings>
```

对于日常文件和目录管理任务， shutil 模块提供了更易于使用的更高级别的接口:

```python
>>> import shutil
>>> shutil.copyfile('data.db', 'archive.db')
'archive.db'
>>> shutil.move('/build/executables', 'installdir')
'installdir'
```

## 文件通配符

glob 模块提供了一个在目录中使用通配符搜索创建文件列表的函数:

```python
>>> import glob
>>> glob.glob('*.py')
['primes.py', 'random.py', 'quote.py']
```

## 命令行参数

通用实用程序脚本通常需要处理命令行参数。这些参数作为列表存储在 sys 模块的 argv 属性中。例如，
以下输出来自在命令行运行 python demo.py one two three

```python
>>> import sys
>>> print(sys.argv)
['demo.py', 'one', 'two', 'three']
```

argparse 模块提供了一种更复杂的机制来处理命令行参数。以下脚本可提取一个或多个文件名，并可
选择要显示的行数：

```python
import argparse

parser = argparse.ArgumentParser(
        prog='top',
        description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)
```

当在通过 python top.py --lines=5 alpha.txt beta.txt 在命令行运行时，该脚本会将 args.
lines 设为 5 并将 args.filenames 设为 ['alpha.txt', 'beta.txt']。

## 错误输出重定向和程序终止

sys 模块还具有 stdin ， stdout 和 stderr 的属性。后者对于发出警告和错误消息非常有用，即使在 stdout 被
重定向后也可以看到它们:

```python
>>> sys.stderr.write('Warning, log file not found starting a new one\n')
Warning, log file not found starting a new one
```

终止脚本的最直接方法是使用 sys.exit() 。

## 字符串模式匹配

re 模块为高级字符串处理提供正则表达式工具。对于复杂的匹配和操作，正则表达式提供简洁，优化的
解决方案:

```python
>>> import re
>>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
>>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'cat in the hat'
```

当只需要简单的功能时，首选字符串方法因为它们更容易阅读和调试:

```python
>>> 'tea for too'.replace('too', 'two')
'tea for two
```

## 数学

math 模块提供对浮点数学的底层 C 库函数的访问:

```python
>>> import math
>>> math.cos(math.pi / 4)
0.70710678118654757
>>> math.log(1024, 2)
10.0
```

random 模块提供了进行随机选择的工具:

```python
>>> import random
>>> random.choice(['apple', 'pear', 'banana'])
'apple'
>>> random.sample(range(100), 10) # sampling without replacement
[30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
>>> random.random() # random float
0.17970987693706186
>>> random.randrange(6) # random integer chosen from range(6)
4
```

statistics 模块计算数值数据的基本统计属性（均值，中位数，方差等） :

```python
>>> import statistics
>>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
>>> statistics.mean(data)
1.6071428571428572
>>> statistics.median(data)
1.25
>>> statistics.variance(data)
1.3720238095238095
```

SciPy 项目 <https://scipy.org> 有许多其他模块用于数值计算。

## 互联网访问

有许多模块可用于访问互联网和处理互联网协议。其中两个最简单的 urllib.request 用于从 URL 检
索数据，以及 smtplib 用于发送邮件:

```python
>>> from urllib.request import urlopen
>>> with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
...     for line in response:
...         line = line.decode() # Convert bytes to a str
...         if line.startswith('datetime'):
...             print(line.rstrip()) # Remove trailing newline
...
datetime: 2022-01-01T01:36:47.689215+00:00
>>> import smtplib
>>> server = smtplib.SMTP('localhost')
>>> server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
... """To: jcaesar@example.org
... From: soothsayer@example.org
...
... Beware the Ides of March.
... """)
>>> server.quit()
```

（请注意，第二个示例需要在 localhost 上运行的邮件服务器。）

## 日期和时间

datetime 模块提供了以简单和复杂的方式操作日期和时间的类。虽然支持日期和时间算法，但实现的
重点是有效的成员提取以进行输出格式化和操作。该模块还支持可感知时区的对象。

```python
>>> # dates are easily constructed and formatted
>>> from datetime import date
>>> now = date.today()
>>> now
datetime.date(2003, 12, 2)
>>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
'12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'
>>> # dates support calendar arithmetic
>>> birthday = date(1964, 7, 31)
>>> age = now - birthday
>>> age.days
14368
```

## 数据压缩

常见的数据存档和压缩格式由模块直接支持，包括： zlib, gzip, bz2, lzma, zipfile 和 tarfile。 :

```python
>>> import zlib
>>> s = b'witch which has which witches wrist watch'
>>> len(s)
41
>>> t = zlib.compress(s)
>>> len(t)
37
>>> zlib.decompress(t)
b'witch which has which witches wrist watch'
>>> zlib.crc32(s)
226805979
```

## 性能测量

一些 Python 用户对了解同一问题的不同方法的相对性能产生了浓厚的兴趣。 Python 提供了一种可以立即
回答这些问题的测量工具。

例如，元组封包和拆包功能相比传统的交换参数可能更具吸引力。 timeit 模块可以快速演示在运行效
率方面一定的优势:

```python
>>> from timeit import Timer
>>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
0.57535828626024577
>>> Timer('a,b = b,a', 'a=1; b=2').timeit()
0.54962537085770791
```

与 timeit 的精细粒度级别相反， profile 和 pstats 模块提供了用于在较大的代码块中识别时间关
键部分的工具。

## 质量控制

开发高质量软件的一种方法是在开发过程中为每个函数编写测试，并在开发过程中经常运行这些测试。
doctest 模块提供了一个工具，用于扫描模块并验证程序文档字符串中嵌入的测试。测试构造就像将
典型调用及其结果剪切并粘贴到文档字符串一样简单。这通过向用户提供示例来改进文档，并且它允许
doctest 模块确保代码保持对文档的真实:

```python
def average(values):
    """Computes the arithmetic mean of a list of numbers.
    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod() # automatically validate the embedded tests
```

unittest 模块不像 doctest 模块那样易于使用，但它允许在一个单独的文件中维护更全面的测试集:

```python
import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)
unittest.main() # Calling from the command line invokes all tests
```

## 自带电池

Python 有“自带电池”的理念。通过其包的复杂和强大功能可以最好地看到这一点。例如:


-  xmlrpc.client 和 xmlrpc.server 模块使得实现远程过程调用变成了小菜一碟。尽管存在于
模块名称中，但用户不需要直接了解或处理 XML。


-  email 包是一个用于管理电子邮件的库，包括 MIME 和其他符合 RFC 2822 规范的邮件文档。与
smtplib 和 poplib 不同（它们实际上做的是发送和接收消息），电子邮件包提供完整的工具集，
用于构建或解码复杂的消息结构（包括附件）以及实现互联网编码和标头协议。


- json 包为解析这种流行的数据交换格式提供了强大的支持。 csv 模块支持以逗号分隔值格式
直接读取和写入文件，这种格式通常为数据库和电子表格所支持。 XML 处理由 xml.etree.
ElementTree ， xml.dom 和 xml.sax 包支持。这些模块和软件包共同大大简化了 Python 应用
程序和其他工具之间的数据交换。


- sqlite3 模块是 SQLite 数据库库的包装器，提供了一个可以使用稍微非标准的 SQL 语法更新和
访问的持久数据库。


- 国际化由许多模块支持，包括 gettext ， locale ，以及 codecs 包。

# 标准数据库简介-2

## 格式化输出

reprlib 模块提供了一个定制化版本的 repr() 函数，用于缩略显示大型或深层嵌套的容器对象:

```python
>>> import reprlib
>>> reprlib.repr(set('supercalifragilisticexpialidocious'))
"{'a', 'c', 'd', 'e', 'f', 'g', ...}"
```

pprint 模块提供了更加复杂的打印控制，其输出的内置对象和用户自定义对象能够被解释器直接读取。
当输出结果过长而需要折行时，“美化输出机制”会添加换行符和缩进，以更清楚地展示数据结构:

```python
>>> import pprint
>>> t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
...         'yellow'], 'blue']]]
...
>>> pprint.pprint(t, width=30)
[[[['black', 'cyan'],
    'white',
    ['green', 'red']],
    [['magenta', 'yellow'],
    'blue']]]
```

textwrap 模块能够格式化文本段落，以适应给定的屏幕宽度:

```python
>>> import textwrap
>>> doc = """The wrap() method is just like fill() except that it returns
... a list of strings instead of one big string with newlines to separate
... the wrapped lines."""
...
>>> print(textwrap.fill(doc, width=40))
The wrap() method is just like fill()
except that it returns a list of strings
instead of one big string with newlines
to separate the wrapped lines.
```

locale 模块处理与特定地域文化相关的数据格式。 locale 模块的 format 函数包含一个 grouping 属性，可
直接将数字格式化为带有组分隔符的样式:

```python
>>> import locale
>>> locale.setlocale(locale.LC_ALL, 'English_United States.1252')
'English_United States.1252'
>>> conv = locale.localeconv() # get a mapping of conventions
>>> x = 1234567.8
>>> locale.format("%d", x, grouping=True)
'1,234,567'
>>> locale.format_string("%s%.*f", (conv['currency_symbol'],
...                         conv['frac_digits'], x), grouping=True)
'$1,234,567.80'
```

## 模板

string 模块包含一个通用的 Template 类，具有适用于最终用户的简化语法。它允许用户在不更改应
用逻辑的情况下定制自己的应用。

。。。。。。。本章后面内容暂略。。。。。。。

# 虚拟环境和包

Python 应用程序通常会使用不在标准库内的软件包和模块。应用程序有时需要特定版本的库，因为应用
程序可能需要修复特定的错误，或者可以使用库的过时版本的接口编写应用程序。

这意味着一个 Python 安装可能无法满足每个应用程序的要求。如果应用程序 A 需要特定模块的 1.0 版本
但应用程序 B 需要 2.0 版本，则需求存在冲突，安装版本 1.0 或 2.0 将导致某一个应用程序无法运行。

这个问题的解决方案是创建一个virtual environment，一个目录树，其中安装有特定 Python 版本，以及许
多其他包。
然后，不同的应用将可以使用不同的虚拟环境。要解决先前需求相冲突的例子，应用程序 A 可以拥有自
己的安装了 1.0 版本的虚拟环境，而应用程序 B 则拥有安装了 2.0 版本的另一个虚拟环境。如果应用程
序 B 要求将某个库升级到 3.0 版本，也不会影响应用程序 A 的环境。

##  创建虚拟环境

用于创建和管理虚拟环境的模块称为 venv。 venv 通常会安装你可用的最新版本的 Python。如果您的系
统上有多个版本的 Python，您可以通过运行 python3 或您想要的任何版本来选择特定的 Python 版本。

要创建虚拟环境，请确定要放置它的目录，并将 venv 模块作为脚本运行目录路径:

```python
python3 -m venv tutorial-env
```

这将创建 tutorial-env 目录，如果它不存在的话，并在其中创建包含 Python 解释器副本和各种支持
文件的目录。

虚拟环境的常用目录位置是 .venv。这个名称通常会令该目录在你的终端中保持隐藏，从而避免需要对
所在目录进行额外解释的一般名称。它还能防止与某些工具所支持的 .env 环境变量定义文件发生冲突。

创建虚拟环境后，您可以激活它。

在 Windows 上，运行:

```python
tutorial-env\Scripts\activate.bat
```

在 Unix 或 MacOS 上，运行:

```python
source tutorial-env/bin/activate
```

激活虚拟环境将改变你所用终端的提示符，以显示你正在使用的虚拟环境，并修改环境以使 python 命
令所运行的将是已安装的特定 Python 版本。例如：

```python
$ source ~/envs/tutorial-env/bin/activate
(tutorial-env) $ python
Python 3.5.1 (default, May 6 2016, 10:59:36)
...
>>> import sys
>>> sys.path
['', '/usr/local/lib/python35.zip', ...,
'~/envs/tutorial-env/lib/python3.5/site-packages']
>>>
```

## 使用 pip 管理包

你可以使用一个名为 pip 的程序来安装、升级和移除软件包。默认情况下 pip 将从 Python Package Index
<https://pypi.org> 安装软件包。你可以在你的 web 浏览器中查看 Python Package Index。

pip 有许多子命令: ”install”, ”uninstall”, ”freeze” 等等。（请在 installing-index 指南页查看完整的 pip 文档。）

您可以通过指定包的名称来安装最新版本的包：

```python
(tutorial-env) $ python -m pip install novas
Collecting novas
    Downloading novas-3.1.1.3.tar.gz (136kB)
Installing collected packages: novas
    Running setup.py install for novas
Successfully installed novas-3.1.1.3
```

您还可以通过提供包名称后跟 == 和版本号来安装特定版本的包：

```python
(tutorial-env) $ python -m pip install requests==2.6.0
Collecting requests==2.6.0
    Using cached requests-2.6.0-py2.py3-none-any.whl
Installing collected packages: requests
Successfully installed requests-2.6.0
```

如果你重新运行这个命令， pip 会注意到已经安装了所请求的版本并且什么都不做。您可以提供不同的
版本号来获取该版本，或者您可以运行 pip install --upgrade 将软件包升级到最新版本：

```python
(tutorial-env) $ python -m pip install --upgrade requests
Collecting requests
Installing collected packages: requests
    Found existing installation: requests 2.6.0
        Uninstalling requests-2.6.0:
            Successfully uninstalled requests-2.6.0
Successfully installed requests-2.7.0
```

pip uninstall 后跟一个或多个包名称将从虚拟环境中删除包。


pip show 将显示有关特定包的信息：

```python
(tutorial-env) $ pip show requests
---
Metadata-Version: 2.0
Name: requests
Version: 2.7.0
Summary: Python HTTP for Humans.
Home-page: http://python-requests.org
Author: Kenneth Reitz
Author-email: me@kennethreitz.com
License: Apache 2.0
Location: /Users/akuchling/envs/tutorial-env/lib/python3.4/site-packages
Requires:
```

pip list 将显示虚拟环境中安装的所有软件包：

```python
(tutorial-env) $ pip list
novas (3.1.1.3)
numpy (1.9.2)
pip (7.0.3)
requests (2.7.0)
setuptools (16.0)
```

pip freeze 将生成一个类似的已安装包列表，但输出使用 pip install 期望的格式。一个常见的约定是
将此列表放在 requirements.txt 文件中：

```python
(tutorial-env) $ pip freeze > requirements.txt
(tutorial-env) $ cat requirements.txt
novas==3.1.1.3
numpy==1.9.2
requests==2.7.0
```

然后可以将 requirements.txt 提交给版本控制并作为应用程序的一部分提供。然后用户可以使用
install -r 安装所有必需的包：

```python
(tutorial-env) $ python -m pip install -r requirements.txt
Collecting novas==3.1.1.3 (from -r requirements.txt (line 1))
...
Collecting numpy==1.9.2 (from -r requirements.txt (line 2))
...
Collecting requests==2.7.0 (from -r requirements.txt (line 3))
...
Installing collected packages: novas, numpy, requests
    Running setup.py install for novas
Successfully installed novas-3.1.1.3 numpy-1.9.2 requests-2.7.0
```

pip 有更多选择。有关 pip 的完整文档，请参阅 installing-index 指南。当您编写一个包并希望在 Python
包索引中使它可用时，请参考 distributing-index 指南