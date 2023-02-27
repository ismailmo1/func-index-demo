from time import monotonic

from sqlalchemy.exc import IntegrityError, OperationalError

from app import app, db

with app.app_context():
    start_time = monotonic()
    elapsed_seconds = 0
    retry_timeout_sec = 30
    while elapsed_seconds < retry_timeout_sec:
        try:
            db.create_all()
        except OperationalError:
            # db hasn't started up yet - retry
            elapsed_seconds = monotonic() - start_time
            continue
        except IntegrityError:
            # we've already created tables
            # should use factory pattern to circumvent this in real apps
            break

if __name__ == "__main__":
    app.run()
