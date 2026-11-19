from pydantic import BaseModel, Field

class EstadoInput(BaseModel):
    nome: str = Field(..., min_length=2, max_length=100, examples=["Santa Catarina"])
    sigla: str = Field(..., min_length=2, max_length=2, examples=["SC"])

class EstadoResponse(EstadoInput):
    id: int = Field(..., examples=[1])