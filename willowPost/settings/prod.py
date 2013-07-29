from __init__.py import *
DEBUG = False

TEMPLATE_LOADERS = (
(
    'django.template.loaders.cached.Loader', (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    ),
    ),
)
CACHES['default']['KEY_PREFIX'] = 'willowPost'
DATABASES['default']['NAME'] = 'willowPost'
