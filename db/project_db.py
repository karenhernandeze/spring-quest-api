import sqlalchemy
from sqlalchemy.sql.sqltypes import Integer, String

metadata = sqlalchemy.MetaData()

project = sqlalchemy.Table(
    "projects",
    metadata,
    sqlalchemy.Column("project_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("userid", sqlalchemy.String),
    sqlalchemy.Column("projectname", sqlalchemy.String),
    sqlalchemy.Column("projecttype", sqlalchemy.String),
    sqlalchemy.Column("description", sqlalchemy.String),
    sqlalchemy.Column("exepctedstartdate", sqlalchemy.String),
    sqlalchemy.Column("exepctedenddate", sqlalchemy.String),
    sqlalchemy.Column("country", sqlalchemy.String),
    sqlalchemy.Column("city", sqlalchemy.String),
    sqlalchemy.Column("categoryid", sqlalchemy.ARRAY(Integer)),
    sqlalchemy.Column("collaboratorsid", sqlalchemy.ARRAY(Integer)),
    sqlalchemy.Column("photosid", sqlalchemy.ARRAY(String)),
    sqlalchemy.Column("phases", sqlalchemy.Integer),
    sqlalchemy.Column("donorsid", sqlalchemy.ARRAY(Integer)),
    sqlalchemy.Column("serviceid", sqlalchemy.String),

    # sqlalchemy.Column("services" ),
    # sqlalchemy.Column("moneyToRaise" ),
    # sqlalchemy.Column("knowledge" ),
    # sqlalchemy.Column("people" ),
    # sqlalchemy.Column("payment" ),
)
