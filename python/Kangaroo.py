def kangaroo(x1, v1, x2, v2):
    diffX = (x1-x2)
    diffV = v1-v2 if v1-v2 > 0 else (v1-v2) * -1
    if diffX > 0:
        return 'YES' if diffX%diffV == 0 else 'NO'
    else:
        return 'NO'

if __name__ == '__main__':
    print (kangaroo(0, 2, 5, 3))