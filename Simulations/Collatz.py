from matplotlib import pyplot as plt

def collatz(x):
    z = 0
    while x > 1:
        if x % 2:
            x = x * 3 + 1
        else:
            x /= 2
        z += 1
    return z

li = []
for i in range(0, 200):
    li.append(collatz(i))


plt.plot(li)
plt.show()
