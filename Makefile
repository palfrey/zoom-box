requirements.txt: requirements.in
	./uv pip compile requirements.in -o requirements.txt

.venv/bin/python:
	./uv venv

install: .venv/bin/python
	./uv pip install -r requirements.txt

zoom-install: install
	cd paracrine && ../.venv/bin/python main.py -i ./box/inventory.yaml --apply
