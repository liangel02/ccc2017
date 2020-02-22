n = int(input())
tides = input()

sets = (n/2)
sets = int(sets)

tides = tides.split(" ")
tides = list(map(int, tides))
tides.sort()

lowTides = []
highTides = []
measurement = []


for i in range(0, sets, 1):
    lowTides.append(tides[i])
for i in range(sets, len(tides), 1):
    highTides.append(tides[i])
lowTides.sort(reverse=True)

for i in range(0, len(lowTides), 1):
    measurement.append(lowTides[i])
    measurement.append(highTides[i])

string = " ".join(str(e) for e in measurement)
print(string)
