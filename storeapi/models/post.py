from pydantic import BaseModel

# BaseModel is using for type declaration
class UserPostIn(BaseModel):
    body: str


class UserPost(UserPostIn):
    id: int


class CommentIn(BaseModel):
    body: str
    post_id: int


class Comment(CommentIn):
    id: int


class UserPostWithComments(BaseModel):
    post: UserPost
    comments: list[Comment]


# {
#     "post": { "id": 0, "body": "My Post"},
#     "comments": [{"id": 2, "post_id": 0, "body": "My comment"}]
# }
