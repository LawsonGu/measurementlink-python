# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ni/measurementlink/sessionmanagement/v1/session_management_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ni_measurement_service._internal.stubs.ni.measurementlink import (
    pin_map_context_pb2 as ni_dot_measurementlink_dot_pin__map__context__pb2,
)


DESCRIPTOR = _descriptor.FileDescriptor(
    name="ni/measurementlink/sessionmanagement/v1/session_management_service.proto",
    package="ni.measurementlink.sessionmanagement.v1",
    syntax="proto3",
    serialized_options=b"\n+com.ni.measurementlink.sessionmanagement.v1B\026SessionManagementProtoP\001Z\023sessionmanagementv1\242\002\004NIMS\252\0028NationalInstruments.MeasurementLink.SessionManagement.V1\312\002'NI\\MeasurementLink\\SessionManagement\\V1\352\002*NI::MeasurementLink::SessionManagement::V1",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\nHni/measurementlink/sessionmanagement/v1/session_management_service.proto\x12\'ni.measurementlink.sessionmanagement.v1\x1a(ni/measurementlink/pin_map_context.proto"\x17\n\x07Session\x12\x0c\n\x04name\x18\x01 \x01(\t"\xb8\x01\n\x12SessionInformation\x12\x41\n\x07session\x18\x01 \x01(\x0b\x32\x30.ni.measurementlink.sessionmanagement.v1.Session\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\x14\n\x0c\x63hannel_list\x18\x03 \x01(\t\x12\x1a\n\x12instrument_type_id\x18\x04 \x01(\t\x12\x16\n\x0esession_exists\x18\x05 \x01(\x08"\xa4\x01\n\x16ReserveSessionsRequest\x12:\n\x0fpin_map_context\x18\x01 \x01(\x0b\x32!.ni.measurementlink.PinMapContext\x12\x11\n\tpin_names\x18\x02 \x03(\t\x12\x1a\n\x12instrument_type_id\x18\x03 \x01(\t\x12\x1f\n\x17timeout_in_milliseconds\x18\x04 \x01(\x05"h\n\x17ReserveSessionsResponse\x12M\n\x08sessions\x18\x01 \x03(\x0b\x32;.ni.measurementlink.sessionmanagement.v1.SessionInformation"i\n\x18UnreserveSessionsRequest\x12M\n\x08sessions\x18\x01 \x03(\x0b\x32;.ni.measurementlink.sessionmanagement.v1.SessionInformation"\x1b\n\x19UnreserveSessionsResponse"h\n\x17RegisterSessionsRequest\x12M\n\x08sessions\x18\x01 \x03(\x0b\x32;.ni.measurementlink.sessionmanagement.v1.SessionInformation"\x1a\n\x18RegisterSessionsResponse"j\n\x19UnregisterSessionsRequest\x12M\n\x08sessions\x18\x01 \x03(\x0b\x32;.ni.measurementlink.sessionmanagement.v1.SessionInformation"\x1c\n\x1aUnregisterSessionsResponse"F\n#ReserveAllRegisteredSessionsRequest\x12\x1f\n\x17timeout_in_milliseconds\x18\x01 \x01(\x05"u\n$ReserveAllRegisteredSessionsResponse\x12M\n\x08sessions\x18\x01 \x03(\x0b\x32;.ni.measurementlink.sessionmanagement.v1.SessionInformation2\xc6\x06\n\x18SessionManagementService\x12\x94\x01\n\x0fReserveSessions\x12?.ni.measurementlink.sessionmanagement.v1.ReserveSessionsRequest\x1a@.ni.measurementlink.sessionmanagement.v1.ReserveSessionsResponse\x12\x9a\x01\n\x11UnreserveSessions\x12\x41.ni.measurementlink.sessionmanagement.v1.UnreserveSessionsRequest\x1a\x42.ni.measurementlink.sessionmanagement.v1.UnreserveSessionsResponse\x12\x97\x01\n\x10RegisterSessions\x12@.ni.measurementlink.sessionmanagement.v1.RegisterSessionsRequest\x1a\x41.ni.measurementlink.sessionmanagement.v1.RegisterSessionsResponse\x12\x9d\x01\n\x12UnregisterSessions\x12\x42.ni.measurementlink.sessionmanagement.v1.UnregisterSessionsRequest\x1a\x43.ni.measurementlink.sessionmanagement.v1.UnregisterSessionsResponse\x12\xbb\x01\n\x1cReserveAllRegisteredSessions\x12L.ni.measurementlink.sessionmanagement.v1.ReserveAllRegisteredSessionsRequest\x1aM.ni.measurementlink.sessionmanagement.v1.ReserveAllRegisteredSessionsResponseB\xf5\x01\n+com.ni.measurementlink.sessionmanagement.v1B\x16SessionManagementProtoP\x01Z\x13sessionmanagementv1\xa2\x02\x04NIMS\xaa\x02\x38NationalInstruments.MeasurementLink.SessionManagement.V1\xca\x02\'NI\\MeasurementLink\\SessionManagement\\V1\xea\x02*NI::MeasurementLink::SessionManagement::V1b\x06proto3',
    dependencies=[
        ni_dot_measurementlink_dot_pin__map__context__pb2.DESCRIPTOR,
    ],
)


