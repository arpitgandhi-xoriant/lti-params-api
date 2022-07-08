"""
Settings for the lti_params_api app.
"""

from os.path import abspath, dirname, join


def root(*args):
    """
    Get the absolute path of the given path relative to the project root.
    """
    return join(abspath(dirname(__file__)), *args)


USE_TZ = True

INSTALLED_APPS = (
    'lti_params_api',
)

def plugin_settings(settings):  # pylint: disable=unused-argument
    """
    Defines lti_params_api-specific settings when app is used as a plugin to edx-platform.
    """
    pass