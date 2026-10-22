# Exception handling
def getPort():
    port = int(input("Enter port:"))
    if not 0<= port <=65535:
        raise ValueError(f"PORT is out of range.{port}")
    return port

try:
    getPort()
except ValueError as e:
    print(e)