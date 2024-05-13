Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> hour, min = map(int, input().split())
... if min < 45:
...     min = min + 15
...     hour -= 1
...     if hour < 0:
...         hour = 23
... else:
...     min -= 45
... 
