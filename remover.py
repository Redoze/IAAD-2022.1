import streamlit as st
from funcs import *
import time

def remover():

    st.header('Operação de Remoção')
    st.markdown("---")

    aba1, aba2 = st.tabs(["Médico", "Especialidade"])
                
    with aba1:

        coluna1, coluna2 = st.columns(2)

        with coluna1:
            st.subheader('Remover Médico')

            cnx = create_connection()
            cursor = cnx.cursor()
            cursor.execute("SELECT CodMed FROM medico")
            resultado = cursor.fetchall()
            valores = []
            
            with st.form(key="Remover_medico"):
                valores = [i[0] for i in resultado]
                input_CodMed = st.selectbox(label="Escolha o Código do Médico", options = valores)
                input_button_submit = st.form_submit_button('Remover')

            if input_button_submit:

                cursor.execute("DELETE FROM medico WHERE CodMed =" + input_CodMed)
                cnx.commit()
                cursor.close()
                cnx.close()
                st.success(f"Médico {input_CodMed} removido com sucesso!")

                st.warning('Atualizando página')
                with st.spinner('Aguarde a atualização da página para efetuar uma nova operação'):
                    time.sleep(10)
                st.experimental_rerun()

        with coluna2:
            tabela_bd('Médicos', 'medico')

    with aba2:

        coluna1, coluna2 = st.columns(2)
    
        with coluna1:

            st.subheader("Remover Especilidade")

            cnx = create_connection()
            cursor = cnx.cursor()
            cursor.execute("SELECT CodEspec FROM especialidade")
            resultado = cursor.fetchall()
            valores = []

            with st.form(key="Remover_especialidade"):
                valores = [i[0] for i in resultado]
                input_CodEsp = st.selectbox(label="Escolha o Código da Especialidade", options = valores)
                input_button_submit = st.form_submit_button('Remover')

            if input_button_submit:

                cursor.execute("DELETE FROM especialidade WHERE CodEspec =" + input_CodEsp)
                cnx.commit()
                cursor.close()
                st.success(f"Especialidade {input_CodEsp} removida com sucesso!")

                st.warning('Atualizando página')
                with st.spinner('Aguarde a atualização da página para efetuar uma nova operação'):
                    time.sleep(10)
                st.experimental_rerun()

        with coluna2:
            tabela_bd('Especialidade', 'especialidade')
