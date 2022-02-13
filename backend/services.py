import databases as _databases


def create_database():
    return _databases.Base.metadata.create_all(bind=_databases.engine)