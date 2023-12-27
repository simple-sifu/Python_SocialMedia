from pydantic import BaseModel, ConfigDict

# BaseModel is using for type declaration
class UserPostIn(BaseModel):
    body: str


class UserPost(UserPostIn):
    id: int
    model_config = ConfigDict(from_attributes=True)


class CommentIn(BaseModel):
    body: str
    post_id: int


class Comment(CommentIn):
    id: int
    model_config = ConfigDict(from_attributes=True)


class UserPostWithComments(BaseModel):
    post: UserPost
    comments: list[Comment]


# {
#     "post": { "id": 0, "body": "My Post"},
#     "comments": [{"id": 2, "post_id": 0, "body": "My comment"}]
# }
