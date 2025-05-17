import streamlit as st
from biblioteca import cadastroAlunos

with st.form("my_form",clear_on_submit=True):
    st.text_input("Digite o id do aluno", key="id")
    st.text_input("Digite o nome do aluno", key="name")
    st.text_input("Digite a data de nascimento do aluno", key="dataDeNascimento")
    st.text_input("Digite o email do aluno", key="email")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        # st.write("slider", slider_val, "checkbox", checkbox_val)
        cadastrado = cadastroAlunos(st.session_state.id,st.session_state.name,st.session_state.dataDeNascimento,st.session_state.email)

        if not cadastrado:
            st.write("Erro! Id já em uso!")
        else:
            st.write("Aluno cadastrado com sucesso!")
