"""
URL definitions for the lti_params_api app.
"""
from django.conf.urls import url

from .views import LTIParams


USAGE_ID_PATTERN = r'(?P<usage_id>(?:i4x://?[^/]+/[^/]+/[^/]+/[^@]+(?:@[^/]+)?)|(?:[^/]+))'

urlpatterns = [
    url(
        r'^lti_params_list/{usage_key}/$'.format(
            usage_key=USAGE_ID_PATTERN
        ),
        LTIParams.as_view(),
        name="get_lti_params_list"
    ),
]