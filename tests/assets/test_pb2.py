# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b"\n\ntest.proto\x12'ni.measurementlink.measurement.tests.v1\"\x8c\x03\n\x14MeasurementParameter\x12\x12\n\nfloat_data\x18\x01 \x01(\x02\x12\x13\n\x0b\x64ouble_data\x18\x02 \x01(\x01\x12\x12\n\nint32_data\x18\x03 \x01(\x05\x12\x13\n\x0buint32_data\x18\x04 \x01(\r\x12\x12\n\nint64_data\x18\x05 \x01(\x03\x12\x13\n\x0buint64_data\x18\x06 \x01(\x04\x12\x11\n\tbool_data\x18\x07 \x01(\x08\x12\x13\n\x0bstring_data\x18\x08 \x01(\t\x12\x19\n\x11\x64ouble_array_data\x18\t \x03(\x01\x12\x18\n\x10\x66loat_array_data\x18\n \x03(\x02\x12\x18\n\x10int32_array_data\x18\x0b \x03(\x05\x12\x19\n\x11uint32_array_data\x18\x0c \x03(\r\x12\x18\n\x10int64_array_data\x18\r \x03(\x03\x12\x19\n\x11uint64_array_data\x18\x0e \x03(\x04\x12\x17\n\x0f\x62ool_array_data\x18\x0f \x03(\x08\x12\x19\n\x11string_array_data\x18\x10 \x03(\tB7\xaa\x02\x34NationalInstruments.MeasurementServices.Measurementsb\x06proto3"
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "test_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = (
        b"\252\0024NationalInstruments.MeasurementServices.Measurements"
    )
    _MEASUREMENTPARAMETER._serialized_start = 56
    _MEASUREMENTPARAMETER._serialized_end = 452
# @@protoc_insertion_point(module_scope)
