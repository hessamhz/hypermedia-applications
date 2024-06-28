from os import environ

stage = environ.get("STAGE")
if not stage:
    raise ValueError("stage is not set")

if stage == "dev":
    from settings.dev import *
elif stage == "production":
    from settings.production import *
