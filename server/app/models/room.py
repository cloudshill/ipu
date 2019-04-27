from uuid import uuid4

from .config import db


def uuid4_for_str():
    return str(uuid4())


class Room(db.Model):
    __tablename__ = 'rooms'

    id = db.Column(db.String(255), primary_key=True, default=uuid4_for_str)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime)
    thumbnail_url = db.Column(db.String(255), nullable=True)
    users = db.relationship("User", backref="rooms")
    comments = db.relationship("Comment", backref="rooms")

    def __repr__(self):
        return 'id: {}, name: {}, created_at: {}, thumbnail_url: {}, users: {}'. \
            format(self.id, self.name, self.created_at, self.thumbnail_url, self.users)

    def __to_dict__(self):
        return {
            'room': {
                'id': self.id,
                'name': self.name,
                'created_at': self.created_at,
                'thumbnail_url': self.thumbnail_url,
                'users': self.users,
            }
        }
