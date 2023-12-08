import grpc
import broadcast_pb2
import broadcast_pb2_grpc
from concurrent import futures


with grpc.insecure_channel('localhost:11451') as channel:
    stup = broadcast_pb2_grpc.broadcastStub(channel)
    response = stup.broadcast(
        broadcast_pb2.broadcastRequest(token='', socket='', depth=0))
print(response.message)
