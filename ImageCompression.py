from multiprocessing.dummy import Process
import imutils
from importlib.resources import path
import PIL
from PIL import Image, ImageOps
import os
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
import multiprocessing
from multiprocessing import Pool
import glob
import time
from itertools import repeat
import shutil

root = tk.Tk()
root.withdraw()

inputfilepath = filedialog.askdirectory()

inputfolder = inputfilepath + '/'

outputfolder = Path(inputfolder).parent / 'Output/'
print(outputfolder)
outputfolder.mkdir(exist_ok = True)

print(inputfolder)

quality = 70

def compress_images(inputfile):
    # Open every image:
    img = Image.open(inputfile)
    img = ImageOps.exif_transpose(img)

    filename = inputfile.split('/')[-1]

    # Compress every image and save it with a new name:
    img.save(outputfolder / filename, optimize=True, quality=quality)

if __name__ == '__main__':
    filelst = []

    for filename in glob.iglob(inputfolder + '/**', recursive=True):
        if os.path.isfile(filename) and filename.endswith('jpg'):
            filelst.append(filename)

        print(filelst)
    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
        st = time.time()

        pool.map(compress_images, filelst)

        et = time.time()

        print('Time Taken Map:', et - st) 


