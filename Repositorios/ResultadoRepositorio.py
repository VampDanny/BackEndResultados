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

    # Numero de Votos Totales
    def getTotalVotos(self):
        query = {
            "$group":{
                "_id": "$candidato",
                "total_votos": {
                    "$sum": 1
                },
                "doc": {
                    "$first": "$$ROOT"
                }
            }
        }
        pipeline = [query]
        return self.queryAggregation(pipeline)
    
    # Numero de Votos Totales por Mesa
    def getTotalVotosMesas(self):
        query = {
            "$group":{
                "_id": "$mesa",
                "total_votos": {
                    "$sum": 1
                },
                "doc": {
                    "$first": "$$ROOT"
                }
            }
        }
        pipeline = [query]
        return self.queryAggregation(pipeline)

    # Numero de Votos Totales por Candidato
    def getTotalVotosCandidato(self, id_candidato):
        query1 = {
          "$match": {"candidato.$id": ObjectId(id_candidato)}
        }
        query2 = {
          "$group": {
            "_id": "$candidato",
            "votos_candidato": {
              "$sum": 1
            }
          }
        }
        pipeline = [query1,query2]
        return self.queryAggregation(pipeline)

    # Numero de Votos Totales por Partido
    def getVotosPartidos(self):
        query1 = {
          "$match": {"candidato.partido.$id"}
        }
        query2 = {
          "$group": {
            "_id": "$partido",
            "votos_partido": {
              "$sum": 1
            }
          }
        }
        pipeline = [query1,query2]
        return self.queryAggregation(pipeline)
