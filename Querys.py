import Connection

# Підключення до бази даних
connection = Connection.create_connection("postgres", "C", "root", "localhost", "5432")
cursor = connection.cursor()

def run_query(sql_query, params=None, comment=None):
    # Подключення к базе даних и выполнение запроса
    try:
        if comment:
            print(comment)  # Друкуємо коментар перед виконанням запиту
        cursor.execute(sql_query, params)

        # Получение результатов запроса
        records = cursor.fetchall()

        # Вывод результатов
        for record in records:
            print(record)

    except Exception as e:
        print(f"Помилка виконання запиту: {e}")

try:
    # Запит 1: Відобразити всіх пацієнтів, які народилися після 1998 року. Відсортувати по прізвищу пацієнта:
    sql_query = """
    SELECT * FROM Patients
    WHERE BirthYear > 1998
    ORDER BY LastName;
    """
    run_query(sql_query, comment="Запит 1: Відобразити всіх пацієнтів, які народилися після 1998 року. Відсортувати по прізвищу пацієнта")

    # Запит 2: Порахувати кількість пацієнтів дитячої категорії та кількість пацієнтів дорослої категорії
    sql_query = """
    SELECT Category, COUNT(*) as PatientCount
    FROM Patients
    GROUP BY Category;
    """
    run_query(sql_query, comment="Запит 2: Порахувати кількість пацієнтів дитячої категорії та кількість пацієнтів дорослої категорії")

    # Запит 3: Порахувати суму лікування та суму лікування з урахуванням пільги для кожного пацієнта (запит з обчислювальним полем)
    sql_query = """
    SELECT PatientID, SUM(CAST(DailyCost AS NUMERIC) * DaysSpent * (1 - CAST(Discount AS NUMERIC)/100.0)) as TotalTreatmentCost
    FROM Hospitalizations
    GROUP BY PatientID;
    """
    run_query(sql_query, comment="Запит 3: Порахувати суму лікування та суму лікування з урахуванням пільги для кожного пацієнта (запит з обчислювальним полем)")

    # Запит 4: Відобразити всі звернення до лікаря заданої спеціалізації (запит з параметром)
    specialization_to_select = 'Хірург'
    sql_query = """
    SELECT Patients.*
    FROM Patients
    JOIN Hospitalizations ON Patients.PatientID = Hospitalizations.PatientID
    JOIN Doctors ON Hospitalizations.DoctorID = Doctors.DoctorID
    WHERE Doctors.Specialization = 'Хірург';
    """
    surgeon_patients = cursor.fetchall()


    run_query(sql_query, comment=f"Запит 4: Відобразити всі звернення до лікаря заданої спеціалізації '{specialization_to_select}' (запит з параметром)")

    # Запит 5: Порахувати кількість звернень пацієнтів до кожного лікаря (підсумковий запит)
    sql_query = """
    SELECT DoctorID, COUNT(2) as TotalVisits
    FROM Hospitalizations
    GROUP BY DoctorID;
    """
    run_query(sql_query, comment="Запит 5: Порахувати кількість звернень пацієнтів до кожного лікаря (підсумковий запит)")

    # Запит 6: Порахувати кількість пацієнтів кожної категорії, які лікувалися у лора, терапевта, хірурга (перехресний запит)
    sql_query = """
    SELECT Category, Specialization, COUNT(*) as PatientCount
    FROM Patients
    JOIN Hospitalizations ON Patients.PatientID = Hospitalizations.PatientID
    JOIN Doctors ON Hospitalizations.DoctorID = Doctors.DoctorID
    GROUP BY Category, Specialization;
    """
    run_query(sql_query, comment="Запит 6: Порахувати кількість пацієнтів кожної категорії, які лікувалися у лора, терапевта, хірурга (перехресний запит)")

except Exception as e:
    print(f"Помилка виконання запиту: {e}")

# Закриття підключення
cursor.close()
connection.close()
