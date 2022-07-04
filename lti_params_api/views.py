"""
Views for the lti_params_api app.
"""
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from common.djangoapps.util.views import ensure_valid_course_key
from lti_params_api.serializers import LTIListParamSerializer
from openedx.core.lib.api.view_utils import view_auth_classes

from lti_params_api.utils import get_usage_ids, get_block_data
from lti_params_api.patch.course_experience_utils_custom import (
    get_course_outline_block_tree
)


@view_auth_classes(is_authenticated=True)
class LTIParams(APIView):
    """
    This class will handle API request and filter data.
    """
    @ensure_valid_course_key
    def get(self, request):

        lti_metadata = []
        course_id = request.query_params.get('course_id')
        if course_id:

            course_block_tree = get_course_outline_block_tree(
                request,
                course_id
            )

            lti_usage_ids = get_usage_ids(course_block_tree)

            for lti_usage_data in lti_usage_ids:
                lti_metadata.append(get_block_data(lti_usage_data))

            lti_serialized_data = LTIListParamSerializer(
                lti_metadata,
                many=True
            )

            return Response(lti_serialized_data.data)
        else:
            return Response(
                {
                    "developer_message": "please provide valid course_id"
                },
                status.HTTP_400_BAD_REQUEST
            )
