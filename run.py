from blogspace import app
import sqlalchemy as sa
import sqlalchemy.orm as so
from blogspace import app, db
from blogspace.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Post': Post}


if __name__ == "__main__":
    app.run(port=8000, debug=True)

