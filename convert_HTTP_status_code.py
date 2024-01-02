from fastapi import Response, status

def change_status_code(code: int, response: Response) -> None:
    if code == 400:
        response.status_code = status.HTTP_400_BAD_REQUEST
    elif code == 500:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR