def checkKey(key):
    if key in dict_values:
        print("Key is present in dictionary values")
    else:
        print("Key is not present in dictionary values")

dict_values = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
key=int(input("Enter a key value to check in dictionary: "))
checkKey(key)