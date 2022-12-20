from dataclasses import dataclass, field
from typing import List, Optional


@dataclass()
class FeatureParameters:
    categorical_features: List[str]
    numerical_features: List[str]
    target_column: Optional[str]
    use_logarithm_trick: bool = field(default=False)
