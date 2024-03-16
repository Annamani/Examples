def test_range(num):
    if num in range(0,11):
        print(num," is in the Given range")
    else:
        print(num," is NOT in the Given range")


num=int(input("Enter a number: "))
test_range(num)