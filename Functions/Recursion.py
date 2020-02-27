#python also accepts function recurison, which means a defined function can call itself Recursion is a common mathemathical and programming concept. This has the benefit of meaning that you can loop through data to reach a result the developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathemathically-elegant approach to programming
#in this example, tri_recursion() is a function that we have defined to call itself("recurse") We use the k variable as the data, which decrements (-1) every time we recurse. the recursion ends when the condition is not greater than 0(i.e. when it is 0).
#to a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.

def tri(k):
    if(k>0):
        result = k+tri(k-1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri(6)
