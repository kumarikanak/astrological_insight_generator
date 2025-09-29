uvicorn main:app --reload
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d "{\"name\":\"Ritika\",\"birth_date\":\"1995-08-20\"}"