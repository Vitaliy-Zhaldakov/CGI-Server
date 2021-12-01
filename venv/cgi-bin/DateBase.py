import sqlite3

# Создание соедиения с базой
connection = sqlite3.connect("Photo-videoTechnic.db")
# Создание курсора
cursor = connection.cursor()

# Создание таблиц
# cursor.execute("""CREATE TABLE IF NOT EXISTS type
#                   (typeID INTEGER PRIMARY KEY AUTOINCREMENT,
#                   typeName VARCHAR(40));
#                """)
# connection.commit()
#
# cursor.execute("""CREATE TABLE IF NOT EXISTS maxResolution
#                     (resolutionID INTEGER PRIMARY KEY AUTOINCREMENT,
#                     resolution VARCHAR(30));
#                 """)
# connection.commit()
#
# cursor.execute("""CREATE TABLE IF NOT EXISTS videoCameras
#                     (videoCamID INTEGER PRIMARY KEY AUTOINCREMENT,
#                     manufacturer VARCHAR(20),
#                     model VARCHAR(40),
#                     resolutionID INTEGER,
#                     price INTEGER,
#                     FOREIGN KEY (resolutionID) REFERENCES maxResolution(resolutionID));
#                 """)
# connection.commit()
#
# cursor.execute("""CREATE TABLE IF NOT EXISTS cameras
#                     (cameraID INTEGER PRIMARY KEY AUTOINCREMENT,
#                     manufacturer VARCHAR(20),
#                     model VARCHAR(40),
#                     typeID INTEGER,
#                     price INTEGER,
#                     FOREIGN KEY (typeID) REFERENCES type(typeID));
#                 """)
# connection.commit()
#
# cursor.execute("""CREATE TABLE IF NOT EXISTS actionCameras
#                     (actionCamID INTEGER PRIMARY KEY AUTOINCREMENT,
#                     manufacturer VARCHAR(20),
#                     model VARCHAR(40),
#                     resolutionID INTEGER,
#                     price INTEGER,
#                     FOREIGN KEY (resolutionID) REFERENCES maxResolution(resolutionID));
#                 """)
# connection.commit()

types = [('Camera with interchangeable optics'),
         ('Film camera'),
         ('Instant printing camera'),
         ('Compact camera'),
         ('Slr camera')]

resolutions = [('720x480'),
               ('1920x1080'),
               ('2560x1440'),
               ('2688x1520'),
               ('2704x1520'),
               ('2880x2160'),
               ('3840x2160')]

cameras = [('Fujifilm', 'QuickSnap CD20', '2', '1799'),
           ('Canon', 'Zoemini C', '3', '6299'),
           ('Fujifilm', 'Instax mini 9', '3', '5999'),
           ('DEXP', 'Kid`s Printing Cam', '3', '5299'),
           ('DEXP', 'Kid`s Cam', '4', '1650'),
           ('Rekam', 'iLook K410i', '4', '1199'),
           ('Sony', 'Alpha ILCE-6000B Body', '1', '47999')]

videoCameras = [('Canon', 'XA11', '2', '106999'),
                ('Sony', 'FDR-AX53', '7', '89999'),
                ('Panasonic', 'V260', '2', '22999'),
                ('Rekam', 'DVC-560', '4', '6299')]

actionCameras = [('Aceline', 'S-60', '7', '2699'),
                 ('Digma', 'DiCam 300', '7', '1899'),
                 ('Aceline', 'S-40', '2', '1499'),
                 ('Digma', 'DiCam 170', '2', '1299'),
                 ('SJCAM', 'FUNCAM', '2', '1199')]

# Данные таблиц
# Данные таблицы type
# cursor.execute("INSERT INTO type(typeName) VALUES('Camera with interchangeable optics');")
# cursor.execute("INSERT INTO type(typeName) VALUES('Film camera');")
# cursor.execute("INSERT INTO type(typeName) VALUES('Instant printing camera');")
# cursor.execute("INSERT INTO type(typeName) VALUES('Compact camera');")
# cursor.execute("INSERT INTO type(typeName) VALUES('Slr camera');")
# connection.commit()

# Данные таблицы maxResolution
# cursor.execute("INSERT INTO maxResolution(resolution) VALUES('720x480');")
# cursor.execute("INSERT INTO maxResolution(resolution) VALUES('1920x1080');")
# cursor.execute("INSERT INTO maxResolution(resolution) VALUES('2560x1440');")
# cursor.execute("INSERT INTO maxResolution(resolution) VALUES('2688x1520');")
# cursor.execute("INSERT INTO maxResolution(resolution) VALUES('2704x1520');")
# cursor.execute("INSERT INTO maxResolution(resolution) VALUES('2880x2160');")
# cursor.execute("INSERT INTO maxResolution(resolution) VALUES('3840x2160');")
# connection.commit()

