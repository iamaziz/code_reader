virtualenv .env -p python3
source .env/bin/activate
pip install -r requirements.txt
streamlit run app.py