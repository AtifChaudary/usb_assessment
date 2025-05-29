# Buckzy API Integration

This project is a Flask-based implementation for integrating the following Buckzy API services:

- Entity Documents Management
- Customer Management (Individual & Corporate)
- SPOT Rates
- Buckzy Account Management
- Payout Transactions

---

## 📁 Project Structure
```
project_root/
├── app/
│   ├── routes/                 # Flask route handlers
│   ├── services/               # API service layer
│   ├── serializers/            # Input validation with marshmallow
│   └── utils/                  # Auth & error handling
├── config.py                   # Buckzy API configuration
├── run.py                      # Application entry point
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository & navigate into it
```
git clone https://github.com/AtifChaudary/usb_assessment.git
cd usb_assessment
```

### 2. Create virtual environment (optional but recommended)
```
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Configure your Buckzy API credentials
Edit `config.py` and fill in:
```python
API_KEY = 'your_api_key_here'
AUTH_HOST = 'your_auth_host'
API_HOST = 'your_api_host'
CLIENT_ID = 'your_client_id_here'
CLIENT_SECRET = 'your_client_secret_here'
USERNAME = 'your_username_here'
PASSWORD = 'your_password_here'
```

### 5. Run the Flask server
```
python run.py or flask run
```

The API will start at: `http://localhost:5001/`

---

## 🧪 Example API Calls

### POST /customers
Create a customer.

### GET /spot-rates?fromCurrency=USD&toCurrency=INR
Fetch real-time SPOT rate.

### GET /accounts/<client_id>
Retrieve Buckzy account details.

### POST /entities/<customer_id>
Add an entity to a registered customer.

### POST /payouts
Initiate a payout transaction.

---