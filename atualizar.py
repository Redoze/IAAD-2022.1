import streamlit as st
from app import *
from funcs import *

def atualizar():

    st.header('Operação de Atualização')
    st.markdown("---")

    aba1, aba2 = st.tabs(["Medico", "Especialidade"])

    with aba1:

        st.subheader('Atualizar Médico')

        cnx = create_connection()
        cursor = cnx.cursor()
        cursor.execute("SELECT CodMed FROM medico")
        resultado = cursor.fetchall()
        valores = []

        for i in resultado:
            valores.append(i[0])

        with st.form(key="update_medico"):
            input_Cod = st.selectbox(label="Insira o Código do Médico a ser alterado", options = valores)
            input_field = st.selectbox(label="Selecione o campo a ser alterado", options=["Código do Médico","Nome do Médico", "Genero", "Telefone", "Email", "Código da especialidade"])
            input_value = st.text_input(label="Insira o novo valor")
            input_button_submit = st.form_submit_button('Atualizar')

        if input_button_submit:
            st.info(f'Código do Médico: {input_Cod}')
            st.info(f'Campo alterado: {input_field}')
            st.info(f'Novo valor: {input_value}')

            if input_field == "Código do Médico":
                input_field = "CodMed"
            if input_field == "Nome do Médico":
                input_field = "NomeMed"
            if input_field == "Gênero":
                input_field = "Genero"
            if input_field == "Código da especialidade":
                input_field = "CodEspec"

            query = f"UPDATE medico SET {input_field} = %s WHERE CodMed = %s"
            values = (input_value, input_Cod)
            cursor.execute(query, values)
            cnx.commit()
            cursor.close()
            cnx.close()
            st.success("Médico alterado com sucesso!")

        tabela_bd('Médicos', 'medico')

    with aba2:

        st.subheader('Atualizar Especialidade')

        cnx = create_connection()
        cursor = cnx.cursor()
        cursor.execute("SELECT CodEspec FROM especialidade")
        resultado = cursor.fetchall()
        valores = []

        for i in resultado:
            valores.append(i[0])
        
        with st.form(key="update_especialidade"):
            input_Cod = st.selectbox(label="Insira o Código da Especialidade a ser alterada", options = valores)
            input_field = st.selectbox(label="Selecione o campo a ser alterado", options=["Código do especialista","Nome da especialidade", "Descrição"])
            input_value = st.text_input(label="Insira o novo valor")
            input_button_submit = st.form_submit_button('Atualizar')

        if input_button_submit:
            st.info(f'Código da especialidade: {input_Cod}')
            st.info(f'Campo alterado: {input_field}')
            st.info(f'Novo valor: {input_value}')

            if input_field == "Código da especialidade":
                input_field = "CodEspec"
            if input_field == "Nome da especialidade":
                input_field = "NomeEspec"
            if input_field == "Descrição":
                input_field = "Descricao"

            query = f"UPDATE especialidade SET {input_field} = %s WHERE CodEspec = %s"
            values = (input_value, input_Cod)
            cursor.execute(query, values)
            cnx.commit()
            cursor.close()
            cnx.close()
            st.success("Especialidade alterada com sucesso!")

        tabela_bd('Especialidade', 'especialidade')
