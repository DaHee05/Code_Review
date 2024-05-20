Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = int(input())
... cnt = 0
... 
... for n in range(num):
...     alphabet = True
...     s = str(input())
...     
...     for i in range(1, len(s)):
...         if s[i] in s[0:i] and s[i-1] != s[i]:
...             alphabet = False
...     if alphabet == False:
...         cnt += 1
...         
