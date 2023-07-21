import streamlit as st
import os
import base64

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
    # st.title("DataChatter: Connecting Databases with Chat AI")
    
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

    # Dropdown list to select the database
    database_options = ["SQL Database", "CSV Files", "Excel Sheets", "PDF Documents"]
    selected_database = st.selectbox("Select Database:", database_options)

    # Dropdown list to select the specific file, sheet, or SQL database
    selected_item = ""
    if selected_database == "CSV Files":
        csv_files = ["file1.csv", "file2.csv", "file3.csv"]  # Replace with your actual CSV files
        selected_item = st.selectbox("Select CSV File:", csv_files)
    elif selected_database == "Excel Sheets":
        excel_sheets = ["sheet1", "sheet2", "sheet3"]  # Replace with your actual Excel sheets
        selected_item = st.selectbox("Select Excel Sheet:", excel_sheets)
    elif selected_database == "PDF Documents":
        pdf_files = ["doc1.pdf", "doc2.pdf", "doc3.pdf"]  # Replace with your actual PDF files
        selected_item = st.selectbox("Select PDF Document:", pdf_files)
    elif selected_database == "SQL Database":
        # Add your logic to get the list of available SQL databases
        sql_databases = ["db1", "db2", "db3"]  # Replace with your actual SQL databases
        selected_item = st.selectbox("Select SQL Database:", sql_databases)

    # Show available data for users to query on and corresponding data formats
    st.markdown("<p class='header'>Available Data</p>", unsafe_allow_html=True)
    st.markdown(f"<p class='subheader'>in {selected_database} - {selected_item}:</p>", unsafe_allow_html=True)
    if selected_database == "SQL Database":
        st.markdown("<p class='info'>You can query data from your SQL database using SQL queries.</p>", unsafe_allow_html=True)
        st.markdown("<p class='info'>Example Query: Display data from table table_name where condition;</p>", unsafe_allow_html=True)
    elif selected_database == "CSV Files":
        st.markdown("<p class='info'>You can query data from CSV files using simple filtering.</p>", unsafe_allow_html=True)
        st.markdown("<p class='info'>Example Query: Show me data from 'file.csv' where column='value';</p>", unsafe_allow_html=True)
    elif selected_database == "Excel Sheets":
        st.markdown("<p class='info'>You can query data from Excel sheets using column filtering.</p>", unsafe_allow_html=True)
        st.markdown("<p class='info'>Example Query: Show me data from 'sheet_name' where column='value';</p>", unsafe_allow_html=True)
    else:
        st.markdown("<p class='info'>You can query data from structured PDFs using specific keywords.</p>", unsafe_allow_html=True)
        st.markdown("<p class='info'>Example Query: Show me data from 'file.pdf' where keyword='value';</p>", unsafe_allow_html=True)

# Text input for user query
    user_query = st.text_input("Enter your question here:", key="user_query")

    # Button to submit the user query
    send_button = st.button("Send", key="send_button")
    if send_button or (user_query and st.session_state.user_query_enter):
        st.session_state.user_query_enter = False
        if user_query.strip() != "":
            # Process user query and get the response
            response = process_user_query(selected_database, selected_item, user_query)
            st.markdown("<p class='header'>Assistant:</p>", unsafe_allow_html=True)
            st.markdown(f"<p class='info'>{response}</p>", unsafe_allow_html=True)
        else:
            st.warning("Please enter a valid query.")
    

if __name__ == "__main__":
    main()
