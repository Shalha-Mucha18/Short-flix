from mangum import Mangum
from backend.app.main import app

handler = Mangum(app, lifespan="off", api_gateway_base_path="/api/shorts")

__all__ = ["handler"]
