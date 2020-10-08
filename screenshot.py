import time
import pyautogui
import tkinter as tk

# screenshot function 
def screenshot():
    name = int(round(time.time() * 1000))
    name = 'C:/Users/ashish/Projects/PythonProjects/screenshotdata/{}.png'.format(name)
    img = pyautogui.screenshot(name)
    img.show()

# creating Buttons 
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text="Take Screenshot",
    command=screenshot
)
button.pack(side=tk.LEFT)

close = tk.Button(
    frame,
    text="QUIT",
    command=quit
)
close.pack(side=tk.LEFT)

root.mainloop()