x = 0b111
y = 0b101
z = x&y
r = x|y
print(z)
print(r)
def f(n):
    print("{:8b}".format(n))
f(z)
f(z>>2)
f(z<<2)