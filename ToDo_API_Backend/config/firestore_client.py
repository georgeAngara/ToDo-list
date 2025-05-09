from google.cloud import firestore

# Inicializa el cliente de Firestore
db = firestore.Client(project="p-george")

# Puedes también inicializar con una clave manual:
# db = firestore.Client.from_service_account_json("ruta/clave.json")