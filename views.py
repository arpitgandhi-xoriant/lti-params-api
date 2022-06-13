"""
Views for the lti_params_api app.
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from xmodule.modulestore.django import modulestore
from openedx.features.course_experience.utils import get_course_outline_block_tree

from cms.djangoapps.contentstore.views.helpers import usage_key_with_run
try:
    from common.djangoapps.util.views import ensure_valid_course_key
except ImportError:
    from util.views import ensure_valid_course_key

class LTIParams(APIView):
    """
    This class will handle API request and filter data.
    """
    @ensure_valid_course_key
    def get(self, request, course_id):
        lti_usage_keys = []
        lti_metadata = []

        course_block_tree = get_course_outline_block_tree(request, course_id)

        for chapter in course_block_tree.get('children') or []:
            for sequential in chapter.get('children') or []:
                for vertical in sequential.get('children') or []:
                    for component in vertical.get('children') or []:
                        if component['type'] == 'lti_advantage_consumer':
                            lti_usage_keys.append(component['id'])

        return Response(lti_usage_keys)

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
