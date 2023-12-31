# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import Bucket_pb2 as Bucket__pb2


class RoutingStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.objectFind = channel.unary_unary(
                '/Routing/objectFind',
                request_serializer=Bucket__pb2.objectInfo.SerializeToString,
                response_deserializer=Bucket__pb2.findReply.FromString,
                )
        self.userLogin = channel.unary_unary(
                '/Routing/userLogin',
                request_serializer=Bucket__pb2.objectInfo.SerializeToString,
                response_deserializer=Bucket__pb2.findReply.FromString,
                )
        self.userLogoff = channel.unary_unary(
                '/Routing/userLogoff',
                request_serializer=Bucket__pb2.objectInfo.SerializeToString,
                response_deserializer=Bucket__pb2.findReply.FromString,
                )
        self.joinRoom = channel.unary_unary(
                '/Routing/joinRoom',
                request_serializer=Bucket__pb2.objectInfo.SerializeToString,
                response_deserializer=Bucket__pb2.findReply.FromString,
                )
        self.leaveRoom = channel.unary_unary(
                '/Routing/leaveRoom',
                request_serializer=Bucket__pb2.objectInfo.SerializeToString,
                response_deserializer=Bucket__pb2.findReply.FromString,
                )


class RoutingServicer(object):
    """Missing associated documentation comment in .proto file."""

    def objectFind(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def userLogin(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def userLogoff(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def joinRoom(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def leaveRoom(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RoutingServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'objectFind': grpc.unary_unary_rpc_method_handler(
                    servicer.objectFind,
                    request_deserializer=Bucket__pb2.objectInfo.FromString,
                    response_serializer=Bucket__pb2.findReply.SerializeToString,
            ),
            'userLogin': grpc.unary_unary_rpc_method_handler(
                    servicer.userLogin,
                    request_deserializer=Bucket__pb2.objectInfo.FromString,
                    response_serializer=Bucket__pb2.findReply.SerializeToString,
            ),
            'userLogoff': grpc.unary_unary_rpc_method_handler(
                    servicer.userLogoff,
                    request_deserializer=Bucket__pb2.objectInfo.FromString,
                    response_serializer=Bucket__pb2.findReply.SerializeToString,
            ),
            'joinRoom': grpc.unary_unary_rpc_method_handler(
                    servicer.joinRoom,
                    request_deserializer=Bucket__pb2.objectInfo.FromString,
                    response_serializer=Bucket__pb2.findReply.SerializeToString,
            ),
            'leaveRoom': grpc.unary_unary_rpc_method_handler(
                    servicer.leaveRoom,
                    request_deserializer=Bucket__pb2.objectInfo.FromString,
                    response_serializer=Bucket__pb2.findReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Routing', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Routing(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def objectFind(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Routing/objectFind',
            Bucket__pb2.objectInfo.SerializeToString,
            Bucket__pb2.findReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def userLogin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Routing/userLogin',
            Bucket__pb2.objectInfo.SerializeToString,
            Bucket__pb2.findReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def userLogoff(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Routing/userLogoff',
            Bucket__pb2.objectInfo.SerializeToString,
            Bucket__pb2.findReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def joinRoom(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Routing/joinRoom',
            Bucket__pb2.objectInfo.SerializeToString,
            Bucket__pb2.findReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def leaveRoom(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Routing/leaveRoom',
            Bucket__pb2.objectInfo.SerializeToString,
            Bucket__pb2.findReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class chatStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.send = channel.unary_unary(
                '/chat/send',
                request_serializer=Bucket__pb2.chatMessage.SerializeToString,
                response_deserializer=Bucket__pb2.findReply.FromString,
                )


class chatServicer(object):
    """Missing associated documentation comment in .proto file."""

    def send(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_chatServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'send': grpc.unary_unary_rpc_method_handler(
                    servicer.send,
                    request_deserializer=Bucket__pb2.chatMessage.FromString,
                    response_serializer=Bucket__pb2.findReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'chat', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class chat(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def send(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/chat/send',
            Bucket__pb2.chatMessage.SerializeToString,
            Bucket__pb2.findReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
