# -*- coding: utf-8 -*-
from flask.ext.security import Security, SQLAlchemyUserDatastore
from coin import coin
from coin.models import db, Role, User

user_datastore = SQLAlchemyUserDatastore(db, User, Role)

security = Security(coin, user_datastore)


@security.context_processor
def security_context_processor():

    return dict()


@security.mail_context_processor
def security_mail_processor():

    return dict()


# [Emails with Celery](https://pythonhosted.org/Flask-Security/customizing.html#emails-with-celery)