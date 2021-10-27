#######  1.  #########
n= 256		# 2^8 :-)
cnt = 0
for i in range(n):
    cnt +=1
    # print(cnt, i)
print("1,", cnt)

#######  2. ##########
n = 256
cnt = 0
while n:
    cnt+=1
    #print(cnt, n)
    n = n-1
print("2,", cnt)

######   3. ##########
n = 256
i = 0
k = 2
cnt = 0
## Assume k << n
while i<n:
    cnt+=1
    i = i+k
    #print(cnt,i)
print("3,", cnt)

########   4.   #####
n = 256
i = 1
k=2
cnt=0
## Assume k << n
while i<n:
    cnt+=1
    i = i*k
    #print(cnt,i)
print('4,', cnt)


#######  5. #######
n = 256
i = n
k=2
cnt=0
## Assume k << n
while i>1:
    cnt+=1
    i = i/k
    # print(cnt,i)
print('5,', cnt)

#######  6. #######
n = 256
i = 1
cnt=0
while i*i<n:
    cnt+=1
    i = i+1
    #print(cnt, i)
print('6,', cnt)

########  7. ####
n = 256
i = 1
j = 0
cnt=0
while j<n:
    cnt+=1
    j = j+i
    i = i+1
print('7,', cnt)

######  8. #######
n = 256
i = 0
while i<n:
    j = 0
    while j<n:
        #print(f'{i},{j}')
        j = j+1
    i = i+1
print('8,', cnt)

#############8’#######
n = 256
cnt = 0
p = 0
i = 1
while i< n: 
	i = i*2
	p = p+1
j = 1
while j<p:
    j = j*2
    cnt+=1
print('8_,', cnt)

######  9. #######
cnt = 0
i = 0
n = 256
while i<n:
    j = 0
    while j<n:
        #print(f'{i},{j}')
        j = j*k
        cnt+=1
    i = i+1
print('9,', cnt)

###### 10.########
i = 0
n = 256
while i<n:
    i = i+1

j = 0
while j<n:
    #print(f'{i},{j}')
    j = j*k
    cnt +=1
print('10,',cnt)

