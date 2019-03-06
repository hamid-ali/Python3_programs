def mes_len(s):
                try:
                    size=len(s)
                    return(size)
                except:
                        return"No.s dont have any size"
sentence = input("enter ur sentence:    ")
print("Length of entered sentence is " + str(mes_len((sentence))))
print(mes_len(123456))