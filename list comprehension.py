# for loop
temps = [100.0, 98.6, 78.34, 88.5, 34.2]
windChillRate = 0.9

lst = []

for i in range(len(temps)):
    lst.append(temps[i] *(1+ windChillRate))
    
print(lst)


# map()
temps = [100.0, 98.6, 78.34, 88.5, 34.2]
windChillRate = 0.9

def getWindChills(temps):
    return temps * (1 + windChillRate)

final_temps = map(getWindChills, temps)
list(final_temps)
print(list(final_temps))

# list comprehension
temps = [100.0, 98.6, 78.34, 88.5, 34.2]
windChillRate = 0.9

lst = [x*(1 + windChillRate) for x in temps]
    
print(lst)


