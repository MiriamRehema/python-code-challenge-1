def two_are_positive(a, b, c):
#using the if/else statement check whether the integers:
#a and b are positive while c is negative:
#a and c are positive while b is negative
#b and c are positive while a is negative
#otherwise return false

    if (a > 0 and b > 0 and c <= 0) or (a > 0 and c > 0 and b <= 0) or (b > 0 and c > 0 and a <= 0):
        return True
    else:
        return False
print(two_are_positive(4,-9,5))
print(two_are_positive(4,-9,-8))
print(two_are_positive(-4,-9,-8))