from .base import *

working_environment = env.str("WORK_ENV", default="local")


if working_environment == "production":
    from .production import *
elif working_environment == "staging":
    from .staging import *
elif working_environment == "test":
    from .test import *
else:
    from .local import *
