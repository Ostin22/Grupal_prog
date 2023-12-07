n = float(input("Ingrese una cantidad: "))
medida = input("Ingrese un tipo de unidad: ")
mm = "mm"
cm = "cm"
m = "m"
hm = "hm"
km = "km"
if(medida == mm or medida == cm or medida == m or medida == hm or medida == km):
    if(medida == mm):
        cm = n / 10
        m = n / 1000
        hm = n / 100000
        km = n / 1000000
        print("mm = ", n)
        print("cm = ", cm)
        print("m = ", m)
        print("hm = ", hm)
        print("km = ", km)
    if(medida == cm):
        mm = n * 10
        m = n / 100
        hm = n / 10000
        km = n / 100000
        print("mm = ", mm)
        print("cm = ", n)
        print("m = ", m)
        print("hm = ", hm)
        print("km = ", km)
    if(medida == m):
        mm = n * 1000
        cm = n * 100
        hm = n / 100
        km = n / 1000
        print("mm = ", mm)
        print("cm = ", cm)
        print("m = ", n)
        print("hm = ", hm)
        print("km = ", km)
    if(medida == hm):
        mm = n * 100000
        cm = n * 10000
        m = n * 100
        km = n / 10
        print("mm = ", mm)
        print("cm = ", cm)
        print("m = ", m)
        print("hm = ", n)
        print("km = ", km)
    if(medida == km):
        mm = n * 1000000
        cm = n * 100000
        m = n * 1000
        hm = n * 10
        print("mm = ", mm)
        print("cm = ", cm)
        print("m = ", m)
        print("hm = ", hm)
        print("km = ", n)
else:
    print("--------------------------------")
    print("Ingrese un tipo de unidad valido")