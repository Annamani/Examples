def histogram(numbers):
    for n in numbers:
        output = ''  
        times = n            
        while times > 0:
            output += "@ "
            times = times - 1          
        print(output)



histogram([2, 3, 6, 5])