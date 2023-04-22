import mysql.connector
from app import *

def create_connection():                                        
    cnx = mysql.connector.connect(user='root',                  #########################################################################
                                password='iaadtask',           ########## ADICIONE SEUS DADOS DE CONEXÃO COM O BANCO DE DADOS ##########
                                host='localhost',               #########################################################################
                                database='clinicasmedicas')
    return cnx