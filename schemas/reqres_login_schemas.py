
from voluptuous import Schema, PREVENT_EXTRA

login_pass_schema = Schema(
    {
        "token": str,
    },
    extra=PREVENT_EXTRA,
    required=True
)

login_fail_schema = Schema({
    "error": "Missing password"
},
    extra=PREVENT_EXTRA,
    required=True
)