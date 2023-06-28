#Python program to check if the number is an Armstrong number or not

#Taking input
num = int(input("Enter the number: "))

#initialize sum
sum = 0

#find the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 3

#display the result

    if num == sum:
        print(num, "is an Armstrong number")

    else:
        print(num, "is not Armstrong number")
