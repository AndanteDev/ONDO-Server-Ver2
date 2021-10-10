from starlette import status


class APIException(Exception):
    status_code: int
    msg: str
    detail: str

    def __init__(
        self,
        *,
        status_code: int = status.HTTP_503_SERVICE_UNAVAILABLE,
        detail: str = None,
        ex: Exception = None,
    ):
        self.status_code = status_code
        self.detail = detail
        super().__init__(ex)


class PermissionDeniedException(APIException):
    def __init__(self, ex: Exception = None):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"You do not have permission to make this request.",
            ex=ex,
        )


class TodayDiaryAlreadyExistsException(APIException):
    def __init__(self, ex: Exception = None):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Today diary already exists. Try tomorrow",
            ex=ex,
        )


class FailToSaveChangeException(APIException):
    def __init__(self, ex: Exception = None):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Fail to save change, Try again",
            ex=ex,
        )
