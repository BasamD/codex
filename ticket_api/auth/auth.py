from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Dummy token data
TOKENS = {
    "internal": {"scopes": ["internal"]},
    "external": {"scopes": ["external"], "customer_id": 1},
}

async def get_current_token(token: str = Depends(oauth2_scheme)):
    token_data = TOKENS.get(token)
    if not token_data:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return token_data

def check_scope(required: str):
    async def checker(token_data = Depends(get_current_token)):
        if required not in token_data["scopes"]:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
    return checker
