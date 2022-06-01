"""
URL definitions for the lti_params_api app.
"""


from django.conf.urls import url

from cms.djangoapps.lti_params_api import views


urlpatterns = [
    url(
        r'^lti_params_list/$',
        views.LTIParams.as_view(),
        name="get_lti_params_list"
    ),
]