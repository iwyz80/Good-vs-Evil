def goodVsEvil(good, evil):
    #TODO Go get'em boys...
    good_count = split_sum(good)
    evil_count = split_sum(evil)
    if good_count > evil_count:


        return "Battle Result: Good triumphs over Evil"
    elif evil_count > good_count:

        return "Battle Result: Evil eradicates all trace of Good"
    else:

        return "Battle Result: No victor on this battle field"

def split_sum (string):
    ls = string.split(' ')
    if len(ls) >= 7:
        multiplier = [1,2,2,2,3,5,10]
    else:
        multiplier = [1,2,3,3,4,10]
    sum_s = 0
    for i in range (len (ls)):
        val = int(ls[i]) * multiplier[i]
        
             

        sum_s += val
        

    if sum_s > 2**31:
        return 0
    else:
        return sum_s

print (goodVsEvil('1 0 0 0 0 6', '0 1 0 1 1 1 20'))