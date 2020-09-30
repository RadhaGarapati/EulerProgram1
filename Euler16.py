a = 2 ** 1000
data = []
ans = 0

for i in str(a):
    data.append(int(i))
for i in range(0, len(data)):
    ans += data[i]
print(ans)
