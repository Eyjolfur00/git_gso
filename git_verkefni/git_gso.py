#Eyjólfur J.

file = open("gso.txt","w")

file.write("tilgangslaus texti ")
file.close()


nafn = str(input("Sláðu inn nafn : "))
kennitala = input("Sláðu inn kennitölu : ")
print("-----------------------------")
print("Nafn þitt er",nafn)
print("Kennitalan þín er : ",kennitala)
print("Takk fyrir  :)")
print("-----------------------------")
file = open("gso.txt","r")
