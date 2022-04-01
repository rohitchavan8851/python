
try:
    f = open("F:\python\does.txt")
except Exception as e:
    print(e)
finally:
    print("I will run definately either try execute or except execute")
    # f.close()
