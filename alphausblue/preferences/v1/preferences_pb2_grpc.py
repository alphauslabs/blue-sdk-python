# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from alphausblue.preferences.v1 import preferences_pb2 as preferences_dot_v1_dot_preferences__pb2


class PreferencesStub(object):
    """Preferences service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetPreferences = channel.unary_unary(
                '/blueapi.preferences.v1.Preferences/GetPreferences',
                request_serializer=preferences_dot_v1_dot_preferences__pb2.GetPreferencesRequest.SerializeToString,
                response_deserializer=preferences_dot_v1_dot_preferences__pb2.Preference.FromString,
                )


class PreferencesServicer(object):
    """Preferences service definition.
    """

    def GetPreferences(self, request, context):
        """WORK-IN-PROGRESS: Gets current preferences.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PreferencesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetPreferences': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPreferences,
                    request_deserializer=preferences_dot_v1_dot_preferences__pb2.GetPreferencesRequest.FromString,
                    response_serializer=preferences_dot_v1_dot_preferences__pb2.Preference.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'blueapi.preferences.v1.Preferences', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Preferences(object):
    """Preferences service definition.
    """

    @staticmethod
    def GetPreferences(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.preferences.v1.Preferences/GetPreferences',
            preferences_dot_v1_dot_preferences__pb2.GetPreferencesRequest.SerializeToString,
            preferences_dot_v1_dot_preferences__pb2.Preference.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
