# -*- coding: utf-8 -*-

from flask.ext.sqlalchemy import SQLAlchemy
import datetime

DB_CONNECTOR = 'sqlite:///week.db'
TEST_DB_CONNECTOR = 'sqlite:///test.db'


class ORM(object):

    def __init__(self, app):
        self.db = SQLAlchemy(app)

        class Action(self.db.Model):
            __tablename__ = 'action'

            id = self.db.Column(self.db.Integer, primary_key=True)
            name = self.db.Column(self.db.String)
            freq = self.db.Column(self.db.Integer)

            def __init__(self, name, freq):
                self.name = name
                self.freq = freq

            def __repr__(self):
                return "<Action('%s', '%d')>" % (self.name, self.freq)

        self.Action = Action
        self.db.create_all()

        class ActionDate(self.db.Model):
            __tablename__ = 'actiondate'

            id = self.db.Column(self.db.Integer, primary_key=True)
            name = self.db.Column(self.db.String)
            date = self.db.Column(self.db.Date)

            def __init__(self, name, date):
                self.name = name
                self.date = date

            def __repr__(self):
                return "<ActionDate('%s', '%s')>" % (self.name, self.date)

        self.ActionDate = ActionDate
        self.db.create_all()

    def add_action(self, name, freq):
        action = self.Action(name, freq)
        self.db.session.add(action)
        self.db.session.commit()

    def delete_action(self, name):
        action = self.Action.query.filter_by(name=name).first()
        self.db.session.delete(action)
        self.db.session.commit()

    def all_actions(self):
        return self.Action.query.all()

    def add_point(self, name, date):
        actiondate = self.ActionDate(name, date)
        self.db.session.add(actiondate)
        self.db.session.commit()

    def all_points_interval(self, start_date, end_date):
        return self.ActionDate.query.filter(
                    self.ActionDate.date.between(start_date, end_date)).all()
