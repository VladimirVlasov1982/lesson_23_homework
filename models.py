from marshmallow import Schema, fields, validates_schema, ValidationError

VALID_CMD_PARAMS = (
    "filter",
    "map",
    "unique",
    "sort",
    "limit"
)


class RequestSchema(Schema):
    file_name = fields.Str(required=True)
    cmd1 = fields.Str(required=True)
    value1 = fields.Str(required=True)
    cmd2 = fields.Str(required=True)
    value2 = fields.Str(required=True)

    @validates_schema
    def validate_request(self, values, *args, **kwargs):
        if values['cmd1'] not in VALID_CMD_PARAMS:
            raise ValidationError("'cmd1' is not valid")
        if values['cmd2'] not in VALID_CMD_PARAMS:
            raise ValidationError("'cmd2' is not valid")
        return values
