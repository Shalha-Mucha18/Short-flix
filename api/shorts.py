try:
    from mangum import Mangum
    from backend.app.main import app
    
    handler = Mangum(app, lifespan="off", api_gateway_base_path="/api/shorts")
except Exception as e:
    # Fallback handler for debugging
    def handler(event, context):
        return {
            "statusCode": 500,
            "body": f"Error loading app: {str(e)}"
        }
