Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = [i for i in range(1,31)]
...     
... for i in range (28):
...     yes = int(input())
...     s.remove(yes)
...     
... print(min(s))
