"""
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9    """

n=int(input("Enter a number = "))
for i in range(n):
	for j in range(1,n+1):
		print(j,end=" ")
	print()



"""
1 1 1 1 1 1 1 1 1
2 2 2 2 2 2 2 2 2
3 3 3 3 3 3 3 3 3
4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5
6 6 6 6 6 6 6 6 6
7 7 7 7 7 7 7 7 7
8 8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9   """

n=int(input("Enter a number = "))
for i in range(1,n+1):
	for j in range(n):
		print(i,end=" ")
	print()


"""
* * * * * * * * *
* * * * * * * * *
* * * * * * * * *
* * * * * * * * *
* * * * * * * * *
* * * * * * * * *
* * * * * * * * *
* * * * * * * * *
* * * * * * * * *   """

n=int(input("Enter a number = "))
for i in range(n):
	for j in range(n):
		print('*',end=" ")
	print()


"""
A B C D E F G
A B C D E F G
A B C D E F G
A B C D E F G
A B C D E F G
A B C D E F G
A B C D E F G   """

li=['A','B','C','D','E','F','G']
n=len(li)
for i in range(n):
	for j in range(n):
		print(li[j],end=" ")
	print()


"""
9 8 7 6 5 4 3 2 1
9 8 7 6 5 4 3 2 1
9 8 7 6 5 4 3 2 1
9 8 7 6 5 4 3 2 1
9 8 7 6 5 4 3 2 1
9 8 7 6 5 4 3 2 1
9 8 7 6 5 4 3 2 1
9 8 7 6 5 4 3 2 1
9 8 7 6 5 4 3 2 1  """

n=int(input("Enter a number = "))
for i in range(n):
	for j in range(n,0,-1):
		print(j,end=" ")
	print()


"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
1 2 3 4 5 6 7
1 2 3 4 5 6 7 8
1 2 3 4 5 6 7 8 9   """

n=int(input("Enter a number = "))
for i in range(1,n+1):
	for j in range(i):
		print(j+1,end=" ")
	print()


"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6 6 6
7 7 7 7 7 7 7
8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9  """

n=int(input("Enter a number = "))
for i in range(1,n+1):
	for j in range(i):
		print(i,end=" ")
	print()


"""
*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
* * * * * * * *
* * * * * * * * *   """

n=int(input("Enter a number = "))
for i in range(1,n+1):
	for j in range(i):
		print('*',end=" ")
	print()


"""
A
A B
A B C
A B C D
A B C D E
A B C D E F
A B C D E F G   """

li=['A','B','C','D','E','F','G']
n=len(li)
for i in range(1,n+1):
	for j in range(i):
		print(li[j],end=" ")
	print()


"""
9
9 8
9 8 7
9 8 7 6
9 8 7 6 5
9 8 7 6 5 4
9 8 7 6 5 4 3
9 8 7 6 5 4 3 2
9 8 7 6 5 4 3 2 1    """


n=int(input("Enter a number = "))
for i in range(1,n+1):
	for j in range(i):
		print(n-j,end=" ")
	print()


"""
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
6 5 4 3 2 1
7 6 5 4 3 2 1
8 7 6 5 4 3 2 1
9 8 7 6 5 4 3 2 1    """

n=int(input("Enter a number = "))
for i in range(1,n+1):
	for j in range(i):
		print(i-j,end=" ")
	print()

"""
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8
1 2 3 4 5 6 7
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1      """

n=int(input("Enter a number = "))
for i in range(n):
	for j in range(n-i):
		print(j+1,end=" ")
	print()
print('\n')


"""
9 8 7 6 5 4 3 2 1
9 8 7 6 5 4 3 2
9 8 7 6 5 4 3
9 8 7 6 5 4
9 8 7 6 5
9 8 7 6
9 8 7
9 8
9   """
n=int(input("Enter a number = "))
for i in range(n):
	for j in range(n-i):
		print(n-j,end=" ")
	print()

print('\n')


"""
9 8 7 6 5 4 3 2 1
8 7 6 5 4 3 2 1
7 6 5 4 3 2 1
6 5 4 3 2 1
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1    """
n=int(input("Enter a number = "))
for i in range(n):
	for j in range(n-i):
		print((n-i)-j,end=" ")
	print()

print('\n')


