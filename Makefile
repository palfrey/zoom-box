requirements.txt: requirements.in
	./uv pip compile requirements.in -o requirements.txt

install:
	./uv pip install -r requirements.txt
