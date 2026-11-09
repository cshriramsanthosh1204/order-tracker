import sqlite3

conn = sqlite3.connect("orders.db")   # creates the file if it doesn't exist

conn.execute("DROP TABLE IF EXISTS orders")
conn.execute("""
    CREATE TABLE orders (
        order_id TEXT PRIMARY KEY,
        item TEXT,
        status TEXT
    )
""")

conn.executemany(
    "INSERT INTO orders VALUES (?, ?, ?)",
    [
        ("BT1042", "boAt Airdopes 141", "Packed"),
        ("BT1043", "boAt Rockerz 450", "Out for delivery"),
        ("BT1044", "boAt Stone 352", "Delivered"),
    ],
)

conn.commit()   # saves the changes permanently
conn.close()