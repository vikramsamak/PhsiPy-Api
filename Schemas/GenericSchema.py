from pydantic import BaseModel

from typing import Any, Dict, Generic, TypeVar

T = TypeVar("T")


class GenericResponse(BaseModel, Generic[T]):
    Definition: str
    Given: Dict[str, Any]
    Result: T
