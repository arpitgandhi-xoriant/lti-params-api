"""
App Configuration for lti_params_api
"""
from django.apps import AppConfig


class LTIParamsAPIConfig(AppConfig):
    name = 'lti_params_api'
    verbose_name = "LTI Params API"

    plugin_app = {
        'url_config': {
            'lms.djangoapp': {
                'namespace': 'lti_params_api',
                'regex': r'^api/lti_params_api/lti_params_list/',
                'relative_path': 'urls',
            },
        }
    }