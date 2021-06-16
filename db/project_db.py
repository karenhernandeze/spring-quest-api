import sqlalchemy

metadata = sqlalchemy.MetaData()

project = sqlalchemy.Table(
    "projects",
    metadata,
    sqlalchemy.Column("project_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("userid", sqlalchemy.String),
    sqlalchemy.Column("projectname", sqlalchemy.String),
    sqlalchemy.Column("projecttype", sqlalchemy.String),
    sqlalchemy.Column("exepctedstartdate", sqlalchemy.Date),
    sqlalchemy.Column("exepctedenddate", sqlalchemy.Date),
    sqlalchemy.Column("country", sqlalchemy.String),
    sqlalchemy.Column("city", sqlalchemy.String),
    sqlalchemy.Column("categoryid", sqlalchemy.String),
    sqlalchemy.Column("collaboratorsid", sqlalchemy.String),
    sqlalchemy.Column("photosid", sqlalchemy.String),
    sqlalchemy.Column("phases", sqlalchemy.Integer),
    sqlalchemy.Column("currentphase", sqlalchemy.Integer),
    sqlalchemy.Column("serviceid", sqlalchemy.String),

    # sqlalchemy.Column("services" ),
    # sqlalchemy.Column("moneyToRaise" ),
    # sqlalchemy.Column("knowledge" ),
    # sqlalchemy.Column("people" ),
    # sqlalchemy.Column("payment" ),
)
