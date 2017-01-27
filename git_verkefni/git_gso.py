#Eyjólfur J.
skra = input("Skráðu inn nafn skráar")
nafnskra = skra +".txt"
file = open(nafnskra,"w+")

file.write("tilgangslaus texti ""\n")
file.close()


nafn = input("Sláðu inn nafn : ")
kennitala = input("Sláðu inn kennitölu : ")
aldur = int(input("Sláðu inn aldur"))

file = open(nafnskra,"a")
file.write(nafn+"\n")
file.write(kennitala+"\n")
file.write(str(aldur))
file.close()



