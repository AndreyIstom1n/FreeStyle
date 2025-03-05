#pip install pyinstaller установка сборщика exe файла
#pyinstaller --onefile --noconsole --icon=cat.ico .\WindowApplication.py - создание исполнительного файла
#https://image.online-convert.com/ru/convert-to-ico - конвертация для иконки
from tkinter import *
def switch_fullscreen(event=None):
    window.attributes('-fullscreen', not window.attributes('-fullscreen'))  #переключение полноэкранного режима
def exit_app(event=None):
    window.destroy()


window = Tk()
window.title("Title of Application")
window.attributes('-fullscreen', True)  #полноэкранный режим по умолчанию

label = Label(window, text="Label 1", font=('Calibri, 40'),fg='green')  #надпись
label.grid(column=0, row=0, sticky='nw', padx=20, pady=20)  #расположение

fullscreenButton = Button(window, text='Switching to full-screen mode', font=('Calibri, 20'),bg='blue',fg='red', command=switch_fullscreen)  #назначение кнопки
fullscreenButton.grid(column=0, row=1, sticky='sw', padx=20, pady=20)

exitButton = Button(window, text='Exit', font=('Calibri, 20'), command=exit_app)
exitButton.grid(column=1, row=1, sticky='se', padx=20, pady=20)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)

window.mainloop()  # функция mainloop вызывает бесконечный цикл окна, поэтому окно будет ждать любого взаимодействия
# с пользователем, пока не будет закрыто.
