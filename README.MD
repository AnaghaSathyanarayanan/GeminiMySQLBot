# GeminiMySQLBot

A Streamlit and AI-based web application that allows users to query a MySQL database using **natural language prompts**.  
It integrates **Gemini API** for converting user input into SQL and executes those queries on a **XAMPP-based MySQL** database.

---

## 🚀 Features

- 💬 Natural language to SQL using Gemini API
- 🗃️ Real-time MySQL database integration via XAMPP
- 🖥️ User-friendly Streamlit interface
- 🧪 Built-in unit tests for Gemini API and DB connection
- 🔐 Secure `.env` support for API keys and DB credentials

---

## 📁 Project Structure

```
├── app.py                 # Streamlit app entry point
├── database.py           # MySQL database connection logic
├── gemini_helper.py      # Handles Gemini API communication
├── ui.py                 # Streamlit UI components
├── .env                  # Stores API keys and DB config (not committed)
├── requirements.txt      # Python dependencies
├── resources/
│   └── sql.txt           # SQL examples and saved queries
├── tests/
│   ├── __init__.py
│   ├── list_models.py
│   ├── test_db_connection.py
│   └── test_gemini.py
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/AnaghaSathyanarayanan/GeminiMySQLBot
cd GeminiMySQLBot
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

### 4. Start XAMPP and Create the Database

#### ✅ Open XAMPP Control Panel
- Start **Apache** and **MySQL** modules

#### ✅ Create a MySQL Database
1. Go to your browser and open **phpMyAdmin** via `http://localhost/phpmyadmin`
2. Click on **"New"** in the left sidebar
3. Name your database (e.g., `gemini_db`)
4. Create required tables (manually or via SQL script)

---

### 5. Configure `.env` File
Create a `.env` file in the root folder:

```
GEMINI_API_KEY=your_gemini_api_key
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=
DB_NAME=gemini_db
```

> ⚠️ Replace `your_gemini_api_key` and `DB_NAME` with your actual credentials.

---

### 6. Start the Streamlit App
```bash
streamlit run app.py
```

---

## ✅ Usage

1. Launch the app in your browser (usually at `http://localhost:8501`)
2. Enter a **natural language prompt**, such as:
   > "Show me the list of students enrolled in 2024"
3. Gemini API will convert your prompt to SQL, execute it, and display results.

---

## 🧪 Testing

To run unit tests:

```bash
pytest tests/
```

---

## 📌 Dependencies

- Python 3.x
- Streamlit
- google-generativeai (for Gemini)
- mysql-connector-python
- python-dotenv
- pytest

---

## 📄 License

MIT License

---

## ✨ Credits

Created by **AnaghaSathyanarayanan**  
Powered by **Gemini API**, **MySQL**, and **Streamlit**
