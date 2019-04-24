from .config import db


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.String(255), primary_key=True)
    user_id = db.Column(db.String(255), db.ForeignKey('users.id'))
    room_id = db.Column(db.String(255), db.ForeignKey('rooms.id'))
    content = db.Column(db.Text)
    created_at = db.Column(db.Time)

    def __init__(self, user_id, room_id, content, created_at):
        self.user_id = user_id
        self.room_id = room_id
        self.content = content
        self.created_at = created_at

    def __to_dict__(self):
        return {
            'comment': {
                'id': self.id,
                'user_id': self.user_id,
                'room_id': self.room_id,
                'content': self.content,
                'created_at': self.created_at,
            }
        }
