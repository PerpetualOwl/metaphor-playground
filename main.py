from metaphor_python import Metaphor
import sys
import spacy
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

import en_core_web_sm

nlp = en_core_web_sm.load()

reference_phrases = [
    "Here are the",
    "Here is the",
    "I recommend",
    "Top places to",
    "Worst things to"
]

similarity_threshold = 0.7

def calculate_cosine_similarity(vec1, vec2):
    return cosine_similarity(vec1.reshape(1, -1), vec2.reshape(1, -1))[0][0]

def convert_query(query):
    query_tokens = [token.text for token in nlp(query)]
    query_embeddings = np.array([token.vector for token in nlp(query)])
    similarities = [calculate_cosine_similarity(query_embeddings[0], nlp(phrase).vector) for phrase in reference_phrases]
    max_similarity = max(similarities)
    
    if max_similarity < similarity_threshold:
        converted_query = "Here are the " + " ".join(query_tokens)
        return converted_query
    else:
        return query

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"Detected {len(sys.argv) - 1} arguments. Please use the following format: python main.py <metaphor api key> <query>")
    client = Metaphor(api_key=sys.argv[1])

    query = " ".join(sys.argv[2:])

    #hardcoded to make it faster
    query = query.lower().replace("what", "here")

    converted_query = convert_query(query)

    print(converted_query)

    response = client.search(converted_query)

    print(response)
   
