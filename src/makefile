UI_FILES	:= main_window parameters

compiling:
	for ui_file in $(UI_FILES); do pyuic5 -x ./UiForm/$${ui_file}.ui -o ./PyUi/$${ui_file}.py; done

run:
	python3 main.py