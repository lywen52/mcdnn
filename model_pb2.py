# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: model.proto

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
  name='model.proto',
  package='uw.syhan.mcdnn',
  serialized_pb=_b('\n\x0bmodel.proto\x12\x0euw.syhan.mcdnn\"\x95\x01\n\x0eModelParameter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12)\n\x04type\x18\x02 \x02(\x0e\x32\x1b.uw.syhan.mcdnn.RequestType\x12\x0f\n\x07\x63ompute\x18\x03 \x01(\t\x12\x0e\n\x06memory\x18\x04 \x01(\t\x12\x17\n\x0floading_latency\x18\x05 \x01(\x02\x12\x10\n\x08\x61\x63\x63uracy\x18\x06 \x01(\x02\"P\n\x10\x41pplicationModel\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\x06models\x18\x02 \x03(\x0b\x32\x1e.uw.syhan.mcdnn.ModelParameter*#\n\x0bRequestType\x12\x08\n\x04\x46\x41\x43\x45\x10\x01\x12\n\n\x06OBJECT\x10\x02')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_REQUESTTYPE = _descriptor.EnumDescriptor(
  name='RequestType',
  full_name='uw.syhan.mcdnn.RequestType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FACE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OBJECT', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=265,
  serialized_end=300,
)
_sym_db.RegisterEnumDescriptor(_REQUESTTYPE)

RequestType = enum_type_wrapper.EnumTypeWrapper(_REQUESTTYPE)
FACE = 1
OBJECT = 2



_MODELPARAMETER = _descriptor.Descriptor(
  name='ModelParameter',
  full_name='uw.syhan.mcdnn.ModelParameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='uw.syhan.mcdnn.ModelParameter.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='uw.syhan.mcdnn.ModelParameter.type', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='compute', full_name='uw.syhan.mcdnn.ModelParameter.compute', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='memory', full_name='uw.syhan.mcdnn.ModelParameter.memory', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='loading_latency', full_name='uw.syhan.mcdnn.ModelParameter.loading_latency', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='accuracy', full_name='uw.syhan.mcdnn.ModelParameter.accuracy', index=5,
      number=6, type=2, cpp_type=6, label=1,
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
  serialized_start=32,
  serialized_end=181,
)


_APPLICATIONMODEL = _descriptor.Descriptor(
  name='ApplicationModel',
  full_name='uw.syhan.mcdnn.ApplicationModel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='uw.syhan.mcdnn.ApplicationModel.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='models', full_name='uw.syhan.mcdnn.ApplicationModel.models', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=183,
  serialized_end=263,
)

_MODELPARAMETER.fields_by_name['type'].enum_type = _REQUESTTYPE
_APPLICATIONMODEL.fields_by_name['models'].message_type = _MODELPARAMETER
DESCRIPTOR.message_types_by_name['ModelParameter'] = _MODELPARAMETER
DESCRIPTOR.message_types_by_name['ApplicationModel'] = _APPLICATIONMODEL
DESCRIPTOR.enum_types_by_name['RequestType'] = _REQUESTTYPE

ModelParameter = _reflection.GeneratedProtocolMessageType('ModelParameter', (_message.Message,), dict(
  DESCRIPTOR = _MODELPARAMETER,
  __module__ = 'model_pb2'
  # @@protoc_insertion_point(class_scope:uw.syhan.mcdnn.ModelParameter)
  ))
_sym_db.RegisterMessage(ModelParameter)

ApplicationModel = _reflection.GeneratedProtocolMessageType('ApplicationModel', (_message.Message,), dict(
  DESCRIPTOR = _APPLICATIONMODEL,
  __module__ = 'model_pb2'
  # @@protoc_insertion_point(class_scope:uw.syhan.mcdnn.ApplicationModel)
  ))
_sym_db.RegisterMessage(ApplicationModel)


# @@protoc_insertion_point(module_scope)
