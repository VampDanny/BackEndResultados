from Repositorios.InterfazRepositorio import InterfazRepositorio
from Modelos.Resultado import Resultado
from bson import ObjectId

class ResultadoRepositorio(InterfazRepositorio[Resultado]):
    #Da las votaciones por mesa
    def getListadoCandidatosInscritosMesa(self, id_mesa):
        theQuery = {"mesa.$id": ObjectId(id_mesa)}
        return self.query(theQuery)

    #Da las votaciones por candidato
    def getListadoMesasCandidatoInscrito(self, id_candidato):
        theQuery = {"candidato.$id": ObjectId(id_candidato)}
        return self.query(theQuery)

    # Numero de Votos por candidato
    def getTotalVotos(self):
        query = {
            "$group":{
                "_id": "$candidato",
                "total_votos_candidato": {
                    "$sum": "1"
                },
                "doc": {
                    "$first": "$$ROOT"
                }
            }
        }
        pipeline = [query]
        return self.queryAggregation(pipeline)
