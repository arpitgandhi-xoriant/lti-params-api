"""
URL definitions for the lti_params_api app.
"""
from django.conf import settings
from django.urls import re_path

from .views import LTIParams


urlpatterns = [
    re_path(
        r'^lti_params_list/{}/$'.format(
            settings.COURSE_ID_PATTERN
        ),
        LTIParams.as_view(),
        name="get-lti-params-list"
    ),
]
