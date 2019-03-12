import sqlite3

# TODO: Update insert to update version table
# TODO: Update select statement to join table so I can see the full CI and version in one go
# TODO: Test to ensure that ci_version table is working as expected and referenctial integrity is maintained
# TODO: Next learn to import from csv and write into CI objects.
# TODO: Next learn object marshalling and make CI objects somewhat persistent. 
conn = sqlite3.connect(":memory:")
# Enabling foreign keys for sqlite3
conn.execute("PRAGMA foreign_keys = 1")
# 'cmdb.db')
from ci import ConfigurationItem

ci_1 = ConfigurationItem('PMP Template', 'Template', 'PMP')
ci_2 = ConfigurationItem('Organizational Change Request Template', 'Form', 'OCRF')

c = conn.cursor()
# TODO: Add acive or inactive as an attribute and field in database.
c.execute("""CREATE TABLE cis (
          id integer PRIMARY KEY,
          doc_type text,
          identifier text,
          name text
          )""")

# TODO: Add release date to the version table
c.execute("""CREATE TABLE version (
          id integer PRIMARY KEY,
          version int,
          minor int,
          doc_number text,
          pending int,
          released int
          )""")

c.execute("""CREATE TABLE ci_version (
            id integer PRIMARY KEY,
            version_id int,
            ci_id int,
            FOREIGN KEY(version_id) REFERENCES version(id),
            FOREIGN KEY(ci_id) REFERENCES cis(id))""")


def insert_ci(ci):
    with conn:
        c.execute("INSERT into cis VALUES(NULL, :type, :identifier,:name)",
            {'type':ci.type,'identifier': ci.identifier,'name':ci.name})
    # TODO: insert relevant data into versions table as well
def deactivate_ci(ci):
    pass
def update_status(ci):
    # with conn:
    #     c.execute()
    # TODO: insert relevant data into versions table as well
    pass
def get_cis(identifier=""):
    if identifier == "":
        c.execute("SELECT * from CIs")
    else:
        c.execute("SELECT * from cis WHERE identifier = :identifier",
        {'identifier': identifier})
    return c.fetchall()

insert_ci(ci_1)
insert_ci(ci_2)
print(get_cis())

conn.close()
