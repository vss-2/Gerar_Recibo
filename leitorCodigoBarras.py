import cv2
import pyperclip
from pyzbar.pyzbar import decode

if __name__ == "__main__":
        cap = cv2.VideoCapture(0)
        cap.set(3, 640)
        cap.set(4, 480)

        while True:
                for cdg_barra in decode(cap):
                        if(cdg_barra.type.lower() == 'code128'):
                                pyperclip.paste(str(cdg_barra.data.decode('utf-8')))
                                exit()
                for cdg_barra in decode(cap):
                        if(cdg_barra.type.lower() == 'code128'):
                                pyperclip.paste(str(cdg_barra.data.decode('utf-8')))
                                exit()
