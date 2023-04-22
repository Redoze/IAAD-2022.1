import streamlit as st
from consultar import *
from cadastrar import *
from atualizar import *
from remover import *
from criar import *
try:
    st.set_page_config(
        page_title="Operações CRUD",
        page_icon="📄"
    )

    def main():
        
            st.sidebar.title('Operações CRUD')
            st.sidebar.markdown("---")
            
            tabs = ["Consultar", "Cadastrar", "Atualizar", "Remover", "Criar"]
            selected_tab = st.sidebar.radio("Selecione a operação que deseja realizar", tabs)

            if selected_tab == "Consultar":
                consultar()
            elif selected_tab == "Cadastrar":
                cadastrar()
            elif selected_tab == "Remover":
                remover()
            elif selected_tab == "Atualizar":
                atualizar()
            elif selected_tab == "Criar":
                criar()

    if __name__ == "__main__":
        main()

except st.StreamlitAPIException:
    st.warning('Por favor, atualize a página')
