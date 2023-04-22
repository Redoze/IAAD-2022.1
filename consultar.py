import streamlit as st
from app import *
from conexao import *

def consultar():

    st.header("Consulta do Bando de Dados")
    st.markdown("---")

    cnx = create_connection()
    cursor = cnx.cursor()

    cursor.execute("SHOW TABLES")
    resultado = cursor.fetchall()
    valores = []

    for i in resultado:
        valores.append(i[0])

    opicoes = st.multiselect("Escolha as tabelas que deseja visualizar", options= valores)

    for i in (opicoes):
        conv_string = str(i)
        if i == 'medico':
            st.subheader("Tabela Médico")
        elif i == 'especialidade':
            st.subheader("Tabela Especialidade")
        cursor.execute("SELECT * FROM " + conv_string)
        resultado = cursor.fetchall()
        st.dataframe(resultado)

        if conv_string == 'medico':
            st.caption('Coluna 0 = Código do Médico')
            st.caption("Coluna 1 = Nome do Médico")
            st.caption("Coluna 2 = Gênero")
            st.caption("Coluna 3 = Telefone")
            st.caption("Colune 4 = Email")
            st.caption("Coluna 5 = Código de especialidade")
        if conv_string == 'especialidade':
            st.caption('Coluna 0 = Código de especialidade')
            st.caption("Coluna 1 = Nome da especialidade")
            st.caption("Coluna 2 = Descrição da especialidade")