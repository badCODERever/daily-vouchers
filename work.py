Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
========= RESTART: C:\Users\User\Desktop\python\partstring - Copy.py =========
Traceback (most recent call last):
  File "C:\Users\User\Desktop\python\partstring - Copy.py", line 3, in <module>
    for i in range(0,len(string)-len(sub_string)+1):
NameError: name 'sub_string' is not defined
>>> 
========= RESTART: C:\Users\User\Desktop\python\partstring - Copy.py =========
>>> string[0:1]
'B'
>>> string[1:2]
'A'
>>> string[2:3]
'N'
>>> string[3:4]
'A'
>>> string[4:5]
'N'
>>> string[5:6]
'A'
>>> for i in range(len(string)):
	print(string[i:i+1])

	
B
A
N
A
N
A
>>> string[0:2]
'BA'
>>> string[1:3]
'AN'
>>> string[2:4]
'NA'
>>> string[3:5]
'AN'
>>> string[4:6]
'NA'
>>> for i in range(len(string)):
	for j in range(len(string)-i+1):
		print(i+":"+j)

		
Traceback (most recent call last):
  File "<pyshell#17>", line 3, in <module>
    print(i+":"+j)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> for i in range(len(string)):
	for j in range(len(string)-i+1):
		print(str(i+":"+j))

		
Traceback (most recent call last):
  File "<pyshell#19>", line 3, in <module>
    print(str(i+":"+j))
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> for i in range(len(string)):
	for j in range(len(string)-i+1):
		print(str(i, j))

		
Traceback (most recent call last):
  File "<pyshell#21>", line 3, in <module>
    print(str(i, j))
TypeError: str() argument 2 must be str, not int
>>> for i in range(len(string)):
	for j in range(len(string)-i+1):
		print(i, j)

		
0 0
0 1
0 2
0 3
0 4
0 5
0 6
1 0
1 1
1 2
1 3
1 4
1 5
2 0
2 1
2 2
2 3
2 4
3 0
3 1
3 2
3 3
4 0
4 1
4 2
5 0
5 1
>>> for i in range(len(string)):
	for j in range(len(string)):
		print(i, j)

		
0 0
0 1
0 2
0 3
0 4
0 5
1 0
1 1
1 2
1 3
1 4
1 5
2 0
2 1
2 2
2 3
2 4
2 5
3 0
3 1
3 2
3 3
3 4
3 5
4 0
4 1
4 2
4 3
4 4
4 5
5 0
5 1
5 2
5 3
5 4
5 5
>>> for i in range(len(string)):
	for j in range(len(string)+1):
		print(i, j)

		
0 0
0 1
0 2
0 3
0 4
0 5
0 6
1 0
1 1
1 2
1 3
1 4
1 5
1 6
2 0
2 1
2 2
2 3
2 4
2 5
2 6
3 0
3 1
3 2
3 3
3 4
3 5
3 6
4 0
4 1
4 2
4 3
4 4
4 5
4 6
5 0
5 1
5 2
5 3
5 4
5 5
5 6
>>> for i in range(len(string)):
	for j in range(i+1,len(string)+1):
		print(i, j)

		
0 1
0 2
0 3
0 4
0 5
0 6
1 2
1 3
1 4
1 5
1 6
2 3
2 4
2 5
2 6
3 4
3 5
3 6
4 5
4 6
5 6
>>> for i in range(len(string)):
	for j in range(i+1,len(string)+1):
		print(i+j)

		
1
2
3
4
5
6
3
4
5
6
7
5
6
7
8
7
8
9
9
10
11
>>> for i in range(len(string)):
	for j in range(i+1,len(string)+1):
		print(string[i:j])

		
B
BA
BAN
BANA
BANAN
BANANA
A
AN
ANA
ANAN
ANANA
N
NA
NAN
NANA
A
AN
ANA
N
NA
A
>>> li=[]
>>> for i in range(len(string)):
	for j in range(i+1,len(string)+1):
		li.append(i:j)
		
SyntaxError: invalid syntax
>>> 
>>> for i in range(len(string)):
	for j in range(i+1,len(string)+1):
		li.append(string[i:j])

		
>>> li
['B', 'BA', 'BAN', 'BANA', 'BANAN', 'BANANA', 'A', 'AN', 'ANA', 'ANAN', 'ANANA', 'N', 'NA', 'NAN', 'NANA', 'A', 'AN', 'ANA', 'N', 'NA', 'A']
>>> li.sort(key=len))
SyntaxError: invalid syntax
>>> li.sort(key=len)
>>> li
['B', 'A', 'N', 'A', 'N', 'A', 'BA', 'AN', 'NA', 'AN', 'NA', 'BAN', 'ANA', 'NAN', 'ANA', 'BANA', 'ANAN', 'NANA', 'BANAN', 'ANANA', 'BANANA']
>>> for i in range(len(li)):
	print(li[i]
