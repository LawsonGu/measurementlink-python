# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ni_measurementlink_service._internal.stubs.ni.measurementlink.discovery.v1 import (
    discovery_service_pb2 as ni_dot_measurementlink_dot_discovery_dot_v1_dot_discovery__service__pb2,
)


class DiscoveryServiceStub(object):
    """The service used as a registry for other services. This service can be used to discover
    and activate other services present in the system.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterService = channel.unary_unary(
            "/ni.measurementlink.discovery.v1.DiscoveryService/RegisterService",
            request_serializer=ni_dot_measurementlink_dot_discovery_dot_v1_dot_discovery__service__pb2.RegisterServiceRequest.SerializeToString,
            response_deserializer=ni_dot_measurementlink_dot_discovery_dot_v1_dot_discovery__service__pb2.RegisterServiceResponse.FromString,
        )
        self.UnregisterService = channel.unary_unary(
            "/ni.measurementlink.discovery.v1.DiscoveryService/UnregisterService",
            request_serializer=ni_dot_measurementlink_dot_discovery_dot_v1_dot_discovery__service__pb2.UnregisterServiceRequest.SerializeToString,
            response_deserializer=ni_dot_measurementlink_dot_discovery_dot_v1_dot_discovery__service__pb2.UnregisterServiceResponse.FromString,
        )
        self.EnumerateServices = channel.unary_unary(
            "/ni.measurementlink.discovery.v1.DiscoveryService/EnumerateServices",
            request_serializer=ni_dot_measurementlink_dot_discovery_dot_v1_dot_discovery__service__pb2.EnumerateServicesRequest.SerializeToString,
            response_deserializer=ni_dot_measurementlink_dot_discovery_dot_v1_dot_discovery__service__pb2.EnumerateServicesResponse.FromString,
        )
        self.ResolveService = channel.unary_unary(
            "/ni.measurementlink.discovery.v1.DiscoveryService/ResolveService",
            request_serializer=ni_dot_measurementlink_dot_discovery_dot_v1_dot_discovery__service__pb2.ResolveServiceRequest.SerializeToString,
            response_deserializer=ni_dot_measurementlink_dot_discovery_dot_v1_dot_discovery__service__pb2.ServiceLocation.FromString,
        )


class DiscoveryServiceServicer(object):
    """The service used as a registry for other services. This service can be used to discover
    and activate other services present in the system.
    """

    def RegisterService(self, request, context):
        """Registers a service instance with the discovery service.
        Status Codes for errors:
        - INVALID_ARGUMENT:
        - ServiceDescriptor.display_name is empty
        - ServiceDescriptor.provided_interfaces is empty
        - ServiceDescriptor.service_class is empty
        - ServiceLocation.location is empty
        - Both ServiceLocation.insecure_port and ServiceLocation.ssl_authenticated_port are empty
        - Either ServiceLocation.insecure_port or ServiceLocation.ssl_authenticated_port contain an invalid port number
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UnregisterService(self, request, context):
        """Unregisters a service instance with the discovery service."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def EnumerateServices(self, request, context):
        """Enumerate all services which implement a specific service interface.
        This is useful for plugin type systems where the possible services are not known ahead of time.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ResolveService(self, request, context):
        """Given a description of a service, returns information that can be used to establish communication
        with that service. If necessary, the service will be started by the discovery service if it has not
        already been started. Activation of the service is accomplished through use of a .serviceconfig file
        which includes information describing the service. Services that register a .serviceconfig file must
        call RegisterService when their service is started or this call will never complete successfully when
        the discovery service attempts to start it.
        Status Codes for errors:
        - INVALID_ARGUMENT: provided_interfaces is empty
        - NOT_FOUND: No service matching the resolve request was found
        - FAILED_PRECONDITION: More than one service matching the resolve request was found
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_DiscoveryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "RegisterService": grpc.unary_unary_rpc_method_handler(
            servicer.RegisterService,
            request_deserializer=ni_dot_measurementlink_dot_discovery_dot_v1_dot_discovery__service__pb2.RegisterServiceRequest.FromString,
            response_serializer=ni_dot_measurementlink_dot_discovery_dot_v1_dot_discovery__service__pb2.RegisterServiceResponse.SerializeToString,
        ),
        "UnregisterService": grpc.unary_unary_rpc_method_handler(
            servicer.UnregisterService,
            request_deserializer=ni_dot_measurementlink_dot_discovery_dot_v1_dot_discovery__service__pb2.UnregisterServiceRequest.FromString,
            response_serializer=ni_dot_measurementlink_dot_discovery_dot_v1_dot_discovery__service__pb2.UnregisterServiceResponse.SerializeToString,
        ),
        "EnumerateServices": grpc.unary_unary_rpc_method_handler(
            servicer.EnumerateServices,
            request_deserializer=ni_dot_measurementlink_dot_discovery_dot_v1_dot_discovery__service__pb2.EnumerateServicesRequest.FromString,
            response_serializer=ni_dot_measurementlink_dot_discovery_dot_v1_dot_discovery__service__pb2.EnumerateServicesResponse.SerializeToString,
        ),
        "ResolveService": grpc.unary_unary_rpc_method_handler(
            servicer.ResolveService,
            request_deserializer=ni_dot_measurementlink_dot_discovery_dot_v1_dot_discovery__service__pb2.ResolveServiceRequest.FromString,
            response_serializer=ni_dot_measurementlink_dot_discovery_dot_v1_dot_discovery__service__pb2.ServiceLocation.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "ni.measurementlink.discovery.v1.DiscoveryService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class DiscoveryService(object):
    """The service used as a registry for other services. This service can be used to discover
    and activate other services present in the system.
    """

    @staticmethod
    def RegisterService(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/ni.measurementlink.discovery.v1.DiscoveryService/RegisterService",
            ni_dot_measurementlink_dot_discovery_dot_v1_dot_discovery__service__pb2.RegisterServiceRequest.SerializeToString,
            ni_dot_measurementlink_dot_discovery_dot_v1_dot_discovery__service__pb2.RegisterServiceResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def UnregisterService(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/ni.measurementlink.discovery.v1.DiscoveryService/UnregisterService",
            ni_dot_measurementlink_dot_discovery_dot_v1_dot_discovery__service__pb2.UnregisterServiceRequest.SerializeToString,
            ni_dot_measurementlink_dot_discovery_dot_v1_dot_discovery__service__pb2.UnregisterServiceResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def EnumerateServices(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/ni.measurementlink.discovery.v1.DiscoveryService/EnumerateServices",
            ni_dot_measurementlink_dot_discovery_dot_v1_dot_discovery__service__pb2.EnumerateServicesRequest.SerializeToString,
            ni_dot_measurementlink_dot_discovery_dot_v1_dot_discovery__service__pb2.EnumerateServicesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ResolveService(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/ni.measurementlink.discovery.v1.DiscoveryService/ResolveService",
            ni_dot_measurementlink_dot_discovery_dot_v1_dot_discovery__service__pb2.ResolveServiceRequest.SerializeToString,
            ni_dot_measurementlink_dot_discovery_dot_v1_dot_discovery__service__pb2.ServiceLocation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
