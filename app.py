from flask import Flask, request, render_template, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'yourpassword'
app.config['MYSQL_DB'] = 'incident_management'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

# Add a route to log incidents
@app.route('/log', methods=['POST'])
def log_incident():
    if request.method == 'POST':
        incident = request.form['incident']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO incidents(description) VALUES (%s)", [incident])
        mysql.connection.commit()
        cur.close()
        return jsonify({'message': 'Incident logged successfully!'})

if __name__ == "__main__":
    app.run(debug=True)
