from tutorial import Calculator
from tutorial.ttypes import *
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

transport = TSocket.TSocket('localhost', 9090)
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = Calculator.Client(protocol)
transport.open()

result = client.add(1, 2)
print(f'1 + 2 = {result}')

result = client.subtract(5, 3)
print(f'5 - 3 = {result}')

result = client.multiply(2, 3)
print(f'2 * 3 = {result}')

try:
    result = client.divide(6, 0)
    print(f'6 / 0 = {result}')
except InvalidOperation as e:
    print(f'Invalid operation: {e.message}')
