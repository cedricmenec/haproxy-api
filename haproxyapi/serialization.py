from marshmallow import Schema, fields

class BackendSchema(Schema):
    iid = fields.Integer()
    name = fields.String()
    requests = fields.Integer()
    status = fields.String()


class ServerSchema(Schema):
    sid = fields.Integer()
    name = fields.String()
    check_code = fields.Integer()
    check_status = fields.String()
    last_status = fields.String()
    status = fields.String()
    last_agent_check = fields.String()
    address = fields.String()
    requests = fields.Integer()
    weight = fields.Integer()
