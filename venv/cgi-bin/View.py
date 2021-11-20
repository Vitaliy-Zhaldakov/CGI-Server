#!/usr/bin/python

# Импорт модулей для обработки CGI
import cgi, cgitb
import html
import sqlite3

# Создание соедиения с базой
connection = sqlite3.connect("X:\\PyCharm Community Edition 2021.2.2\\CGI-Server\\venv\\Photo-videoTechnic.db")
# Создание курсора
cursor = connection.cursor()

# Создание экземпляра FieldStorage
form = cgi.FieldStorage()

# Получение данных из полей
table = form.getvalue('Таблицы')
addTable = form.getvalue('table')

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<meta charset=""UTF-8"">")
print ("<title>Фото-видео техника</title>")
print ("</head>")
print ("<body bgcolor = #7FFFD4 background = url(picture.jpg)>")
print ("<h1 align = 'center'>Фото-видео техника</h1>")

# Форма выбора таблиц для вывода
print("""<form action = "/cgi-bin/View.py" method = "post">
<select name = "Таблицы">
<option value = "cameras">Фотоаппараты</option>
<option value = "videoCameras">Видеокамеры</option>
<option value = "actionCameras">Экшн-камеры</option>
<option value = "type">Виды фотоаппаратов</option>
<option value = "maxResolution">Разрешения</option>
</select>
<input type = "submit" value = "Вывести" />
</form>""")

# Форма выбора таблиц для добавления данных
print("""<form action = "/cgi-bin/View.py" method = "post">
<input type = 'radio' name = 'table' value = 'cameras' /> Фотоаппараты <br>
<input type = 'radio' name = 'table' value = 'videoCameras' /> Видеокамеры <br>
<input type = 'radio' name = 'table' value = 'actionCameras' /> Экшн-камеры <br>
<input type = 'radio' name = 'table' value = 'maxResolution' /> Разрешения <br><br>
<input type = "submit" value = "Добавить данные" />
</form>""")

# Вывод таблиц на экран
if table == 'cameras':
    # Запрос таблицы Фотоаппараты
    cursor.execute("""SELECT cameraID, manufacturer, model, typeName, price
                   FROM cameras JOIN type ON cameras.typeID = type.typeID""")
    cameras = cursor.fetchall()

    # Таблица Фотоаппараты
    print("<table cellspacing = '10'>"
          "<caption><h2>Фотоаппараты</h2></caption>"
          "<tr>"
          "<th>ID</th>"
          "<th>Производитель</th>"
          "<th>Модель</th>"
          "<th>Тип</th>"
          "<th>Цена</th>"
          "</tr>")
    for row in cameras:
        print("<tr><td align = 'center'>", row[0], "</td><td align = 'center'>", row[1],
              "</td><td align = 'center'>", row[2], "</td><td align = 'center'>", row[3],
              "</td><td align = 'center'>", row[4], "₽" "</td></tr>")
    print("</table>")

elif table == 'videoCameras':
    # Запрос таблицы Видеокамеры
    cursor.execute("""SELECT videoCamID, manufacturer, model, resolution, price
                       FROM videoCameras JOIN maxResolution ON videoCameras.resolutionID = maxResolution.resolutionID""")
    videoCams = cursor.fetchall()

    # Таблица Видеокамеры
    print("<table cellspacing = '10'>"
          "<caption><h2>Видеокамеры</h2></caption>"
          "<tr>"
          "<th>ID</th>"
          "<th>Производитель</th>"
          "<th>Модель</th>"
          "<th>Разрешение</th>"
          "<th>Цена</th>"
          "</tr>")
    for row in videoCams:
        print("<tr><td align = 'center'>", row[0], "</td><td align = 'center'>", row[1],
              "</td><td align = 'center'>", row[2], "</td><td align = 'center'>", row[3],
              "</td><td align = 'center'>", row[4], "₽" "</td></tr>")
    print("</table>")

