from tkinter import *
from threading import Thread
import os
# import time

bg_color = "white"
fg_color = "gray"
pointer = 0.3

unit = 3.779528

root = Tk()
root.title("Plotter")
# root.geometry("600x600")

C = Canvas(root, bg=bg_color, height=960, width=960)
File_loc = f"{os.getcwd()}/Temp/combined_data.txt"
# (x1, y1, x2, y2)
coordinates = []


# Multi Threading
def threading():
    thread_1 = Thread(target=draw)
    thread_1.start()


# =============================================================
def draw():
    ptr = 0
    for x in coordinates:
        coord = x
        print(coord)
        C.create_line(coord, width=pointer, fill=fg_color)
        C.pack()
        root.update()
        # time.sleep(0.01)
        if ptr == len(coordinates) - 1:
            print("Done!!")
        else:
            ptr += 1


with open(File_loc, 'r') as axis:
    for line in axis.readlines():
        line = line.strip()
        line = line.split(",")
        line = [float(line[0]) * unit, float(line[1]) * unit, float(line[2]) * unit,
                float(line[3]) * unit]

        coordinates.append(line)

    axis.close()


threading()

root.mainloop()
