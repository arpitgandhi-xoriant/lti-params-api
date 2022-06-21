"""
Views for the lti_params_api app.
"""
from rest_framework.views import APIView
from rest_framework.response import Response

from .patch.course_experience_utils_custom import get_course_outline_block_tree
from .utils import get_usage_ids, get_block_data

from lms.djangoapps.lti_params_api.serializers import LTIListParamSerializer
from common.djangoapps.util.views import ensure_valid_course_key

class LTIParams(APIView):
    """
    This class will handle API request and filter data.
    """
    @ensure_valid_course_key
    def get(self, request, course_id):

        lti_metadata = []

        course_block_tree = get_course_outline_block_tree(request, course_id)

        lti_usage_ids = get_usage_ids(course_block_tree)

        for lti_usage_id in lti_usage_ids:
            lti_metadata.append(get_block_data(lti_usage_id))

        lti_serialized_data = LTIListParamSerializer(lti_metadata, many=True)

        return Response(lti_serialized_data.data)
