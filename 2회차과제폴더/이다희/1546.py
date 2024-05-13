Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = int(input())
... score = list(map(int, input().split()))
... m = max(score)
... 
... for i in range (num):
...     score[i] = score[i]/m*100
...     
