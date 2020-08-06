---
title: Python 🐍🐍🐍
---

# Python

## Control Flow
1. if Statements
    * Cấu trúc điều kiện if...else 
    * Tùy chọn if...elif...elif... thay thế  switch...case trong các ngôn ngữ khác 
2. for Statements
    * Vòng lặp for lặp qua cái item của sequence(list or string)
3. The range() Function
    * Sử dụng range(n) vòng lặp chạy từ 0 đến n-1
4. break and continue Statements, and else Clauses on Loops
    * **break**: Dừng chương trình
    * **continue**: Dùng để tiếp tục vòng lặp tiếp 
5. pass Statements
    * Sử dụng để yêu câu phải có cú pháp. Câu lệnh này không làm gì cả
6. Defining Functions
    * Sử dụng **def** khai bao Function
    * Tạo 1 Function tính giai thừa 
    ```python
    def Factotial(n):
        while (n>0):
            if (n == 1):
                return 1
            else: return n*Factotial(n-1)
    ```
## Data Structures
1. More on Lists 
    * list.append(x): Thêm phần tử  vào cuối List tương đương `a[len(a):] = [x]` 
    * list.extend(iterable): Extend the list by appending all the items from the iterable. Equivalent to `a[len(a):] = iterable`
    * list.insert(i, x): Chèn item x vào vị trí i. `a.insert(len(a), x)` is equivalent to `a.append(x)`
    * list.remove(x): Remove item có giá trị bằng x. Trả về  `ValueError` nếu không tìm thấy item đó
    * list.pop([i]): Remove item ở vị trí i và trả về  giá trị của nó. `a.pop()` remove và trả về giá trị của item cuối cùng của list
    * list.clear(): Remove toàn bộ item trong list
    * list.index(x[, start[, end]]): Trả về  vị trí của item trong lists. Trả về  `ValueError` nếu không tìm thấy item đó.
    ```bash
    >>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    >>> fruits.index('banana')
    4
    >>> fruits.index('banana', 4)
    6
    ```
    * list.count(x): Trả về  số  lần xuất hiện của item x trong list, nếu không có item x trong x trả về 0
    * list.sort(key=None, reverse=False): Sắp xếp các item trong list
    * list.reverse(): Đảo ngược lại list
    * list.copy(): Return a shallow copy of the list  Equivalent to `a[:]`
2. Using Lists as Stacks
    * LIFO 
    ```bash
    >>> stack = [3, 4, 5]
    >>> stack.append(6)
    >>> stack
    [3, 4, 5, 6]
    >>> stack.pop()
    6
    >>> stack
    [3, 4, 5]
    ```
3. Using Lists as Queues
    * FIFO. **However, lists are not efficient for this purpose**
    * Để  thực hiện như 1 hàng đợi, sử dụng `collections.deque`
    ```bash
    >>> from collections import deque
    >>> queue = deque(["Eric", "John", "Michael"])
    >>> queue.append("Terry") 
    >>> queue
    deque(['Eric', 'John', 'Michael', 'Terry'])
    >>> queue.popleft()
    'Eric'
    >>> queue
    deque(['John', 'Michael', 'Terry'])
    ```
4. List Comprehensions
    * List Comprehensions cung cấp các cách ngắn gọn để  tạo ra List
    * Tạo 1 list các số  chính phương
    ```bash
    >>> squares = []
    >>> for x in range(10):
    ...     squares.append(x**2)
    ...
    >>> squares
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    ```
    * Có thể  tạo list theo cách sau
    ```bash
    squares = list(map(lambda x: x**2, range(10)))
    ```
    or
    ```
    squares = [x**2 for x in range(10)]
    ```
