from unittest import TestCase
from unittest.mock import MagicMock, patch
from get_nacionality import get_nacionality_by_name
from MyException import MyException


class Test(TestCase):
    @patch("requests.get")
    def test_get_nacionality_by_name(self, mock_requests):
        mock_response = MagicMock()
        mock_response.text = """
        {   
            "name" : "david",
            "country" : [
                {
                    "country_id" : "GB",
                    "probability" : 0.044
                },
                {
                    "country_id" : "ES",
                    "probability" : 0.042
                }
            ]
        }
        """
        mock_requests.return_value = mock_response
        country_code = get_nacionality_by_name("david")
        self.assertEqual(country_code, "GB")

    def test_normal_get_nacionality_by_name(self):
        #test sin mock
        country_code = get_nacionality_by_name("david")
        print(country_code)
        self.assertEqual(country_code, "GB")

    @patch("requests.get")
    def test_error_get_nacionality_by_name(self, mock_requests):
        MagicMock(side_effect=ConnectionError)

        mock_requests.side_effect = ConnectionError
        self.assertRaises(MyException, get_nacionality_by_name, "david" )

    @patch("requests.get")
    def test_error_get_nacionality_by_name(self, mock_requests):
        MagicMock(side_effect=ConnectionError)

        mock_requests.side_effect = TimeoutError
        with self.assertRaises(MyException) as cm:
            get_nacionality_by_name("david")
        self.assertEqual(cm.exception.message, "Error timeout" )