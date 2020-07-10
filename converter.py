c =input("Enter the temperature: ")
f=(9.0/5)*c+32
print(int(f))

def leng(m, s):
    h = m/60 + s/3600
    print(int(h))

m = input("Enter number of minutes: ")
s = input("Enter number of sec: ")

leng(m,s)
