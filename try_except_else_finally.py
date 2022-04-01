try:
    f = open("F:\python\Roy.txt")

except Exception as e:
    print(e)

else:
    print("This will run only if exception is not run")

finally:
    print("I will run definately either try execute or except execute")
    # f.close()