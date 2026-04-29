import os
import neo4j


NEO4J_URI = os.environ['NEO4J_URI']
NEO4J_USER = os.environ['NEO4J_USER']
NEO4J_PASSWORD = os.environ['NEO4J_PASSWORD']
# NEO4J_URI = 'neo4j+ssc://ed1d0e32.databases.neo4j.io'
# NEO4J_USER = 'ed1d0e32'
# NEO4J_PASSWORD = 'x3oyqu0Sdq83ozZnjrAvWBTX2_jC3bP8Oa88zDOGrbM'
# NEO4J_DATABASE = 'ed1d0e32'

def get_driver():
    return neo4j.GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
