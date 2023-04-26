import streamlit as st
from funcs import *
import time

def atualizar():

    st.header('Operação de Atualização')
    st.markdown("---")

    aba1, aba2 = st.tabs(["Medico", "Especialidade"])

    with aba1:

        coluna1, coluna2 = st.columns(2)

        with coluna1:
        
            def atualizar_medico(input_field, input_value, input_Cod):
                query = f"UPDATE medico SET {input_field} = %s WHERE CodMed = %s"
                values = (input_value, input_Cod)
                cursor.execute(query, values)
                cnx.commit()
                cursor.close()
                cnx.close()
                st.success("Médico alterado com sucesso!")
                st.info(f'Código do Médico: {input_Cod}')
                st.info(f'Campo alterado: {input_field}')
                st.info(f'Novo valor: {input_value}')

                st.warning('Atualizando página')
                with st.spinner('Aguarde a atualização da página para efetuar uma nova operação'):
                    time.sleep(10)
                st.experimental_rerun()

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
                input_field = st.selectbox(label="Selecione o campo a ser alterado", options=["Código do Médico","Nome do Médico", "Gênero", "Telefone", "Email", "Código da especialidade"])
                input_value = st.text_input(label="Insira o novo valor")
                input_button_submit = st.form_submit_button('Atualizar')

            if input_button_submit:

                if input_field == "Código do Médico":
                    input_field = "CodMed"

                    if len(input_value) == 7:
                        atualizar_medico(input_field, input_value, input_Cod)
                    elif len(input_value) != 7:
                        st.warning("Insira 7 caracteres para o Código Médico")

                if input_field == "Nome do Médico":
                    input_field = "NomeMed"

                    if len(input_value) > 0 and len(input_value) <= 40:
                        atualizar_medico(input_field, input_value, input_Cod)
                    elif len(input_value) == 0:
                        st.warning('Você deve inserir o Nome do Médico')
                    elif len(input_value) > 15:
                        st.warning('Você deve inserir até no máximo 40 caracteres para o Nome do Médico')

                if input_field == "Gênero":
                    input_field = "Genero"
                    input_value = input_value.upper()

                    if input_value == 'M' or input_value == 'F' or len(input_value) == 0:
                        atualizar_medico(input_field, input_value, input_Cod)
                    elif input_value != 'M' or input_value != 'F':
                        st.warning('Você deve abreviar o gênero apenas para as letras "M" ou "F"')

                if input_field == "Telefone":

                    if len(input_value) <= 16:
                        atualizar_medico(input_field, input_value, input_Cod)
                    elif len(input_value) > 16:
                        st.warning("Insira no máximo 16 caracteres para o Número do Telefone")

                if input_field == "Email":

                    if len(input_value) > 0 and len(input_value) <=40:
                        atualizar_medico(input_field, input_value, input_Cod)
                    elif len(input_value) == 0:
                        st.warning('Você deve inserir o Email')
                    elif len(input_value) > 40:
                        st.warning('Você deve inserir até no máximo 40 caracteres para o Email')

                if input_field == "Código da especialidade":
                    input_field = "CodEspec"

                    if len(input_value) == 7:
                        atualizar_medico(input_field, input_value, input_Cod)
                    elif len(input_value) != 7:
                        st.warning("Insira 7 caracteres para o Código da Especialidade")

        with coluna2:
            tabela_bd('Médicos', 'medico')

    with aba2:

        coluna1, coluna2 = st.columns(2)

        with coluna1:

            def atualizar_especialidade(input_field, input_value, input_Cod):
                query = f"UPDATE especialidade SET {input_field} = %s WHERE CodEspec = %s"
                values = (input_value, input_Cod)
                cursor.execute(query, values)
                cnx.commit()
                cursor.close()
                cnx.close()
                st.success(f'Especialidade {input_Cod} alterada com sucesso!')
                st.info(f'Campo alterado: {input_field}')
                st.info(f'Novo valor: {input_value}')

                st.warning('Atualizando página')
                with st.spinner('Aguarde a atualização da página para efetuar uma nova operação'):
                    time.sleep(10)
                st.experimental_rerun()

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
                input_field = st.selectbox(label="Selecione o campo a ser alterado", options=["Código da especialidade","Nome da especialidade", "Descrição"])
                input_value = st.text_input(label="Insira o novo valor")
                input_button_submit = st.form_submit_button('Atualizar')

            if input_button_submit:
                if input_field == "Código da especialidade":
                    input_field = "CodEspec"

                    if len(input_value) == 7:
                        atualizar_especialidade(input_field, input_value, input_Cod)
                    elif len(input_value) != 7:
                        st.warning("Insira 7 caracteres para o Código da Especialidade")

                if input_field == "Nome da especialidade":
                    input_field = "NomeEspec"

                    if len(input_value) > 0 and len(input_value) <=15:
                        atualizar_especialidade(input_field, input_value, input_Cod)
                    elif len(input_value) == 0:
                        st.warning('Você deve inserir o Nome da Especialidade')
                    elif len(input_value) > 15:
                        st.warning('Você deve inserir até no máximo 15 caracteres para o Nome da Especialidade')

                if input_field == "Descrição":
                    input_field = "Descricao"

                    if len(input_value) > 0:
                        atualizar_especialidade(input_field, input_value, input_Cod)
                    elif len(input_value) == 0:
                        st.warning('Você deve inserir uma Descrição para a Especialidade')

        with coluna2:
            tabela_bd('Especialidade', 'especialidade')
