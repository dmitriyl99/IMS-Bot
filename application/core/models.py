from application import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model):
    """
    Model for users in bot
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    username = db.Column(db.String(100))
    phone_number = db.Column(db.String(15))
    language = db.Column(db.String(5))
    company_name = db.Column(db.String)
    calls = db.relationship('Call', lazy='dynamic', backref='user')


class AdminUser(db.Model, UserMixin):
    """
    Model for users in administration panel
    """
    __tablename__ = 'admin_users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), index=True)
    password_hash = db.Column(db.String(120))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Call(db.Model):
    """
    Model for call orders
    """
    __tablename__ = 'calls'
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(15))
    time = db.Column(db.String(50))
    confirmed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class TVChannel(db.Model):
    """
    Model for TV channels
    """
    __tablename__ = 'tv_channels'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    price_files = db.relationship('PriceFile', lazy='dynamic')


class PriceFile(db.Model):
    """
    Model for prices in files
    """
    __tablename__ = 'price_files'
    id = db.Column(db.Integer, primary_key=True)
    telegram_id = db.Column(db.String)
    file_path = db.Column(db.String)
    channel_id = db.Column(db.Integer, db.ForeignKey('tv_channels.id'))
    is_package = db.Column(db.Boolean, default=False)


class AdCampaign(db.Model):
    """
    Model for advertising campaigns
    """
    __tablename__ = 'ad_campaigns'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(150))
    target_audience = db.Column(db.String)
    age_of_audience = db.Column(db.String)

    class TargetAudiences:
        MALE = 'male'
        FEMALE = 'female'
        MALE_AND_FEMALE = 'male_and_female'


class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    text_ru = db.Column(db.String)
    text_uz = db.Column(db.String)


class FAQ(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text_ru = db.Column(db.String)
    text_uz = db.Column(db.String)


@login.user_loader
def load_user(user_id):
    return AdminUser.query.get(int(user_id))
