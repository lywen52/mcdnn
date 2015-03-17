# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: jni/define/uw/log.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='jni/define/uw/log.proto',
  package='uw.syhan.resourcemonitor',
  serialized_pb=_b('\n\x17jni/define/uw/log.proto\x12\x18uw.syhan.resourcemonitor\"n\n\nRMLogEntry\x12\x31\n\x04type\x18\x01 \x02(\x0e\x32#.uw.syhan.resourcemonitor.RMLogType\x12\x10\n\x08\x64\x61tetime\x18\x02 \x02(\x05\x12\x0c\n\x04\x64\x61ta\x18\x03 \x02(\x02\x12\r\n\x05\x64\x61ta2\x18\x04 \x01(\x02\"=\n\x06RMLogs\x12\x33\n\x05\x65ntry\x18\x01 \x03(\x0b\x32$.uw.syhan.resourcemonitor.RMLogEntry*l\n\tRMLogType\x12\x07\n\x03\x43PU\x10\x01\x12\n\n\x06MEMORY\x10\x02\x12\x0b\n\x07\x42\x41TTERY\x10\x03\x12\n\n\x06SCREEN\x10\x04\x12\x0b\n\x07NETWORK\x10\x05\x12\r\n\tBANDWIDTH\x10\x06\x12\x0c\n\x08NETSTATE\x10\x07\x12\x07\n\x03GPU\x10\x08')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_RMLOGTYPE = _descriptor.EnumDescriptor(
  name='RMLogType',
  full_name='uw.syhan.resourcemonitor.RMLogType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CPU', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MEMORY', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BATTERY', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SCREEN', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NETWORK', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BANDWIDTH', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NETSTATE', index=6, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GPU', index=7, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=228,
  serialized_end=336,
)
_sym_db.RegisterEnumDescriptor(_RMLOGTYPE)

RMLogType = enum_type_wrapper.EnumTypeWrapper(_RMLOGTYPE)
CPU = 1
MEMORY = 2
BATTERY = 3
SCREEN = 4
NETWORK = 5
BANDWIDTH = 6
NETSTATE = 7
GPU = 8



_RMLOGENTRY = _descriptor.Descriptor(
  name='RMLogEntry',
  full_name='uw.syhan.resourcemonitor.RMLogEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='uw.syhan.resourcemonitor.RMLogEntry.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='datetime', full_name='uw.syhan.resourcemonitor.RMLogEntry.datetime', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='uw.syhan.resourcemonitor.RMLogEntry.data', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data2', full_name='uw.syhan.resourcemonitor.RMLogEntry.data2', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=163,
)


_RMLOGS = _descriptor.Descriptor(
  name='RMLogs',
  full_name='uw.syhan.resourcemonitor.RMLogs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entry', full_name='uw.syhan.resourcemonitor.RMLogs.entry', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=165,
  serialized_end=226,
)

_RMLOGENTRY.fields_by_name['type'].enum_type = _RMLOGTYPE
_RMLOGS.fields_by_name['entry'].message_type = _RMLOGENTRY
DESCRIPTOR.message_types_by_name['RMLogEntry'] = _RMLOGENTRY
DESCRIPTOR.message_types_by_name['RMLogs'] = _RMLOGS
DESCRIPTOR.enum_types_by_name['RMLogType'] = _RMLOGTYPE

RMLogEntry = _reflection.GeneratedProtocolMessageType('RMLogEntry', (_message.Message,), dict(
  DESCRIPTOR = _RMLOGENTRY,
  __module__ = 'jni.define.uw.log_pb2'
  # @@protoc_insertion_point(class_scope:uw.syhan.resourcemonitor.RMLogEntry)
  ))
_sym_db.RegisterMessage(RMLogEntry)

RMLogs = _reflection.GeneratedProtocolMessageType('RMLogs', (_message.Message,), dict(
  DESCRIPTOR = _RMLOGS,
  __module__ = 'jni.define.uw.log_pb2'
  # @@protoc_insertion_point(class_scope:uw.syhan.resourcemonitor.RMLogs)
  ))
_sym_db.RegisterMessage(RMLogs)


# @@protoc_insertion_point(module_scope)