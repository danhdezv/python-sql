import sqlite3

try:
    connection = sqlite3.connect("company.db") ##CREATE DATABASE company:

    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys = 1")
    

    #Consulta SQL CREAR TABLA OFFICE
    sql_command = """
        CREATE TABLE IF NOT EXISTS office (
        id INTEGER PRIMARY KEY ,
        name VARCHAR(20)
        
    ); """

    #EJECUCION CONSULTA  SQL CREAR TABBLA OFFICE
    cursor.execute(sql_command)

    #Consulta SQL CREAR TABLA EMPLOYEE
    sql_command = """
        CREATE TABLE IF NOT EXISTS employee (
        id INTEGER PRIMARY KEY ,
        name VARCHAR(20),
        last_name VARCHAR(30),
        gender CHAR(1),
        birth_date DATE,
        FOREIGN KEY (officeid) REFERENCES office (id)

    ); """

    #EJECUCION SQL DE CREAR TABLA EMPLOYEE
    cursor.execute(sql_command)

    #Consulta SQL INSERTAR EMPLEADO EN EMPLOYE
    sql_command = """
        INSERT INTO employee (
            id , name , last_name ,gender ,birth_date
        ) VALUES (
            NULL, "Pancho","Rios RODRIGUEZ","H","1990-06-19 , 1")
        ;
    """
    #EJECUCION SQL INSERTAR EMPLEADO EN EMPLOYE
    cursor.execute(sql_command)

    #Consulta SQL INSERTAR REGISTRO  EN OFFICE
    sql_command = """
        INSERT INTO office (
            id , name 
            ) values (
                NULL,
                "MKT"
        );
    """
    #EJECUCION SQL INSERTAR EMPLEADO EN EMPLOYE
    cursor.execute(sql_command)


    #cursor.execute(sql_command) EJECUTA COMANDO SQL
    cursor.execute("SELECT id,name FROM employee ; ")
    ##    print(sql_command)
    result = cursor.fetchall()
    print("TABLA EMPLOYEE")
    print(result)
    
    print("_____________________")
    print("TABLA OFFICE")
    cursor.execute("SELECT * FROM OFFICE;")
    ##    print(sql_command)
    result = cursor.fetchall()
    
    print(result)

    connection.commit()
    connection.close()

except Exception as identifier:
    print("Something went wrong")
    print(identifier)