# Данные таблицы cameras
# cursor.execute("INSERT INTO cameras(manufacturer, model, typeID, price) VALUES('Fujifilm', 'QuickSnap CD20', '2', '1799');")
# cursor.execute("INSERT INTO cameras(manufacturer, model, typeID, price) VALUES('Canon', 'Zoemini C', '3', '6299');")
# cursor.execute("INSERT INTO cameras(manufacturer, model, typeID, price) VALUES('Fujifilm', 'Instax mini 9', '3', '5999');")
# cursor.execute("INSERT INTO cameras(manufacturer, model, typeID, price) VALUES('DEXP', 'Kid`s Printing Cam', '3', '5299');")
# cursor.execute("INSERT INTO cameras(manufacturer, model, typeID, price) VALUES('DEXP', 'Kid`s Cam', '4', '1650');")
# cursor.execute("INSERT INTO cameras(manufacturer, model, typeID, price) VALUES('Rekam', 'iLook K410i', '4', '1199');")
# cursor.execute("INSERT INTO cameras(manufacturer, model, typeID, price) VALUES('Sony', 'Alpha ILCE-6000B Body', '1', '47999');")
# connection.commit()

# Данные таблицы videoCameras
# cursor.execute("INSERT INTO videoCameras(manufacturer, model, resolutionID, price) VALUES('Canon', 'XA11', '2', '106999');")
# cursor.execute("INSERT INTO videoCameras(manufacturer, model, resolutionID, price) VALUES('Sony', 'FDR-AX53', '7', '89999');")
# cursor.execute("INSERT INTO videoCameras(manufacturer, model, resolutionID, price) VALUES('Panasonic', 'V260', '2', '22999');")
# cursor.execute("INSERT INTO videoCameras(manufacturer, model, resolutionID, price) VALUES('Rekam', 'DVC-560', '4', '6299');")
# connection.commit()

# Данные таблицы actionCameras
# cursor.execute("INSERT INTO actionCameras(manufacturer, model, resolutionID, price) VALUES('Aceline', 'S-60', '7', '2699');")
# cursor.execute("INSERT INTO actionCameras(manufacturer, model, resolutionID, price) VALUES('Digma', 'DiCam 300', '7', '1899');")
# cursor.execute("INSERT INTO actionCameras(manufacturer, model, resolutionID, price) VALUES('Aceline', 'S-40', '2', '1499');")
# cursor.execute("INSERT INTO actionCameras(manufacturer, model, resolutionID, price) VALUES('Digma', 'DiCam 170', '2', '1299');")
# cursor.execute("INSERT INTO actionCameras(manufacturer, model, resolutionID, price) VALUES('SJCAM', 'FUNCAM', '2', '1199');")
# connection.commit()


# cursor.execute("DELETE FROM cameras WHERE cameraID = 9")
#cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ = 7 WHERE NAME = 'cameras';")
#connection.commit()

import xml.etree.ElementTree as Etree

# Создание структуры файла
file = open('X:\\PyCharm Community Edition 2021.2.2\\CGI-Server\\venv\\Data.xml', 'w')

# Определение корня и потомка (таблица)
data = Etree.Element('data')
table = Etree.SubElement(data, 'table')

# Извлечение данных из таблицы Фотоаппараты
cursor.execute("SELECT * FROM cameras")
cameras = cursor.fetchall()

# Создание структуры записей как потомков таблицы
for row in cameras:
    entry = Etree.SubElement(table, 'entry')

    # Поля записи
    id = Etree.SubElement(entry, 'field')
    manufacturer = Etree.SubElement(entry, 'field')
    model = Etree.SubElement(entry, 'field')
    type = Etree.SubElement(entry, 'field')
    price = Etree.SubElement(entry, 'field')

    id.text = str(row[0])
    manufacturer.text = str(row[1])
    model.text = str(row[2])
    type.text = str(row[3])
    price.text = str(row[4])

# Импорт в файл
tableData = str(Etree.tostring(data))
file.write(tableData)
file.close()


# Экспорт из файла
tree = Etree.parse('X:\\PyCharm Community Edition 2021.2.2\\CGI-Server\\venv\\Data.xml')
root = tree.getroot()

for table in root:
    for entry in table:
        manufacturer = entry[0].text
        model = entry[1].text
        type = entry[2].text
        price = entry[3].text
        cursor.execute("INSERT INTO cameras(manufacturer, model, typeID, price) VALUES(?, ?, ?, ?)",
                       (manufacturer, model, type, price))

# Закрытие соединения
connection.close()
