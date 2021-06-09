#เรียงจำนวนจากน้อยไปมาก input().split() ทำให้รับค่ากได้nครั้ง เเต่ละครั้งต้องเว้นวรรค เช่นรับ 1 2 3 4 เป็นต้น
a=[str(e) for e in input("รับจำนวน *เเนะนำ 4ตัว*").split()]
b=len(a)
i=1
sum=0
j=0
k=2
all=0
while j<b:
    while i<=(b-1):
        if (int(a[i])-int(a[i-1]))<0:
            sum = int(a[i]) - int(a[i - 1])
            a[i]=a[i-1]
            a[i - 1] = str(int(a[i - 1]) + sum)
            print(a[0],a[1],a[2],a[3])
        i=i+1
    if i>(b-1):
        i=1
        while i <=(b-1):
            if (int(a[i]) - int(a[i - 1])) < 0:
             sum = int(a[i]) - int(a[i - 1])
             a[i] = a[i - 1]
             a[i - 1] = str(int(a[i - 1]) + sum)
             print(a[0], a[1], a[2], a[3])
            i = i + 1
        j=j+1

print(b,"มีจำนวนทั้งหมด")
print("เรียงได้",a[0], a[1], a[2], a[3])