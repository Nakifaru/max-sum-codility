def solution(A):

    sums_of_digits = []
    sums_of_integers = []

    #loop through A to access individual integers
    for integer in A:
        #split the integer to a list containing digits
        #First convert the integer to a string to allow converting to a list
        digits = list(str(integer))
        #add the two digits
        sum_digits = int(digits[0]) + int(digits[1])
        #add the sum of our digits to the sum_digits list
        sums_of_digits.append(sum_digits)

    #loop through the sums of digits while checking for duplicates
    #current index is i
    i = 0
    for sum in sums_of_digits:
        #check for the duplicate in the sum of digits list but only in indexes from the current index
        #point of uncertainty **** it seems that I make the array shorter after each loop since I increment i
        if sums_of_digits[i:].count(sum) > 1:
            #hold the index of the next element in memory as y
            y = i + 1
            #if there is a duplicate, loop through digits beginning from the next index
            for x in sums_of_digits[y:]:
                if x == sum:
                    sums_of_integers.append(A[i] + A[y])
                y += 1
        i += 1


    #Assign the maximum sum to max_sum and if no digits had the same sum assign it to -1
    if len(sums_of_integers) > 0:
        max_sum = max(sums_of_integers)
    else:
        max_sum = -1
    
    
    print(max_sum)
    return max_sum




solution([51, 71, 17, 42]) #93 -> 51 + 42
solution([42, 33, 60]) #102 -> 42 + 60
solution([51, 32, 43]) #-1 -> no similar sum 