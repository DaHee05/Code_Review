Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s=[]
... for i in range (10):
...     a = int(input())
...     s.append(a%42)
... 
... s = set(s)
