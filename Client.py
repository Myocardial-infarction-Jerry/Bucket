import grpc
import logging
import random
from concurrent import futures

import Bucket_pb2
import Bucket_pb2_grpc


class chat:
    def send(self, request, context):
        logging.info(request.message)
        return Bucket_pb2.findReply(suc=True, socket=[])


if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

    port = random.randint(30000, 40000)
    socket = f"localhost:{port}"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=20))
    Bucket_pb2_grpc.add_chatServicer_to_server(chat(), server)
    server.add_insecure_port(socket)
    server.start()
    logging.info(f"Server started, listening on port {port}.")
    logging.info(f"CTRL+C to exit.")

    token = input("Input your nickname: ")
    channel = grpc.insecure_channel("localhost:11451")
    stub = Bucket_pb2_grpc.RoutingStub(channel)
    stub.userLogin(
        Bucket_pb2.objectInfo(
            token=token, socket=socket))
    try:
        while True:
            target = input("Object name: ")
            option = input("Is it a room [y/N]: ")
            if option == "y":
                stub.joinRoom(Bucket_pb2.objectInfo(
                    token=target, socket=socket))

            while True:
                message = input(
                    'Input message (\'quit\' to quit): ')
                if message == "quit":
                    break
                sockets = stub.objectFind(
                    Bucket_pb2.objectInfo(token=target, socket=socket))
                if not sockets.suc:
                    logging.info(f"Object {target} not found.")
                    continue
                for soc in sockets.socket:
                    with grpc.insecure_channel(soc) as chatChannel:
                        chatStub = Bucket_pb2_grpc.chatStub(chatChannel)
                        chatStub.send(Bucket_pb2.chatMessage(
                            message=f"{token}: {message}"))

    except KeyboardInterrupt:
        stub.userLogoff(Bucket_pb2.objectInfo(token=token, socket=socket))
        exit(0)
    except:
        stub.userLogoff(Bucket_pb2.objectInfo(token=token, socket=socket))
