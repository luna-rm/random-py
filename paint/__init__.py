import pygame as pg
import cv2 as cv
import os
import numpy as np
from keras.models import load_model

pg.init()

WIDTH = 480
HEIGHT = 480
PIXEL = WIDTH // 30

WIND = pg.display.set_mode((WIDTH, HEIGHT))
WIND.fill((255,255,255))

MODEL = load_model('./saved_model.h5')

def init_grid(rows, cols, color):
    grid = []
    for i in range(rows):
        grid.append([])
        for i2 in range(cols):
            grid[i].append(color)
            
    return grid

def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pg.draw.rect(win, pixel, (j*PIXEL, i*PIXEL, PIXEL, PIXEL))
    
    pg.display.update()
    
def get_pos_grid(pos):
    x, y = pos
    row = y // PIXEL
    col = x // PIXEL

    if row >= 30:
        raise IndexError

    return row, col
        
pg.display.update()

run = True
clock = pg.time.Clock()
grid = init_grid(30, 30, (255, 255, 255))

def predict():
    try:
        pg.image.save(WIND, 'image.png')
        img = cv.imread('image.png', 0)
    
        final_img = cv.resize(img, (48, 48))
        final_img = np.expand_dims(final_img, axis=0)      
        
        final_img = final_img/255.0
        aux = np.argmax(MODEL.predict(final_img))
        pg.display.set_caption(str(aux))
        
        os.remove('image.png')
    except Exception as e:
        pg.display.set_caption('ERROR')
    
    
        
while run:
    clock.tick(60)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        if pg.mouse.get_pressed()[0]:
            pos = pg.mouse.get_pos()
            
            try:
                row, col = get_pos_grid(pos)
                grid[row][col] = (0,0,0)
            except IndexError:
                print('ERROR')
    predict()
    draw_grid(WIND, grid)
    
pg.quit()