import streamlit as st
from funcs import *

def consultar():

    st.header("Consulta do Bando de Dados")
    st.markdown("---")

    cnx = create_connection()
    cursor = cnx.cursor()

    cursor.execute("SHOW TABLES")
    resultado = cursor.fetchall()
    valores = []

    for i in resultado:
        letra_i = i[0] 
        if letra_i == 'especialidade':
            palavra_tabela = 'Especialidade'
        elif letra_i == 'medico':
            palavra_tabela = 'Médico'
        valores.append(palavra_tabela)

    opicoes = st.multiselect("Escolha as tabelas que deseja visualizar", options= valores)

    for i in (opicoes):

        if i == 'Médico':
            st.subheader("Tabela Médico")
            i = 'medico'
        elif i == 'Especialidade':
            st.subheader("Tabela Especialidade")
            i = 'especialidade'

        query2 = "SELECT * FROM " + i
        df = pd.read_sql_query(query2, cnx)
        if i == 'medico':
            df.columns = ["Código do Médico", "Nome do Médico", "Gênero", 'Telefone',' Email','Código de especialidade']
        if i == 'especialidade':
            df.columns = ["Código de especialidade", "Nome da especialidade", "Descrição da especialidade"]

        st.dataframe(df)
