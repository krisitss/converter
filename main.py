"""
THIS IS CONVERTER
"""
# converts F value to C value
def convertCtoF():
    C = float(input("ievadi C:"))
    F = (C*9/5) +32
    print(F)

# converts KM value to MI value
def convertKMtoMI():
    kms = float(input("Ievadi KM:"))
    if kms>0:
        mi = round(kms*0.62, 2)
        print(f"Rezultāts ir {mi} jūdzes")
    else: 
        print("Nederīga vērtība")

# converts eur to usd
def convertEURtoUSD():
    eur = float(input("Ievadi EUR:"))
    if eur>0:
        usd = round(eur*1.17, 2)
        print(f"Rezultāts ir {usd} dolāri")
    else:
        print("Nederīga vērtība")

# converts area
def convertArea():
    square_m = float(input("Ievadi m^2:"))
    if square_m>0:
        ha = square_m / 10000
        print(f"{square_m} m^2 ir {ha} hektāri")
    else:
        print("Nederīga vērtība")

convertArea()