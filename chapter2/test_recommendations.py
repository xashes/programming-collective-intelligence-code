import pytest
from recommendations import *


def test_sim_distance():
    assert round(sim_distance(critics, 'Lisa Rose', 'Gene Seymour'), 2) == 0.29


def test_sim_pearson():
    assert round(sim_pearson(critics, 'Lisa Rose', 'Gene Seymour'), 2) == 0.40


def test_topMatches():
    assert [person for _, person in topMatches(critics, 'Toby', n=3)] == [
        'Lisa Rose', 'Mick LaSalle', 'Claudia Puig'
    ]


def test_getRecomendations():
    assert [(round(score, 2), movie)
            for score, movie in getRecommendations(critics, 'Toby')
            ] == [(3.35, 'The Night Listener'), (2.83, 'Lady in the Water'),
                  (2.53, 'Just My Luck')]
