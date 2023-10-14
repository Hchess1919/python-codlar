import tkinter
veri1=" "
veri2=" "

def yaz():
    dosya = open("asü.txt", "a")
    yazilacak = str(veri1.get())+"\n"
    dosya.write(yazilacak)
    dosya.close()
def oku():
    dosya = open("asü.txt","r")
    okunan=dosya.read()
    veri3.config(text=okunan)
    dosya.close()


pencere=tkinter.Tk()
pencere.title("rehber")
pencere.geometry("300x250")
button1=tkinter.Button(pencere,text="dosya yaz",command=yaz)
button1.grid(column=1,row=1)
veri1=tkinter.Entry()
veri1.grid(column=2,row=1)
button2=tkinter.Button(pencere,text="dosya oku",command=oku)
button2.grid(column=1,row=2)
veri2=tkinter.Text(height=5,width=15)
veri2.grid(column=2,row=2)
veri3=tkinter.Label(text="okunacak veri")
veri3.grid(column=2,row=3)
pencere.mainloop()
