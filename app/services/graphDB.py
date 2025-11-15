"""_summary_

Returns:
    _type_: _description_
"""
import neo4j

# Neo4j connection (add your connection details)
NEO4J_URI = "neo4j+ssc://02fdb929.databases.neo4j.io"  # Update with your Neo4j URI
NEO4J_USER = "neo4j"  # Update with your username
NEO4J_PASSWORD = "TM8o8VAxEtLEszI0rpJ-iRdnJWMFhg3qWXGXTNXNBZo"  # Update with your password


def get_driver():
    return neo4j.GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
