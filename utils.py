"""
It will have helper methods for processing the LTI params.
"""
from cms.djangoapps.contentstore.views.helpers import usage_key_with_run
from xmodule.modulestore.django import modulestore

def get_usage_ids(course_block_tree):
    """
    This will return all the advanced LTI usage_id of the given course tree.
    """
    lti_usage_ids = []

    for chapter in course_block_tree.get('children', []):
        for sequential in chapter.get('children', []):
            for vertical in sequential.get('children', []):
                for component in vertical.get('children', []):
                    if component['type'] == 'lti_advantage_consumer':
                        lti_usage_ids.append(component['id'])

    return lti_usage_ids

def get_block_data(usage_id):
    """
    This will return metadata of given LTI in dict format.
    """
    usage_key = usage_key_with_run(usage_id)

    module_store = modulestore()
    lti_info = module_store.get_item(usage_key)

    lti_info_dict = {}
    lti_info_dict["block_key"] = usage_id
    lti_info_dict["display_name"] = lti_info.get_parent().display_name
    lti_info_dict['launch_url'] = lti_info.launch_url
    lti_info_dict['tool_id'] = str(lti_info.tool_id)
    lti_info_dict['custom_parameters'] = lti_info.custom_parameters
    lti_info_dict['scored'] = lti_info.has_score
    lti_info_dict['send_email'] = lti_info.ask_to_send_email
    lti_info_dict['send_name'] = lti_info.ask_to_send_name
    lti_info_dict['send_username'] = lti_info.ask_to_send_username

    return lti_info_dict
