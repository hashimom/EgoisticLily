# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: elily.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='elily.proto',
  package='elilypb',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0b\x65lily.proto\x12\x07\x65lilypb\"\x1c\n\nConvertReq\x12\x0e\n\x06in_str\x18\x01 \x01(\t\".\n\x0b\x43onvertResp\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07out_str\x18\x02 \x01(\t\"#\n\x11PartialConvertReq\x12\x0e\n\x06in_str\x18\x01 \x01(\t\"5\n\x12PartialConvertResp\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07out_str\x18\x02 \x03(\t2\x93\x01\n\x0c\x45LilyService\x12\x36\n\x07\x43onvert\x12\x13.elilypb.ConvertReq\x1a\x14.elilypb.ConvertResp\"\x00\x12K\n\x0ePartialConvert\x12\x1a.elilypb.PartialConvertReq\x1a\x1b.elilypb.PartialConvertResp\"\x00\x62\x06proto3')
)




_CONVERTREQ = _descriptor.Descriptor(
  name='ConvertReq',
  full_name='elilypb.ConvertReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='in_str', full_name='elilypb.ConvertReq.in_str', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=52,
)


_CONVERTRESP = _descriptor.Descriptor(
  name='ConvertResp',
  full_name='elilypb.ConvertResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='elilypb.ConvertResp.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='out_str', full_name='elilypb.ConvertResp.out_str', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=100,
)


_PARTIALCONVERTREQ = _descriptor.Descriptor(
  name='PartialConvertReq',
  full_name='elilypb.PartialConvertReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='in_str', full_name='elilypb.PartialConvertReq.in_str', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=102,
  serialized_end=137,
)


_PARTIALCONVERTRESP = _descriptor.Descriptor(
  name='PartialConvertResp',
  full_name='elilypb.PartialConvertResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='elilypb.PartialConvertResp.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='out_str', full_name='elilypb.PartialConvertResp.out_str', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=192,
)

DESCRIPTOR.message_types_by_name['ConvertReq'] = _CONVERTREQ
DESCRIPTOR.message_types_by_name['ConvertResp'] = _CONVERTRESP
DESCRIPTOR.message_types_by_name['PartialConvertReq'] = _PARTIALCONVERTREQ
DESCRIPTOR.message_types_by_name['PartialConvertResp'] = _PARTIALCONVERTRESP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConvertReq = _reflection.GeneratedProtocolMessageType('ConvertReq', (_message.Message,), {
  'DESCRIPTOR' : _CONVERTREQ,
  '__module__' : 'elily_pb2'
  # @@protoc_insertion_point(class_scope:elilypb.ConvertReq)
  })
_sym_db.RegisterMessage(ConvertReq)

ConvertResp = _reflection.GeneratedProtocolMessageType('ConvertResp', (_message.Message,), {
  'DESCRIPTOR' : _CONVERTRESP,
  '__module__' : 'elily_pb2'
  # @@protoc_insertion_point(class_scope:elilypb.ConvertResp)
  })
_sym_db.RegisterMessage(ConvertResp)

PartialConvertReq = _reflection.GeneratedProtocolMessageType('PartialConvertReq', (_message.Message,), {
  'DESCRIPTOR' : _PARTIALCONVERTREQ,
  '__module__' : 'elily_pb2'
  # @@protoc_insertion_point(class_scope:elilypb.PartialConvertReq)
  })
_sym_db.RegisterMessage(PartialConvertReq)

PartialConvertResp = _reflection.GeneratedProtocolMessageType('PartialConvertResp', (_message.Message,), {
  'DESCRIPTOR' : _PARTIALCONVERTRESP,
  '__module__' : 'elily_pb2'
  # @@protoc_insertion_point(class_scope:elilypb.PartialConvertResp)
  })
_sym_db.RegisterMessage(PartialConvertResp)



_ELILYSERVICE = _descriptor.ServiceDescriptor(
  name='ELilyService',
  full_name='elilypb.ELilyService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=195,
  serialized_end=342,
  methods=[
  _descriptor.MethodDescriptor(
    name='Convert',
    full_name='elilypb.ELilyService.Convert',
    index=0,
    containing_service=None,
    input_type=_CONVERTREQ,
    output_type=_CONVERTRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='PartialConvert',
    full_name='elilypb.ELilyService.PartialConvert',
    index=1,
    containing_service=None,
    input_type=_PARTIALCONVERTREQ,
    output_type=_PARTIALCONVERTRESP,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ELILYSERVICE)

DESCRIPTOR.services_by_name['ELilyService'] = _ELILYSERVICE

# @@protoc_insertion_point(module_scope)