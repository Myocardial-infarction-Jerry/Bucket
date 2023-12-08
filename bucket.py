import os
import grpc
import json
import logging
import socket
import broadcast_pb2
import broadcast_pb2_grpc
from concurrent import futures

config = json.load(open(os.path.dirname(__file__)+"/config.json"))


class Peer:
    def __init__(self):
        self.token = config['token']
        self.socList = config['defaultList']
        self.rttList = [config['timeout']]*len(self.socList)

        for soc in self.socList:
            with grpc.insecure_channel(soc, options=[('grpc.keepalive_timeout_ms', config['timeout'])]) as channel:
                stub = broadcast_pb2_grpc.broadcastStub(channel)
                result = stub.broadcast(broadcast_pb2.broadcastRequest(
                    token=self.token, socket=soc, depth=config['maxDepth']))
                if not result:
                    logging.info(f"Fail to connect {soc}")

    def broadcast(self, request, context):
        print(f"Connection from {context.peer()}")
        return broadcast_pb2.broadcastResult(success=True, message=context.peer())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    broadcast_pb2_grpc.add_broadcastServicer_to_server(Peer(), server)
    server.add_insecure_port('[::]:11451')
    server.start()
    server.wait_for_termination()
    exit
