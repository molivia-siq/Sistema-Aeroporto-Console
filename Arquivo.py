def existe_arquivo(nome):
    import os
    if os.path.exists(nome):
        return True
    else:
        return False

#--------------------- PILOTOS ----------------------------

def existeArqP(dic):

    # print('oiiiiii')

    if (existe_arquivo("pilotos.txt")):

        # print('aiai')

        arq=open("pilotos.txt","r")

        # linha= arq.readline()
        # linha=linha[:-1]

        # while linha != "":

        #     inf= linha.split(";")

        #     rp=int(inf[0])
        #     inf[2]= inf[2]
        #     del inf[0]
        #     dic[rp]=inf

        #     linha= arq.readline()
        #     linha=linha[:-1]

        for linha in arq:

            linha = linha[:len(linha)-1]
            # print(linha)

            inf= linha.split(";")
            # print(inf)

            rp=int(inf[0])
            del inf[0]
            dic[rp]=inf

        arq.close()


def linhaArqP(dic):

    arq=open('pilotos.txt', 'w')

    for elem in dic:

        rp = str(elem)
        info= dic[elem]
        nome=info[0]
        data=info[1]
        horas= info[2]
        email=info[3]
        tel=info[4]

        linha= rp + ';' + nome + ';' + data + ';' + horas + ';' + email + ';' + tel + '\n'

        arq.write(linha)

    arq.close()


#--------------------- FIM PILOTOS ----------------------------
    

#--------------------- VOOS ----------------------------

def existeArqVoo(dic):
    
    if (existe_arquivo('voos.txt')):

        arq= open('voos.txt','r')

        # linha= arq.readline()
        # print (linha)
        # linha=linha[:-1]
        # while linha != '':

        #     inf= linha.split(';')
        #     print(inf)
        #     inf[5]= inf[5].split('-')

        #     num= int(inf[0])
        #     inf[2]= inf[2]

        #     del inf[0]

        #     dic[num]= inf

        #     linha= arq.readline()

        #     linha=linha[:-1]

        for linha in arq:

            linha = linha[:len(linha)-1]

            inf= linha.split(';')
            inf[5]= inf[5].split('-')

            num= int(inf[0])

            del inf[0]

            dic[num]= inf

        arq.close()


def linhaArqVoo(dic):

    arq=open('voos.txt', 'w')

    for elem in dic:

        num= str(elem)
        info= dic[elem]
        cidO= info[0]
        cidD= info[1]
        tempo= info[2]
        aeronave= info[3]
        cidsE = "-".join(info[4])

        linha= num + ';' + cidO + ';' + cidD + ';' + tempo + ';' + aeronave + ';' + cidsE + '\n'

        arq.write(linha)

    arq.close()

#--------------------- FIM VOOS ----------------------------

#--------------------- VIAGENS ----------------------------


def existeArqVi(dic):

    h= existe_arquivo("viagens.txt")

    if (h):

        arq=open("viagens.txt","r")

        # linha= arq.readline()
        # linha=linha[:-1]

        # while linha != "":
        #     inf= linha.split(";")
        #     num=inf[0],
        #     piloto=int(inf[1]),
        #     data=inf[2],
        #     hora=inf[3],
        #     passageiros=int(inf[4])
        #     chave=num + piloto + data + hora
        #     dic[chave]=passageiros
        #     linha= arq.readline()
        #     linha=linha[:-1]

        for linha in arq:

            linha = linha[:len(linha)-1]
            # print(linha)

            inf= linha.split(";")
            # print (inf)
            num= int(inf[0])
            piloto=int(inf[1])
            data=inf[2]
            hora=inf[3]
            passageiros= int(inf[4])
            chave= (num , piloto , data , hora)
            dic[chave]= passageiros

        arq.close()


def linhaArVi(dic):

    arq=open('viagens.txt', 'w')

    for elem in dic:

        passageiros= str(dic[elem])

        chave= list(elem)
        num= str(chave[0])
        piloto= str(chave[1])
        data= chave[2]
        hora= chave[3]
        linha= num + ';' + piloto + ';' + data + ';' + hora + ';' + passageiros + '\n'

        arq.write(linha)

    arq.close()


#--------------------- FIM VIAGENS ----------------------------