import cv2 as cv
from os import listdir, getcwd
from os.path import exists
from pyperclip import paste
from pyzbar.pyzbar import decode


if __name__ == "__main__":
        print(listdir(getcwd()))

        nome_img = input('Insira o nome da imagem a ser escaneada:\n')

        if(exists(nome_img)):
                img = cv.imread(str(nome_img))

                for cdg_barra in decode(img):
                        if(cdg_barra.type.lower() == 'code128'):
                                print(cdg_barra.data.decode('utf-8'))

                exit()

