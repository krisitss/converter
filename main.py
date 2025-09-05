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
    mi = round(kms*0.62, 2)
    print(f"Rezultāts ir {mi} jūdzes")