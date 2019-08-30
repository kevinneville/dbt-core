from typing import Any, Optional

from . import data_types


class Table:
    def __init__(self, rows: Any, column_names: Optional[Any] = ..., column_types: Optional[Any] = ..., row_names: Optional[Any] = ..., _is_fork: bool = ...) -> None: ...
    def __len__(self): ...
    def __iter__(self): ...
    def __getitem__(self, key: Any): ...
    @property
    def column_types(self): ...
    @property
    def column_names(self): ...
    @property
    def row_names(self): ...
    @property
    def columns(self): ...
    @property
    def rows(self): ...
    def print_csv(self, **kwargs: Any) -> None: ...
    def print_json(self, **kwargs: Any) -> None: ...


class TypeTester:
    def __init__(self, force: Any = ..., limit: Optional[Any] = ..., types: Optional[Any] = ...) -> None: ...
    def run(self, rows: Any, column_names: Any): ...