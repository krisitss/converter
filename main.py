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

def convertEURtoUSD():
    eur = float(input("Ievadi EUR:"))
    if eur>0:
        usd = round(eur*1.17, 2)
        print(f"Rezultāts ir {usd} dolāri")
    else:
        print("Nederīga vērtība")