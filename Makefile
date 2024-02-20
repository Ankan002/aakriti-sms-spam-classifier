install-extra-deps:
	python3 config/deps_installer.py

dev:
	python3 config/deps_installer.py && streamlit run app.py

start:
	python3 config/deps_installer.py && streamlit run app.py

dev-api:
	python3 config/deps_installer.py && python3 api.py

start-api:
	python3 config/deps_installer.py && python3 api.py