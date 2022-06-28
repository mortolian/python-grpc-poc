# gRPC POC

gRPC is a modern open source high performance Remote Procedure Call (RPC) framework that can run in any environment. 
It can efficiently connect services in and across data centers with pluggable support for load balancing, tracing, 
health checking and authentication. It is also applicable in last mile of distributed computing to connect devices, 
mobile applications and browsers to backend services.

## Protocol Buffers

Protocol buffers provide a language-neutral, platform-neutral, extensible mechanism for serializing structured data 
in a forward-compatible and backward-compatible way. It’s like JSON, except it's smaller and faster, and it generates 
native language bindings.

Protocol buffers are a combination of the definition language (created in .proto files), the code that the proto 
compiler generates to interface with data, language-specific runtime libraries, and the serialization format for 
data that is written to a file (or sent across a network connection).

## Resources

### GRPC - RPC Service Compilors for various languages

This generates different files to the ones you get from Google.

- https://grpc.io/docs/languages/

#### Generate files for Python

```commandline
 python -m grpc_tools.protoc -I./protobufs --python_out=. --grpc_python_out=. ./protobufs/lookup.proto
```

### Setup Python

```commandline
python -m pip install grpcio
python -m pip install grpcio-tools
```

### Setup Protoc

#### Google Protobuf Documentation

- https://github.com/protocolbuffers/protobuf

##### Download `protoc` to compile protobufs to any other language that is not c++.

- https://github.com/protocolbuffers/protobuf/releases/tag/v21.2

### How to generate language modules/classes from proto files

Generate Python code from a .proto file

```commandline
protoc --python_out=[path/to/output_directory] [input_file.proto]
```

Generate Python code from a .proto file that imports other .proto files (most popular use)

```commandline
protoc --python_out=[path/to/output_directory] --proto_path=[path/to/import_search_path] [input_file.proto]
```

Generate code for multiple languages

```commandline
protoc --python_out=[path/to/c#_output_directory] --php_out=[path/to/js_output_directory] [input_file.proto]
```

### Complete Protocol Buffers Documentation From Google

- https://developers.google.com/protocol-buffers/

### Some Other Interesting URLs

- https://linuxcommandlibrary.com/man/protoc
- https://tsh.io/blog/grpc-php/
- 