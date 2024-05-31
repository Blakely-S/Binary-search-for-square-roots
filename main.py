while 1<2:
 try:
    def srt(n):
        first_number = 0 
        last_number = n
        
        while first_number < n:
            middle_number = (first_number + last_number) / 2
            test_number = middle_number * middle_number
            if abs(test_number - n) < .001:
                return middle_number
            elif test_number < n:
                first_number = middle_number + 1
            else:
                last_number = middle_number - 1
        return -1
    
    m = srt(int(input('input a number:')))
    if m - int(m) >= .5:
        print('Answer is: ' + str(int(m) + 1))
    else:
        print('Answer is: ' + str(int(m)))
 except:
   print('You broke it')