elif table == 'actionCameras':
    # Запрос таблицы Экшн-камеры
    cursor.execute("""SELECT actionCamID, manufacturer, model, resolution, price
                    FROM actionCameras JOIN maxResolution ON actionCameras.resolutionID = maxResolution.resolutionID""")
    actionCams = cursor.fetchall()

    # Таблица Экшн-камеры
    print("<table cellspacing = '10'>"
          "<caption><h2>Экшн-камеры</h2></caption>"
          "<tr>"
          "<th>ID</th>"
          "<th>Производитель</th>"
          "<th>Модель</th>"
          "<th>Разрешение</th>"
          "<th>Цена</th>"
          "</tr>")
    for row in actionCams:
        print("<tr><td align = 'center'>", row[0], "</td><td align = 'center'>", row[1],
              "</td><td align = 'center'>", row[2], "</td><td align = 'center'>", row[3],
              "</td><td align = 'center'>", row[4], "₽" "</td></tr>")
    print("</table>")

elif table == 'type':
    # Запрос таблицы Типы
    cursor.execute("""SELECT typeID, typeName
                    FROM type""")
    types = cursor.fetchall()

    # Таблица Виды фотоаппаратов
    print("<table cellspacing = '10'>"
          "<caption><h2>Виды фотоаппаратов</h2></caption>"
          "<tr>"
          "<th>ID</th>"
          "<th>Наименования</th>"
          "</tr>")
    for row in types:
        print("<tr><td align = 'center'>", row[0], "</td><td align = 'center'>", row[1])
    print("</table>")

elif table == 'maxResolution':
    # Запрос таблицы Разрешения
    cursor.execute("""SELECT resolutionID, resolution
                        FROM maxResolution""")
    resolutions = cursor.fetchall()

    # Таблица Разрешения
    print("<table cellspacing = '10'>"
          "<caption><h2>Максимальные разрешения</h2></caption>"
          "<tr>"
          "<th>ID</th>"
          "<th>Разрешения</th>"
          "</tr>")
    for row in resolutions:
        print("<tr><td align = 'center'>", row[0], "</td><td align = 'center'>", row[1])
    print("</table>")

# Добавление данных в таблицы (просто формочка, когда сюда заходит сначала выполнялся наш запрос,
# а уже потом с формочек читались данные, которые вводили
if addTable == 'cameras':
    print("""<form action = "/cgi-bin/View.py" method = "post">
    Производитель: <input type = "text" name = "manufacturer" /> 
    Модель: <input type = "text" name = "model" />
    Тип фотоаппарата: <input type = "text" name = "type" />
    Цена: <input type = "text" name = "price" />
    <input type = 'submit' value = 'Добавить'>
    </form>""")

elif addTable == 'videoCameras':
    print("""<form action = "/cgi-bin/View.py" method = "post">
        Производитель: <input type = "text" name = "manufacturer" /> 
        Модель: <input type = "text" name = "model" />
        Разрешение: <input type = "text" name = "resolutionID" />
        Цена: <input type = "text" name = "price" />
        <input type = 'submit' value = 'Добавить'>
        </form>""")

# Получение данных из полей
manufacturer = form.getvalue('manufacturer')
model = form.getvalue('model')
typeCam = form.getvalue('type')
price = form.getvalue('price')
resolution = form.getvalue('resolutionID')

# Добавление данных в таблицы
if typeCam:
    cursor.execute("INSERT INTO cameras(manufacturer, model, typeID, price) VALUES(?, ?, ?, ?)",
                   (manufacturer, model, typeCam, price))
    connection.commit()

if resolution:
    cursor.execute("INSERT INTO videoCameras(manufacturer, model, resolutionID, price) VALUES(?, ?, ?, ?)",
                   (manufacturer, model, resolution, price))
    connection.commit()

print ("</body>")
print ("</html>")

# Nikon, D3500 Kit 18-55mm VR AF-P, 5, 39999

# Sony, FDR-AX700, 7, 124990