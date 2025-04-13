import pymysql

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'university',
    'port': 3306
}

try:
    print("Attempting to connect using pymysql...")
    conn = pymysql.connect(**db_config)
    print("✅ Successfully connected using pymysql!")
except Exception as e:
    print(f"❌ pymysql error: {e}")
