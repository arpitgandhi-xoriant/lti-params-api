"""
Tests for lti_params_api
"""
from common.djangoapps.student.roles import CourseInstructorRole
from common.djangoapps.student.tests.factories import UserFactory
from rest_framework.test import APIClient
from rest_framework.test import force_authenticate
from xmodule.modulestore.tests.django_utils import ModuleStoreTestCase
from xmodule.modulestore.tests.factories import CourseFactory, ItemFactory


class TestLTIParams(ModuleStoreTestCase):
    """
    Tests for lti_params_api
    """
    def setUp(self):
        super(TestLTIParams, self).setUp()
        course = CourseFactory.create(
            org='edX',
            course='100',
            display_name='lti_course',
        )
        chapter = ItemFactory.create(
            category='chapter',
            parent_location=course.location
        )
        section = ItemFactory.create(
            category='sequential',
            parent_location=chapter.location
        )
        vertical = ItemFactory.create(
            category='vertical',
            parent_location=section.location,
            display_name='Télécharger et utiliser Cisco Packet Tracer'
        )
        ItemFactory.create(
            category='lti_advantage_consumer',
            parent_location=vertical.location,
            ask_to_send_email=True,
            ask_to_send_name=True,
            custom_parameters=["course=i2cs", "version=7.1", "lang=en", "module=m0/", "app=sgp", "launch=adl"],
            has_score=True,
            launch_url='https://hub-qa.netacad.com/kernel/lti/launch?client_id=573080',
            display_name='knowledge_check',
            tool_id=99
        )

        self.course_id = course.id

    def test_lti_params(self):
        """
        Test for lti_params returned correctly.
        """

        instructor = UserFactory()
        CourseInstructorRole(self.course_id).add_users(instructor)

        client = APIClient()
        client.force_authenticate(user=instructor)

        query_string = '/api/lti_params_api/lti_params_list/?course_id={0}'.format(self.course_id)
        response = client.get(query_string)
        data = response.data[0]
        self.assertEqual('i4x://edX/100/lti_advantage_consumer/knowledge_check', data['block_key'])
        self.assertEqual(data['display_name'], 'Télécharger et utiliser Cisco Packet Tracer')
        self.assertEqual(data['launch_url'], 'https://hub-qa.netacad.com/kernel/lti/launch?client_id=573080')
        self.assertEqual(data['lti_display_name'], 'knowledge_check')
        self.assertEqual(data['tool_id'], '99')
        self.assertEqual(data['custom_parameters'], ["course=i2cs", "version=7.1", "lang=en", "module=m0/", "app=sgp", "launch=adl"])
        self.assertEqual(data['scored'], True)
        self.assertEqual(data['send_email'], True)
        self.assertEqual(data['send_name'], True)

    def test_no_course(self):
        """
        Test for no course in request.
        """

        instructor = UserFactory()
        CourseInstructorRole(self.course_id).add_users(instructor)

        client = APIClient()
        client.force_authenticate(user=instructor)

        query_string = '/api/lti_params_api/lti_params_list/'
        response = client.get(query_string)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, {'developer_message': 'please provide valid course_id'})

    def test_no_authentication(self):
        """
        Test for no authentication provided.
        """

        client = APIClient()
        query_string = '/api/lti_params_api/lti_params_list/?course_id={0}'.format(self.course_id)
        response = client.get(query_string)

        self.assertEqual(response.status_code, 401)
