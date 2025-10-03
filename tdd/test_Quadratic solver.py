from Class_excercises.tdd.Quadratic_solver import quadraticsolver
import pytest

one_solution_tests = [[1,2,1,(-1,-1)],
                      [1,4,4,(-2,-2)],
                      [1,-4,4,(2,2)],
                      [2,2**1.5,1,(-2**-0.5,-2**-0.5)],
                      ]

two_solution_tests = [[1,1,0,(0,-1)],
                      [1,0,-1,(1,-1)],
                      [4,0,-1,(0.5,-0.5)],
                      ]

'''complex_solution_tests = [[],
                          [],
                          [],
                          [],
                          ]
'''''

@pytest.mark.parametrize("a,b,c,solution", one_solution_tests)
def test_quadraticsolver_one_solution(a,b,c,solution):
    answers = quadraticsolver(a,b,c)
    a1 = answers[0]
    a2 = answers[1]
    b1 = solution[0]
    b2 = solution[1]
    assert (round(a1,5),round(a2,5)) == (round(b1,5),round(b2,5))

@pytest.mark.parametrize("a,b,c,solution", two_solution_tests)
def test_quadraticsolver_two_solution(a,b,c,solution):
    answers = quadraticsolver(a,b,c)
    a1 = answers[0]
    a2 = answers[1]
    b1 = solution[0]
    b2 = solution[1]
    assert (round(a1,5),round(a2,5)) == (round(b1,5),round(b2,5))
