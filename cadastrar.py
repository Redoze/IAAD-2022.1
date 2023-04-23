import streamlit as st
from app import *
from funcs import *

def cadastrar():
    st.header("Operação de Cadastro")
    st.markdown("---")

    aba1, aba2 = st.tabs(["Médico","Especialidade"])
    
    with aba1:

        st.subheader("Cadastrar Médico")

        cnx = create_connection()
        cursor = cnx.cursor()
        cursor.execute("SELECT CodEspec FROM especialidade")
        resultado = cursor.fetchall()
        valores = []

        for i in resultado:
            valores.append(i[0])

        with st.form(key="include_medico"):
            input_CodMed = st.text_input(label="Insira o Código do Médico", help = "insira um valor númerico de 7 digitos", max_chars = 7)
            input_name = st.text_input(label="Insira o nome do Médico", max_chars = 40)
            input_genero = st.selectbox(label="Selecione seu Gênero", options=["M", "F"])
            input_telefone = st.text_input(label="Insira o Telefone", max_chars = 16)
            input_email = st.text_input(label="Insira o Email", max_chars = 40)
            input_CodEspec = st.selectbox(label="Insira o Código da Especialidade", options = valores)
            input_button_submit = st.form_submit_button('Cadastrar')

        if input_button_submit:
            if len(input_CodMed) == 7 and len(input_name) != 0:
                query = "INSERT INTO Medico (CodMed, NomeMed, Genero, Telefone, Email, CodEspec) VALUES (%s, %s, %s, %s, %s, %s)"
                values = (input_CodMed, input_name, input_genero, input_telefone, input_email, input_CodEspec)
                cursor.execute(query, values)
                cnx.commit()
                cursor.close()
                cnx.close()

                st.success("Médico adicionado com sucesso!")
                st.info(f'Código do Médico: {input_CodMed}')
                st.info(f'Médico: {input_name}')
                st.info(f'Gênero: {input_genero}')
                st.info(f'Telefone: {input_telefone}')
                st.info(f'Email: {input_email}')
                st.info(f'Código da Especialidade: {input_CodEspec}')
                
            elif len(input_CodMed) < 7:
                st.warning('Você deve inserir 7 caracteres para o Código do Médico')
            elif len(input_name) == 0:
                st.warning('Você deve inserir o Nome do Médico')

        tabela_bd('Médicos', 'medico')
        
    with aba2:

        st.subheader("Cadastrar Especilidade")

        with st.form(key="include_especialidade"):
            input_CodEsp = st.text_input(label="Insira o Código da Especialidade", help = "insira um valor númerico de 7 digitos", max_chars = 7)
            input_name = st.text_input(label="Insira o nome da Especialidade", max_chars = 15)
            input_descricao = st.text_input(label="Descrição da Especialidade")
            input_button_submit = st.form_submit_button('Cadastrar')

        if input_button_submit:
            if len(input_CodEsp) == 7 and len(input_name) and len(input_descricao)!= 0:
                query = "INSERT INTO especialidade (CodEspec, NomeEspec, Descricao) VALUES (%s, %s, %s)"
                values = (input_CodEsp, input_name, input_descricao)
                cursor.execute(query, values)
                cnx.commit()
                cursor.close()
                cnx.close()

                st.success("Especialidade adicionada com sucesso!")
                st.info(f'Código Especialidade: {input_CodEsp}')
                st.info(f'Nome: {input_name}')
                st.info(f'Descrição: {input_descricao}')
                
            elif len(input_CodEsp) < 7:
                st.warning('Você deve inserir 7 caracteres para o Código da Especialidade')
            elif len(input_name) == 0:
                st.warning('Você deve inserir o Nome da Especialidade')
            elif len(input_descricao) == 0:
                st.warning('Você deve inserir uma Descrição para a Especialidade')
        tabela_bd('Especialidade', 'especialidade')
