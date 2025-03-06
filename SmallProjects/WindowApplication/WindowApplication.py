from tkinter import *
from PIL import Image, ImageTk


def switch_fullscreen(event=None):
    window.attributes('-fullscreen', not window.attributes('-fullscreen'))  #переключение полноэкранного режима


def exit_app(event=None):
    window.destroy()


def showkitten(event=None):
    label.configure(text='KITTEN!!!!')
    try:
        image_path = '..\\source\\kitten.jpg'  # Укажите путь к изображению
        image = Image.open(image_path)  # Открываем изображение с помощью Pillow
        image = image.resize((800, 600), Image.Resampling.LANCZOS)  # Масштабируем изображение
        photo = ImageTk.PhotoImage(image)  # Преобразуем изображение для tkinter

        # Создаем Label для отображения изображения
        image_label = Label(
            window,
            image=photo
        )

        image_label.image = photo  # Сохраняем ссылку на изображение, чтобы оно не удалилось сборщиком мусора

        image_label.grid(
            column=1,
            row=1,
            sticky='nw',
            padx=20,
            pady=20
        )

    except Exception as e:
        print(f"Error loading image: {e}")


window = Tk()
window.title("Title of Application")
window.attributes('-fullscreen', True)  #полноэкранный режим по умолчанию
#надпись
label = Label(
    window,
    text="Label 1",
    font='Calibri, 40',
    fg='green'
)
#расположение
label.grid(
    column=0,
    row=0,
    sticky='nw',
    padx=20,
    pady=20
)
#назначение кнопки
fullscreenButton = Button(
    window,
    text='Switching to full-screen mode',
    font='Calibri, 20',
    bg='#90EE90',
    borderwidth=10,
    activebackground='#7FFFD4',
    command=switch_fullscreen
)
fullscreenButton.grid(
    column=0,
    row=1,
    sticky='sw',
    padx=20,
    pady=20
)

exitButton = Button(
    window,
    text='Exit',
    font='Calibri, 20',
    fg="#F08080",
    borderwidth=10,
    activeforeground='#8B0000',
    command=exit_app
)
exitButton.grid(
    column=2,
    row=1,
    sticky='se',
    padx=20,
    pady=20
)

kittenButton = Button(
    window,
    text='Show the kitten.',
    font='Calibri,30',
    bg='#87CEEB',
    fg='#D2691E',
    activebackground='#000080',
    activeforeground='#800000',
    borderwidth=5,
    command=showkitten
)
kittenButton.grid(
    column=2,
    row=0,
    sticky='ne',
    padx=20,
    pady=20
)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)

window.mainloop()  # функция mainloop вызывает бесконечный цикл окна, поэтому окно будет ждать любого взаимодействия
# с пользователем, пока не будет закрыто.
