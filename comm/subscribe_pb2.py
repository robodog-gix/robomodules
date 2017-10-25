# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: subscribe.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='subscribe.proto',
  package='roboModules',
  syntax='proto2',
  serialized_pb=_b('\n\x0fsubscribe.proto\x12\x0broboModules\"\xcb\x01\n\tSubscribe\x12\x11\n\tmsg_types\x18\x01 \x03(\x05\x12-\n\x03\x64ir\x18\x02 \x02(\x0e\x32 .roboModules.Subscribe.Direction\x12\x31\n\x08protocol\x18\x03 \x02(\x0e\x32\x1f.roboModules.Subscribe.Protocol\"+\n\tDirection\x12\r\n\tSUBSCRIBE\x10\x00\x12\x0f\n\x0bUNSUBSCRIBE\x10\x01\"\x1c\n\x08Protocol\x12\x07\n\x03TCP\x10\x00\x12\x07\n\x03UDP\x10\x01')
)



_SUBSCRIBE_DIRECTION = _descriptor.EnumDescriptor(
  name='Direction',
  full_name='roboModules.Subscribe.Direction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUBSCRIBE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSUBSCRIBE', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=163,
  serialized_end=206,
)
_sym_db.RegisterEnumDescriptor(_SUBSCRIBE_DIRECTION)

_SUBSCRIBE_PROTOCOL = _descriptor.EnumDescriptor(
  name='Protocol',
  full_name='roboModules.Subscribe.Protocol',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TCP', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UDP', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=208,
  serialized_end=236,
)
_sym_db.RegisterEnumDescriptor(_SUBSCRIBE_PROTOCOL)


_SUBSCRIBE = _descriptor.Descriptor(
  name='Subscribe',
  full_name='roboModules.Subscribe',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg_types', full_name='roboModules.Subscribe.msg_types', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dir', full_name='roboModules.Subscribe.dir', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='protocol', full_name='roboModules.Subscribe.protocol', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SUBSCRIBE_DIRECTION,
    _SUBSCRIBE_PROTOCOL,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=236,
)

_SUBSCRIBE.fields_by_name['dir'].enum_type = _SUBSCRIBE_DIRECTION
_SUBSCRIBE.fields_by_name['protocol'].enum_type = _SUBSCRIBE_PROTOCOL
_SUBSCRIBE_DIRECTION.containing_type = _SUBSCRIBE
_SUBSCRIBE_PROTOCOL.containing_type = _SUBSCRIBE
DESCRIPTOR.message_types_by_name['Subscribe'] = _SUBSCRIBE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Subscribe = _reflection.GeneratedProtocolMessageType('Subscribe', (_message.Message,), dict(
  DESCRIPTOR = _SUBSCRIBE,
  __module__ = 'subscribe_pb2'
  # @@protoc_insertion_point(class_scope:roboModules.Subscribe)
  ))
_sym_db.RegisterMessage(Subscribe)


# @@protoc_insertion_point(module_scope)
