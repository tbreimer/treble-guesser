from tkinter import *
import random
import time

notes = ["g", "f", "e", "d", "c", "b", "a", "g", "f", "e", "d"]
y_coords = [113, 128, 143, 158, 174, 189, 205, 220, 235, 250, 266]

def set_global_vars():
    global trials
    global misses
    global stop

    global start_time

set_global_vars()

index = 0
trials = 0
misses = 0

stop = int(input("How many trials would you like? "))

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

clef_img = PhotoImage(file="/home/tbreimer/Python/Treble/treble.png")
note_img = PhotoImage(file="/home/tbreimer/Python/Treble/note.png")

print("Get ready to focus on the window!")
time.sleep(1)
print("Ready")
time.sleep(1)
print("Set")
time.sleep(1)
print("Go!")
time.sleep(1)

start_time = time.time()

def generate_note():
    canvas.delete("all")
    
    global index

    old_index = index

    while (old_index == index):
        index = random.randint(0, len(notes) - 1)
        
    coord = y_coords[index]
    
    canvas.create_image((150, 200), image=clef_img)
    canvas.create_image((200, coord), image=note_img)

def show_stats():
    canvas.destroy()
    print("-------------------------------------")
    print("Great Job!")
    print("You got", trials, "correct, with", misses, "misses,")
    print("in", round(time.time() - start_time, 2), "seconds, for an average of", round((time.time() - start_time)/trials, 3), "seconds per note")

generate_note()

def keyPressed(key):
    global trials
    global misses
    
    if (key.char == notes[index]):
        print("Correct!", notes[index])
        
        trials += 1

        if (trials >= stop):
            show_stats()
        else:
            generate_note()
    else:
        misses += 1
        print("Wrong! Try Again")

canvas.bind_all('<KeyPress>', keyPressed)





    
    
