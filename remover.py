import streamlit as st
from app import *
from conexao import *
from tabelas import *

def remover():

    st.header('Operação de Remoção')
    st.markdown("---")

    aba1, aba2 = st.tabs(["Médico", "Especialidade"])
                
    with aba1:

        st.subheader('Remover Médico')

        cnx = create_connection()
        cursor = cnx.cursor()
        cursor.execute("SELECT CodMed FROM medico")
        resultado = cursor.fetchall()
        valores = []

        for i in resultado:
            valores.append(i[0])

        with st.form(key="Remover_medico"):
            input_CodMed = st.selectbox(label="Insira o Código do Médico", options = valores)
            input_name = st.text_input(label="Insira o nome do Médico", max_chars = 40)
            input_genero = st.selectbox(label="Selecione seu Gênero", options=["M", "F"])
            input_telefone = st.text_input(label="Insira o Telefone", max_chars = 16)
            input_email = st.text_input(label="Insira o Email", max_chars = 40)
            input_CodEspec = st.text_input(label="Insira o Código da Especialidade", max_chars= 7)
            input_button_submit = st.form_submit_button('Remover')

        if input_button_submit:
            st.info(f'Código do Médico: {input_CodMed}')
            st.info(f'Médico: {input_name}')
            st.info(f'Gênero: {input_genero}')
            st.info(f'Telefone: {input_telefone}')
            st.info(f'Email: {input_email}')
            st.info(f'Código da Especialidade: {input_CodEspec}')

            cnx = create_connection()
            cursor = cnx.cursor()
            query = "DELETE FROM medico WHERE CodMed=%s OR NomeMed=%s OR Genero=%s OR Telefone=%s OR Email=%s OR CodEspec=%s"
            values = (input_CodMed, input_name, input_genero, input_telefone, input_email, input_CodEspec)
            cursor.execute(query, values)
            cnx.commit()
            cursor.close()
            cnx.close()
            st.success("Médico removido com sucesso!")

        tabela_bd('Médicos', 'medico')

    with aba2:
        def delete_especialidades(cnx, input_CodEsp, input_name, input_descricao):
            cursor = cnx.cursor()
            query = "DELETE FROM especialidade WHERE CodEspec = %s OR NomeEspec = %s OR Descricao = %s"
            values = (input_CodEsp, input_name, input_descricao)
            cursor.execute(query, values)
            cnx.commit()
            cursor.close()
            st.success("Especialidade removida com sucesso!")
        
        st.subheader("Remover Especilidade")

        cnx = create_connection()
        cursor = cnx.cursor()
        cursor.execute("SELECT CodEspec FROM especialidade")
        resultado = cursor.fetchall()
        valores = []

        for i in resultado:
            valores.append(i[0])

        with st.form(key="Remover_especialidade"):
            input_CodEsp = st.selectbox(label="Insira o Código da Especialidade", options = valores)
            input_name = st.text_input(label="Insira o nome da Especialidade", max_chars = 15)
            input_descricao = st.text_input(label="Descrição da Especialidade")
            input_button_submit = st.form_submit_button('Remover')

        if input_button_submit:
            st.info(f'Código Especialidade: {input_CodEsp}')
            st.info(f'Nome: {input_name}')
            st.info(f'Descrição: {input_descricao}')
            
            with create_connection() as cnx:
                delete_especialidades(cnx, input_CodEsp, input_name, input_descricao)

        tabela_bd('Especialidade', 'especialidade')