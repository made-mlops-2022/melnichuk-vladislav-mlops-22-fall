from dataclasses import dataclass, field


@dataclass()
class TrainParameters:
    model_type: str = field(default="RandomForestRegressor")
    random_state: int = field(default=255)
