import strawberry
import fastapi
import strawberry.fastapi

@strawberry.type
class Query:
    @strawberry.field
    def hello(self,name : str)->str:
        return f'Hello {name}'

schema = strawberry.Schema(Query)

graphql_app = strawberry.fastapi.GraphQLRouter(schema)

app = fastapi.FastAPI()

app.include_router(graphql_app,prefix = '/graphql')