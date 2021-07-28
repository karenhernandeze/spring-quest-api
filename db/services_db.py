import sqlalchemy
metadata = sqlalchemy.MetaData()

service = sqlalchemy.Table(
    "services",
    metadata,
    sqlalchemy.Column("service_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("money_to_raise", sqlalchemy.String),
    sqlalchemy.Column("time_hrs", sqlalchemy.Integer),
    sqlalchemy.Column("description", sqlalchemy.String)
)
