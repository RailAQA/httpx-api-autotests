from clients.users.users_schema import CreateUserResponseSchema, CreateUsersRequestSchema, UserSchema
from tools.assertions.base import assert_equal


def assert_create_user_response(request: CreateUsersRequestSchema, response: CreateUserResponseSchema):
    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.first_name, request.first_name, "first_name")
    assert_equal(response.user.middle_name, request.middle_name, "middle_name")

def assert_user(request: UserSchema, response: UserSchema):
    assert_equal(actual=response.id, expected=request.id)
    assert_equal(actual=response.email, expected=request.email)
    assert_equal(actual=response.last_name, expected=request.last_name)
    assert_equal(actual=response.first_name, expected=request.first_name)
    assert_equal(actual=response.middle_name, expected=request.middle_name)