_SESSION = _descriptor.Descriptor(
    name="Session",
    full_name="ni.measurementlink.sessionmanagement.v1.Session",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="ni.measurementlink.sessionmanagement.v1.Session.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=159,
    serialized_end=182,
)


_SESSIONINFORMATION = _descriptor.Descriptor(
    name="SessionInformation",
    full_name="ni.measurementlink.sessionmanagement.v1.SessionInformation",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="session",
            full_name="ni.measurementlink.sessionmanagement.v1.SessionInformation.session",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="resource_name",
            full_name="ni.measurementlink.sessionmanagement.v1.SessionInformation.resource_name",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="channel_list",
            full_name="ni.measurementlink.sessionmanagement.v1.SessionInformation.channel_list",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="instrument_type_id",
            full_name="ni.measurementlink.sessionmanagement.v1.SessionInformation.instrument_type_id",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="session_exists",
            full_name="ni.measurementlink.sessionmanagement.v1.SessionInformation.session_exists",
            index=4,
            number=5,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=185,
    serialized_end=369,
)


_RESERVESESSIONSREQUEST = _descriptor.Descriptor(
    name="ReserveSessionsRequest",
    full_name="ni.measurementlink.sessionmanagement.v1.ReserveSessionsRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="pin_map_context",
            full_name="ni.measurementlink.sessionmanagement.v1.ReserveSessionsRequest.pin_map_context",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="pin_names",
            full_name="ni.measurementlink.sessionmanagement.v1.ReserveSessionsRequest.pin_names",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="instrument_type_id",
            full_name="ni.measurementlink.sessionmanagement.v1.ReserveSessionsRequest.instrument_type_id",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="timeout_in_milliseconds",
            full_name="ni.measurementlink.sessionmanagement.v1.ReserveSessionsRequest.timeout_in_milliseconds",
            index=3,
            number=4,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=372,
    serialized_end=536,
)


_RESERVESESSIONSRESPONSE = _descriptor.Descriptor(
    name="ReserveSessionsResponse",
    full_name="ni.measurementlink.sessionmanagement.v1.ReserveSessionsResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="sessions",
            full_name="ni.measurementlink.sessionmanagement.v1.ReserveSessionsResponse.sessions",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=538,
    serialized_end=642,
)


_UNRESERVESESSIONSREQUEST = _descriptor.Descriptor(
    name="UnreserveSessionsRequest",
    full_name="ni.measurementlink.sessionmanagement.v1.UnreserveSessionsRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="sessions",
            full_name="ni.measurementlink.sessionmanagement.v1.UnreserveSessionsRequest.sessions",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=644,
    serialized_end=749,
)


_UNRESERVESESSIONSRESPONSE = _descriptor.Descriptor(
    name="UnreserveSessionsResponse",
    full_name="ni.measurementlink.sessionmanagement.v1.UnreserveSessionsResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=751,
    serialized_end=778,
)


