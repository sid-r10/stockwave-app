# 🚀 StockWave.ai — Backend API

StockWave.ai is a full-stack stock analysis platform that allows users to track stocks, manage watchlists, and receive alerts based on market movements.

This repository contains the **backend API** built with FastAPI.

---

## 🧰 Tech Stack

* **Python 3.12+**
* **FastAPI**
* **Uvicorn**
* **AWS DynamoDB** (planned)
* **JWT Authentication** (planned)

---

## 📁 Project Structure

```
stockwave-backend/
├── app/
│   ├── main.py
│   ├── api/
│   ├── services/
│   ├── db/
│   ├── schemas/
│   └── core/
├── venv/
├── requirements.txt
└── .env
```

---

## ⚙️ Prerequisites

Make sure you have installed:

* Python 3.12+
* pip (comes with Python)

---

## 🧪 Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/<your-username>/stockwave-backend.git
cd stockwave-backend
```

---

### 2. Create and activate virtual environment

#### Mac/Linux:

```
python3 -m venv venv
source venv/bin/activate
```

#### Windows:

```
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Run the application

```
uvicorn app.main:app --reload
```

---

## 🌐 API Access

Once the server is running:

* Base URL:
  http://127.0.0.1:8000/

* Interactive API Docs (Swagger):
  http://127.0.0.1:8000/docs

* Alternative Docs (ReDoc):
  http://127.0.0.1:8000/redoc

---

## 🧪 Sample Endpoint

```
GET /
```

Response:

```json
{
  "message": "👋 Welcome to StockWave.ai API",
  "status": "running"
}
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory.

Example:

```
JWT_SECRET=your_secret_key
AWS_ACCESS_KEY=your_access_key
AWS_SECRET_KEY=your_secret_key
STOCK_API_KEY=your_api_key
```

---

## 🚧 Roadmap

* [ ] User Authentication (JWT)
* [ ] Stock Data Integration
* [ ] Watchlist Feature
* [ ] Alerts System (Email/WhatsApp)
* [ ] AWS DynamoDB Integration
* [ ] Deployment on AWS Free Tier

---

## 🤝 Contributing

This is a personal project, but suggestions and feedback are welcome.

---

## 📄 License

This project is for educational and portfolio purposes.
