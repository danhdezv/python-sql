import sqlite3

try:
    connection = sqlite3.connect("company.db") ##CREATE DATABASE company:

    cursor = connection.cursor()
    #Consulta SQL
    sql_command = """
        CREATE TABLE IF NOT EXISTS employee (
        id INTEGER PRIMARY KEY ,
        name VARCHAR(20),
        last_name VARCHAR(30),
        gender CHAR(1),
        birth_date DATE
    ); """
    #Consulta SQL
    cursor.execute(sql_command)
    sql_command = """
        INSERT INTO employee (
            id , name , last_name ,gender ,birth_date
        ) VALUES (
            NULL, "NAME1","LAST_NAME","G","1988-10-11")
        ;
    """
    #cursor.execute(sql_command) EJECUTA COMANDO SQL
    cursor.execute("SELECT id FROM employee WHERE id < 20;")
    ##    print(sql_command)
    result = cursor.fetchall()
    print(result)
    

    cursor.execute("SELECT * FROM employee WHERE id < 20;")
    ##    print(sql_command)
    result = cursor.fetchone()
    print("_____________________")
    print(result)

    connection.commit()
    connection.close()

except Exception as identifier:
    print("Something went wrong")
    print(identifier)


