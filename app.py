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
    **JSTC**: _**J**ust **S**how **T**he **C**ode_
    <sup>_Read source code like reading a book_.</sup>
    """
    st.markdown(title, unsafe_allow_html=True)


st1, st2 = st.columns(2, gap="large")
with st1:
    header()
with st2:
    CHOICES = ["Algorithms (CS fundamentals)", "AIMA-Python", "Keras", "Transformers", "PyTorch Tutorial", "Lightning (PyTorch)",
               "Scikit Learn", "Requests"]
    choice = st.selectbox(
        "Choose Repo To Read Source Code", CHOICES
    )
if choice:
    from repo_builder import main

    c = choice.lower()
    if c.startswith("keras"):
        main(URL="https://github.com/keras-team/keras", TARGET_DIR="keras")
    if c.startswith("pytorch"):
        main("https://github.com/yunjey/pytorch-tutorial", "pytorch-tutorial")
    if c.startswith("algorithms"):
        main("https://github.com/keon/algorithms", "algorithms")
    if c.startswith("scikit"):
        main("https://github.com/scikit-learn/scikit-learn", "scikit-learn/sklearn")
    if c.startswith("requests"):
        main("https://github.com/psf/requests", "requests", SPLIT_ON=1)
    if c.startswith("transformers"):
        main("https://github.com/huggingface/transformers", "transformers", 1)
    if c.startswith("lightning"):
        main("https://github.com/Lightning-AI/lightning", "lightning", 1)
    if c.startswith("aima"):
        main("https://github.com/aimacode/aima-python", "aima-python", 1)
