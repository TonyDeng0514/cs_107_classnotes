# map()
temps = [100.0, 98.6, 78.34, 88.5, 34.2]
windChillRate = 0.9

def getWindChills(temps):
    return temps * (1 + windChillRate)

final_temps = map(getWindChills, temps)
list(final_temps)
