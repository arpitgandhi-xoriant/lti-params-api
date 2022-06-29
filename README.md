# LTI PARAMS API


This app is to get params of Advantage LTIs.



Install
-------
Clone app in your edx-platform:

    git clone https://github.com/arpitgandhi-xoriant/lti-params-api.git
    
Install app in your devstack:

    pip install lti-params-api/
    
Add url in lms/urls.py:

    urlpatterns += [
        url(r'api/lti_params_api/', include('lti_params_api.urls'))
    ]


> Restart LMS

    
API Call
---
    
    <lms_url>/api/lti_params_api/lti_params_list/?course_id=<encoded_course_id_string>
