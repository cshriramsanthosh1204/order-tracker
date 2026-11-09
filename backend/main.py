import sqlite3
from fastapi import FastAPI, HTTPException

app = FastAPI()

def get_connection():
    conn = sqlite3.connect("orders.db")
    conn.row_factory = sqlite3.Row   # lets us read columns by name
    return conn

@app.get("/orders/{order_id}")
def get_order(order_id: str):
    conn = get_connection()
    query = "SELECT order_id, item, status FROM orders where order_id =?"  # <-- YOUR PART: replace the dots with a SQL query
    row = conn.execute(query, (order_id.upper(),)).fetchone()
    conn.close()
    if row is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return dict(row)