# 🚨 Incident Management System 🚨

### 📝 Overview
The **Incident Management System** is a web-based tool built with Python's Flask framework. It allows users to track, resolve, and monitor incidents across an organization's infrastructure. The system also integrates a 🤖 chatbot for automated incident queries, making it easier for users to interact with the platform and get real-time updates. 

### ✨ Features
- 🛠️ **Incident tracking and resolution**: Record, update, and monitor incidents.
- 🤖 **Chatbot integration**: An interactive chatbot to handle user queries and provide updates on incidents.
- 📊 **Web dashboard**: A user-friendly dashboard for tracking incidents and viewing reports.
- 💾 **MySQL database**: For securely storing incident details.
- 🧪 **Automated testing with Selenium**: Ensures the system's stability and reliability.

### 🛠️ Technologies Used
- **Backend**: 🐍 Python, Flask
- **Frontend**: 🎨 HTML, CSS, JavaScript (Flask templates)
- **Database**: 🗄️ MySQL
- **Testing**: 🧪 Selenium (for automated browser testing)
- **Version Control**: 🌀 Git
- **Deployment**: 🚀 GitHub

### 🔧 Prerequisites
Make sure you have the following installed:
- 🐍 Python 3.x
- 🗄️ MySQL
- ⚙️ Flask
- 🧪 Selenium
- 🌐 ChromeDriver (for Selenium)
- 🌀 Git

### 🚀 Installation Guide
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AishikDasgupta/incident-management-system.git
   cd incident-management-system
   ```

2. **Set up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup**:
   - Install MySQL and create a database:
     ```sql
     CREATE DATABASE incident_db;
     ```
   - Update the database configurations in `config.py`:
     ```python
     SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/incident_db'
     ```

5. **Run the Application**:
   ```bash
   flask run
   ```

6. **Open the App**:
   Navigate to `🌐 http://127.0.0.1:5000/` in your browser to access the system.

### 🤖 Chatbot
The chatbot is integrated into the system and provides real-time assistance for incident queries. It uses basic natural language processing (NLP) techniques and responds to user queries based on incident status.

### 🧪 Automated Testing
This project includes automated testing for the web interface using Selenium.

To run the Selenium tests:
1. Install ChromeDriver (compatible with your Chrome version).
2. Place the `chromedriver` executable in your project directory.
3. Run the tests:
   ```bash
   python -m unittest tests/test_incident.py
   ```

### 🤝 Contributing
Feel free to fork this repository and submit pull requests. All contributions are welcome!

### 📜 License
This project is licensed under the MIT License.
