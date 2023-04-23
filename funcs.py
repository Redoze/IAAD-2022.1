import streamlit as st
import mysql.connector
from app import *

def create_connection():                                        
    cnx = mysql.connector.connect(user='root',                  #########################################################################
                                password='SUA SENHA',           ########## ADICIONE SEUS DADOS DE CONEXÃO COM O BANCO DE DADOS ##########
                                host='localhost',               #########################################################################
                                database='clinicasmedicas')
    return cnx

def tabela_bd (nome_tabela_plural, nome_tabela):

    st.subheader(nome_tabela_plural)

    cnx = create_connection()
    cursor = cnx.cursor()
    query = "SELECT * FROM " + nome_tabela
    cursor.execute(query)
    resultado = cursor.fetchall()
    st.dataframe(resultado)
    cnx.commit()
    cursor.close()
    cnx.close()

    if nome_tabela == 'medico':
        st.caption('Coluna 0 = Código do Médico')
        st.caption("Coluna 1 = Nome do Médico")
        st.caption("Coluna 2 = Gênero")
        st.caption("Coluna 3 = Telefone")
        st.caption("Colune 4 = Email")
        st.caption("Coluna 5 = Código de especialidade")
        
    if nome_tabela == 'especialidade':
        st.caption('Coluna 0 = Código de especialidade')
        st.caption("Coluna 1 = Nome da especialidade")
        st.caption("Coluna 2 = Descrição da especialidade")
