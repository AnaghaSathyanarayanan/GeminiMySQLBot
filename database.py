import pymysql
from dotenv import load_dotenv
import os

# Load secrets from .env file
load_dotenv()

# MySQL credentials from .env
db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME'),
    'port': 3306
}

# Connect to MySQL
def get_connection():
    return pymysql.connect(**db_config)

# Function to fetch student and course details
def fetch_student_course_data():
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        SELECT s.student_id, s.first_name, s.last_name, s.email, c.course_name
        FROM students s
        JOIN courses c ON s.course_id = c.course_id
    """
    cursor.execute(query)
    return cursor.fetchall()
