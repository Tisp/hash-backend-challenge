from os import getenv

GRPC_SERVER = getenv("GRPC_CONNECT_URL", "localhost:50051")
BLACK_FRIDAY_DATE = getenv("BLACK_FRIDAY_DATE", "27/11")
