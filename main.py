print("Алгоритм Евклида")
a = int(input("Введите число a\n"))
b = int(input("Введите число b\n"))
while(a!=0 and b!=0):
    if(a>b):
        a,b = a%b, b%a
    else: b = b%a
print(a+b)