from fastapi import APIRouter

router = APIRouter(prefix="/reference", tags=["reference"])

FAKE_DATA = {
    "sites": ["A", "B"],
    "customers": ["Customer1", "Customer2"],
    "rate-codes": ["R1", "R2"],
    "origins": ["Origin1", "Origin2"],
}

@router.get("/{name}")
async def get_reference(name: str):
    return FAKE_DATA.get(name, [])
