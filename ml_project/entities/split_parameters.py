from dataclasses import dataclass, field


@dataclass()
class SplitParameters:
    size_val: float = field(default=0.15)
    random_state: int = field(default=42)
