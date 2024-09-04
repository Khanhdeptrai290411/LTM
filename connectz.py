import mysql.connector

# Kết nối tới MySQL
db_config = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345',
    database='MeetingApp',
)

cursor = db_config.cursor()

# Câu lệnh tạo bảng với IF NOT EXISTS để tránh lỗi nếu bảng đã tồn tại
# Q1 = 'CREATE TABLE IF NOT EXISTS User(user_id INT PRIMARY KEY AUTO_INCREMENT, user_name VARCHAR(50), email VARCHAR(50) UNIQUE, password_hash VARCHAR(255), status BOOLEAN DEFAULT TRUE, created_at DATETIME DEFAULT CURRENT_TIMESTAMP)'
# Q2 = 'CREATE TABLE IF NOT EXISTS `Group` (ID INT PRIMARY KEY AUTO_INCREMENT, group_name VARCHAR(50), created_time DATETIME, creator_id INT, FOREIGN KEY (creator_id) REFERENCES User(user_id))'
# Q3 = 'CREATE TABLE IF NOT EXISTS Participant(ID INT PRIMARY KEY AUTO_INCREMENT, group_id INT, user_id INT, FOREIGN KEY (group_id) REFERENCES `Group`(ID), FOREIGN KEY (user_id) REFERENCES User(user_id))'
# Q4 = 'CREATE TABLE IF NOT EXISTS Message(ID INT PRIMARY KEY AUTO_INCREMENT, id_sender INT, receiver INT, Type VARCHAR(50), content VARCHAR(255), timestamp DATETIME, FOREIGN KEY (id_sender) REFERENCES User(user_id), FOREIGN KEY (receiver) REFERENCES `Group`(ID))'
# Q5 = 'DROP TABLE IF EXISTS Message, Participant, `Group`, User'



# cursor.execute(Q1)
# cursor.execute(Q2)
# cursor.execute(Q3)
# cursor.execute(Q4)
# cursor.execute(Q5)


db_config.commit()
cursor.close()
db_config.close()
