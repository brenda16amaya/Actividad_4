from pymongo.mongo_client import MongoClient # Importar la base MongoClient 

#CONEXIÓN
def conexion(): # Se define la función como conexión a la base de datos de MongoDB
    uri = "mongodb+srv://brenda16amaya:4321@cluster0.0wjciop.mongodb.net/?retryWrites=true&w=majority" # La uri de conexión a la base de datos MongoDB
    # Create a new client and connect to the server
    return MongoClient(uri) # Se conecta al MongoDB

#CREATE
""" Código necesario para crear un create en MongoDB"""


#READ
""" Código necesario para crear un read en MongoDB"""
def lecturaDatos(): # Función para realizar la lectura (READ) en MongoDB
    client = conexion() # Conexión con la base de datos MongoDB
    db = client.actividad4.data_real # Da acceso a una data_real en la base de datos que se nombra actividad4
    data_list = [] # Se crea una lista vacía para almacenar los documentos encontrados en la data_real
    for data_real_bd in db.find(): # Itera a través de los documentos encontrados en la data_real y los agrega a la lista
        data_list.append(data_real_bd)
    return data_list  # Se regresa a la lista de documentos recuperados

#UPDATE
""" Código necesario para actualizar un dato en la BD"""

#DELETE
""" Código necesario para eliminar un dato en la BD"""