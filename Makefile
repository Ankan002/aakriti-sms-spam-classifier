install-extra-deps:
	python3 config/deps_installer.py

dev:
	python3 config/deps_installer.py && streamlit run app.py