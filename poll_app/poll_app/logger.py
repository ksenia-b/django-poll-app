from cmreslogging.handlers import CMRESHandler
import logging

handler = CMRESHandler(hosts=[{'host': 'localhost', 'port': 9200}],
                           auth_type=CMRESHandler.AuthType.NO_AUTH,
                           es_index_name="my_python_index")
log = logging.getLogger("PythonTest")
log.setLevel(logging.INFO)
log.addHandler(handler)