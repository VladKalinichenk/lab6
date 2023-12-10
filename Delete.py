import Connection

# Підключення до бази даних
connection = Connection.create_connection("postgres", "C", "root", "localhost", "5432")
cursor = connection.cursor()
try:
    # Створення таблиці
    create_table_query = """
    DROP TABLE IF EXISTS Hospitalizations,Doctors,Patients;
    """
    cursor.execute(create_table_query)
    connection.commit()
except Exception as e:
    print(f"Помилка при створенні таблиці: {e}")