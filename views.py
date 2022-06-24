"""
Views for the lti_params_api app.
"""
from edx_rest_framework_extensions.auth.jwt.authentication import JwtAuthentication
from edx_rest_framework_extensions.auth.session.authentication import \
    SessionAuthenticationAllowInactiveUser

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from common.djangoapps.util.views import ensure_valid_course_key
from lms.djangoapps.lti_params_api.serializers import LTIListParamSerializer
from openedx.core.lib.api.view_utils import view_auth_classes
from openedx.core.lib.api.authentication import OAuth2AuthenticationAllowInactiveUser

from .patch.course_experience_utils_custom import get_course_outline_block_tree
from .utils import get_usage_ids, get_block_data

class LTIParams(APIView):
    """
    This class will handle API request and filter data.
    """
    authentication_classes = (
        JwtAuthentication,
        OAuth2AuthenticationAllowInactiveUser,
        SessionAuthenticationAllowInactiveUser
    )
    permission_classes = (permissions.IsAuthenticated,)

    @ensure_valid_course_key
    @view_auth_classes(is_authenticated=True)
    def get(self, request, course_id):

        lti_metadata = []

        course_block_tree = get_course_outline_block_tree(request, course_id)

        lti_usage_ids = get_usage_ids(course_block_tree)

        for lti_usage_data in lti_usage_ids:
            lti_metadata.append(get_block_data(lti_usage_data))

        lti_serialized_data = LTIListParamSerializer(lti_metadata, many=True)

        return Response(lti_serialized_data.data)
