from dataclasses import dataclass
from typing import Any, Optional

@dataclass
class ModelState:
    model: Optional[Any] = None
_state = ModelState()
    
def set_model(model: Any) -> None:
        _state.model = model
    
def get_model() -> Any:
        if _state.model is None:
            raise RuntimeError("Model is not loaded.")
        return _state.model