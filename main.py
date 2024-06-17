from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator


class GoogleTranslator:
    def __init__(self, window):
        self.window = window
        self.sentence = StringVar()
        self.translated_text= StringVar()

        self.entry1 = Entry(window, width=29, font=('Arial Bold', 18), textvariable=self.sentence)
        self.entry1.place(x=20, y=100)

        self.entry2 = Entry(window, width=29, font=('Arial Bold', 18), textvariable=self.translated_text)
        self.entry2.place(x=650, y=100)

        translate_button = Button(window, width=18, height=7, text='Translate', relief='flat', bg='green', command=self.translate)
        translate_button.place(x=480, y=300)

        self.combobox_des = ttk.Combobox(window, height=15, values=['en', 'ja'])
        self.combobox_des.place(x=400, y=50)
        self.combobox_des.set("SELECT LANGUAGE")

        self.combobox_s = ttk.Combobox(window, height=15, values=['ko'])
        self.combobox_s.place(x=150, y=50)
        self.combobox_s.set("SELECT LANGUAGE")

    
    def translate(self):
        src_lang = self.combobox_s.get()
        des_lang = self.combobox_des.get()
        text_to_language = self.sentence.get()

        translator = Translator()
        translated_text = translator.translate(text_to_language, src=src_lang, dest=des_lang).text
        self.translated_text.set(translated_text)


if __name__ == "__main__":
    window = Tk()
    window.title("Google Translator 🌏")  # window 창의 제목 설정
    window.geometry("1100x400")  # window 창 해상도 설정
    window.resizable(False, False)  # 창 크기 변경 불가

    app = GoogleTranslator(window)

    window.mainloop()