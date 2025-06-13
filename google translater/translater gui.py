from tkinter import *
from googletrans import Translator, LANGUAGES

root = Tk()
root.title("Language Translator")
root.geometry("400x400")
root.config(bg="lightblue")

translator = Translator()
languages = list(LANGUAGES.values())

Label(root, text="Enter text:", bg="lightblue").pack(pady=5)
input_text = Text(root, height=5, width=40)
input_text.pack()

Label(root, text="From:", bg="lightblue").pack()
src_lang = StringVar()
src_lang.set("english")
OptionMenu(root, src_lang, *languages).pack()

Label(root, text="To:", bg="lightblue").pack()
dest_lang = StringVar()
dest_lang.set("tamil")
OptionMenu(root, dest_lang, *languages).pack()

Label(root, text="Translated Text:", bg="lightblue").pack(pady=5)
output_text = Text(root, height=5, width=40)
output_text.pack()

def translate():
    translated = translator.translate(input_text.get("1.0", END), src=src_lang.get(), dest=dest_lang.get())
    output_text.delete("1.0", END)
    output_text.insert(END, translated.text)

Button(root, text="Translate", command=translate, bg="green", fg="white").pack(pady=10)

root.mainloop()
