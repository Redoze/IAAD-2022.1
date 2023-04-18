import streamlit as st;
import mysql.connector
import pandas as pd

st.set_page_config(
    page_title="Operações CRUD",
    page_icon="📄",
    layout="centered",
)

# Função para criar uma conexão com o banco de dados
def create_connection():                                        #########################################################################
    cnx = mysql.connector.connect(user='root',                  ########## ADICIONE SEUS DADOS DE CONEXÃO COM O BANCO DE DADOS ##########
                                password='iaadtask',            #########################################################################
                                host='localhost',
                                database='clinicasmedicas')
    return cnx

st.title('Operações CRUD')
st.markdown("---")

def tab1():
    aba, aba2, aba4 = st.tabs(["Clínica", "Médico","Especialidade"]) #aba3, ... "Paciente"
    with aba:
     
        st.subheader('Cadastrar clínica')

        with st.form(key="include_clínica"):
            input_CodCli = st.text_input(label="Insira o Código da Clínica")
            input_name = st.text_input(label="Insira o nome da Clínica")
            input_endereco = st.text_input(label="Insira o Endereco da Clínica")
            input_telefone = st.text_input(label="Insira o Telefone")
            input_email = st.text_input(label="Insira o Email")
            input_button_submit = st.form_submit_button('Enviar')

        if input_button_submit:
            st.write(f'Código da Clínica: {input_CodCli}')
            st.write(f'Clínica: {input_name}')
            st.write(f'Endereco: {input_endereco}')
            st.write(f'Telefone: {input_telefone}')
            st.write(f'Email: {input_email}')

    with aba2:

        st.subheader("Cadastrar Médico")

        with st.form(key="include_medico"):
            input_CodMed = st.number_input(label="Insira o Código do Médico", format="%d", step=1)
            input_name = st.text_input(label="Insira o nome do Médico")
            input_genero = st.selectbox(label="Selecione seu Gênero", options=["M", "F"])
            input_telefone = st.text_input(label="Insira o Telefone")
            input_email = st.text_input(label="Insira o Email")
            input_CodEspec = st.text_input(label="Insira o Código da Especialidade")
            input_button_submit = st.form_submit_button('Enviar')

        if input_button_submit:
            st.write(f'Código do Médico: {input_CodMed}')
            st.write(f'Médico: {input_name}')
            st.write(f'Gênero: {input_genero}')
            st.write(f'Telefone: {input_telefone}')
            st.write(f'Email: {input_email}')
            st.write(f'Código da Especialidade: {input_CodEspec}')

    # with aba3:

    #     st.subheader("Cadastrar Paciente")

    #     with st.form(key="include_paciente"):
    #         input_Cpfpac = st.number_input(label="Insira o Cpf do Paciente",min_value=0,max_value=99999999999, format="%d", step=1)
    #         input_name = st.text_input(label="Insira o nome do Paciente")
    #         input_nascimento = st.date_input("Digite a data de nascimento:")
    #         input_genero = st.selectbox(label="Selecione o Gênero", options=["M", "F"])
    #         input_telefone = st.number_input(label="Insira o Telefone",format="%d", step=1)
    #         input_email = st.text_input(label="Insira o Email")
    #         input_button_submit = st.form_submit_button(label='Enviar')

    #     if input_button_submit:
    #         st.write(f'Cpf do Paciente : {input_Cpfpac}')
    #         st.write(f'Paciente: {input_name}')
    #         st.write(f'Nacimento: {input_nascimento}')
    #         st.write(f'Gênero: {input_genero}')
    #         st.write(f'Telefone: {input_telefone}')
    #         st.write(f'Email: {input_email}')
             
    with aba4:

        st.subheader("Cadastrar Especilidade")

        with st.form(key="include_especialidade"):
            input_CodEsp = st.number_input(label="Insira o Código da Especialidade", format="%d", step=1)
            input_name = st.text_input(label="Insira o nome da Especialidade")
            input_descricao = st.text_input(label="Descricao da Especialidade")
            input_button_submit = st.form_submit_button('Enviar')

        if input_button_submit:
            st.write(f'Codigo Especialidade: {input_CodEsp}')
            st.write(f'Nome: {input_name}')
            st.write(f'Descricao: {input_descricao}')
                

