Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> h, m = map(int, input().split())
... t = int(input())
... h += t//60
... m += t%60
... if m > 59:
...     m -= 60
...     h +=1
... if h > 23:
...     h = h - 24
...     
