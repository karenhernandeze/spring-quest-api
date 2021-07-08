import sqlalchemy
metadata = sqlalchemy.MetaData()

categories = sqlalchemy.Table(
    "categories",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("category_name", sqlalchemy.String)
)
