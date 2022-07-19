from glob import glob

import streamlit as st


# -- config page
def config(URL):
    # st.set_page_config(layout='wide')
    hide_streamlit_style = """
						<style>
						#MainMenu {visibility: hidden;}
						footer {visibility: hidden;}
						</style>
						"""
    title = f"""
	<sub>{URL}</sub>
	"""
    header = hide_streamlit_style + title
    st.markdown(header, unsafe_allow_html=True)


# -- scan files
def scan_files(TARGET_DIR):
    execlude = ("__", "app")
    files = [f for f in glob(f"{TARGET_DIR}/**/*.py", recursive=True) if not f.startswith(execlude)]
    files = [f for f in files if not "__" in f and not "setup.py" in f]
    return files


# -- display contents
def render_file(f):
    with open(f, "r") as f_:
        code = f_.read()
    with st.expander(f"{f}"):
        st.code(code, language="python")


def main(URL, TARGET_DIR):
    config(URL)
    files = scan_files(TARGET_DIR)
    topics = sorted(set([n.split("/")[2] for n in files]))
    tabs = st.tabs(topics)
    for tab, tab_name in zip(tabs, topics):
        for f in sorted(files):
            file_topic = f.split("/")[2]
            if file_topic == tab_name:
                with tab:
                    render_file(f)


if __name__ == "__main__":
    # repos params
    URL = "https://github.com/scikit-learn/scikit-learn"
    TARGET_DIR = "scikit-learn/sklearn"

    main(URL, TARGET_DIR)
