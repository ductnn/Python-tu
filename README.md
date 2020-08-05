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
    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    fruits.index('banana')
    4
    fruits.index('banana', 4)
    6
    ```
    * list.count(x): Trả về  số  lần xuất hiện của item x trong list, nếu không có item x trong x trả về 0
    * list.sort(key=None, reverse=False): Sắp xếp các item trong list
    * list.reverse(): Đảo ngược lại list
    * list.copy(): Return a shallow copy of the list  Equivalent to `a[:]`
2. Using Lists as Stacks

## Modules
## Errors and Exceptions
## Classes
## Virtual Environments
## Packages

1. ML Basic
2. Algorithm
3. Syntax basic
4. Syntax basic_2
5. Network automation

### Follow [me](https://github.com/ductnn)