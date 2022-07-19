from glob import glob

import streamlit as st


# -- config page
def config():
    # st.set_page_config(layout='wide')
    hide_streamlit_style = """
    					<style>
    					#MainMenu {visibility: hidden;}
    					footer {visibility: hidden;}
    					</style>
    					"""
    title = """ 
    <sub>[source code](https://github.com/keon/algorithms)</sub>
    """
    header = hide_streamlit_style + title
    st.markdown(header, unsafe_allow_html=True)


# -- scan files
execlude = ("__init__.py", "algorithms/tests/", "docs/", "__", "app.py")
files = [
    f for f in glob("algorithms/**/*.py", recursive=True) if not f.startswith(execlude)
]
files = [f for f in files if not "__" in f and not "setup.py" in f]


# -- display contents
@st.cache(suppress_st_warning=True)
def render_file(f):
    with open(f, "r") as f_:
        code = f_.read()
    with st.expander(f"{f}"):
        st.code(code, language="python")


def main():
    config()
    topics = sorted(set([n.split("/")[2] for n in files]))
    tabs = st.tabs(topics)
    for tab, tab_name in zip(tabs, topics):
        for f in files:
            file_topic = f.split("/")[2]
            if file_topic == tab_name:
                with tab:
                    render_file(f)


if __name__ == "__main__":
    main()
