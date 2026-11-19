from fastapi import APIRouter, HTTPException, status
from schemas.estado_schema import EstadoInput, EstadoResponse
from services.estado_service import EstadoService

router = APIRouter(prefix="/estados", tags=["Estados"])

service = EstadoService()

@router.get("/", response_model=list[EstadoResponse], status_code=status.HTTP_200_OK)
def listar_estados():
    return service.listar_todos()

@router.get("/{estado_id}", response_model=EstadoResponse, status_code=status.HTTP_200_OK)
def buscar_estado(estado_id: int):
    estado = service.buscar_por_id(estado_id)
    if not estado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Estado não encontrado.",
        )
    return estado

@router.post("/", response_model=EstadoResponse, status_code=status.HTTP_201_CREATED)
def criar_estado(dados: EstadoInput):
    novo_estado = service.criar(dados)
    if not novo_estado:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro ao salvar o estado no banco de dados.",
        )
    return novo_estado

@router.put("/{estado_id}", response_model=EstadoResponse, status_code=status.HTTP_200_OK)
def atualizar_estado(estado_id: int, dados: EstadoInput):
    estado_atualizado = service.atualizar(estado_id, dados)
    if not estado_atualizado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Estado não encontrado para atualização",
        )
    return estado_atualizado
@router.delete("/{estado_id}", status_code=status.HTTP_200_OK)
def excluir_estado(estado_id: int):
    sucesso = service.excluir(estado_id)
    if not sucesso:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            datail="Estado não encontrado para exclusão.",
        )
    return {"mensagem": "Estado excluído com sucesso!"}

