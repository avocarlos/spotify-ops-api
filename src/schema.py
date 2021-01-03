from graphene import ObjectType, Schema
from resolvers.authentication import Authenticate

class Mutation(ObjectType):
    authenticate = Authenticate.Field()

schema = Schema(mutation=Mutation)