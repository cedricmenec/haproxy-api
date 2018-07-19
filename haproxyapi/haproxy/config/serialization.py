from marshmallow import Schema, fields

class HaProxyConfigOptionSchema(Schema):
    keyword = fields.String()
    value = fields.String()

class HaProxyConfigConfigSchema(Schema):
    keyword = fields.String()
    value = fields.String()

class HaProxyConfigServerSchema(Schema):
    name = fields.String()
    host = fields.String()
    port = fields.Integer()
    attributes = fields.List(fields.String())

class HaProxyConfigBindSchema(Schema):
    host = fields.String()
    port = fields.Integer()
    attributes = fields.List(fields.String())

class HaProxyConfigAclSchema(Schema):
    name = fields.String()
    value = fields.String()

class HaProxyConfigGroupSchema(Schema):
    name = fields.String()
    user_names = fields.List(fields.String())

class HaProxyConfigUseBackendSchema(Schema):
    backend_condition = fields.String()
    backend_name = fields.String()
    is_default = fields.Boolean()
    operator = fields.String()

class HaProxyConfigUserSchema(Schema):
    name = fields.String()
    passwd = fields.String()
    passwd_type = fields.String()
    group_names = fields.List(fields.String())

class HaProxyConfigBlockSchema(Schema):
    options = fields.Nested(HaProxyConfigOptionSchema, many=True)
    configs = fields.Nested(HaProxyConfigConfigSchema, many=True)
    servers = fields.Nested(HaProxyConfigServerSchema, many=True)
    binds = fields.Nested(HaProxyConfigBindSchema, many=True)
    acls = fields.Nested(HaProxyConfigAclSchema, many=True)
    users = fields.Nested(HaProxyConfigUserSchema, many=True)
    groups = fields.Nested(HaProxyConfigGroupSchema, many=True)
    usebackends = fields.Nested(HaProxyConfigUseBackendSchema, many=True)

class HaProxyConfigNamedConfigBlockSchema(HaProxyConfigBlockSchema):
    name = fields.String()

class HaProxyConfigSchema(Schema):
    globall = fields.Nested(HaProxyConfigBlockSchema)
    defaults = fields.Nested(HaProxyConfigNamedConfigBlockSchema, many=True)
    listens = fields.Nested(HaProxyConfigNamedConfigBlockSchema, many=True)
    backends = fields.Nested(HaProxyConfigNamedConfigBlockSchema, many=True)
    frontends = fields.Nested(HaProxyConfigNamedConfigBlockSchema, many=True)
