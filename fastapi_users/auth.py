from fastapi import HTTPException, Request

from fastapi_users.models import User


def get_user_by_id(user_id: int) -> User:
    session = SessionLocal()
    user = session.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


def get_current_user_info(request: Request) -> User:
    try:
        user_id = int(request.headers["X-User-ID"])
    except (KeyError, ValueError):
        raise HTTPException(status_code=401, detail="Unauthorized")

    return get_user_by_id(user_id)
