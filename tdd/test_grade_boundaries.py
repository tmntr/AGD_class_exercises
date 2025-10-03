from Class_excercises.tdd.grade_boundaries import calc_grade
import pytest


min_boundary_test_data = [("A*",264),
                      ("A",229),
                      ("B",189),
                      ("C",150),
                      ("D",111),
                      ("E",72),
                      ("U",0),
                      ]

max_boundary_test_data = [("A*",350),
                      ("A",263),
                      ("B",228),
                      ("C",188),
                      ("D",149),
                      ("E",110),
                      ("U",71),
                      ]
erroneous_test_data = [400,-20,"A"]


@pytest.mark.parametrize("grade,score", min_boundary_test_data)
def test_calc_grade_min_boundary(grade,score):
    assert calc_grade(score) == grade

@pytest.mark.parametrize("grade,score", max_boundary_test_data)

def test_calc_grade_max_boundary(grade,score):
    assert calc_grade(score) == grade

def test_calc_grade_erroneous():
    with pytest.raises(TypeError):
        calc_grade('A')
    with pytest.raises(ValueError):
        calc_grade(400)
    with pytest.raises(ValueError):
        calc_grade(-20)
