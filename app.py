import streamlit as st

st.set_page_config(page_title="Code Reader", page_icon="🧐", layout="wide")


def _init_source_code_clone():
    import os

    if "keras" in os.listdir():
        return
    import subprocess

    subprocess.call(["sh", "./init.sh"])


class App:
    def __init__(self):
        _init_source_code_clone()

    @staticmethod
    def header():
        title = """
        # _Code Reader_
        """
        st.markdown(title, unsafe_allow_html=True)
        st.button(label="JSTC: Just Show The Code", help="Read source code like reading a book", disabled=True)

    def run(self):
        st1, st2 = st.columns(2, gap="large")
        with st1:
            self.header()
        with st2:
            msg = "Choose Repo To Read Source Code"
            choice = st.selectbox(msg, options=self._available_repos)
        if choice:
            self.handler(choice)

    @property
    def _available_repos(self):
        return [
            "Algorithms (CS fundamentals)",
            "AIMA-Python",
            "Keras",
            "Transformers",
            "PyTorch Tutorial",
            "Lightning (PyTorch)",
            "Scikit Learn",
            "Requests",
        ]

    @staticmethod
    def handler(choice):
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


if __name__ == "__main__":
    App().run()
