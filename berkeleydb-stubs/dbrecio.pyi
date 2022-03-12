from typing import Any

class DBRecIO:
    db: Any
    key: Any
    txn: Any
    len: Any
    pos: int
    closed: int
    softspace: int
    def __init__(self, db, key, txn: Any | None = ...) -> None: ...
    def close(self) -> None: ...
    def isatty(self): ...
    def seek(self, pos, mode: int = ...) -> None: ...
    def tell(self): ...
    def read(self, n: int = ...): ...
    def truncate(self, size: Any | None = ...) -> None: ...
    def write(self, s) -> None: ...
    def writelines(self, list) -> None: ...
    def flush(self) -> None: ...
