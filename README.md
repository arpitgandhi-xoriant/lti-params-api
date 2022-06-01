# LTI PARAMS API


This app is to get params of Advantage LTIs.



Install
-------
Clone app in cms/djangoapps:

    git clone https://github.com/arpitgandhi-xoriant/lti_params_api.git
    
add app in cms/envs/common.py under "INSTALLED_APPS":

    "cms.djangoapps.lti_params_api"
    
Add url in cms/urls.py:

    urlpatterns += [
        url(r'api/lti_params_api/', include('cms.djangoapps.lti_params_api.urls'))
    ]


> Restart CMS

    
API Call
---
    
    <studio_url>/api/lti_params_api/lti_params_list/<usage_key>

