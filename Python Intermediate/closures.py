def log(message):
    def logging():
        return message + " from inner function"
    return logging
    
x = log("A log")
y = log("B log")

print(x())
print(y())
