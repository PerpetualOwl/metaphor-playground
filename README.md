# metaphor-playground

I made a quick query conversion script that makes some subset of queries work better in the metaphor api

The idea is to convert more traditional search queries like "best boots for january" to "Here are the best boots for january." This could in some cases yield better results from the Metaphor Search engine. This project could be expanded with a model trained on a better dataset and handling more cases more specifically.

## setup

python version 3.10.8

install dependencies

```pip install -r requirements.txt```

download nlp model from spacy

```python -m spacy download en_core_web_sm```


## usage

```python main.py <metaphor-api-key> <query>```

It prints the query result directly into the standard output.