_REGISTERSESSIONSREQUEST = _descriptor.Descriptor(
    name="RegisterSessionsRequest",
    full_name="ni.measurementlink.sessionmanagement.v1.RegisterSessionsRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="sessions",
            full_name="ni.measurementlink.sessionmanagement.v1.RegisterSessionsRequest.sessions",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=780,
    serialized_end=884,
)


_REGISTERSESSIONSRESPONSE = _descriptor.Descriptor(
    name="RegisterSessionsResponse",
    full_name="ni.measurementlink.sessionmanagement.v1.RegisterSessionsResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=886,
    serialized_end=912,
)


_UNREGISTERSESSIONSREQUEST = _descriptor.Descriptor(
    name="UnregisterSessionsRequest",
    full_name="ni.measurementlink.sessionmanagement.v1.UnregisterSessionsRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="sessions",
            full_name="ni.measurementlink.sessionmanagement.v1.UnregisterSessionsRequest.sessions",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=914,
    serialized_end=1020,
)


_UNREGISTERSESSIONSRESPONSE = _descriptor.Descriptor(
    name="UnregisterSessionsResponse",
    full_name="ni.measurementlink.sessionmanagement.v1.UnregisterSessionsResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1022,
    serialized_end=1050,
)


_RESERVEALLREGISTEREDSESSIONSREQUEST = _descriptor.Descriptor(
    name="ReserveAllRegisteredSessionsRequest",
    full_name="ni.measurementlink.sessionmanagement.v1.ReserveAllRegisteredSessionsRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="timeout_in_milliseconds",
            full_name="ni.measurementlink.sessionmanagement.v1.ReserveAllRegisteredSessionsRequest.timeout_in_milliseconds",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1052,
    serialized_end=1122,
)


_RESERVEALLREGISTEREDSESSIONSRESPONSE = _descriptor.Descriptor(
    name="ReserveAllRegisteredSessionsResponse",
    full_name="ni.measurementlink.sessionmanagement.v1.ReserveAllRegisteredSessionsResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="sessions",
            full_name="ni.measurementlink.sessionmanagement.v1.ReserveAllRegisteredSessionsResponse.sessions",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1124,
    serialized_end=1241,
)

_SESSIONINFORMATION.fields_by_name["session"].message_type = _SESSION
_RESERVESESSIONSREQUEST.fields_by_name[
    "pin_map_context"
].message_type = ni_dot_measurementlink_dot_pin__map__context__pb2._PINMAPCONTEXT
_RESERVESESSIONSRESPONSE.fields_by_name["sessions"].message_type = _SESSIONINFORMATION
_UNRESERVESESSIONSREQUEST.fields_by_name["sessions"].message_type = _SESSIONINFORMATION
_REGISTERSESSIONSREQUEST.fields_by_name["sessions"].message_type = _SESSIONINFORMATION
_UNREGISTERSESSIONSREQUEST.fields_by_name["sessions"].message_type = _SESSIONINFORMATION
_RESERVEALLREGISTEREDSESSIONSRESPONSE.fields_by_name["sessions"].message_type = _SESSIONINFORMATION
DESCRIPTOR.message_types_by_name["Session"] = _SESSION
DESCRIPTOR.message_types_by_name["SessionInformation"] = _SESSIONINFORMATION
DESCRIPTOR.message_types_by_name["ReserveSessionsRequest"] = _RESERVESESSIONSREQUEST
DESCRIPTOR.message_types_by_name["ReserveSessionsResponse"] = _RESERVESESSIONSRESPONSE
DESCRIPTOR.message_types_by_name["UnreserveSessionsRequest"] = _UNRESERVESESSIONSREQUEST
DESCRIPTOR.message_types_by_name["UnreserveSessionsResponse"] = _UNRESERVESESSIONSRESPONSE
DESCRIPTOR.message_types_by_name["RegisterSessionsRequest"] = _REGISTERSESSIONSREQUEST
DESCRIPTOR.message_types_by_name["RegisterSessionsResponse"] = _REGISTERSESSIONSRESPONSE
DESCRIPTOR.message_types_by_name["UnregisterSessionsRequest"] = _UNREGISTERSESSIONSREQUEST
DESCRIPTOR.message_types_by_name["UnregisterSessionsResponse"] = _UNREGISTERSESSIONSRESPONSE
DESCRIPTOR.message_types_by_name[
    "ReserveAllRegisteredSessionsRequest"
] = _RESERVEALLREGISTEREDSESSIONSREQUEST
DESCRIPTOR.message_types_by_name[
    "ReserveAllRegisteredSessionsResponse"
] = _RESERVEALLREGISTEREDSESSIONSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Session = _reflection.GeneratedProtocolMessageType(
    "Session",
    (_message.Message,),
    {
        "DESCRIPTOR": _SESSION,
        "__module__": "ni.measurementlink.sessionmanagement.v1.session_management_service_pb2"
        # @@protoc_insertion_point(class_scope:ni.measurementlink.sessionmanagement.v1.Session)
    },
)
_sym_db.RegisterMessage(Session)

