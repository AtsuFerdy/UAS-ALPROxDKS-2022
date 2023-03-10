from pathlib import Path
import string
import subprocess as sp
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# WINDOW GUI
window = Tk()
window.geometry("800x500+300+90")
window.configure(bg="#FFFFFF")
window.iconbitmap('./assets/rks.ico')
window.title('One Time Pad Program')
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=500,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

# BG CYBER
canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    400.0,
    250.0,
    image=image_image_1
)

# BG PUTIH
canvas.create_rectangle(
    135.0,
    57.0,
    666.0,
    442.0,
    fill="#FFFFFF",
    outline="")

# GAMBAR RKS
image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    754.0,
    50.0,
    image=image_image_2
)

# JUDUL
canvas.create_text(
    261.0,
    89.0,
    anchor="nw",
    text="One Time Pad",
    fill="#011B28",
    font=("Play Regular", 40 * -1)
)

# INPUT FILE
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    450.5,
    196.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=338.0,
    y=180.0,
    width=225.0,
    height=31.0
)

# INPUT KEY
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    450.5,
    240.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=338.0,
    y=224.0,
    width=225.0,
    height=31.0
)

# GAMBAR KUNCI
image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    537.0,
    106.0,
    image=image_image_3
)

# GAMBAR POLTEK
image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    51.0,
    48.0,
    image=image_image_4
)
canvas.create_text(
    301.0,
    410.0,
    anchor="nw",
    text="Made by RKS-B 2022 Group 4",
    fill="#011B28",
    font=("Play Regular", 15 * -1)
)

# FILE NAME TEXT
canvas.create_rectangle(
    246.0,
    136.0,
    563.0,
    138.0,
    fill="#011B28",
    outline="")

canvas.create_text(
    248.0,
    192.0,
    anchor="nw",
    text="File Name ",
    fill="#011B28",
    font=("Play Regular", 15 * -1)
)

# SECRET KEY TEXT
canvas.create_text(
    248.0,
    237.0,
    anchor="nw",
    text="Secret Key",
    fill="#011B28",
    font=("Play Regular", 15 * -1)
)


def enkripsi():
    nama_file = entry_1.get()
    kunci = entry_2.get()
    if nama_file == '':
        messagebox.showerror(title='Pemberitahuan!', message='Harap Lengkapi!')
    elif kunci == '':
        messagebox.showerror(title='Pemberitahuan!', message='Harap Lengkapi!')
    else:
        file = open(f"{nama_file}.txt").read().lower()
        teks = ""
        for i in range(len(file)):
            if file[i].islower():
                if len(kunci) < len(file):
                    kunci += kunci[i % len(kunci)]
                elif len(kunci) > len(file):
                    kunci = kunci[i:len(file)]
                letter_index = (string.ascii_lowercase.index(
                    file[i]) + string.ascii_lowercase.index(kunci[i])) % 26
                teks += string.ascii_lowercase[letter_index]
            else:
                teks += file[i]

        tulis_ulang = open(f'enkrip.txt', 'w+')
        tulis_ulang.write(teks)
        messagebox.showinfo(title='Pemberitahuan!', message='Enkripsi Selesai')
        sp.Popen(['Notepad.exe', 'enkrip.txt'])
        window.quit()


def dekripsi():
    nama_file = entry_1.get()
    kunci = entry_2.get()
    if nama_file == '':
        messagebox.showerror(title='Pemberitahuan!', message='Harap Lengkapi!')
    elif kunci == '':
        messagebox.showerror(title='Pemberitahuan!', message='Harap Lengkapi!')
    else:
        file = open(f"{nama_file}.txt").read().lower()
        teks = ""
        for i in range(len(file)):
            if file[i].islower():
                if len(kunci) < len(file):
                    kunci += kunci[i % len(kunci)]
                elif len(kunci) > len(file):
                    kunci = kunci[i:len(file)]
                letter_index = (string.ascii_lowercase.index(
                    file[i]) - string.ascii_lowercase.index(kunci[i])) % 26
                teks += string.ascii_lowercase[letter_index]
            else:
                teks += file[i]
        tulis_ulang = open(f'dekrip.txt', 'w+')
        tulis_ulang.write(teks)
        messagebox.showinfo(title='Pemberitahuan!', message='Dekripsi Selesai')
        sp.Popen(['Notepad.exe', 'dekrip.txt'])
        window.quit()


def ucapan():
    messagebox.showinfo(
        title='Thank you!', message='Created by Group 4:\n1. M. Raihan Ferdyansyah\n2. Yufi Rahmadhani\n3. Naya Amanda Pradisia'
    )
    window.quit()


# ENKRIPSI
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: enkripsi(),
    relief="flat"
)
button_1.place(
    x=284.0,
    y=292.0,
    width=109.0,
    height=48.0
)
canvas.create_text(
    278.0,
    300.0,
    anchor="nw",
    text="Encrypt",
    fill="#FFFFFF",
    font=("Play Regular", 20 * -1)
)

# QUIT
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ucapan(),
    relief="flat"
)
button_2.place(
    x=344.0,
    y=348.0,
    width=109.0,
    height=48.0
)
canvas.create_text(
    338.0,
    356.0,
    anchor="nw",
    text="Quit",
    fill="#FFFFFF",
    font=("Play Regular", 20 * -1)
)

# DEKRIPSI
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: dekripsi(),
    relief="flat"
)
button_3.place(
    x=408.0,
    y=292.0,
    width=109.0,
    height=48.0
)
canvas.create_text(
    402.0,
    300.0,
    anchor="nw",
    text="Decrypt",
    fill="#FFFFFF",
    font=("Play Regular", 20 * -1)
)

window.resizable(False, False)
window.mainloop()
