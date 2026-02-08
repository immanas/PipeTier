from flask import Flask, request, jsonify
import mysql.connector
import time

app = Flask(__name__)

# Retry loop because DB may start after Flask
for i in range(10):
    try:
        db = mysql.connector.connect(
            host="mysql",          # IMPORTANT: service name, not localhost
            user="root",
            password="Manas@123",
            database="pipetier_db"
        )
        break
    except:
        time.sleep(3)

cursor = db.cursor(dictionary=True)

@app.route("/")
def health():
    return "PipeTier backend running"

@app.route("/records", methods=["POST"])
def add_record():
    data = request.json
    content = data.get("content")

    cursor.execute(
        "INSERT INTO records (content) VALUES (%s)",
        (content,)
    )
    db.commit()
    return {"message": "record added"}, 201

@app.route("/records", methods=["GET"])
def get_records():
    cursor.execute("SELECT * FROM records")
    return jsonify(cursor.fetchall())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
