from . import main
import pytest

@pytest.mark.yes
def test_plagiarised():
    sim_object = main.TextSimilarity()
    assert sim_object("The dog walked through the park on the sunny day that yesterday was.", "The dog meandered through the park on the sunny day that yesterday was.") == "Plagiarism detected."

@pytest.mark.yes
def test_dissimilar():
    sim_object = main.TextSimilarity()
    assert sim_object("The dog walked through the park on the sunny day that yesterday was.", "Copenhagen is the capital city of Denmark. Denmark is a Scandinavian country.") == "Likely to have dissimilar topics."

@pytest.mark.yes
def test_author():
    sim_object = main.TextSimilarity()
    assert sim_object("The dog walked through the park on the sunny day that yesterday was.", "The cat walked through the park on the cold day that yesterday was.") == "Likely to have the same author."

@pytest.mark.yes
def test_unplagiarised():
    sim_object = main.TextSimilarity()
    assert sim_object("The dog walked through the park on the sunny day that yesterday was.", "Yesterday, the dog went on a wlak through the park as it was sunny") == "Plagiarism unlikely."