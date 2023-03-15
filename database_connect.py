import postgresql
# connect to PostgreSQL (DigitalOcean database)


def connect(user: str, password: str, host: str, port: str, name: str):
    url = f'postgresql://{user}:{password}@{host}:{port}/{name}'
    return postgresql.open(url)


db = connect(
    'doadmin',
    '*********',
    'bookforces-do-user-12590875-0.b.db.ondigitalocean.com',
    '25060',
    'defaultdb')