SessionInformation = _reflection.GeneratedProtocolMessageType(
    "SessionInformation",
    (_message.Message,),
    {
        "DESCRIPTOR": _SESSIONINFORMATION,
        "__module__": "ni.measurementlink.sessionmanagement.v1.session_management_service_pb2"
        # @@protoc_insertion_point(class_scope:ni.measurementlink.sessionmanagement.v1.SessionInformation)
    },
)
_sym_db.RegisterMessage(SessionInformation)

ReserveSessionsRequest = _reflection.GeneratedProtocolMessageType(
    "ReserveSessionsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _RESERVESESSIONSREQUEST,
        "__module__": "ni.measurementlink.sessionmanagement.v1.session_management_service_pb2"
        # @@protoc_insertion_point(class_scope:ni.measurementlink.sessionmanagement.v1.ReserveSessionsRequest)
    },
)
_sym_db.RegisterMessage(ReserveSessionsRequest)

ReserveSessionsResponse = _reflection.GeneratedProtocolMessageType(
    "ReserveSessionsResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _RESERVESESSIONSRESPONSE,
        "__module__": "ni.measurementlink.sessionmanagement.v1.session_management_service_pb2"
        # @@protoc_insertion_point(class_scope:ni.measurementlink.sessionmanagement.v1.ReserveSessionsResponse)
    },
)
_sym_db.RegisterMessage(ReserveSessionsResponse)

UnreserveSessionsRequest = _reflection.GeneratedProtocolMessageType(
    "UnreserveSessionsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _UNRESERVESESSIONSREQUEST,
        "__module__": "ni.measurementlink.sessionmanagement.v1.session_management_service_pb2"
        # @@protoc_insertion_point(class_scope:ni.measurementlink.sessionmanagement.v1.UnreserveSessionsRequest)
    },
)
_sym_db.RegisterMessage(UnreserveSessionsRequest)

UnreserveSessionsResponse = _reflection.GeneratedProtocolMessageType(
    "UnreserveSessionsResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _UNRESERVESESSIONSRESPONSE,
        "__module__": "ni.measurementlink.sessionmanagement.v1.session_management_service_pb2"
        # @@protoc_insertion_point(class_scope:ni.measurementlink.sessionmanagement.v1.UnreserveSessionsResponse)
    },
)
_sym_db.RegisterMessage(UnreserveSessionsResponse)

RegisterSessionsRequest = _reflection.GeneratedProtocolMessageType(
    "RegisterSessionsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _REGISTERSESSIONSREQUEST,
        "__module__": "ni.measurementlink.sessionmanagement.v1.session_management_service_pb2"
        # @@protoc_insertion_point(class_scope:ni.measurementlink.sessionmanagement.v1.RegisterSessionsRequest)
    },
)
_sym_db.RegisterMessage(RegisterSessionsRequest)

RegisterSessionsResponse = _reflection.GeneratedProtocolMessageType(
    "RegisterSessionsResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _REGISTERSESSIONSRESPONSE,
        "__module__": "ni.measurementlink.sessionmanagement.v1.session_management_service_pb2"
        # @@protoc_insertion_point(class_scope:ni.measurementlink.sessionmanagement.v1.RegisterSessionsResponse)
    },
)
_sym_db.RegisterMessage(RegisterSessionsResponse)

