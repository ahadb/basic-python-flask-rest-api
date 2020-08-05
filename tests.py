import base64
import json
import unittest
from app import app


class BasicRestTestClass(unittest.TestCase):
    # initialization logic for the test suite declared in the test module
    # code that is executed before all tests in one test run
    @classmethod
    def setUpClass(cls):
        pass

    # clean up logic for the test suite declared in the test module
    # code that is executed after all tests in one test run
    @classmethod
    def tearDownClass(cls):
        pass

        # initialization logic
        # code that is executed before each test

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    # code that is executed after each test
    def tearDown(self):
        pass

        # test method

    def open_with_auth(self, url, method, username, password):
        return self.app.open(url,
                             method=method,
                             headers={
                                 'Authorization': 'Basic ' + base64.b64encode(
                                     bytes(username + ":" + password, 'ascii')).decode('ascii')
                             }
                             )

    def test_auth(self):
        result = self.open_with_auth('/', 'GET', 'ahad',
                                     'bokhari')
        self.assertEqual(result.status_code, 200)

    def test_index(self):
        res = self.open_with_auth('/', 'GET', 'ahad',
                                  'bokhari')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data, b'{"hello":"world"}\n')

    def test_get_tasks(self):
        result = self.open_with_auth('/todo/tasks', 'GET', 'ahad',
                                     'bokhari')
        self.assertEqual(result.status_code, 200)
        data = json.loads(result.get_data(as_text=True))
        learn_python = {'id': 1, 'title': 'Learn Python',
                        'description': 'A clever way to learn Python is to start with the basics', 'done': False}
        learn_flask = {'title': 'Learn Flask', 'description': 'Flask is one awesome package that is un-opinonated',
                       'id': 2, 'done': False}

        self.assertEqual(data["tasks"][0], learn_python)
        self.assertEqual(data["tasks"][1], learn_flask)
        self.assertEqual(data["tasks"][2]["done"], True)

    def test_get_task_by_id(self):
        result = self.open_with_auth('/todo/tasks/3', 'GET', 'ahad',
                                     'bokhari')
        self.assertEqual(result.status_code, 200)
        data = json.loads(result.get_data(as_text=True))
        self.assertEqual(data["task"]["done"], True)


# runs the unit tests in the module

if __name__ == '__main__':
    unittest.main()
