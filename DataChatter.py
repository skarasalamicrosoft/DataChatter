import streamlit as st
import os
import base64
import subprocess

# Initialize session state variables
if "user_query_enter" not in st.session_state:
    st.session_state.user_query_enter = False

# Define a function to process user queries and return responses
def process_user_query(database, selected_item, query):
    # Placeholder logic to process queries (replace this with your actual implementation)
    response = f"Running query on {database} - {selected_item}: {query}"
    return response

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

def main():
    
    background_image_path = os.path.join(os.getcwd(), "background_image.jpg")

    # Set the title and description for the app
    st.title("DataChatter: Connecting Databases with Chat AI")
    
    set_background('C:\\Users\\skarasala\\source\\repos\\CFS-TRADE-TRDE-Screening\\DataChatter\\DataChatter\\background_image.jpg')
    st.markdown(
        f"""
        <style>
        .reportview-container {{
            background-image: url('{background_image_path}');
            background-size: cover;
            background-repeat: no-repeat;
            height: 100vh;
        }}
        .title {{
            color: #F44336;
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 30px;
        }}
        .header {{
            color: #0B5394;
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 15px;
        }}
        .subheader {{
            color: #0B5394;
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 10px;
        }}
        .info {{
            color: #38761D;
            font-size: 16px;
            font-weight: bold;
            margin-bottom: 5px;
        }}
        .stTextInput, .stSelectbox {{
        color: #2E5266;
        font-weight: bold;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<p class='title'>Welcome to DataChatter!</p>", unsafe_allow_html=True)
    st.markdown("<p class='info'>Ask any question related to your personal data.</p>", unsafe_allow_html=True)
    if st.button("Chat with Website"):
        subprocess.Popen(["streamlit", "run", "chat_with_website.py"])
    if st.button("Chat with PDF"):
        subprocess.Popen(["streamlit", "run", "chat_with_pdf.py"])
    if st.button("Chat with CSV"):
        subprocess.Popen(["streamlit", "run", "csvreader.py"])
    if st.button("Chat with SQL Database"):
        subprocess.Popen(["streamlit", "run", "chat_with_website.py"])
    st.markdown("<p class='info'>Ask any question related to Domain that we have below seamlessly without worrying about selecting/uploading datafiles</p>", unsafe_allow_html=True)
    if st.button("Chat with Investment Banker"):
        subprocess.Popen(["streamlit", "run", "InvestmentBanker.py"])
if __name__ == "__main__":
    main()