UnregisterSessionsRequest = _reflection.GeneratedProtocolMessageType(
    "UnregisterSessionsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _UNREGISTERSESSIONSREQUEST,
        "__module__": "ni.measurementlink.sessionmanagement.v1.session_management_service_pb2"
        # @@protoc_insertion_point(class_scope:ni.measurementlink.sessionmanagement.v1.UnregisterSessionsRequest)
    },
)
_sym_db.RegisterMessage(UnregisterSessionsRequest)

UnregisterSessionsResponse = _reflection.GeneratedProtocolMessageType(
    "UnregisterSessionsResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _UNREGISTERSESSIONSRESPONSE,
        "__module__": "ni.measurementlink.sessionmanagement.v1.session_management_service_pb2"
        # @@protoc_insertion_point(class_scope:ni.measurementlink.sessionmanagement.v1.UnregisterSessionsResponse)
    },
)
_sym_db.RegisterMessage(UnregisterSessionsResponse)

ReserveAllRegisteredSessionsRequest = _reflection.GeneratedProtocolMessageType(
    "ReserveAllRegisteredSessionsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _RESERVEALLREGISTEREDSESSIONSREQUEST,
        "__module__": "ni.measurementlink.sessionmanagement.v1.session_management_service_pb2"
        # @@protoc_insertion_point(class_scope:ni.measurementlink.sessionmanagement.v1.ReserveAllRegisteredSessionsRequest)
    },
)
_sym_db.RegisterMessage(ReserveAllRegisteredSessionsRequest)

ReserveAllRegisteredSessionsResponse = _reflection.GeneratedProtocolMessageType(
    "ReserveAllRegisteredSessionsResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _RESERVEALLREGISTEREDSESSIONSRESPONSE,
        "__module__": "ni.measurementlink.sessionmanagement.v1.session_management_service_pb2"
        # @@protoc_insertion_point(class_scope:ni.measurementlink.sessionmanagement.v1.ReserveAllRegisteredSessionsResponse)
    },
)
_sym_db.RegisterMessage(ReserveAllRegisteredSessionsResponse)


DESCRIPTOR._options = None

_SESSIONMANAGEMENTSERVICE = _descriptor.ServiceDescriptor(
    name="SessionManagementService",
    full_name="ni.measurementlink.sessionmanagement.v1.SessionManagementService",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=1244,
    serialized_end=2082,
    methods=[
        _descriptor.MethodDescriptor(
            name="ReserveSessions",
            full_name="ni.measurementlink.sessionmanagement.v1.SessionManagementService.ReserveSessions",
            index=0,
            containing_service=None,
            input_type=_RESERVESESSIONSREQUEST,
            output_type=_RESERVESESSIONSRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="UnreserveSessions",
            full_name="ni.measurementlink.sessionmanagement.v1.SessionManagementService.UnreserveSessions",
            index=1,
            containing_service=None,
            input_type=_UNRESERVESESSIONSREQUEST,
            output_type=_UNRESERVESESSIONSRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="RegisterSessions",
            full_name="ni.measurementlink.sessionmanagement.v1.SessionManagementService.RegisterSessions",
            index=2,
            containing_service=None,
            input_type=_REGISTERSESSIONSREQUEST,
            output_type=_REGISTERSESSIONSRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="UnregisterSessions",
            full_name="ni.measurementlink.sessionmanagement.v1.SessionManagementService.UnregisterSessions",
            index=3,
            containing_service=None,
            input_type=_UNREGISTERSESSIONSREQUEST,
            output_type=_UNREGISTERSESSIONSRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="ReserveAllRegisteredSessions",
            full_name="ni.measurementlink.sessionmanagement.v1.SessionManagementService.ReserveAllRegisteredSessions",
            index=4,
            containing_service=None,
            input_type=_RESERVEALLREGISTEREDSESSIONSREQUEST,
            output_type=_RESERVEALLREGISTEREDSESSIONSRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_SESSIONMANAGEMENTSERVICE)

DESCRIPTOR.services_by_name["SessionManagementService"] = _SESSIONMANAGEMENTSERVICE

# @@protoc_insertion_point(module_scope)