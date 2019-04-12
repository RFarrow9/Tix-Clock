import time
import sys

while True:
    from datetime import datetime
    now = datetime.now()
    #print ("%s:%s:%s" % (now.hour,now.minute,now.second),end=''),
    #print("\r")
    
    hour_digit_one = now.hour//10
    hour_digit_two = now.hour%10

    minute_digit_one = now.minute//10
    minute_digit_two = now.minute%10

    sec_digit_one = now.second//10
    sec_digit_two = now.second%10

    str_hour1 = "O"*hour_digit_one
    str_hour2 = "O"*hour_digit_two
    str_min1 = "O"*minute_digit_one
    str_min2 = "O"*minute_digit_two
    str_sec1 = "O"*sec_digit_one
    str_sec2 = "O"*sec_digit_two

    print(str_hour1," ",str_hour2," ",str_min1," ",str_min2," ",str_sec1," ",str_sec2, end="",flush=True)
    
    time.sleep(1)
   



    


