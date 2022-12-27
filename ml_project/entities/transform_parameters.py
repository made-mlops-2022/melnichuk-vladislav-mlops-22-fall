from dataclasses import dataclass
from typing import Optional


@dataclass()
class TransformParameters:
    ohe_categorical: Optional[bool]
    normalize_numerical: Optional[bool]
