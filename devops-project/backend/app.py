from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

DB_CONFIG = {
        'host' : 'postgres',
        'database' : 'devopsdb',
        'user' : 'postgres',
        'password' : 'password'

}
@app.route('/')
def home():
    return jsonify({'message':'Backend Running Successfully' })
@app.route('/health')
def health():
    return jsonify({'status':'healthy'})

@app.route('/products')
def products():
    conn= psycopg2.connect(**DB_CONFIG)
    cur=conn.cursor()

    cur.execute('SELECT * FROM products;')
    rows=cur.fetchall()

    result = []

    for row in rows:
        result.append({
            'id':row[0],
            'name':row[1],
            'price':row[2]
            })

    cur.close()
    conn.close()

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=5000)