5. Nested List Comprehensions
6. The del statement
    * Remove item trong list, khác với pop() trả về  item bị xóa.
    ```bash
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
7. Tuples and Sequences
    * Tuples are **immutable**, Lists are **mutable**
8. Sets
    * Set là tập các element không trùng nhau, không có thứ tự
    ```bash
    >>> S = {'a', 'b', 'c', 'd', 'e', 'a'}
    >>> S
    {'a', 'b', 'c', 'd', 'e'}
    >>> set(S)
    {'e', 'a', 'b', 'd', 'c'}
    ```
9. Dictionaries
    * Dictionaries đánh dấu bằng *key*, là cặp `key: value`
    ```bash
    >>> animals = {'cat': 'meow', 'chipu': 'ooo', 'mouse': 999}
    {'cat': 'meow', 'chipu': 'ooo', 'mouse': 999}
    >>> animals['bird'] = 0
    >>> animals
    {'cat': 'meow', 'chipu': 'ooo', 'mouse': 999, 'bird': 0}
    ```
    * `dict()` xây dựng dictionaries từ các cặp *key-value*
    ```bash
    >>> dict([('J', 11), ('Q', 12), ('K', 13), ('A', 1)])
    {'J': 11, 'Q': 12, 'K': 13, 'A': 1}
    ```
## Modules and Packages
1. Modules
    * Module: Python has a way to put definitions in a file and use them in a script or in an interactive instance of the interpreter. 
    * Các definitions từ 1 module có thể  được *import* vào module khác hoặc module chính. 
    * Tạo file **fibo.py**
    ```python
    def fib(n):    # write Fibonacci series up to n
        a, b = 0, 1
        while a < n:
            print(a, end=' ')
            a, b = b, a+b
        print()

    def fib2(n):   # return Fibonacci series up to n
        result = []
        a, b = 0, 1
        while a < n:
            result.append(a)
            a, b = b, a+b
        return result
    ```
    * `import fibo` trong interpreter
    ```bash
    >>> import fibo
    ```
    ```bash
    >>> fibo.fib(1000)
    0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
    >>> fibo.fib2(100)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    >>> fibo.__name__
    'fibo'
    ```
    * Trong trường hợp nếu không muốn sử dụng toàn bộ module mà chỉ sử dụng 1 phần, sử dụng `from...import`
    ```bash
    >>> from fibo import fib
    ```
2. Packages 
    * Package trong Python là một thư mục chứa một hoặc nhiều modules hay các package khác nhau, nó được tạo ra  nhằm mục đích phân bố các modules có cùng chức năng hay một cái gì đó, để dễ quản lý source code
    * Tạo 1 package chỉ cần tạo 1 thư mục, tên thư mục là tên package và phải có file `__init__.py`, file này sẽ được gọi ra đầu tiên khi import package
## Errors and Exceptions
1. Errors
2. Exceptions 
    * Xử  lý lỗi ngoại lệ, là Error được phát hiện khi thực hiện chương trình.
    * Tạo chương trình tính thương 2 số
    ```python
    def test(a, b):
        return a / b
    print(test(6, 0))
    ```
    Kết quả
    ```bash
    Traceback (most recent call last):
        File "test.py", line 4, in <module>
            print(test(6, 0))
        File "test.py", line 2, in test
            return a / b
    ZeroDivisionError: division by zero
    ```
3. Handling Exceptions
    * Sử dụng `try...except`
    * Nếu khối lệnh trong `try` có 1 lỗi gì đó xảy ra thì chương trình sẽ tìm các except bên dưới, nếu có except thỏa mãn nó sẽ thực thi code trong khối except đó 
    ```python
    def test(a, b):
        return a / b

    try :
        print(test(6, 0))
    except ZeroDivisionError:
        print('Bug Bug !!!')
    ```
    Kết quả
    ```bash
    Bug Bug !!!
    ```
4. Raising Exceptions
    * Cho phép chỉ định *exception* khi xảy ra lỗi
    ```bash
    >>> raise ValueError('Hello World !!!')
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    ValueError: Hello World !!!
    ```
## Classes
+ Khai báo class
```python
class Person:
    pass:
``` 
+ Khai báo các thuộc tính (name, age, sex) và các phương thức (getName(), setAge(), getAge(), setMale(), getMAle()) trong class
```python
class Person:
    # thuộc tính
    name = "DUCTN";
    age = 22;
    male = True
    # phương thức
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def setAge(self, age):
        self.age = age
    
    def getAge(self):
        return self.age
    
    def setMale(self, male):
        self.male = male
    
    def getMale(self):
        return self.male
```
+ Khởi tạo class sau khi khái báo
```python
person = Person()
```
## Virtual Environments
1. Intro
    * Khi thực hiện 1 project, việc tạo ra 1 môi trường ảo giúp project thực hiện được độc lập với các project khác, phù hợp theo yêu cầu, đúng phiên bản với các modules hay packages sử dụng mà không nằm trong thư viện chuẩn của python. 
    * Tránh bị conflic giữa các app khi đang code.
    * Các app khác nhau có thể sử dụng trong các môi trường khác nhau
2. Creating Virtual Environments
    * Tạo môi trường ảo tên `ductn`
    ```bash
    $ python3 -m venv ductn
    ```
    * Kích hoạt môi trường
    ```bash
    $ source ductn/bin/activate
    ```
    * Cài đặt các gói package
    Tải ver mới nhất
    ```bash
    (ductn) $ pip install requests
    ```
    Tải ver cụ thể
    ```bash
    (ductn) $ pip install requests==2.6
    ```
    Update ver 
    ```bash
    (ductn) $ pip install --upgrade requests
    ```
    * Khi có thông tin về  tên và ver của các packages trong requirements.txt, chỉ cần thực thi lệnh sau để  cài đặt.
    ```bash
    $ pip install -r requirements.txt
    ```
    * Đưa lists các packages và 1 file, sử dụng
    ```
    $ pip freeze > requirements.txt
    ```
1. ML Basic
2. Algorithm
3. Syntax basic
4. Syntax basic_2
5. Network automation

### Follow [me](https://github.com/ductnn)