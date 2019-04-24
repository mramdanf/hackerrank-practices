# 12:00 -> 00:00 night

def timeConversion(s):
    flag = s[-2:]
    time = s[:-2]
    freFix = time[:2]
    postFix = time[2:]
    if flag == 'AM':
        if freFix == '12':
            print ('00' + postFix)
        else:
            print (time)
    elif flag == 'PM':
        if freFix == '12':
            print (time)
        else:
            if freFix == '01':
                print ('13' + postFix)
            elif int(freFix) > 1:
                tmp = 13 + (int(freFix) - 1)
                print (str(tmp) + postFix)
        


if __name__ == '__main__':
    timeConversion('07:05:45PM')