ADMIN_SIDEBAR_MENU = [
    {
        "id": "ADMIN_DASHBOARD",
        "name": "Dashboard",
        "icon": "fa-solid fa-gauge",  # Using Font Awesome or your preferred icons
        "path": "/adminpanel/dashboard/",
        "submenus": []
    },
     {
        "id": 'ADMIN_USERS',
        "name": "Users",
        "icon": "fa-solid fa-users",
        "path": "#",  # No path, since it has submenus
        "submenus": [
            {"id": "ADMIN_ALL_USERS", "name": "All Users", "path": "/adminpanel/users/"},
            {"id": "ADMIN_ADD_STAFF", "name": "Add Staff", "path": "/adminpanel/users/add/staff/"},
        ]
    },
    {
        "id": 'ADMIN_PRODUCTS',
        "name": "Products",
        "icon": "fa-solid fa-box",
        "path": "#",  # No path, since it has submenus
        "submenus": [
            {"id": "ADMIN_ALL_PRODUCTS", "name": "All Products", "path": "/adminpanel/products/"},
            {"id": "ADMIN_ADD_PRODUCT", "name": "Add Product", "path": "/adminpanel/products/add/"},
        ]
    },
    {
        "id": "ADMIN_SETTINGS",
        "name": "Settings",
        "icon": "fa-solid fa-gear",
        "path": "/adminpanel/settings/",
        "submenus": []
    }
]
