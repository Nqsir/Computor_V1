# Computor_V1

Simple Polynomial equation solver (degree 2 max.)

Example: ```py Computor_v1``` ```-d``` for detailed mode

```Please enter your polynomial expression : "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"


Polynomial degree = 2
Reduced form:  4 * X^0 + 4 * X^1  -9.3 * X^2 = 0
Discriminant is strictly positive, the two solutions are:
 0.9052 

-0.4751
```


Example: ```py Computor_v1 -d``` for detailed mode

```
/*/-------
 Detailed mode activated 
/*/-------

Please enter your polynomial expression : 5 * X^1 - 9.3 * X^2 = 1 * X^0 

/*/-------
Pattern catched [('', '', '5', '1'), ('', '-', '9.3', '2'), ('=', '', '1', '0')]     
/*/-------


/*/-------
Prepared pattern to simplify [['', '', 5.0, 1], ['', '', -9.3, 2], ['', '', -1.0, 0]]
/*/-------


/*/-------
Reduced pattern [['', '', -1.0, 0], ['', '', 5.0, 1], ['', '', -9.3, 2]]
/*/-------

Polynomial degree = 2
Reduced form:  -1 * X^0 + 5 * X^1  -9.3 * X^2 = 0

/*/-------
Discriminant = -12.200000000000003
/*/-------

Discriminant is strictly negative, the two solutions are:
(-5 - i * √-12.20) / 5.0 

(-5 + i * √-12.20) / 5.0 
```
