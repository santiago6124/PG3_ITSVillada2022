import pymysql
while True:
    connection = pymysql.connect( host='localhost', user= 'bdi', passwd='pepe1234', db='EjExceptions')
    cur = connection.cursor()
    code = input("Ingrese el código para la base de datos (No borre la base de datos porfa): ")

    try:
        cur.execute(code)
    except pymysql.err.ProgrammingError as error:
        print(error, "\n*****Error de sintaxis*****")
    except pymysql.err.InternalError as error:
        print(error, "\n*****ERROR*****")
    except pymysql.err.OperationalError as error:
        print(error, "\n*****ERROR, Query puede estar vacía*****")
    except pymysql.err.IntegrityError as error:
        print(error, "\n*****ERROR*****")
    except pymysql.err.DataError as error:
        print(error, "\n*****ERROR*****")
    except pymysql.err.NotSupportedError as error:
        print(error, "\n*****ERROR*****")
    except pymysql.err.DatabaseError as error:
        print(error, "\n*****ERROR*****")
    except Exception as error:
        print(error, "\n*****ERROR*****")
    ans=input("Si no desea seguir ingresando codigo ingrese [n], si quiere seguir ingrese cualquier otra letra: ")
    if ans=="n":
            break
    connection.close()
      