import Connection

# Підключення до бази даних
connection = Connection.create_connection("postgres", "C", "root", "localhost", "5432")
cursor = connection.cursor()

try:
    # Створення таблиці "Лікарі"
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Doctors (
        DoctorID INTEGER PRIMARY KEY,
        LastName TEXT,
        FirstName TEXT,
        MiddleName TEXT,
        Specialization TEXT,
        Experience INTEGER
        )
    """
    cursor.execute(create_table_query)
    connection.commit()
except Exception as e:
    print(f"Помилка при створенні таблиці Doctors: {e}")

try:
    # Створення таблиці "Пацієнти"
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Patients (
        PatientID serial PRIMARY KEY,
        LastName varchar(255),
        FirstName varchar(255),
        MiddleName varchar(255),
        Address varchar(255),
        Phone varchar(255),
        BirthYear INTEGER,
        Category varchar(255)

    )
    """
    cursor.execute(create_table_query)
    connection.commit()
except Exception as e:
    print(f"Помилка при створенні таблиці Patients: {e}")

try:
    # Створення таблиці "Прибування в стаціонарі"
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Hospitalizations (
        ArrivalID serial PRIMARY KEY,
        PatientID INTEGER,
        ArrivalDate varchar(255),
        DaysSpent INTEGER,
        DailyCost varchar(255),
        Discount INTEGER,
        DoctorID INTEGER
    )
    """
    cursor.execute(create_table_query)
    connection.commit()
except Exception as e:
    print(f"Помилка при створенні таблиці Hospitalizations: {e}")

cursor.close()
connection.close()