def tab2():
    aba, aba2, aba4 = st.tabs(["Clínica", "Médico","Especialidade"])#, aba3 .... , "Paciente"
    with aba:
     
        st.subheader('Remover clínica')

        with st.form(key="Remover_clinica"):
            input_CodCli = st.number_input(label="Insira o Código da Clínica", format="%d", step=1)
            input_name = st.text_input(label="Insira o nome da Clínica")
            input_endereco = st.text_input(label="Insira o Endereço da Clínica")
            input_telefone = st.number_input(label="Insira o Telefone",format="%d", step=1)
            input_email = st.text_input(label="Insira o Email")
            input_button_submit = st.form_submit_button('Enviar')

        if input_button_submit:
            st.write(f'Código da Clínica: {input_CodCli}')
            st.write(f'Clínica: {input_name}')
            st.write(f'Endereço: {input_endereco}')
            st.write(f'Telefone: {input_telefone}')
            st.write(f'Email: {input_email}')
            
            # Conecta-se ao banco de dados
            cnx = create_connection()
            cursor = cnx.cursor()
            
            # Busca se há alguma clínica com os valores informados
            query = "SELECT * FROM clinica WHERE CodCli = %s OR NomeCli = %s OR Endereco = %s OR Telefone = %s OR Email = %s"
            values = (input_CodCli, input_name, input_endereco, input_telefone, input_email)
            cursor.execute(query, values)
            
            if cursor.rowcount > 0:  # Se houver, remove a clínica
                query = "DELETE FROM clinica WHERE CodCli = %s"
                cursor.execute(query, (input_CodCli,))
                cnx.commit()
                st.success(f"Clínica removida com sucesso!")
            else:
                st.warning("Não foi possível encontrar uma clínica com os valores informados.")
            
            # Fecha a conexão com o banco de dados
            cursor.close()
            cnx.close()

            
    with aba2:

        st.subheader('Remover Médico')

        with st.form(key="Remover_medico"):
            input_CodMed = st.number_input(label="Insira o Código do Médico", format="%d", step=1)
            input_name = st.text_input(label="Insira o nome do Médico")
            input_genero = st.selectbox(label="Selecione seu Gênero", options=["M", "F"])
            input_telefone = st.text_input(label="Insira o Telefone")
            input_email = st.text_input(label="Insira o Email")
            input_CodEspec = st.text_input(label="Insira o Código da Especialidade")
            input_button_submit = st.form_submit_button('Enviar')

        if input_button_submit:
            st.write(f'Código do Médico: {input_CodMed}')
            st.write(f'Médico: {input_name}')
            st.write(f'Gênero: {input_genero}')
            st.write(f'Telefone: {input_telefone}')
            st.write(f'Email: {input_email}')
            st.write(f'Código da Especialidade: {input_CodEspec}')
            cnx = create_connection()
            cursor = cnx.cursor()
            query = "DELETE FROM medicos WHERE CodMed=%s OR NomeMed=%s OR NomeMed=%s OR NomeMed=%s OR Email=%s OR CodEspec=%s"
            values = (input_CodMed, input_name, input_genero, input_telefone, input_email, input_CodEspec)
            cursor.execute(query, values)
            cnx.commit()
            cursor.close()
            cnx.close()
            st.success("Médico removido com sucesso!")


    # with aba3:

    #     st.subheader("Remover Paciente")

    #     def remover_paciente(cnx, cpf, nome, nascimento, genero, telefone, email):
    #         cursor = cnx.cursor()

    #         # Verifica se algum dos valores está presente no banco de dados
    #         query = f"SELECT * FROM pacientes WHERE cpf={cpf} OR nome='{nome}' OR nascimento='{nascimento}' OR genero='{genero}' OR telefone='{telefone}' OR email='{email}'"
    #         cursor.execute(query)
    #         result = cursor.fetchall()

    #         if len(result) > 0:
    #             # Remove o paciente do banco de dados
    #             query = f"DELETE FROM pacientes WHERE cpf={cpf} OR nome='{nome}' OR nascimento='{nascimento}' OR genero='{genero}' OR telefone='{telefone}' OR email='{email}'"
    #             cursor.execute(query)
    #             cnx.commit()
    #             st.success("Paciente removido com sucesso!")
    #         else:
    #             st.error("Nenhum paciente encontrado com os valores informados.")

    #     with st.form(key="Remover_paciente"):
    #         input_Cpfpac = st.number_input(label="Insira o Cpf do Paciente",min_value=0,max_value=99999999999, format="%d", step=1)
    #         input_name = st.text_input(label="Insira o nome do Paciente")
    #         input_nascimento = st.date_input("Digite a data de nascimento:")
    #         input_genero = st.selectbox(label="Selecione o Gênero", options=["M", "F"])
    #         input_telefone = st.number_input(label="Insira o Telefone",format="%d", step=1)
    #         input_email = st.text_input(label="Insira o Email")
    #         input_button_submit = st.form_submit_button(label='Enviar')

    #     if input_button_submit:
    #         st.write(f'Cpf do Paciente : {input_Cpfpac}')
    #         st.write(f'Paciente: {input_name}')
    #         st.write(f'Nacimento: {input_nascimento}')
    #         st.write(f'Gênero: {input_genero}')
    #         st.write(f'Telefone: {input_telefone}')
    #         st.write(f'Email: {input_email}')
    #         with create_connection() as cnx:
    #             remover_paciente(cnx, input_Cpfpac, input_name, input_nascimento, input_genero, input_telefone, input_email)
             
     
    with aba4:
        def delete_especialidades(cnx, input_CodEsp, input_name, input_descricao):
            cursor = cnx.cursor()
            query = "DELETE FROM especialidades WHERE CodEspec = %s OR NomeEspec = %s OR Descricao = %s"
            values = (input_CodEsp, input_name, input_descricao)
            cursor.execute(query, values)
            cnx.commit()
            cursor.close()
            st.success("Especialidade removida com sucesso!")
        
        st.subheader("Remover Especilidade")

        with st.form(key="Remover_especialidade"):
            input_CodEsp = st.number_input(label="Insira o Código da Especialidade", format="%d", step=1)
            input_name = st.text_input(label="Insira o nome da Especialidade")
            input_descricao = st.text_input(label="Descrição da Especialidade")
            input_button_submit = st.form_submit_button('Enviar')

        if input_button_submit:
            st.write(f'Código Especialidade: {input_CodEsp}')
            st.write(f'Nome: {input_name}')
            st.write(f'Descricao: {input_descricao}')

            with create_connection() as cnx:
                delete_especialidades(cnx, input_CodEsp, input_name, input_descricao)
        
       
    #NO CASO PRECISA DE MAIS UMA TAB AI NO 'def main()' CRIAR UMA TABELA NOVA 


def main():
    cnx=create_connection()    
    cursor=cnx.cursor()

    tabs = ["Cadastrar", "Remover", "Atualizar"]
    selected_tab = st.sidebar.radio("Selecione a Operação", tabs)

    if selected_tab == "Cadastrar":
        tab1()
    elif selected_tab == "Remover":
        tab2()
    elif selected_tab == "Atualizar":
        st.write("TAB 3")

if __name__ == "__main__":
    main()
