a="&&&"
str="abc+%%%%%+bcvv"
str=str.replace("%%%%%","a")
print(str)




# import sys
#
# from SPARQLWrapper import SPARQLWrapper, JSON, XML
# from rdflib import Graph
# import json
# #
# # sparql = SPARQLWrapper("http://localhost:3030/dataset.html?tab=query&ds=/KND")
# # sparql.setMethod("POST")
# #
# # sparql.setQuery("""
# # PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# # PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# # PREFIX owl: <http://www.w3.org/2002/07/owl#>
# # PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
# # PREFIX co: <https://raw.githubusercontent.com/tannineo/cs7is1-knd-project/master/chao_ontology.xml#>
# # PREFIX so: <http://schema.org/version/latest/schema.rdf>
# # PREFIX name: <http://schema.org/name>
# # PREFIX address: <http://schema.org/address>
# # PREFIX park: <http://schema.org/Park>
# # PREFIX oh: <http://schema.org/openingHours>
# # PREFIX contains: <http://schema.org/containsPlace>
# # PREFIX lat: <http://schema.org/latitude>
# # PREFIX long: <http://schema.org/longitude>
# # PREFIX geo: <https://schema.org/GeoCoordinates>
# # PREFIX so_geo: <http://schema.org/geo>
# # PREFIX fl: <http://www.w3.org/2001/XMLSchema#float>
# # SELECT ?name ?PARK_obj WHERE{
# # ?PARK_obj address: ?pg_location .
# # ?PARK_obj name: ?name .
# # FILTER regex(str(?PARK_obj) , 'playground')
# # }order by asc(UCASE(str(?name)))
# #
# # """)
# # # sparql.method
# # sparql.setReturnFormat(JSON)
# # # sparql.setRequestMethod("POST")
# # results = sparql.query().convert()
# # Ret=[]
# # print(results[1])
# # for result in results[0]:
# #     Ret.append(result["name"]["value"])
# # print(type(Ret))
# # print(Ret)
# #
# # # for result in results["results"]["bindings"]:
# # #     print(result)
# # # # print(results)
# from rdflib.plugins.sparql.results.jsonresults import JSONResultSerializer
#
# g = Graph()
# g.parse("D:/1.downloads/GalwayWeekendActivity (1).ttl)", format="ttl")
# qres = g.query("""
#
# PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# PREFIX owl: <http://www.w3.org/2002/07/owl#>
# PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
# PREFIX co: <https://raw.githubusercontent.com/tannineo/cs7is1-knd-project/master/chao_ontology.xml#>
# PREFIX so: <http://schema.org/version/latest/schema.rdf>
# PREFIX name: <http://schema.org/name>
# PREFIX address: <http://schema.org/address>
# PREFIX park: <http://schema.org/Park>
# PREFIX oh: <http://schema.org/openingHours>
# PREFIX contains: <http://schema.org/containsPlace>
# PREFIX lat: <http://schema.org/latitude>
# PREFIX long: <http://schema.org/longitude>
# PREFIX geo: <https://schema.org/GeoCoordinates>
# PREFIX so_geo: <http://schema.org/geo>
# PREFIX fl: <http://www.w3.org/2001/XMLSchema#float>
#     SELECT ?name ?PARK_obj WHERE{
# ?PARK_obj address: ?pg_location .
# ?PARK_obj name: ?name .
# FILTER regex(str(?PARK_obj) , 'playground')
# }order by asc(UCASE(str(?name)))
# """)
#
# JSONResultSerializer(qres).serialize(sys.stdout)
# #
# # sparql = SPARQLWrapper("http://localhost:3030/dataset.html?tab=query&ds=/KND")
# # sparql.setQuery("""
# #
# # PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# # PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# # PREFIX owl: <http://www.w3.org/2002/07/owl#>
# # PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
# # PREFIX co: <https://raw.githubusercontent.com/tannineo/cs7is1-knd-project/master/chao_ontology.xml#>
# # PREFIX so: <http://schema.org/version/latest/schema.rdf>
# # PREFIX name: <http://schema.org/name>
# # PREFIX address: <http://schema.org/address>
# # PREFIX park: <http://schema.org/Park>
# # PREFIX oh: <http://schema.org/openingHours>
# # PREFIX contains: <http://schema.org/containsPlace>
# # PREFIX lat: <http://schema.org/latitude>
# # PREFIX long: <http://schema.org/longitude>
# # PREFIX geo: <https://schema.org/GeoCoordinates>
# # PREFIX so_geo: <http://schema.org/geo>
# # PREFIX fl: <http://www.w3.org/2001/XMLSchema#float>
# #     SELECT ?name ?PARK_obj WHERE{
# # ?PARK_obj address: ?pg_location .
# # ?PARK_obj name: ?name .
# # FILTER regex(str(?PARK_obj) , 'playground')
# # }order by asc(UCASE(str(?name)))
# #
# #
# # """)
# #
# # # JSON example
# # print( '\n\n*** JSON Example')
# # sparql.setReturnFormat(XML)
# # results = sparql.query().convert()
# # print(results.toxml())
# # # for result in results["results"]["bindings"]:
# # #     print (result["name"]["value"])