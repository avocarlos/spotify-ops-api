from graphene import Mutation, String
from spotify import SpotifyAPI

class Authenticate(Mutation):
    class Arguments():
        code = String(required = True)

    jwt = String()

    def mutate(root, info, code):
        response = SpotifyAPI.getToken(code)
        return Authenticate(jwt = response.code)


