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


def main(URL, TARGET_DIR):
    files = scan_files(TARGET_DIR)

    st1, st2 = st.columns(2)
    with st2:
        matched_files = _display_filtered_files(files)  # if search_enabled else None
    if matched_files:
        for f in matched_files:
            render_file(f)
        config(URL)
        st.stop()

    topics = sorted(set([n.split("/")[2] for n in files]))
    tabs = st.tabs(topics)
    for tab, tab_name in zip(tabs, topics):
        for f in sorted(files):
            file_topic = f.split("/")[2]
            if file_topic == tab_name:
                with tab:
                    render_file(f)

    config(URL)


if __name__ == "__main__":
    # repos params
    URL = "https://github.com/scikit-learn/scikit-learn"
    TARGET_DIR = "scikit-learn/sklearn"

    main(URL, TARGET_DIR)
