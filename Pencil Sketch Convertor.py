
import cv2
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

messageBox = messagebox.askokcancel("Image Convertor","This program converts images to pencil sketches \n \nPress 'Ok' to open File Explorer and select an image",)

if messageBox == False:
    quit()
else:
    Tk().withdraw()
    filename = askopenfilename()

    image = cv2.imread(filename)

    greyImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    invertedImage = 255-greyImage
    blur = cv2.GaussianBlur(invertedImage,(21,21),0)
    invertedBlur = 255-blur
    sketch = cv2.divide(greyImage,invertedBlur,scale=256.0)

    cv2.imshow("Original",image)
    cv2.imshow("sketch",sketch)
    cv2.waitKey(0)