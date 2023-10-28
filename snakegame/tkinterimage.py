#Import required libraries
import tkinter
from PIL import ImageTk, Image

#Create an instance of tkinter window
win =Tk()

#Define the geometry of the window
win.geometry("650x400")

#Initialize the file name in a variable
path = "file.jpg"

#Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open(path))

#Create a Label Widget to display the text or Image
label = tkinter.Label(win, image = img)
label.pack(fill = "both", expand = "yes")

win.mainloop()