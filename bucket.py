from util import *
import grpc

# 导入生成的gRPC代码
import broadcast_pb2
import broadcast_pb2_grpc


class Peer:

    def __init__(self):
        self.token = generateToken()
        self.tokenList = [self.token]
        self.pingList = [TIMEOUT]
        self.socketList = ["127.0.0.1:11451"]
        request = broadcast_pb2.broadcastRequest(
            token=self.token, socket=self.socket, depth=neighDepth-1)
        result = broadcast(request, "")
        success, message = result.success, result.message
        if not success:
            print("Connect failed.")
            exit(99)

    def broadcast(self, request, context):
        neighToken, neighSocket, neighDepth = request.neighToken, request.socket, request.depth
        self.update(neighToken, neighSocket)
        if neighToken in self.tokenList:
            return broadcast_pb2.broadcastResult(success=True, message="Broadcast terminated, peer has already in list.")

        # 进行测速
        try:
            startTime = time.time()
            with socket.create_connection(neighSocket, TIMEOUT=self.TIMEOUT) as sock:
                elapsedTime = time.time() - startTime
        except socket.TIMEOUT:
            # 超时直接退出
            return broadcast_pb2.broadcastResult(success=False, message="Broadcast unsuccessfully, peer TIMEOUT.")
        except Exception as e:
            # 处理其他异常情况
            return broadcast_pb2.broadcastResult(success=False, message="Broadcast terminated, unknown error occured.")

        # 如果测速时间超过timeout，直接退出
        if elapsedTime > self.TIMEOUT:
            return broadcast_pb2.broadcastResult(success=False, message="Broadcast unsuccessfully, peer TIMEOUT.")

        # 如果邻居列表已满，则移除延迟最高的邻居
        if len(self.socketList) >= self.LISTLEN:
            maxPingIdx = self.pingList.index(max(self.pingList))
            del self.tokenList[maxPingIdx]
            del self.pingList[maxPingIdx]
            del self.socketList[maxPingIdx]

        # 添加新的邻居
        self.tokenList.append(neighToken)
        self.pingList.append(elapsedTime)
        self.socketList.append(neighSocket)

        # 根据ping值进行排序
        sortedIndices = sorted(range(len(self.pingList)),
                               key=lambda x: self.pingList[x])
        self.tokenList = [self.tokenList[i] for i in sortedIndices]
        self.pingList = [self.pingList[i] for i in sortedIndices]
        self.socketList = [self.socketList[i] for i in sortedIndices]

        # 向邻居列表中的所有邻居进行广播
        success = False
        for socket in self.socketList:
            channel = grpc.insecure_channel(neighSocket)
            target = broadcast_pb2_grpc.broadcastStub(channel)
            request = broadcast_pb2.broadcastRequest(
                token=neighToken, socket=neighSocket, depth=neighDepth-1)
            result = target.broadcast(request)
            success, message = success or result.success, result.message

        if success:
            return broadcast_pb2.broadcastResult(success=True, message="Broadcast successfully.")
        else:
            return broadcast_pb2.broadcastResult(success=False, message="Broadcast unsuccessfully, it might be an isolated peer.")


if __name__ == '__main__':
    print("Hello bucket.")
    local = Peer()
