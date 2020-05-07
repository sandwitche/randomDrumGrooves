#exec(open("midi4.py").read())
import tkinter
import os
import sys

def exitn():
    sys.exit("Finished")

def rungenerator():
    os.system("python3 midi4.py -m "+measurese.get()+" -swing "+swing.get()+" -sk "+snki.get()+" -c "+cymbal.get()+" -kick "+kicke.get()+" -snare "+snaree.get())
    finisht=tkinter.Label(main, font=("mincho", 12), text="the midi file has been\ngenerated successfully")
    finisht.grid(column=4, row=6, columnspan=3)
    exitb=tkinter.Button(main, text="Exit", command=exitn)
    exitb.grid(column=4, row=7)


main=tkinter.Tk()
main.title("Random drum grooves generator")
main.geometry('800x350')


text=tkinter.Label(main, font=("mincho", 13), height=5, text="This program generates random midi files of\nrandom drum grooves defined by the settings you enter")
text.grid(column=1, row=0, columnspan=4)

measurest=tkinter.Label(main, font=("mincho", 12), text="measures:", width=15, height=2)
measurest.grid(column=0, row=2)
measurese=tkinter.Entry(main, width=5)
measurese.grid(column=1, row=2)

swing=tkinter.StringVar()
swing.set("1")
swingt=tkinter.Label(main, font=("mincho", 12), text="swing pattern:", width=15, height=2)
swingt.grid(column=0, row=3)
swinge=tkinter.Radiobutton(main, text="Yes", value="1", variable=swing)
swinge.grid(column=1, row=3)
swinge=tkinter.Radiobutton(main, text="No", value=0, variable=swing)
swinge.grid(column=2, row=3)

cymbal=tkinter.StringVar()
cymbal.set("R")
cymbalt=tkinter.Label(main, font=("mincho", 12), text="cymbal type:", width=15, height=2)
cymbalt.grid(column=0, row=4)
cymbale=tkinter.Radiobutton(main, text="Ride", value="R", variable=cymbal)
cymbale.grid(column=1, row=4)
cymbale=tkinter.Radiobutton(main, text="Hi-Hat", value="HH", variable=cymbal)
cymbale.grid(column=2, row=4)

kickt=tkinter.Label(main, font=("mincho", 12), text="kick:", width=20)
kickt.grid(column=3, row=2)
kicke=tkinter.Entry(main, width=5)
kicke.grid(column=4, row=2)

snaret=tkinter.Label(main, font=("mincho", 12), text="snare:", width=20)
snaret.grid(column=3, row=3)
snaree=tkinter.Entry(main, width=5)
snaree.grid(column=4, row=3)

snki=tkinter.StringVar()
snki.set("0")
snkit=tkinter.Label(main, font=("mincho", 12), text="snare and kick\ncollision:", width=15, height=2)
snkit.grid(column=3, row=4)
snkie=tkinter.Radiobutton(main, text="Yes", value="1", variable=snki)
snkie.grid(column=4, row=4)
snkie=tkinter.Radiobutton(main, text="No", value="0", variable=snki)
snkie.grid(column=5, row=4)



btg = tkinter.Button(main, text="Generate", command=rungenerator)
btg.grid(column=6, row=5)

main.mainloop()


