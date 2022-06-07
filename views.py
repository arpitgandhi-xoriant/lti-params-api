"""
Views for the lti_params_api app.
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from xmodule.modulestore.django import modulestore
from cms.djangoapps.contentstore.views.helpers import usage_key_with_run
from cms.djangoapps.lti_params_api.serializers import LTIListParamSerializer


class LTIParams(APIView):
    """
    This class will handle API request and filter data.
    """
    def get(self, request, usage_id):
        lti_metadata = []
        lti_metadata.append(self.get_block_data(usage_id))


        lti_serialized_data = LTIListParamSerializer(lti_metadata, many=True)
        return Response(lti_serialized_data.data)


    def get_block_data(self, usage_id):
        usage_key = usage_key_with_run(usage_id)

        module_store = modulestore()
        lti_info = module_store.get_item(usage_key)

        lti_info_dict = {}
        lti_info_dict["block_key"] = usage_id
        lti_info_dict["display_name"] = lti_info.display_name
        lti_info_dict['launch_url'] = lti_info.launch_url
        lti_info_dict['tool_id'] = str(lti_info.tool_id)
        lti_info_dict['custom_parameters'] = lti_info.custom_parameters
        lti_info_dict['scored'] = lti_info.has_score
        lti_info_dict['send_email'] = lti_info.ask_to_send_email
        lti_info_dict['send_name'] = lti_info.ask_to_send_name
        lti_info_dict['send_username'] = lti_info.ask_to_send_username

        return lti_info_dict