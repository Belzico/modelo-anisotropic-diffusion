.PHONY: clean

NAME 	   	:= Modelos Bordes Imágenes
VERSION		:= 1.0
DEVELOPERS	:= Reinaldo Barrera Travieso, Ariel Plasencia Díaz
COPYRIGHT  	:= Copyright © 2021: $(DEVELOPERS)
UI_FILES	:= main_window parameters

compiling:
	for ui_file in $(UI_FILES); do pyuic5 -x ./UiForm/$${ui_file}.ui -o ./PyUi/$${ui_file}.py; done

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

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'