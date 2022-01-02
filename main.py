import tkinter as tk
from PIL import ImageTk, Image
import threading
import time


class Slideshow:

    def __init__(self, root, image_files, delay):
        self.root = root
        self.image_files = image_files
        self.delay = delay
        self.label = tk.Label(root)
        self.label.pack()
        self.tracker = 0
        thread = threading.Thread(target=self.start_slideshow)
        thread.start()

    def start_slideshow(self):
        while True:
            for file in image_files:
                img = Image.open(file)
                img = ImageTk.PhotoImage(img)
                self.label.config(image=img)
                self.label.photo = img
                time.sleep(self.delay)


if __name__ == "__main__":
    root = tk.Tk()
    image_files = ["test.png", "test1.png"]
    delay = 3
    slideshow = Slideshow(root, image_files, delay)
    root.mainloop()




