"""
URL definitions for the lti_params_api app.
"""
from django.urls import re_path

from lti_params_api.views import LTIParams


urlpatterns = [
    re_path(
        r'^lti_params_list/$',
        LTIParams.as_view(),
        name="get-lti-params-list"
    ),
]