"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
1 2 3 4 5 6 7
1 2 3 4 5 6 7 8
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8
1 2 3 4 5 6 7
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1     """
n=int(input("Enter a number = "))
for i in range(1,n+1):
	for j in range(i):
		print(j+1,end=" ")
	print()
for i in range(n-1):
	for j in range((n-1)-i):
		print(j+1,end=" ")
	print()

print('\n')


"""
A
B A
C B A
D C B A
E D C B A
F E D C B A
G F E D C B A
"""

li=['A','B','C','D','E','F','G']
n=len(li)
for i in range(n):
	for j in range(i+1):
		print(li[i-j],end=" ")
	print()


""" A B C D E F G
    A B C D E F
    A B C D E
    A B C D
    A B C
    A B
    A   """


li=['A','B','C','D','E','F','G']
n=len(li)
for i in range(n):
	for j in range(n-i):
		print(li[j],end=" ")
	print()


""" * * * * * * * * *
    *               *
    *               *
    *               *
    *               *
    *               *
    *               *
    *               *
    * * * * * * * * * """

n=int(input("Enter a number = "))
for i in range(n):
	for j in range(n):
		if(i==0 or i==n-1):
			print('*',end=" ")
		else:
			if(j==0 or j==n-1):
				print('*',end=" ")
			else:
				print(' ',end=" ")

	print()

"""
*
* *
*   *
*     *
*       *
*         *
*           *
*             *
* * * * * * * * *
"""

n=int(input("Enter a number = "))
for i in range(1,n+1):
	for j in range(i):
		if i==1 or i==n:
			print('*',end=" ")
		else:
			if j==0 or j==i-1:
				print('*',end=" ")
			else:
				print(' ',end=" ")
	print()

"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31 32 33 34 35 36
37 38 39 40 41 42 43 44 45
"""
 
v=0
n=int(input("Enter a value = "))
for i in range(1,n+1):
	for j in range(i):
		v+=1
		print(v,end=" ")
	print()

"""
1
1 0
1 0 1
1 0 1 0
1 0 1 0 1
1 0 1 0 1 0
1 0 1 0 1 0 1
1 0 1 0 1 0 1 0
1 0 1 0 1 0 1 0 1
"""

n=int(input("Enter a value = "))
for i in range(1,n+1):
	for j in range(i):
		if j%2==0:
			print('1',end=" ")
		else:
			print('0',end=" ")
	print()


"""               1
                1   2
              1   2   3
            1   2   3   4
          1   2   3   4   5
        1   2   3   4   5   6
      1   2   3   4   5   6   7
    1   2   3   4   5   6   7   8
  1   2   3   4   5   6   7   8   9  """

n=int(input("Enter a number = "))
r=n+1
c=n+n
for i in range(1,n+1):
	v=1
	for j in range(1,c+1):
		if n-i >= j or ((n-i)+(i*2))<=j :
			print(" ",end=" ")
		elif i%2==0 :
			if j%2==0 :
				print(v,end=" ")
				v+=1
			else:
				print(" ",end=" ")
		else :
			if j%2==0:
				print(" ",end=" ")
			else:
				print(v,end=" ")
				v+=1
	print()


"""              0
                1 0 1
              2 1 0 1 2
            3 2 1 0 1 2 3
          4 3 2 1 0 1 2 3 4
        5 4 3 2 1 0 1 2 3 4 5
      6 5 4 3 2 1 0 1 2 3 4 5 6
    7 6 5 4 3 2 1 0 1 2 3 4 5 6 7
  8 7 6 5 4 3 2 1 0 1 2 3 4 5 6 7 8  """

n=int(input("Enter a number = "))
ine=2*n+1
for i in range(0,n+1):
	v=i
	for j in range(0,ine):
		if i==0 or j==n:
			if j==n :
				print('0',end=" ")
			else:
				print(" ",end=" ")
		elif j<n and i!=0:
			if j>=n-i :
				print(v, end=" ")
				v-=1
			else:
				print(" ",end=" ")
		elif j>n and i!=0:
			if j<=n+i :
				v+=1
				print(v, end=" ")
			else:
				print(" ",end=" ")
	print()


""" A B C D E F G G F E D C B A
      A B C D E F F E D C B A
        A B C D E E D C B A
          A B C D D C B A
            A B C C B A
              A B B A
                A A """


lis=['A','B','C','D','E','F','G']
n=len(lis)
inr=2*n
c=inr-1
for i in range(n):
	v=0
	for j in range(inr):
		if j<n:
			if j>=i:
				print(lis[v],end=" ")
				v+=1
			else:
				print(" ", end=" ")
		elif j>=n:
			if j<=c-i:
				v-=1
				print(lis[v],end=" ")
				
			else:
				print(" ", end=" ")	
	print()
		

