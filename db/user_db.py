import sqlalchemy
metadata = sqlalchemy.MetaData()

user = sqlalchemy.Table(
    "users_beneficiary",
    metadata,
    sqlalchemy.Column("user_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("birth", sqlalchemy.Date),
    sqlalchemy.Column("codigo_postal", sqlalchemy.String),
    sqlalchemy.Column("address_user", sqlalchemy.String),
    sqlalchemy.Column("country", sqlalchemy.String),
    sqlalchemy.Column("email", sqlalchemy.String),
    sqlalchemy.Column("first_name", sqlalchemy.String),
    sqlalchemy.Column("gender", sqlalchemy.String),
    sqlalchemy.Column("last_name", sqlalchemy.String),
    sqlalchemy.Column("officialdocument", sqlalchemy.String),
    sqlalchemy.Column("officialdocument2", sqlalchemy.String),
    sqlalchemy.Column("password_user", sqlalchemy.String),
    sqlalchemy.Column("proofofaddress", sqlalchemy.String),
    sqlalchemy.Column("user_type", sqlalchemy.String),
)
