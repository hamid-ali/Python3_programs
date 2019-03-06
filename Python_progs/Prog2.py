def celcius_to_farenhite(c):
                            if c < -273.15:
                                            return"Temp can't go to this value!!!"
                            else:
                                return(c*9/5 + 32)

deg_cel = input("Enter temp in celcius: ")
print("This temp in Farenhite equals to : \n" + str(celcius_to_farenhite(float(deg_cel))))