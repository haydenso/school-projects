from djitellopy import Tello
import tkinter

tello = Tello()

def left(e):
    print("Left")
    tello.send_rc_control(-30, 0, 0, 0)

def right(e):
    print("Right")
    tello.send_rc_control(30, 0, 0, 0)

def forward(e):
    print("Forward")
    tello.send_rc_control(0, 30, 0, 0)

def anticlockwise(e):
    print("Anticlockwise")
    tello.send_rc_control(0, 0, 0, -30)

def clockwise(e):
    print("Clockwise")
    tello.send_rc_control(0, 0, 0, 30)

def back(e):
    print("Back")
    tello.send_rc_control(0, -30, 0, 0)

def up(e):
    print("Up")
    tello.send_rc_control(0, 0, 20, 0)

def down(e):
    print("Down")
    tello.send_rc_control(0, 0, -20, 0)

def allstop(e):
    print("All stop")
    tello.send_rc_control(0, 0, 0, 0)

def land(e):
    print("Land")
    tello.land()
    tello.end()

def takeoff(e):
    print("Take off")
    tello.takeoff()

# Start the program
app = tkinter.Tk()
app.title("My drone!")
print("Connecting")
tello.connect()
# Attach the keypresses to the functions above
app.bind("<Left>", left)
app.bind("<Right>", right)
app.bind("<Up>", forward)
app.bind("<Down>", back)
app.bind("<Escape>", land)
app.bind("<Return>", land)
app.bind("<space>", allstop)
app.bind("<t>", takeoff)
app.bind("<w>", up)
app.bind("<s>", down)
app.bind("<a>", clockwise)
app.bind("<d>", anticlockwise)
# Run the program
app.mainloop()