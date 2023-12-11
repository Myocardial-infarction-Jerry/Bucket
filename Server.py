import os
import grpc
import json
import logging
from concurrent import futures

import Bucket_pb2
import Bucket_pb2_grpc

PATH = os.path.dirname(__file__)


class Routing:
    def __init__(self):
        self.object = {}

    def objectFind(self, request, context):
        if request.token not in self.object:
            return Bucket_pb2.findReply(suc=False, socket=[])

        return Bucket_pb2.findReply(suc=True, socket=self.object[request.token])

    def userLogin(self, request, context):
        self.object[request.token] = [request.socket]
        logging.info(f"User {request.token} login.")
        return Bucket_pb2.findReply(suc=True, socket=[])

    def userLogoff(self, request, context):
        self.object.pop(request.token)
        logging.info(f"User {request.token} logoff.")
        return Bucket_pb2.findReply(suc=True, socket=[])

    def joinRoom(self, request, context):
        if request.token not in self.object:
            self.object[request.token] = []
            logging.info(f"Room {request.token} found.")
        self.object[request.token].append(request.socket)
        return Bucket_pb2.findReply(suc=True, socket=[])

    def leaveRoom(self, request, context):
        self.object[request.token].remove(request.socket)
        if len(self.object[request.token]) == 0:
            self.object.pop(request.token)
            logging.info(f"Room {request.token} dismiss.")
        return Bucket_pb2.findReply(suc=True, socket=[])


if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=20))
    Bucket_pb2_grpc.add_RoutingServicer_to_server(Routing(), server)
    server.add_insecure_port("localhost:11451")
    server.start()
    logging.info(f"Server started, listening on port 11451.")
    logging.info(f"Press CTRL+C to stop.")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        server.stop(0)
