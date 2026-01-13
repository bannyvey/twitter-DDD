from fastapi import Depends, APIRouter

from my_twitter.features.user.dependencies import get_find_user_by_id_use_case
from my_twitter.features.user.domain.use_cases.find_by_id_user import FindByIdUserUseCase

router = APIRouter()

@router.get("/{id}")
async def find_by_id_router(
        id: int,
        find_by_id_use_case: FindByIdUserUseCase = Depends(get_find_user_by_id_use_case)
):
    result = await find_by_id_use_case(id)
    return result
