from sqlalchemy.sql import (
    ClauseElement,
    Executable,
    Select,
    TableClause,
)

class CreateTableAs(Executable, ClauseElement):

    def __init__(self, table: TableClause, selectable: Select) -> None:
        ...
