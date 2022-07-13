import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL


@strawberry.type
class User:
    name: str
    age: int
    user_class: str


@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> User:
        return User(name="Patrick", age=100, user_class='bandit')
    
users: list[str] = []

@strawberry.type
class Mutation:
    @strawberry.field
    def add_user(self, name: str) -> str:
        users.append(name,)
        return name
    
@strawberry.type
class Query:
    @strawberry.field
    def users(self) -> list[str]:
        return users


schema = strawberry.Schema(query=Query, mutation=Mutation)


graphql_app = GraphQL(schema)

app = FastAPI()
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)