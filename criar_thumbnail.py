import cv2
import os
import numpy as np
from scipy import ndimage
import scipy

def mdc(a,b):
    while b !=0:
        resto = a % b
        a = b
        b = resto
    return a

base_dir = f'{os.getcwd()}\\streaming_service\\videos\\'

b = [x for x in os.listdir(base_dir) if  '.mp4' in x]

for i in b:
    cap = cv2.VideoCapture(base_dir+'\\'+i)
    ret, frame1 = cap.read()
    image2 = np.array(frame1)
    print(f'imagem: {i}')
    shape = frame1.shape
    mdc_f = None
    a = shape[0]
    b = shape[1]
    mdc_f = mdc(a=a,b=b)
    
    print(f'dimensoes sugerida = a: {a}, b: {16*mdc_f} ')
    a2 = int(b/(16/9))
    a3 = int(a2/2)

    cropped_frame = frame1[1:a2, 1:b]

    # frame1 = cv2.resize(src=frame1,dsize=(b*mdc_f,a ))

    # cv2.imwrite(
    #     f'{base_dir}\\thumbnail\\' +
    #     i.replace('.mp4', '.jpg')
    #     ,frame1)

    cv2.imwrite(
        f'{base_dir}\\thumbnail\\' +
        i.replace('.mp4', '.jpg')
        ,cropped_frame)

