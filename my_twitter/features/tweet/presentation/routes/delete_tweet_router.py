from fastapi import Path, Depends, HTTPException, status, APIRouter

from my_twitter.dependencies import get_current_user
from my_twitter.features.tweet.dependencies import get_delete_tweet_use_case
from my_twitter.features.tweet.domain.use_cases.delete_tweet import DeleteTweetUseCase

from my_twitter.features.user.domain.entities.user_entity import UserEntity


router = APIRouter()

@router.delete('/{id}')
async def delete_tweet_router(
        id: int = Path(description="Id tweet"),
        current_user: UserEntity = Depends(get_current_user),
        delete_tweet_use_case: DeleteTweetUseCase = Depends(get_delete_tweet_use_case)
):
    # try:
    await delete_tweet_use_case(id, current_user)
    # except TweetNotFound as e:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    # except AuthException as e:
    #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
    # except Exception as e:
    #     raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    return {"result": True}
