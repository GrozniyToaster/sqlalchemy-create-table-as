from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql import (
    ClauseElement,
    Executable,
)



class CreateTableAs(Executable, ClauseElement):

    def __init__(self, table, selectable):
        self.table = table
        self.query = selectable


@compiles(CreateTableAs)
def visit_create_table_as(element, compiler, **kw):
    return "CREATE TABLE %s AS %s" % (
        compiler.process(element.table, asfrom=True, **kw),
        compiler.process(element.query)
    )
