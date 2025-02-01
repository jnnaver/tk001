from tkinter import *
window=Tk()
window.geometry("330x200")
window.title("My first window")

#레이블 : 문자 표현
label1 =Label(window, text="안녕하세요")
label1.pack()
#배치방법
#pack()
button1 = Button(window, text = "클릭하세요")
button1.pack()
label2 = Label(window, text="") 
label2.config(text="멋진 하루 되세요")
label2.pack()
window.mainloop()