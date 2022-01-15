from datetime import datetime

from fastapi import APIRouter
# from sqlalchemy.orm import Session
from starlette.responses import Response

# from app.database.conn import db
# from app.database.schema import Users

from starlette.requests import Request
from inspect import currentframe as frame

router = APIRouter()


@router.get("/")
async def index():
    """
    ELB 상태 체크용 API
    :return:
    """
    # user = Users(status='active', name="HelloWorld")
    # session.add(user)
    # session.commit()
    #
    # Users().create(session, auto_commit=True, name="코알라")

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
