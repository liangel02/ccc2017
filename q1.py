input1 = input()
swifts = input()
semaphores = input()

swifts = swifts.split(" ")
swifts = list(map(int, swifts))
semaphores = semaphores.split(" ")
semaphores = list(map(int, semaphores))
ret = 0
sumSwifts = 0
sumSemaphores = 0

for i in range(0, len(swifts), 1):
    sumSwifts += swifts[i]
    sumSemaphores += semaphores[i]
    if i == 0:
        if swifts[i] == semaphores[i]:
            ret = i + 1
    else:
        if sumSwifts == sumSemaphores:
            ret = i + 1
print(ret)

