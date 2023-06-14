freeze:
	pip3 freeze > requirements.txt 

start:
	uvicorn main:app --reload