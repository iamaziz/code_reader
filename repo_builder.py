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
	> <sub>source: {URL}</sub>
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


def _display_filtered_files(files):
    filter_ = st.text_input("search file names")
    if filter_:
        match = [f for f in files if filter_ in f]
        if len(match) > 0:
            st.markdown(f"> found {len(match)} files")
            return match
        else:
            st.markdown(f"> no match.")
            st.stop()


def main(URL, TARGET_DIR, SPLIT_ON: int = 2):
    files = scan_files(TARGET_DIR)

    st1, st2 = st.columns(2, gap="large")
    with st1:
        config(URL)
    with st2:
        matched_files = _display_filtered_files(files)  # if search_enabled else None
    if matched_files:
        for f in matched_files:
            render_file(f)
        st.stop()

    # rendering all files in st.tabs
    topics = sorted(set([n.split("/")[SPLIT_ON] for n in files]))
    tabs = st.tabs(topics)
    for tab, tab_name in zip(tabs, topics):
        tab_files = [f for f in files if f.split("/")[SPLIT_ON] == tab_name]
        with tab:
            len_files = len(tab_files)
            st.markdown(f">`{len_files} files`") if len_files > 1 else None
            for f in sorted(tab_files):
                render_file(f)


if __name__ == "__main__":
    # repos params
    URL = "https://github.com/scikit-learn/scikit-learn"
    TARGET_DIR = "scikit-learn/sklearn"

    main(URL, TARGET_DIR)
