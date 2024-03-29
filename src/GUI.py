from tkinter import Tk, Canvas, Label, Button, PhotoImage, Frame, Text, Toplevel
from tkinter.filedialog import askopenfile, asksaveasfile
import data, os, sys
from pathlib import Path

allRoots = []
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(fr"{os.getcwd()}\Component\assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class ImageLoader:
    def __init__(self, wd) -> None:
        self.window = wd
        # Load Image
        self.input_image_1 = PhotoImage(
                file=relative_to_assets("image_1.png"))
        self.input_image_2 = PhotoImage(
                file=relative_to_assets("image_3.png"))
        self.input_image_3 = PhotoImage(
                file=relative_to_assets("image_4.png"))
        self.image_image_3 = PhotoImage(
                file=relative_to_assets("image_3.png"))
        self.image_image_4 = PhotoImage(
                file=relative_to_assets("image_4.png"))
        self.button_image_1 = PhotoImage(
                file=relative_to_assets("button_1.png"))
        self.button_image_2 = PhotoImage(
                file=relative_to_assets("button_2.png"))
        self.entry_image_1 = PhotoImage(
                file=relative_to_assets("entry_1.png"))
        self.entry_image_2 = PhotoImage(
                file=relative_to_assets("entry_1.png"))
        self.entry_image_3 = PhotoImage(
                file=relative_to_assets("entry_1.png"))
        self.entry_image_4 = PhotoImage(
                file=relative_to_assets("entry_4.png"))
        self.button_image_solve = PhotoImage(
                file=relative_to_assets("button_solve.png"))
        self.entry_image_5 = PhotoImage(
                file=relative_to_assets("entry_4.png"))
        self.entry_image_6 = PhotoImage(
                file=relative_to_assets("entry_1.png"))
        self.entry_image_7 = PhotoImage(
                file=relative_to_assets("entry_1.png"))

def closeAllRoots():
    global allRoots
    print(allRoots)
    for i in allRoots:
        i.destroy()

def resetMain(window, img_loader, obj):
    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 600,
        width = 1000,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    
    image_1 = canvas.create_image(
        500.0,
        300.0,
        image=img_loader.input_image_1
    )

    
    image_2 = canvas.create_image(
        500.0,
        300.0,
        image=img_loader.input_image_2
    )

    
    image_3 = canvas.create_image(
        523.0,
        325.0,
        image=img_loader.image_image_3
    )

    
    image_4 = canvas.create_image(
        500.0,
        82.0,
        image=img_loader.image_image_4
    )

    
    button_1 = Button(
        image=img_loader.button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: show(obj),
        relief="flat"
    )
    button_1.place(
        x=249.0,
        y=439.0,
        width=206.0,
        height=48.0
    )

    
    button_2 = Button(
        image=img_loader.button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: inputFromKeyboard(img_loader, window, obj),
        relief="flat"
    )
    button_2.place(
        x=545.0,
        y=439.0,
        width=206.0,
        height=48.0
    )

    canvas.create_text(
        260.0,
        194.0,
        anchor="nw",
        text="Tugas Kecil 1 IF2211 Strategi Algoritma",
        fill="#FFFFFF",
        font=("Poppins Bold", 25 * -1)
    )

    canvas.create_text(
        364.0,
        233.0,
        anchor="nw",
        text="Bruteforce Algorithm",
        fill="#FFFFFF",
        font=("Poppins Bold", 25 * -1)
    )

    canvas.create_text(
        370.0,
        357.0,
        anchor="nw",
        text="Valentino Chryslie Triadi / 13522164",
        fill="#FFFFFF",
        font=("Poppins Regular", 15 * -1)
    )

    canvas.create_text(
        483.0,
        334.0,
        anchor="nw",
        text="Oleh",
        fill="#FFFFFF",
        font=("Poppins Regular", 15 * -1)
    )

def main():
    global allRoots

    obj = data.INFO()

    window = Tk()
    allRoots.append(window)

    window.title("Cyberpunk 2077 Breach Protocol")

    window.geometry("1000x600")
    window.configure(bg = "#FFFFFF")

    img_loader = ImageLoader(window)

    resetMain(window, img_loader, obj)
    
    window.bind("<Escape>", lambda e: closeAllRoots())
    window.bind("<F11>", lambda e: window.attributes("-fullscreen",
                                                     not window.attributes("-fullscreen")))
    window.protocol('WM_DELETE_WINDOW', closeAllRoots)  # window is your window window

    window.resizable(False, False)
    window.mainloop()



# TODO: SHOW RESULT

def getLength(l):
    for i in range(len(l)):
        if l[i]  == ():
            return i
    return len(l)

def getParsedResult(arr, matrix, conn):
    max = arr[0][1]
    temp = []
    for i in arr:
        if (i[1] == max):
            temp.append(i)
    arr = sorted(temp, key=lambda x: getLength(x[0]), reverse=False)
    res = ""
    for i in range(getLength(arr[0][0])):
        if (i != 0):
            res += (conn)
        res += (matrix[arr[0][0][i][0]][arr[0][0][i][1]])
    return res

def displayCoordinat(arr, ws):
    max = arr[0][1]
    temp = []
    for i in arr:
        if (i[1] == max):
            temp.append(i)
    arr = sorted(temp, key=lambda x: getLength(x[0]), reverse=False)
    for i in range(getLength(arr[0][0])):
        Label(ws, text=str(arr[0][0][i][1] + 1) + ',' + str(arr[0][0][i][0] + 1)).grid(row=i, column=1, padx=5, pady=5)
    return True

def resetAll(obj, ws, info_window):
    obj.reset()
    info_window.destroy()
    ws.destroy()
    return True

def saveResult(res, matrix, time_executed):
    f = asksaveasfile(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    f.write(str(res[0][1])+"\n")
    f.write(getParsedResult(res, matrix, " ") + "\n")
    max = res[0][1]
    temp = []
    for i in res:
        if (i[1] == max):
            temp.append(i)
    arr = sorted(temp, key=lambda x: getLength(x[0]), reverse=False)
    for i in range(getLength(arr[0][0])):
        f.write(str(arr[0][0][i][1] + 1) + ',' + str(arr[0][0][i][0] + 1) + "\n")
    f.write("\n" + str(round(time_executed*1000)) + " ms")
    f.close()
    return True

def solve(obj, info_window):
    global allRoots
    res = obj.solve()
    # print(res)
    ws = Tk()
    allRoots.append(ws)
    ws.title('Solution Window')
    ws.geometry('1000x600') 
    
    main_frame  =  Frame(ws,  width=1000,  height=600,  bg='grey')
    main_frame.grid(row=0,  column=0,  padx=25,  pady=5, sticky="N"+"E"+"W"+"S")
    
    first_frame  =  Frame(main_frame,  width=400,  height=500,  bg='grey')
    first_frame.grid(row=0,  column=0,  padx=25,  pady=5, sticky="N"+"E"+"W"+"S")
    
    second_frame  =  Frame(main_frame,  width=400,  height=500,  bg='grey')
    second_frame.grid(row=0,  column=1,  padx=25,  pady=5, sticky="N"+"E"+"W"+"S")

    third_frame  =  Frame(main_frame,  width=400,  height=500,  bg='grey')
    third_frame.grid(row=0,  column=2,  padx=25,  pady=5, sticky="N"+"E"+"W"+"S")


    Label(first_frame, text=f"Execution Time: {round(obj.time_executed*1000)} ms").grid(row=0, column=0, padx=10, pady=10, sticky="NW")
    if (res != []):

        Label(first_frame, text=f"Maximum Score: {res[0][1]}").grid(row=1, column=0, padx=10, pady=10, sticky="NW")

        Label(first_frame, text="Buffer: " + getParsedResult(res, obj.matrix, " → ")).grid(row=2, column=0, padx=10, pady=10, sticky="NW")

        Label(second_frame, text="Coordinate:").grid(row=0, column=0, padx=10, pady=10, sticky="NW")

        displayCoordinat(res, second_frame)

        Button(
            third_frame,
            borderwidth=0,
            highlightthickness=0,
            text= "Save Result",
            command=lambda: saveResult(res, obj.matrix, obj.time_executed),
            width=30,
        ).grid(row=0, column=0, padx=10, pady=10, sticky="N" + "E" + "W" + "S")
    else:
        Label(first_frame, text="No solutions found!").grid(row=1, column=0, padx=10, pady=10, sticky="NW")

    Button(
        third_frame,
        borderwidth=0,
        highlightthickness=0,
        text= "Back to Main Menu",
        command=lambda: resetAll(obj,ws,info_window),
        width=30,
    ).grid(row=1, column=0, padx=10, pady=10, sticky="N" + "E" + "W" + "S")

    ws.mainloop()



# TODO: SHOW MATRIX AND SEQUENCE

def displayMatrix(matrix, ws):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            Label(ws, text=matrix[i][j]).grid(row=i, column=j+1, padx=5, pady=5)
    return True

def displaySequence(sequence, ws):
    print(sequence)
    for i in range(len(sequence)):
        Label(ws, text=sequence[i][0]).grid(row=i, column=1, padx=5, pady=5, sticky="W")
        Label(ws, text=sequence[i][1]).grid(row=i, column=2, padx=5, pady=5)
    return True

def show(obj):
    global allRoots
    file_path = askopenfile(mode='r', filetypes=[("Text Files", "*.txt")])
    text = file_path.read()
    f = open("input/input.txt", "w")
    f.write(text)
    f.close()
    obj.parse("input/input.txt")
    obj.print()

    ws = Tk()
    allRoots.append(ws)
    ws.title('Information Window')
    ws.geometry('1000x600') 
    
    main_frame  =  Frame(ws,  width=1000,  height=600,  bg='grey')
    main_frame.grid(row=0,  column=0,  padx=25,  pady=5, sticky="N"+"E"+"W"+"S")

    first_frame  =  Frame(main_frame,  width=300,  height=500,  bg='grey')
    first_frame.grid(row=0,  column=0,  padx=25,  pady=5, sticky="N"+"E"+"W"+"S")

    second_frame  =  Frame(main_frame,  width=250,  height=500,  bg='grey')
    second_frame.grid(row=0,  column=1,  padx=25,  pady=5, sticky="N"+"E"+"W"+"S")

    third_frame  =  Frame(main_frame,  width=50,  height=500,  bg='grey')
    third_frame.grid(row=0,  column=2,  padx=25,  pady=5, sticky="N"+"E"+"W"+"S")

    Label(first_frame, text="Matrix:").grid(row=0, column=0, padx=10, pady=10, sticky="NW")
    displayMatrix(obj.matrix, first_frame)

    Label(second_frame, text="Sequence:").grid(row=0, column=0, padx=10, pady=10, sticky="NW")
    displaySequence(obj.sequences, second_frame)

    Button(third_frame, 
           borderwidth=0,
           highlightthickness=0,
           text="START",
           command=lambda: solve(obj, ws),
           ).grid(row=0, column=0, padx=10, pady=10, sticky="N" + "E" + "W" + "S")

    ws.mainloop()

def showInput(obj):
    global allRoots
    ws = Tk()
    allRoots.append(ws)
    ws.title('Information Window')
    ws.geometry('1000x600') 
    
    main_frame  =  Frame(ws,  width=1000,  height=600,  bg='grey')
    main_frame.grid(row=0,  column=0,  padx=25,  pady=5, sticky="N"+"E"+"W"+"S")

    first_frame  =  Frame(main_frame,  width=300,  height=500,  bg='grey')
    first_frame.grid(row=0,  column=0,  padx=25,  pady=5, sticky="N"+"E"+"W"+"S")

    second_frame  =  Frame(main_frame,  width=250,  height=500,  bg='grey')
    second_frame.grid(row=0,  column=1,  padx=25,  pady=5, sticky="N"+"E"+"W"+"S")

    third_frame  =  Frame(main_frame,  width=50,  height=500,  bg='grey')
    third_frame.grid(row=0,  column=2,  padx=25,  pady=5, sticky="N"+"E"+"W"+"S")

    Label(first_frame, text="Matrix:").grid(row=0, column=0, padx=10, pady=10, sticky="NW")
    displayMatrix(obj.matrix, first_frame)

    Label(second_frame, text="Sequence:").grid(row=0, column=0, padx=10, pady=10, sticky="NW")
    displaySequence(obj.sequences, second_frame)

    Button(third_frame, 
           borderwidth=0,
           highlightthickness=0,
           text="START",
           command=lambda: solve(obj, ws),
           ).grid(row=0, column=0, padx=10, pady=10, sticky="N" + "E" + "W" + "S")

    ws.mainloop()



# TODO: INPUT USER WINDOW

def solveInput(buffer_size, sequence_count, max_sequence_length, matrix_width, matrix_height, token_count, token):
    obj = data.INFO()
    obj.randomGUI(int(buffer_size.get("1.0", "end-1c")), int(sequence_count.get("1.0", "end-1c")), int(max_sequence_length.get("1.0", "end-1c")), int(matrix_width.get("1.0", "end-1c")), int(matrix_height.get("1.0", "end-1c")), int(token_count.get("1.0", "end-1c")), token.get("1.0", "end-1c"))    
    showInput(obj)
    return True

def inputFromKeyboard(img_loader, wd, obj):
    window = wd

    window.geometry("1000x600")
    window.configure(bg = "#FFFFFF")

    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 600,
        width = 1000,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    
    image_1 = canvas.create_image(
        500.0,
        300.0,
        image=img_loader.input_image_1
    )

    
    image_2 = canvas.create_image(
        523.0,
        325.0,
        image=img_loader.input_image_2
    )

    
    
    image_3 = canvas.create_image(
        500.0,
        82.0,
        image=img_loader.input_image_3
    )

    canvas.create_text(
        364.0,
        150.0,
        anchor="nw",
        text="Input From Keyboard",
        fill="#FFFFFF",
        font=("Poppins Bold", 25 * -1)
    )

    
    entry_bg_1 = canvas.create_image(
        312.5,
        262.0,
        image=img_loader.entry_image_1
    )
    buffer_size = Text(
        bd=0,
        bg="#F4F4F4",
        fg="#000716",
        highlightthickness=0
    )
    buffer_size.place(
        x=185.0,
        y=242.0 + 6,
        width=255.0,
        height=25.0
    )

    
    entry_bg_2 = canvas.create_image(
        687.5,
        262.0,
        image=img_loader.entry_image_2
    )
    sequence_count = Text(
        bd=0,
        bg="#F4F4F4",
        fg="#000716",
        highlightthickness=0
    )
    sequence_count.place(
        x=560.0,
        y=242.0 + 6,
        width=255.0,
        height=25.0
    )

    
    entry_bg_3 = canvas.create_image(
        687.5,
        350.0,
        image=img_loader.entry_image_3
    )
    max_sequence_length = Text(
        bd=0,
        bg="#F4F4F4",
        fg="#000716",
        highlightthickness=0
    )
    max_sequence_length.place(
        x=560.0,
        y=330.0 + 6,
        width=255.0,
        height=25.0
    )

    
    entry_bg_4 = canvas.create_image(
        615.0,
        439.0,
        image=img_loader.entry_image_4
    )
    matrix_width = Text(
        bd=0,
        bg="#F4F4F4",
        fg="#000716",
        highlightthickness=0
    )
    matrix_width.place(
        x=560.0,
        y=419.0 + 6,
        width=110.0,
        height=25.0
    )

    
    solve = Button(
        image=img_loader.button_image_solve,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: solveInput(buffer_size, sequence_count, max_sequence_length, matrix_width, matrix_height, token_count, token),
        relief="flat"
    )
    solve.place(
        x=450.0,
        y=496.0,
        width=100.0,
        height=40.0
    )

    back = Button(
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        text="Back",
        command=lambda: resetMain(wd, img_loader, obj),
    )
    back.place(
        x=50.0,
        y=496.0,
        width=100.0,
        height=40.0
    )

    
    entry_bg_5 = canvas.create_image(
        760.0,
        439.0,
        image=img_loader.entry_image_5
    )
    matrix_height = Text(
        bd=0,
        bg="#F4F4F4",
        fg="#000716",
        highlightthickness=0
    )
    matrix_height.place(
        x=705.0,
        y=419.0 + 6,
        width=110.0,
        height=25.0
    )

    
    entry_bg_6 = canvas.create_image(
        312.5,
        350.0,
        image=img_loader.entry_image_6
    )
    token_count = Text(
        bd=0,
        bg="#F4F4F4",
        fg="#000716",
        highlightthickness=0
    )
    token_count.place(
        x=185.0,
        y=330.0 + 6,
        width=255.0,
        height=25.0
    )

    
    entry_bg_7 = canvas.create_image(
        312.5,
        439.0,
        image=img_loader.entry_image_7
    )
    token = Text(
        bd=0,
        bg="#F4F4F4",
        fg="#000716",
        highlightthickness=0
    )
    token.place(
        x=185.0,
        y=419.0 + 6,
        width=255.0,
        height=25.0
    )

    canvas.create_text(
        175.0,
        219.0,
        anchor="nw",
        text="Buffer Size",
        fill="#FFFFFF",
        font=("Poppins Bold", 15 * -1)
    )

    canvas.create_text(
        550.0,
        219.0,
        anchor="nw",
        text="Sequence Count",
        fill="#FFFFFF",
        font=("Poppins Bold", 15 * -1)
    )

    canvas.create_text(
        550.0,
        307.0,
        anchor="nw",
        text="Maximum Sequence Length",
        fill="#FFFFFF",
        font=("Poppins Bold", 15 * -1)
    )

    canvas.create_text(
        550.0,
        396.0,
        anchor="nw",
        text="Matrix Width",
        fill="#FFFFFF",
        font=("Poppins Bold", 15 * -1)
    )

    canvas.create_text(
        695.0,
        396.0,
        anchor="nw",
        text="Matrix Height",
        fill="#FFFFFF",
        font=("Poppins Bold", 15 * -1)
    )

    canvas.create_text(
        175.0,
        307.0,
        anchor="nw",
        text="Unique Token Count ",
        fill="#FFFFFF",
        font=("Poppins Bold", 15 * -1)
    )

    canvas.create_text(
        175.0,
        396.0,
        anchor="nw",
        text="Token",
        fill="#FFFFFF",
        font=("Poppins Bold", 15 * -1)
    )

    canvas.create_text(
        175.0,
        459.0,
        anchor="nw",
        text="Note: Separate each token with space (E5 1C 77 ...)",
        fill="#FFFFFF",
        font=("Poppins Regular", 10 * -1)
    )

    window.resizable(False, False)
    window.mainloop()
