# DNS RESOLVER SERVER
import json
from concurrent import futures
from dns import resolver
import logging
import grpc
import lookup_pb2
import lookup_pb2_grpc
import json


class Resolver(lookup_pb2_grpc.ResolverServicer):
    def Resolve(self, request, context):
        answer = Lookup.Resolve(self, request.name, request.rrdatatype)
        return lookup_pb2.Answer(json=str(answer))


class Lookup():
    def Resolve(self, hostname, rrdatatype):

        rrd = {
            0: "A",
            1: "AAAA"
        }

        answer = resolver.resolve(hostname, rrd[rrdatatype])
        return_answer = []
        for rr in answer:
            return_answer.append(str(rr))

        print(return_answer)
        return json.dumps(return_answer)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    lookup_pb2_grpc.add_ResolverServicer_to_server(Resolver(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
