from typing import Any
import spacy
from scipy.spatial.distance import cosine

nlp = spacy.load('en_core_web_trf')

class TextSimilarity:
    def __init__(self, base: str):
        self.base = base
        self.base_embedding = nlp(base)

    def word_similarity(self, target: str) -> float:
        target_embedding = nlp(target)
        return self.base_embedding.similarity(target_embedding)
    
    def cosine_similarity(self, target: str) -> float:
        self.target = target
        return 1- cosine(self.base_embedding.vector, nlp(target).vector)
    
    def __repr__(self): 
        return f"TextSimilarity({self.base})"
    
    def __call__(self, target: str) -> float:
        distance = self.cosine_similarity(target)
        if distance > 0.75:
            topic_sim = True
        else:
            return "Likely to have dissimilar topics."
        
        word_sim = self.word_similarity(target)
        if word_sim > 0.85 and topic_sim == True:
            return "Plagiarism detected."
        elif word_sim > 0.85:
            return "Likely to have the same author."
        else:
            return "Plagiarism unlikely."
