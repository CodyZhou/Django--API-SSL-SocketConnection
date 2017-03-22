# from rest_framework.test import APIRequestFactory
#
# from pythontest import settings
# from django.core.management import setup_environ
#
#
# TEST_URL = 'http://localhost:8000/api/master/'
#
# factory = APIRequestFactory()
# request = factory.get(TEST_URL)
#
# print(request)
#
# assert request.status_code == 200

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class MasterServerTests(APITestCase):

    url = 'http://localhost:8000/api/master/'
    data_no_command = {"command":"","message":""}
    data_invalid_command = {"command":"testcommand","message":""}
    data_no_message = {"command":"run","message": ""}
    data_valid = {"command":"run","message": "This is a test from client!"}

    def test_get_request(self):
        """
        Used to test get request
        """
        reponse = self.client.get(self.url, format='json')

        self.assertEqual(reponse.status_code, status.HTTP_200_OK)
        self.assertEqual(reponse.content.decode('utf8'), '{"command":"","message":""}')

        # result = self.assertEqual(reponse.status_code, status.HTTP_200_OK)
        # print(reponse.content)
        # if result is None:
        #     print('OK!')
        # else:
        #     print('Not Pass!')
        #     print(reponse.status_code)

    def test_post_no_command(self):
        """
        Used to test bad request
        """
        reponse = self.client.post(self.url, data=self.data_no_command, format='json')
        # print(reponse.content)
        self.assertEqual(reponse.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(reponse.content.decode('utf8'), '{"command":["This field may not be blank."]}')

    def test_post_invalid_command(self):
        """
        Used to test bad request
        """
        reponse = self.client.post(self.url, data=self.data_invalid_command, format='json')
        # print(reponse.content)
        self.assertEqual(reponse.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(reponse.content.decode('utf8'), '{"command":["This command can not be accepted!"]}')

    def test_post_no_message(self):
        """
        Used to test bad request
        """
        reponse = self.client.post(self.url, data=self.data_no_message, format='json')
        # print(reponse.content)
        self.assertEqual(reponse.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(reponse.content.decode('utf8'), '{"errorMessage":"Can not get message, please check it!"}')

    def test_post_master_server_no_run(self):
        """
        Used to test send a valid data, but the master server does not run.
        """
        reponse = self.client.post(self.url, data=self.data_valid, format='json')
        print(reponse.content)
        self.assertEqual(reponse.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(reponse.content.decode('utf8'), '{"errorMessage":"Can not send data to master server!"}')

    def test_post_data_valid(self):
        """
        Used to test send a valid data, the master server does not run, everything is working.
        Notice: this method can not do the test at the same time with method test_post_master_server_no_run().
            Because this method need run master server first.
        """
        reponse = self.client.post(self.url, data=self.data_valid, format='json')
        # print(reponse.content)
        self.assertEqual(reponse.status_code, status.HTTP_200_OK)
        self.assertEqual(reponse.content.decode('utf8'), '{"result":"successful"}')


if __name__ == '__main__':

    mst = MasterServerTests()
    mst.test_get_request()

    mst.test_post_no_command()

