# core/context_processors.py
from .admin_sidebar import ADMIN_SIDEBAR_MENU

def admin_sidebar_context(request):
    return {"admin_sidebar_menu": ADMIN_SIDEBAR_MENU}
