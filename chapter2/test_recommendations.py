import pytest
from recommendations import *


def test_sim_distance():
    assert round(sim_distance(critics_df, 'Lisa Rose', 'Gene Seymour'),
                 2) == 0.29

def test_sim_pearson():
    assert round(sim_pearson(critics, 'Lisa Rose', 'Gene Seymour'), 2) == 0.40
