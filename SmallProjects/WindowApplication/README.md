# Справочник.

##  1. Установка инструмента для упаковки Python-приложений в исполняемые файлы.

    pip install pyinstaller

## 2. Создание исполнительного exe файла.

       pyinstaller --onefile --noconsole --name Kitten --icon=source/cat.ico .\WindowApplication.py

## 3. Обновление exe файла.

    1) Удаление build и exe файла.
       rm -r -fo .\build\
       del dist\Kitten.exe
    2) Сборка проекта.
       pyinstaller --onefile --noconsole --name Kitten --icon=source/cat.ico .\WindowApplication.py

## 4. Пример создания кнопки с дополнительными параметрами.

    fullscreenButton = Button(
    window,
    text='Switching to full-screen mode',
    font=('Calibri', 20),
    bg='blue',              # Цвет фона
    fg='white',             # Цвет текста
    activebackground='green',  # Цвет фона при наведении
    activeforeground='yellow', # Цвет текста при наведении
    highlightbackground='red', # Цвет рамки
    highlightcolor='orange',   # Цвет рамки при фокусе
    command=switch_fullscreen)

## 5. Пример создания надписи с дополнительными параметрами.

    label = Label(
    window,
    text="Привет, это пример Label!",  # Текст
    font=('Arial', 20, 'bold'),       # Шрифт: Arial, размер 20, жирный
    bg='lightblue',                   # Цвет фона
    fg='darkblue',                    # Цвет текста
    padx=20,                          # Горизонтальные отступы
    pady=10,                          # Вертикальные отступы
    relief='ridge',                   # Стиль рамки (ridge, sunken, raised, flat, groove, solid)
    borderwidth=5,                    # Толщина рамки
    width=30,                         # Ширина в символах
    height=3,                         # Высота в строках
    anchor='center',                  # Выравнивание текста (n, s, e, w, ne, nw, se, sw, center)
    justify='left'                    # Выравнивание текста внутри Label (left, right, center))

## 6. Палитра цветов HTML.

    https://colorscheme.ru/html-colors.html?ysclid=m7wj8zqk3l160673666

