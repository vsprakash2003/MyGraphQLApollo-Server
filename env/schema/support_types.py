import graphene


class NewDeptInput(graphene.InputObjectType):
    departmentId = graphene.String(required=True)
    departmentName = graphene.String(required=True)