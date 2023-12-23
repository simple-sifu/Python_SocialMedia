from pydantic import BaseModel

# BaseModel is using for type declaration
class UserPostIn(BaseModel):
    body: str


class UserPost(UserPostIn):
    id: int
