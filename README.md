# metaphor-playground

I made a quick query conversion script that makes some subset of queries work better in the metaphor api

## setup

python version 3.10.8

install dependencies

```pip install -r requirements.txt```

download nlp model from spacy

```python -m spacy download en_core_web_sm```


## usage

```python main.py <metaphor-api-key> <query>```

It prints the query result directly into the standard output.
