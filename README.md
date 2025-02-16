# project structure MincaAI Agent App

app/
    -`.env`
    -`requirements.txt`
    -`README.md`
    -`app.py`
    -`config.py`
    -`.streamlit/config.toml`
 tools/
        -`__init__.py`
        -`research_tools.py`
 agent/
        -`__init__.py`
        -`agent_setup.py`

## Installation
1. git clone repo : https://github.com/Haole3435/MincaAI.git
2. Crate virtual env
- Using Python Venv
```
python -m venv MincaAI
```
```
python MincaAI/bin/activate
```
- Using conda 
In case, your computer already have Conda or miniconda 
```
- conda create -n MincaAI
```
```
- conda activate MincaAI
```
3. Install dependencies:
```
pip install -r requirements.txt
```

## Runing on shell
```
python app.py
```

## Runing on Web Interface
```
streamlit run web_ui.py
```

- Note : I have attached the OpenAI key and PERPLEXITY key at the bottom of the Word report file.