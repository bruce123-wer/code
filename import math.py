def is_prime(n):
    counter = 0
    if n <= 1:
        print(False)
    else:
        for i in range(1,n+1):
            a = n % i
            if a == 0:
                counter += 1
            else:
                continue
        if counter >= 3:
            print(False)
        else:
            print(True)
        
is_prime(10)