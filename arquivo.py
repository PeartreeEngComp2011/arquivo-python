arquivo = open("arquivo.txt")

linhas = arquivo.readlines()

#Abrir novo arquivo

w = open("arquivo2.txt","w")

#Escrevendo no arquivo

w.write("Eulália")

#Abrir novamente o arquivo

w = open("arquivo2.txt","a")

#Escrevendo no arquivo

w.write("Tamiles\n")

#Fechando o arquivo

w.close()

print(linhas)