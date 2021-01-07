from .base import *

# export ENV=PROD <- in production
# export ENV=DEV <- in development

if os.getenv("ENV") == "DEV":
    from .dev import *
elif os.getenv("ENV") == "PROD":
    from .prod import *
