import httpx
import logging
from typing import Optional, Dict, Any
from pydantic import BaseModel

logger = logging.getLogger(__name__)

AUTH_SERVICE_URL = "http://135.181.99.53:8910"


class LoginRequest(BaseModel):
    email: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: Optional[Dict[str, Any]] = None


class AuthServiceError(Exception):
    """Custom exception for auth service errors"""
    pass


async def authenticate_user(email: str, password: str) -> LoginResponse:
    """
    Authenticate user by calling the auth service at localhost:8001
    
    Args:
        email: User's email address
        password: User's password
        
    Returns:
        LoginResponse with access_token
        
    Raises:
        AuthServiceError: If authentication fails
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{AUTH_SERVICE_URL}/auth/login",
                json={
                    "email": email,
                    "password": password
                },
                timeout=10.0
            )
            
            if response.status_code != 200:
                error_detail = "Invalid credentials"
                try:
                    error_data = response.json()
                    error_detail = error_data.get("detail", error_detail)
                except:
                    pass
                raise AuthServiceError(error_detail)
            
            data = response.json()
            
            # Validate required fields
            if "access_token" not in data:
                raise AuthServiceError("Invalid response from auth service")
            
            return LoginResponse(
                access_token=data.get("access_token"),
                token_type=data.get("token_type", "bearer"),
                user=data.get("user")
            )
            
    except httpx.ConnectError as e:
        logger.error(f"Failed to connect to auth service: {e}")
        raise AuthServiceError("Authentication service unavailable. Please try again later.")
    except httpx.TimeoutException as e:
        logger.error(f"Auth service timeout: {e}")
        raise AuthServiceError("Authentication service timeout. Please try again later.")
    except Exception as e:
        logger.error(f"Unexpected error during authentication: {e}")
        raise AuthServiceError("An unexpected error occurred during authentication")
