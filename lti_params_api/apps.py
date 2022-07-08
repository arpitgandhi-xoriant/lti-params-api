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
                'regex': r'',
                'relative_path': 'urls',
            },
        },
        'settings_config': {
            'lms.djangoapp': {
                'common': {
                    'relative_path': 'settings.common',
                },
            },
        }
    }
