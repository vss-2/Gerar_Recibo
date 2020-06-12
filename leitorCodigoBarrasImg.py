import cv2 as cv
from os import listdir, getcwd
from os.path import exists
from pyperclip import paste
from pyzbar.pyzbar import decode


if __name__ == "__main__":
        lista = listdir(getcwd())
	img_suf = ['jpg','png','bmp','ico','webp']
        k = 0
        for l in lista:
                if(l[-3:] in img_suf):
			print(k,'\033[92m'+l+'\033[0m')
		else:
			print(k,l)
                k += 1

        nome_img = input('Insira o nome da imagem a ser escaneada:\n')

        try:
                # Vê se foi input inteiro ou nome
                nome_img = lista[int(nome_img)]
        finally:
                if(exists(nome_img)):
                        img = cv.imread(str(nome_img))

                        for cdg_barra in decode(img):
                                if(cdg_barra.type.lower() == 'code128'):
                                        with open(str(nome_img[:-3]+'txt'), 'w+') as arq:
                                                arq.write(cdg_barra.data.decode('utf-8'))
                                                arq.close()
                else:
                        print('Arquivo não encontrado!')
                exit()
