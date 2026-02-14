#storefront/utils.py
try:
    #django < 5.0
    from django.utils.timezone import utc
except ImportError:
    #django > 5.0
    from datetime import timezone
    utc = timezone.utc 