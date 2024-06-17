from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator


class Translator:
    def __init__(self, window):
        self.sentence = StringVar()
        self.init_value=''

        # entry
        entry1 = Entry(width=29, font=('Arial Bold', 18), textvariable=self.sentence).place(x=0, y=100)

        entry2 = Entry(width=29, font=('Arial Bold', 18), textvariable=self.sentence).place(x=650, y=100)
        
        Button(width=18, height=7, text='Translate', relief='flat', bg='green', command=self.translate).place(x=480, y=300)

    translator = Translator()

    def input(self, value):
        self.init_value += str(value)
        self.sentence.set(self.init_value)

    def translate(self):
        translator.translate(self.sentence)



window = Tk()
window.title("Google Translator 🌏")  # window 창의 제목 설정
window.geometry("1080x400")  # window 창 해상도 설정
window.resizable(False, False)  # 창 크기 변경 불가

# messagebox
message = Message(window, text="번역기", width=100, relief='solid')
message.pack()

# combobox
values=['kr', 'en', 'jp'] 
combobox_des=ttk.Combobox(window, height=15, values=['en', 'ja'])
combobox_des.pack()
combobox_des.set("SELECT LANGUAGE")

# combobox * 
combobox_s=ttk.Combobox(window, height=15, values=['kr'])
combobox_s.pack()
combobox_s.set("SELECT LANGUAGE")

translator = Translator(window)
window.mainloop()
