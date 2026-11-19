from estado import Estado
from schemas.estado_schema import EstadoInput

class EstadoService:

    def listar_todos(self):
        estado = Estado()
        return estado.listar()
    
    def buscar_por_id(self,estado_id: int):
        estado = Estado()
        estado.id = estado_id
        return estado.buscar_por_id
    
    def criar(self, dados: EstadoInput):
        estado = Estado()
        estado.nome = dados.nome.strip()
        estado.sigla = dados.sigla.strip().upper()

        if estado.salvar():
            return {
                "id" : estado.id,
                "nome" : estado.nome,
                "sigla" : estado.sigla,
            }
        return None
    
    def atualizar (self, estado_id: int, dados: EstadoInput):
        estado = Estado()
        estado.id = estado_id

        if not estado.buscar_por_id():
            return None
        
        estado.nome = dados.nome.strip()
        estado.sigla = dados.sigla.strip().upper()
        estado.atualizar()

        return {
            "id" : estado.id,
            "nome" : estado.nome,
            "sigla" : estado.sigla,
        }
    
    def excluir (self, estado_id: int):
        estado = Estado()
        estado.id = estado_id
        return estado.excluir()