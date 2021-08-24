def main():
    #escribe tu código abajo de esta línea
    pactual=(float(input("Insert your actual weight: ")))
pdeseado=(float(input("Insert your desired weight: ")))
meses=(int(input("Insert the months you'll be on the program: ")))
kgporbajar=(float((pactual-pdeseado)/meses))
print("Weight you have to loose per month: ",kgporbajar)
    pass
    


if __name__ == '__main__':
    main()
