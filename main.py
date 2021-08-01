from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import os
import Script_Badge

# Constants
DIRNAME = os.path.dirname(__file__)
WIDTH= 680
HEIGH= 330
BACKGROUND_COLOR= '#96DED1'


def gui():
    main_window = Tk()

    # Main Window geometry
    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()

    # Calculate position (OX, OY)
    x = (screen_width/2) - (WIDTH/2)
    y = (screen_height/2) - (HEIGH/2)
    main_window.geometry('%dx%d+%d+%d' % (WIDTH, HEIGH, x, y))

    # Main window design
    main_window.title("Badge Creator")
    main_window.configure(background= BACKGROUND_COLOR)
    main_window.iconbitmap(os.path.join(DIRNAME, 'img/icon.ico'))

    # Main window structure
    Label (main_window, text ="", background=BACKGROUND_COLOR).grid(row = 0, column = 0)
    Label (main_window, text ="", background=BACKGROUND_COLOR).grid(row = 0, column = 1)
    Label (main_window, text ="", background=BACKGROUND_COLOR).grid(row = 0, column = 2)

    Label (main_window, text ="", width= 20, background=BACKGROUND_COLOR).grid(row = 1, column = 0)
    Label (main_window, text ="Badge Creator", width= 12, font=("Times New Roman", 20, "bold")).grid(row = 1, column = 1)
    Label (main_window, text ="", width= 20, background=BACKGROUND_COLOR).grid(row = 1, column = 2)

    Label (main_window, text ="", width= 20, background=BACKGROUND_COLOR).grid(row = 2, column = 0)


    logo = Image.open(os.path.join(DIRNAME, 'img/logo.png'))
    logo = logo.resize((90, 42), Image. ANTIALIAS) # (width, height)
    logo = ImageTk. PhotoImage(logo)
    Label (main_window, text ="", width= 90, height= 42, image= logo, background= BACKGROUND_COLOR).grid(row = 2, column = 1)

    Label (main_window, text ="", width= 20, background= BACKGROUND_COLOR).grid(row = 2, column = 2)

    # ------------------------------
    folderPath1 = StringVar()

    label1 = Label(main_window, text="Badges directory", background=BACKGROUND_COLOR)
    label1.grid(row = 3, column = 0)

    entry1 = Entry(main_window, textvariable = folderPath1, width= 60)
    entry1.grid(row = 3, column = 1)

    def getFolderPath():
        folder_selected = filedialog.askdirectory()
        folderPath1.set(folder_selected)

    btnFind1 = Button(main_window, text="Browse Folder", command = getFolderPath)
    btnFind1.grid(row = 3 ,column = 2)

    # ------------------------------
    folderPath2 = StringVar()

    label2 = Label(main_window, text="The excel file", background=BACKGROUND_COLOR)
    label2.grid(row = 4, column = 0)

    entry2 = Entry(main_window, textvariable = folderPath2, width= 60)
    entry2.grid(row = 4, column = 1)

    def browsefunc1():
        filename = filedialog.askopenfilename() 
        entry2.insert(END, filename) 

    btnFind2 = Button(main_window, text="Browse file", command= browsefunc1)
    btnFind2.grid(row = 4, column = 2)

    # ----------------------------------------
    folderPath3 = StringVar()

    label3 = Label(main_window, text="The font you use (.ttf file)", background=BACKGROUND_COLOR)
    label3.grid(row = 5, column = 0)

    entry3 = Entry(main_window, textvariable = folderPath3, width= 60)
    entry3.grid(row = 5, column = 1)

    def browsefunc2():
        filename = filedialog.askopenfilename(filetypes=(("ttf files","*.ttf"), ("All files","*.*"))) 
        entry3.insert(END, filename) 

    btnFind3 = Button(main_window, text="Browse file", command= browsefunc2)
    btnFind3.grid(row = 5, column = 2)

    # --------------------
    label4 = Label(main_window, text="The color of the text (RGB values)", background=BACKGROUND_COLOR)
    label4.grid(row = 6, column = 1)

    color1 = Label(main_window, text="R:", background=BACKGROUND_COLOR)
    color1.grid(row = 7, column = 0)

    color2 = Label(main_window, text="G:", background=BACKGROUND_COLOR)
    color2.grid(row = 8, column = 0)

    color3 = Label(main_window, text="B:", background=BACKGROUND_COLOR)
    color3.grid(row = 9, column = 0)

    r = Entry(main_window, width= 10)
    r.grid(row = 7, column = 1)

    g = Entry(main_window, width= 10)
    g.grid(row = 8, column = 1)

    b = Entry(main_window, width= 10)
    b.grid(row = 9, column = 1)

    # --------------------------------------
    label5 = Label(main_window, text="The font size of the text", background=BACKGROUND_COLOR)
    label5.grid(row = 10, column = 0)

    font_size = Entry(main_window, width= 10)
    font_size.grid(row = 10, column = 1)

    label6 = Label(main_window, text="units (PS measurement unit)", background=BACKGROUND_COLOR)
    label6.grid(row = 10, column = 2)

    # -------------------------
    def start_button():
        Script_Badge.start( r.get(),
                            g.get(),
                            b.get(),
                            font_size.get(),
                            entry1.get(),
                            entry2.get(),
                            entry3.get()
                            )

    Button(main_window, text = "START", command= start_button, width= 20, background= '#6495ED').grid(row = 11, column = 1)

    main_window.mainloop()

if __name__ == "__main__":
    gui()