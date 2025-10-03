'''def quadraticsolver(a,b,c):
    from math import sqrt
    x = (0)
    discriminant = b**2 - 4 * a * c
    if round(discriminant,3) == 0:
        x = (round(-b/(2*a)),3)
    elif discriminant > 0:
        possibility1 = (-b+sqrt(discriminant))/(2*a)
        possibility2 = (-b-sqrt(discriminant))/(2*a)
        x = (round(possibility1,3),round(possibility2,3))
    else:
        #the real part must be -b/2a and root(discriminant)/2a the imaginary part
        possibility1 = round(-b/(2*a),3) + (round((sqrt(-discriminant))/(2*a),3))*1j
        possibility2 = round(-b/(2*a),3) - (round((sqrt(-discriminant))/(2*a),3))*1j
        x = (possibility1,possibility2)
    return x'''


def quadraticsolver(a,b,c):
    from math import sqrt
    x = (0)
    discriminant = b**2 - 4*a*c
    possibility1 = (-b+sqrt(discriminant))/(2*a)
    possibility2 = (-b-sqrt(discriminant))/(2*a)
    return (possibility1,possibility2)