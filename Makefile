requirements.txt: requirements.in
	pip-compile

rebuild:
	sudo nixos-rebuild switch --flake .
