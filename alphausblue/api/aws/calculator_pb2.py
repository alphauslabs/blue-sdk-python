# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/aws/calculator.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='api/aws/calculator.proto',
  package='blueapi.api.aws',
  syntax='proto3',
  serialized_options=b'\n\035cloud.alphaus.blueapi.api.awsB\025ApiAwsCalculatorProtoZ*github.com/alphauslabs/blue-sdk-go/api/aws',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18\x61pi/aws/calculator.proto\x12\x0f\x62lueapi.api.aws\"$\n\x13\x41\x64justmentsTypeList\x12\r\n\x05types\x18\x01 \x03(\t\"j\n\x18\x45xcludedServiceFromUsage\x12\x19\n\x11managementAccount\x18\x01 \x01(\t\x12\x13\n\x0bproductCode\x18\x02 \x01(\t\x12\x1e\n\x16\x63onvertedToAdjustments\x18\x03 \x01(\x08\"\xa3\x01\n\x10\x43\x61lculatorConfig\x12\x41\n\x13\x61\x64justmentsTypeList\x18\x01 \x01(\x0b\x32$.blueapi.api.aws.AdjustmentsTypeList\x12L\n\x19\x65xcludedServicesFromUsage\x18\x02 \x03(\x0b\x32).blueapi.api.aws.ExcludedServiceFromUsageBb\n\x1d\x63loud.alphaus.blueapi.api.awsB\x15\x41piAwsCalculatorProtoZ*github.com/alphauslabs/blue-sdk-go/api/awsb\x06proto3'
)




_ADJUSTMENTSTYPELIST = _descriptor.Descriptor(
  name='AdjustmentsTypeList',
  full_name='blueapi.api.aws.AdjustmentsTypeList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='types', full_name='blueapi.api.aws.AdjustmentsTypeList.types', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=45,
  serialized_end=81,
)


_EXCLUDEDSERVICEFROMUSAGE = _descriptor.Descriptor(
  name='ExcludedServiceFromUsage',
  full_name='blueapi.api.aws.ExcludedServiceFromUsage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='managementAccount', full_name='blueapi.api.aws.ExcludedServiceFromUsage.managementAccount', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='productCode', full_name='blueapi.api.aws.ExcludedServiceFromUsage.productCode', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='convertedToAdjustments', full_name='blueapi.api.aws.ExcludedServiceFromUsage.convertedToAdjustments', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=83,
  serialized_end=189,
)


_CALCULATORCONFIG = _descriptor.Descriptor(
  name='CalculatorConfig',
  full_name='blueapi.api.aws.CalculatorConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='adjustmentsTypeList', full_name='blueapi.api.aws.CalculatorConfig.adjustmentsTypeList', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='excludedServicesFromUsage', full_name='blueapi.api.aws.CalculatorConfig.excludedServicesFromUsage', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=192,
  serialized_end=355,
)

_CALCULATORCONFIG.fields_by_name['adjustmentsTypeList'].message_type = _ADJUSTMENTSTYPELIST
_CALCULATORCONFIG.fields_by_name['excludedServicesFromUsage'].message_type = _EXCLUDEDSERVICEFROMUSAGE
DESCRIPTOR.message_types_by_name['AdjustmentsTypeList'] = _ADJUSTMENTSTYPELIST
DESCRIPTOR.message_types_by_name['ExcludedServiceFromUsage'] = _EXCLUDEDSERVICEFROMUSAGE
DESCRIPTOR.message_types_by_name['CalculatorConfig'] = _CALCULATORCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdjustmentsTypeList = _reflection.GeneratedProtocolMessageType('AdjustmentsTypeList', (_message.Message,), {
  'DESCRIPTOR' : _ADJUSTMENTSTYPELIST,
  '__module__' : 'api.aws.calculator_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.api.aws.AdjustmentsTypeList)
  })
_sym_db.RegisterMessage(AdjustmentsTypeList)

ExcludedServiceFromUsage = _reflection.GeneratedProtocolMessageType('ExcludedServiceFromUsage', (_message.Message,), {
  'DESCRIPTOR' : _EXCLUDEDSERVICEFROMUSAGE,
  '__module__' : 'api.aws.calculator_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.api.aws.ExcludedServiceFromUsage)
  })
_sym_db.RegisterMessage(ExcludedServiceFromUsage)

CalculatorConfig = _reflection.GeneratedProtocolMessageType('CalculatorConfig', (_message.Message,), {
  'DESCRIPTOR' : _CALCULATORCONFIG,
  '__module__' : 'api.aws.calculator_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.api.aws.CalculatorConfig)
  })
_sym_db.RegisterMessage(CalculatorConfig)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
