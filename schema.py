# flask_sqlalchemy/schema.py
import graphene
from graphene import relay
from graphene import Scalar
from graphene import Mutation
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import db_session,Key as KeyModel
import rsa
import time;
from datetime import datetime

pubkey, privkey = rsa.newkeys(512)
from base64 import b64encode

class Key(SQLAlchemyObjectType):
    class Meta:
        model = KeyModel
        interfaces = (relay.Node, )

class CreateKey(graphene.Mutation):
    class Arguments:
        name = graphene.String()
    ok = graphene.Boolean()
    key = graphene.Field(lambda: Key)

    @staticmethod
    def mutate(root, info,name):
        data = name + str(time.time())
        signature = rsa.sign(data.encode('utf-8'), privkey, 'SHA-1')
        value = b64encode(signature).decode('ascii') 
        key = KeyModel(id=None,name=name,value=value,created_at= datetime.now())
        db_session.add(key)
        db_session.commit()
        ok = True
        
        return CreateKey(key=key, ok=ok)

class DeleteKey(graphene.Mutation):
    class Arguments:
        name = graphene.String()
    ok = graphene.Boolean()
    key = graphene.Field(lambda: Key)

    @staticmethod
    def mutate(root, info,name): 
        key = db_session.query(
        KeyModel).filter_by(name=name)
        key.delete()
        db_session.commit()
        ok = True
        return CreateKey(key=key, ok=ok)

class Mutations(graphene.ObjectType):
    create_key = CreateKey.Field()
    delete_key = DeleteKey.Field()
class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_keys = SQLAlchemyConnectionField(Key._meta.connection)

schema = graphene.Schema(query=Query,mutation=Mutations)
