from datetime import datetime

from fastapi import APIRouter
from starlette.responses import Response
from starlette.requests import Request
from inspect import currentframe as frame

router = APIRouter()


@router.get("/")
async def index(session: Session = Depends(db.session),):
    """
    ELB 상태 체크용 API
    :return:
    """
    user = Users(status='active', name="HelloWorld")
    session.add(user)
    session.commit()

    User().creat(session, auto_commit=True, name="코알라")
    current_time = datetime.utcnow()
    return Response(f"Notification API (UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')})")


@router.get("/test")
async def test(request: Request):
    """
    ELB 상태 체크용 API
    :return:
    """
    print("state.user", request.state.user)
    try:
        a = 1/0
    except Exception as e:
        request.state.inspect = frame()
        raise e
    current_time = datetime.utcnow()
    return Response(f"Notification API (UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')})")