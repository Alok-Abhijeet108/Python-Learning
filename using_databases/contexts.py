import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts(name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Alok', 6204655536, '123@test.com')")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Abheer', 7209121344, 'test@123.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")
for row in cursor:
    print(*row, sep="\n", end="\n" + "_" * 20 + "\n\n")

cursor.close()
db.close()
