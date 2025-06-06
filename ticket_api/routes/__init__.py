from fastapi import APIRouter
from . import batches, tickets, history, reference

router = APIRouter()
router.include_router(batches.router)
router.include_router(tickets.router)
router.include_router(history.router)
router.include_router(reference.router)
