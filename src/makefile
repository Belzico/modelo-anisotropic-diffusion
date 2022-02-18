.PHONY: clean

NAME 	   	:= Anisotropic Diffusion
VERSION		:= 2.0
DEVELOPERS	:= Reinaldo Barrera Travieso, Ariel Plasencia Díaz
COPYRIGHT  	:= Copyright © 2021: $(DEVELOPERS)
UI_FILES	:= main_window parameters present about_authors about_app help

compile:
	for ui_file in $(UI_FILES); do pyuic5 -x ./UiForm/$${ui_file}.ui -o ./PyUi/$${ui_file}.py; done
	python3 Utils/tools.py

run:
	python3 main.py

info: ## Display project description
	@echo "$(NAME) v$(VERSION)"
	@echo "$(COPYRIGHT)"

version: ## Show the project version
	@echo "$(NAME) v$(VERSION)"

clean: ## Remove temporary files
	rm -rf AnisoDiffusion/__pycache__/
	rm -rf PyForm/__pycache__/
	rm -rf PyUi/__pycache__/
	rm -rf qdarkstyle/__pycache__/
	rm -rf qdarkstyle/dark/__pycache__/
	rm -rf qdarkstyle/light/__pycache__/
	rm -rf Utils/__pycache__/

install: ## Install the project dependencies
	pip3 install json
	pip3 install numpy
	pip3 install PyQt5
	pip3 install Pillow
	pip3 install pathlib
	pip3 install pylab-sdk
	pip3 install python-time
	pip3 install python-sympy
	pip3 install python-scipy
	pip3 install opencv-python
	pip3 install python-skimage
	pip3 install python-matplotlib

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'