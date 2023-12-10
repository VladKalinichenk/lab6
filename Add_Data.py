import Connection

#Подключение к базе данных
connection = Connection.create_connection("postgres", "C", "root", "localhost", "5432")
cursor = connection.cursor()

# Вставка даних до таблиці Пацієнти
try:
    Patient_data = [
        (1, 'Іванов', 'Богдан', 'Іванович', 'м. Київ, вул. Хрещатик, 1', '+380996011849', 1991, 'Доросла'),
        (2, 'Петренко', 'Андрій', 'Григорович', 'м. Львів, вул. Лесі Українки, 2', '+380991671996', 2005, 'Дитяча'),
        (3, 'Марченко', 'Влад', 'Миколайович', 'м. Одеса, вул. Дерибасівська, 3', '+380974960906', 1975, 'Доросла'),
        (4, 'Степанов', 'Дмитро', 'Михайлович', 'м. Харків, вул. Сумська, 4', '+38097965746', 1989, 'Доросла'),
        (5, 'Якименко', 'Олександр', 'Юрійович', 'м. Дніпро, вул. Набережна, 5', '+380674660157', 2015, 'Дитяча'),
        (6, 'Іванова', 'Ганна', 'Олександрівна', 'м. Запоріжжя, вул. Соборна, 6', '+380970963844', 1985, 'Доросла'),
        (7, 'Лисенко', 'Микола', 'Петрович', 'м. Кривий Ріг, вул. Леніна, 7', '+380674136706', 1995, 'Доросла'),
        (8, 'Кравчук', 'Ольга', 'Миколаївна', 'м. Маріуполь, вул. Ілліча, 8', '+3809917890536', 2009, 'Дитяча'),
        (9, 'Петренко', 'Марія', 'Володимирівна', 'м. Маріуполь, вул. Роганного, 1', '+380674360146', 1988, 'Доросла'),

    ]

    insert_Patient_query = """
    INSERT INTO Patients (PatientID, LastName, FirstName, MiddleName, Address, Phone, BirthYear, Category)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (PatientID) DO NOTHING
    """

    for record in Patient_data:
        cursor.execute(insert_Patient_query, record)

    connection.commit()
except Exception as e:
    print(f"Помилка при додаванні даних до таблиці Patients: {e}")

# Вставка даних до таблиці Лікарі
try:
    Doctor_data = [
        (1, 'Кринитський', 'Богдан', 'Петрович', 'Лор', 10),
        (2, 'Шевченко', 'Артем', 'Юрійович', 'Хірург', 5),
        (3, 'Лисенко', 'Ігор', 'Олегович', 'Терапевт', 11),
        (4, 'Якименко', 'Ольга', 'Миколаївна', 'Лор', 7),
    ]

    insert_Doctor_query = """
    INSERT INTO Doctors (DoctorID, LastName, FirstName, MiddleName, Specialization, Experience)
    VALUES (%s, %s, %s, %s, %s, %s)
    ON CONFLICT (DoctorID) DO NOTHING
    """

    for record in Doctor_data:
        cursor.execute(insert_Doctor_query, record)

    connection.commit()
except Exception as e:
    print(f"Помилка при додаванні даних до таблиці Doctors: {e}")

# Вставка даних до таблиці Звернень до лікарні
try:
    Hospitalization_data = [
        (1, 1, '2023-01-02', 6, '200', 10, 4),
        (2, 2, '2023-01-06', 10, '250', 15, 2),
        (3, 3, '2023-01-09', 5, '100', 5, 3),
        (4, 4, '2023-01-13', 2, '150', 20, 1),
        (5, 5, '2023-01-18', 8, '200', 15, 2),
        (6, 6, '2023-01-20', 15, '150', 20, 1),
        (7, 7, '2023-01-21', 11, '100', 5, 3),
        (8, 8, '2023-01-25', 5, '250', 10, 4),
        (9, 9, '2023-01-26', 8, '100', 5, 3),
        (10, 6, '2023-02-01', 4, '200', 15, 2),
        (11, 7, '2023-02-09', 8, '100', 5, 3),
        (12, 1, '2023-02-15', 9, '250', 10, 4),
        (13, 2, '2023-02-22', 17, '150', 20, 1),
        (14, 5, '2023-02-29', 20, '200', 15, 2),
        (15, 3, '2023-03-03', 13, '250', 10, 4),
        (16, 2, '2023-03-08', 6, '150', 20, 1),
        (17, 9, '2023-03-19', 5, '100', 5, 3),
    ]

    insert_Hospitalization_query = """
    INSERT INTO Hospitalizations (ArrivalID, PatientID, ArrivalDate, DaysSpent, DailyCost, Discount, DoctorID)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (ArrivalID) DO NOTHING
    """

    for record in Hospitalization_data:
        cursor.execute(insert_Hospitalization_query, record)

    connection.commit()
except Exception as e:
    print(f"Помилка при додаванні даних до таблиці Hospitalizations: {e}")


cursor.close()
connection.close()
