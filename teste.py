import streamlit as st

st.title('Teste')

st.header('Texto')
st.text('Testando o Streamlit')

st.header('Botão')
st.button('Botão')

st.header('Checkbox')
st.checkbox('Checkbox')

st.header('Radio')
st.radio('Escolha', ('Opção 1', 'Opção 2'))

st.header('Selectbox')
st.selectbox('Escolha', ('Opção 1', 'Opção 2'))

st.image('images/teste.jpg')
