def countApplesAndOranges(s, t, a, b, apples, oranges):
    countApples = 0
    countOranges = 0
    for apple in apples:
        if s <= a+apple <= t: countApples+=1

    for orange in oranges:
        if s <= b+orange <= t: countOranges+=1
    
    print (countApples)
    print (countOranges)
    

if __name__ == '__main__':
    countApplesAndOranges(
        7,
        11,
        5,
        15,
        [-2, 2, 1],
        [5, -6]
    )