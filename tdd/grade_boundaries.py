import warnings

import pytest


def calc_grade(p_score):
    maxscore = 350
    p_grade = ""
    
    
    if isinstance(p_score,int):

        grades = [("A*",264),("A",229),("B",189),("C",150),("D",111),("E",72),("U",0)]
        index = 0
        determined = False

        tempscore = p_score*1

        while index < len(grades) and not determined:
            if tempscore >= grades[index][1]:
                p_grade = grades[index][0]
                determined = True
            else:
                index += 1

        if tempscore > maxscore:
            raise(ValueError)
            #warnings.warn("Your score cannot be that high",UserWarning)

        elif tempscore < 0:
            raise(ValueError)
            #warnings.warn("Your score cannot be that low",UserWarning)
            
    else:
        raise(TypeError)
        #warnings.warn("Please present your score as an integer",UserWarning)
    
    return p_grade

tests = [156,148,299.0,350.1,0,-1,350,-350.1,351]

if __name__ == "__main__":
    for test in tests:
        print(calc_grade(test))


