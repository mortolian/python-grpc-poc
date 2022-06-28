# LOOKUP CLIENT

from __future__ import print_function

import logging

import grpc
import lookup_pb2
import lookup_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = lookup_pb2_grpc.ResolverStub(channel)
        response = stub.Resolve(lookup_pb2.DnsQuestion(name="mortolio.com", rrdatatype="A"))
    print("HOST ANSWER IP: " + response.json)


if __name__ == '__main__':
    logging.basicConfig()
    run()
