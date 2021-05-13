try:
    import tkinter
except ImportError:
    import Tkiner as tkinter


def parabola(x):
    y = x * x / 100
    return y


def draw_axes(canvas):
    canvas.update()
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2
    canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvas.create_line(-x_origin, 0, x_origin, 0, fill="black")
    canvas.create_line(0, y_origin, 0, -y_origin, fill="black")
    # prints out all of the variables defined in a function. will look at all of the variables in the function
    print(locals())


def plot(canvas, x, y):
    canvas.create_line(x, y, x + 1, y + 1, fill="red")


mainWindow = tkinter.Tk()

mainWindow.title("parabola")
mainWindow.geometry("640x480")

canvas = tkinter.Canvas(mainWindow, width=320, height=480)
canvas.grid(row=0, column=0)

canvas2 = tkinter.Canvas(mainWindow, width=320, height=480, background="blue")
canvas2.grid(row=0, column=1)

# repr prints out a representation of an object in memory
print(repr(canvas), repr(canvas2))
draw_axes(canvas)
draw_axes(canvas2)

for x in range(-100, 100):
    y = parabola(x)
    plot(canvas, x, -y)

mainWindow.mainloop()
