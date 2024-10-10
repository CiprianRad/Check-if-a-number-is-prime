# Our is prime function check if a number is prime or not
# We used if conditions to give outputs for integers less than 1 and in the case n=2
'''We took the range from 2 to n//2 + 1 because for every integer it is true that there are no 
    other factors above the whole part of it's division to 2 which is exactly why we used the
    // operator. 
'''
 #Todo: ask if we could have placed in the range n//2, because it goes only to n//2 - 1  

def is_prime(n):
    if n == 2: return True
    if n <= 1 or n % 2 == 0: return False
    for i in range(2, n // 2 + 1):
        if n % i == 0: return False
    return True


'''This function allows us to get valid input from the user, the while True allows us to continously
    loop until we get a valid input from the user. The try block allows us to test the input for
    error, and also to raise/generate an exception in case of a string or other type of input
'''

def get_valid_input():
    while True:
        try:
            n = int(input("Enter an integer:"))
            #if type(n) is int:
            return n
        except ValueError:
            print("Invalid input. Enter a valid integer:")







def main():
    n = get_valid_input()
    print(is_prime(n))
main()