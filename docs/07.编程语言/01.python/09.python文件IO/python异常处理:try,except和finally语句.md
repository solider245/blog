## Python中的异常

Python有许多 [内置的异常](https://www.programiz.com/python-programming/exceptions) ，当您的程序遇到错误时会引发这些异常（程序中的某些错误）。

当发生这些异常时，Python解释器将停止当前进程并将其传递给调用进程，直到对其进行处理。 如果不处理，程序将崩溃。

例如，让我们考虑一个程序，我们有一个 [功能](https://www.programiz.com/python-programming/function) `A` 是调用函数 `B` ，进而调用功能 `C` 。 如果函数中发生异常 `C` 但未处理 `C` 该异常，则该异常将传递给 `B` ，然后 传递 给 `A` 。

如果从未处理过，则会显示一条错误消息，并且我们的程序突然突然中止。

---

## 在Python中捕捉异常

在Python中，可以使用 `try` 语句 处理异常 。

可能引发异常的关键操作放在 `try` 子句中。 处理异常的代码写在该 `except` 子句中。

因此，一旦捕获到异常，我们就可以选择要执行的操作。 这是一个简单的例子。

```py
# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)
```

**输出量**

The entry is a
Oops! <class 'ValueError'> occurred.
Next entry.

The entry is 0
Oops! <class 'ZeroDivisionError'> occured.
Next entry.

The entry is 2
The reciprocal of 2 is 0.5

在此程序中，我们遍历了 randomList 清单。 如前所述，可能导致异常的部分放置在 `try` 块 内部 。

如果没有异常发生， `except` 则跳过 该 块，并且继续正常流程（最后一个值）。 但是，如果发生任何异常，它将被该 `except` 块 捕获 （第一个值和第二个值）。

在这里，我们使用 模块 `exc_info()` 内部 的 函数 打印异常的名称 `sys` 。 我们可以看到 `a` 原因 `ValueError` 和 `0` 原因 `ZeroDivisionError` 。

由于Python中的每个异常都继承自基 `Exception` 类，因此我们还可以通过以下方式执行上述任务：

```py
# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)
```

该程序具有与上述程序相同的输出。

---

## 捕获Python中的特定异常

在上面的示例中，我们在 `except` 子句中 未提及任何特定的例外 。

这不是一个好的编程习惯，因为它将捕获所有异常并以相同的方式处理每种情况。 我们可以指定 `except` 子句应捕获的 异常 。

一个 `try` 子句可以具有任意数量的 `except` 子句来处理不同的异常，但是，只有在发生异常的情况下才会执行一个子句。

我们可以使用值的元组在except子句中指定多个异常。 这是示例伪代码。

```py
try:
   # do something
   pass

except ValueError:
   # handle ValueError exception
   pass

except (TypeError, ZeroDivisionError):
   # handle multiple exceptions
   # TypeError and ZeroDivisionError
   pass

except:
   # handle all other exceptions
   pass
```

---

## 在Python中引发异常

在Python编程中，在运行时发生错误时会引发异常。 我们还可以使用 `raise` 关键字 手动引发异常 。

我们可以选择将值传递给异常，以阐明引发该异常的原因。

```
>>> raise KeyboardInterrupt
Traceback (most recent call last):
...
KeyboardInterrupt

>>> raise MemoryError("This is an argument")
Traceback (most recent call last):
...
MemoryError: This is an argument

>>> try:
...     a = int(input("Enter a positive integer: "))
...     if a <= 0:
...         raise ValueError("That is not a positive number!")
... except ValueError as ve:
...     print(ve)
...
Enter a positive integer: -2
That is not a positive number!
```

---

## Python尝试使用else子句

在某些情况下，如果内部的代码块 `try` 运行无误 ，则可能要运行某个代码块 。 对于这些情况，可以 `else` 在 `try` 语句中 使用optional 关键字 。

**注意** ：else子句中的异常不会由前面的except子句处理。

让我们看一个例子：

```
# program to print the reciprocal of even numbers

try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)
```

**输出量**

如果我们传递一个奇数：

Enter a number: 1
Not an even number!

如果我们传递一个偶数，则将计算并显示倒数。

Enter a number: 4
0.25

但是，如果传递0，则得到的结果 `ZeroDivisionError` 是，其中的代码块 `else` 未由previous处理 `except` 。

Enter a number: 0
Traceback (most recent call last):
  File "<string>", line 7, in <module>
    reciprocal = 1/num
ZeroDivisionError: division by zero

---

## Python尝试...最终

`try` Python中 的 语句可以具有可选 `finally` 子句。 该子句无论如何执行，通常用于释放外部资源。

例如，我们可能通过网络或使用文件或图形用户界面（GUI）连接到远程数据中心。

在所有这些情况下，无论程序是否成功运行，我们都必须在程序停止之前清理资源。 这些操作（关闭文件，GUI或与网络断开连接）在该 `finally` 子句 中执行， 以确保执行。

这是一个 [文件操作](https://www.programiz.com/python-programming/file-operation) 的例子 来说明这一点。

```
try:
   f = open("test.txt",encoding = 'utf-8')
   # perform file operations
finally:
   f.close()
```

这种类型的构造可确保即使在程序执行期间发生异常，也可以关闭文件。