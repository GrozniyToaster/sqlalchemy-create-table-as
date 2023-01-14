# "Create Table As" form for SQLAlchemy

Add `create table as` construct to SQLalchemy

## Usage

Examples:
```python
>>> from sqlalchemy import *
>>> from sqlalchemy_create_table_as import *
>>> str(
...     CreateTableAs(
...         table('new_table'), 
...         select(column('f1'), column('f2')).select_from(table('old_table'))
...         )
... )
'CREATE TABLE new_table AS SELECT f1, f2 \nFROM old_table'
 
>>> t = Table('old_table', MetaData(), Column('f1'), Column('f2'))

>>> str(CreateTableAs(table('new_table'), select(t)))
>>> 'CREATE TABLE new_table AS SELECT old_table.f1, old_table.f2 \nFROM old_table'
```

## Installation

`sqlalchemy-create-table-as` is available on PyPI and can be installed via `pip`

```console
pip install sqlalchemy-create-table-as
```

## Acknowledgements
Package inspired by [sqlalchemy-views](https://pypi.org/project/sqlalchemy-views/) 

And thank you to the various [contributors](https://github.com/GrozniyToaster/sqlalchemy-create-table-as/pulse)!