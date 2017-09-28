import os
import unittest
import tempfile
from flask import json
import datetime

import server


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, server.app.config['DATABASE'] = tempfile.mkstemp()
        server.app.testing = True
        self.app = server.app.test_client()
        server.app.app_context()

    def del_action(self, name):
        return self.app.delete('/del_action?name=' + name,
                               follow_redirects=True)

    def add_action(self, name, freq):
        return self.app.post('/add_action', data=json.dumps(dict(
                             name=name,
                             freq=freq
                             )), follow_redirects=True)

    def test_del_action(self):
        rv = self.del_action('sport')
        assert 'delete' in rv.data

    def test_add_action(self):
        rv = self.add_action('sport', 3)
        assert 'add' in rv.data

    def add_point(self, name, date):
        return self.app.post('/add_point', data=json.dumps(dict(
                             name=name,
                             date=str(date)
                             )), follow_redirects=True)

    def test_add_point(self):
        rv = self.add_point('sport', datetime.datetime.now().date())
        assert 'add point' in rv.data
        rv = self.add_point('sport1', datetime.datetime.now().date())
        assert 'add point' in rv.data
        rv = self.add_point('sport', datetime.datetime.now().date())
        assert 'add point' in rv.data
        rv = self.add_point('sport1', datetime.datetime.now().date())
        assert 'add point' in rv.data

    def show_week(self, start_date, end_date):
        return self.app.get('/show_week?start=' + start_date +
                            '&end=' + end_date,
                            follow_redirects=True)

    def test_show_week(self):
        rv = self.show_week('2017-09-25', '2017-09-28')
        assert 'show week' in rv.data

if __name__ == '__main__':
    unittest.main()
