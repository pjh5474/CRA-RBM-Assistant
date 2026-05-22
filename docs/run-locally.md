## How to Run Locally

### Backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Backend API documentation:

http://localhost:8000/docs

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Environment Variables

Create frontend/.env.local:

NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
