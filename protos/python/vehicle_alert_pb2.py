# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vehicle_alert.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13vehicle_alert.proto\x12\x18telemetry.vehicle_alerts\x1a\x1fgoogle/protobuf/timestamp.proto\"\x84\x01\n\rVehicleAlerts\x12\x36\n\x06\x61lerts\x18\x01 \x03(\x0b\x32&.telemetry.vehicle_alerts.VehicleAlert\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0b\n\x03vin\x18\x03 \x01(\t\"\xb1\x01\n\x0cVehicleAlert\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x35\n\taudiences\x18\x02 \x03(\x0e\x32\".telemetry.vehicle_alerts.Audience\x12.\n\nstarted_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nded_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp*B\n\x08\x41udience\x12\x0b\n\x07Unknown\x10\x00\x12\x0c\n\x08\x43ustomer\x10\x01\x12\x0b\n\x07Service\x10\x02\x12\x0e\n\nServiceFix\x10\x03\x42/Z-github.com/teslamotors/fleet-telemetry/protosb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vehicle_alert_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z-github.com/teslamotors/fleet-telemetry/protos'
  _AUDIENCE._serialized_start=397
  _AUDIENCE._serialized_end=463
  _VEHICLEALERTS._serialized_start=83
  _VEHICLEALERTS._serialized_end=215
  _VEHICLEALERT._serialized_start=218
  _VEHICLEALERT._serialized_end=395
# @@protoc_insertion_point(module_scope)
