#######  1.  #########
n= 256		# 2^8 :-)
for i in range(n):
    print(i)


#######  2. ##########
while n:
    print(n)
    n = n-1


######   3. ##########
i = 0
## Assume k << n
while i<n:
    i = i+k

########   4.   #####
i = 1
## Assume k << n
while i<n:
    i = i*k

#######  5. #######
i = n
## Assume k << n
while i>1:
    i = i/k

#######  6. #######
i = 1
while i*i<n:
    i = i+1
    print(i)

########  7. ####
i = 1
j = 0
while j<n:
    j = j+i
    i = i+1

######  8. #######
i = 0
while i<n:
    j = 0
    while j<n:
        print(f'{i},{j}')
        j = j+1
    i = i+1

#############8’#######
p = 0
i = 1
while i< n 
	i = i*2
	p = p+1
j = 1
while j<p:
j = j*2

######  9. #######
i = 0
while i<n:
    j = 0
    while j<n:
        print(f'{i},{j}')
        j = j*k
    i = i+1

###### 10.########
i = 0
while i<n:
i = i+1

j = 0
while j<n:
print(f'{i},{j}')
j = j*k

