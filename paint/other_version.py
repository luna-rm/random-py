from tkinter import *
import cv2 as cv
import numpy as np
import os
import PIL
from keras.models import load_model


WIDTH = 500
HEIGHT = 500
SIZE = 10
MODEL = load_model('./saved_model.h5')

def stop():
    global aux_close 
    aux_close = False
    
def save_as_png():
    canv.postscript(file = 'img.eps') 

    img = PIL.Image.open('img.eps') 
    img.save('img.png', 'png') 

def predict():
    try:
        save_as_png()
        img = cv.imread('img.png', 0)
        
        final_img = cv.resize(img, (48, 48))
        final_img = np.expand_dims(final_img, axis=0)      
            
        final_img = final_img/255.0
        aux = np.argmax(MODEL.predict(final_img))
        base.title(str(aux))
            
        os.remove('img.png')
        os.remove('img.eps')
    except Exception as e:
        print(e)

def paint(event):
    x1, y1 = (event.x - SIZE//2), (event.y - SIZE//2)
    x2, y2 = (event.x + SIZE//2), (event.y + SIZE//2)

    canv.create_rectangle(x1, y1, x2, y2, outline='black', fill='black')
    #draw.rectangle([x1, y1, x2+SIZE, y2+SIZE], outline='black', fill='black', witdh=SIZE)
    
base = Tk()

canv = Canvas(base, width=WIDTH-10, height=HEIGHT-10, bg='white')
canv.pack()

#img = PIL.Image.new("RGB", (WIDTH, HEIGHT), (255, 255, 255))

canv.bind('<B1-Motion>', paint)

aux_close = True


while aux_close:
    predict()
    base.update()
    base.protocol('WM_DELETE_WINDOW', stop)
