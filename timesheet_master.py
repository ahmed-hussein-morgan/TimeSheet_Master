# type: ignore
import os
from app import Create_app, db
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Create_app('development')

# db = SQLAlchemy(app)

migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    from app.models import Machine  # Import models here
    return dict(db=db, Machine=Machine, Role=Role, IT=IT, Ticket=Ticket, UserTicket=UserTicket)