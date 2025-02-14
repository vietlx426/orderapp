from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from app.api.v1.api import api_router
from app.schedulers.closepool import init_scheduler
from app.websockets import endpoints as websocket_endpoints


app = FastAPI(
    title="Food Ordering App",
    version="1.0.0",
    openapi_url="/api/v1/openapi.json",
    docs_url="/docs",
    swagger_ui_oauth2_redirect_url="/docs/oauth2-redirect",
)

# Add security scheme
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    # Initialize and start scheduler
    scheduler = init_scheduler()
    scheduler.start()

@app.on_event("shutdown")
async def shutdown_event():
    # Shutdown scheduler
    scheduler = init_scheduler()
    scheduler.shutdown()

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
        
    openapi_schema = get_openapi(
        title="Food Ordering API",
        version="1.0.0",
        description="Food Ordering API with OAuth2",
        routes=app.routes,
    )
    
    # Add security schemes
    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2PasswordBearer": {
            "type": "oauth2",
            "flows": {
                "password": {
                    "tokenUrl": "/api/v1/auth/token",
                    "scopes": {}
                }
            }
        }
    }  
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

# Include routers
app.include_router(api_router, prefix="/api/v1")
app.include_router(websocket_endpoints.router)
