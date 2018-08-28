"""
curl -X POST -d "username=admin&password=password123" http://localhost:8000/api-token-auth/

curl -X POST -H "Content-Type: application/json" -d '{"username":"mustafa","password":"fatma1963"}' http://localhost:8000/auth/serializers/api-token-auth/

curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJleHAiOjE1MzQ0ODY4NjgsInVzZXJuYW1lIjoibXVzdGFmYSIsImVtYWlsIjoiIn0.Knu-swHRf9cBpoTUBFWs1n19dcNVkeGBScf_E4fDeco" http://localhost:8000/property/serializers/list/?user=1&permission=3

"""
