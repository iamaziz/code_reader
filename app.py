import streamlit as st

st.set_page_config(layout="wide")


def _init_source_code_clone():
    import os

    if "keras" in os.listdir():
        return
    import subprocess
    subprocess.call(['sh', './init.sh'])


_init_source_code_clone()


def header():
    title = """
    # _Code Reader_
    **JSMTC**: _**J**ust **S**how **M**e **T**he **C**ode_
    <sup>_Read source code like reading a book_.</sup>
    """
    st.markdown(title, unsafe_allow_html=True)


st1, st2 = st.columns(2) #, gap="large")
with st2:
    header()
with st1:
    CHOICES = ["", "Algorithms (CS fundamentals)", "Keras", "PyTorch Tutorial", "Scikit Learn"]
    choice = st.selectbox(
        "Show Source Code To Read", CHOICES
    )
if choice:
    from app_keras import main as keras_app
    from app_pytorch_tut import main as torch_app
    from app_algorithms import main as algorithms_app
    from app_sickit import main as scikitlearn_app

    c = choice.lower()
    if c.startswith("keras"):
        keras_app()
    if c.startswith("pytorch"):
        torch_app()
    if c.startswith("algorithms"):
        algorithms_app()
    if c.startswith("scikit"):
        scikitlearn_app()

# keras_app()
# torch_app()
# algorithms_app()
