"""
Serializers for use in the lti_params_api app.
"""

import json

from rest_framework import serializers

from xmodule.modulestore.django import modulestore

class LTIListParamSerializer(serializers.Serializer):
    """
    LTIListParamSerializer to serialize LTI data.
    """

    block_key = serializers.CharField(max_length=None)
    display_name = serializers.CharField(max_length=None)
    launch_url = serializers.CharField(max_length=None)
    tool_id = serializers.CharField(max_length = 12)
    custom_parameters = serializers.ListField()
    scored = serializers.BooleanField()
    send_email = serializers.BooleanField()
    send_name = serializers.BooleanField()
    send_username = serializers.BooleanField()
