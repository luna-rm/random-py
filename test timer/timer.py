import time


def main():  
    do = 0
    init_sec = time.time()


    while do == 0:
        sec = time.time()    
        print(sec)
        
        if sec - init_sec > 5:
            do = 1
    
main()
