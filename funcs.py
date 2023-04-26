import streamlit as st
import mysql.connector
import pandas as pd

def create_connection():                                        
    cnx = mysql.connector.connect(user='root',                  #########################################################################
                                password='SUA SENHA',           ########## ADICIONE SEUS DADOS DE CONEXÃO COM O BANCO DE DADOS ##########
                                host='localhost',               #########################################################################
                                database='clinicasmedicas')
    return cnx

def tabela_bd (nome_tabela_plural, nome_tabela):

    st.subheader('Tabela ' + nome_tabela_plural)

    cnx = create_connection()
    cursor = cnx.cursor()
    query = "SELECT * FROM " + nome_tabela
    df = pd.read_sql_query(query, cnx)
    if nome_tabela == 'medico':
        df.columns = ["Código do Médico", "Nome do Médico", "Gênero", 'Telefone',' Email','Código de especialidade']
    if nome_tabela == 'especialidade':
        df.columns = ["Código de especialidade", "Nome da especialidade", "Descrição da especialidade"]
    
    st.dataframe(df)
    cnx.commit()
    cursor.close()
    cnx.close()
