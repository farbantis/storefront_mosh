import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Storefront Admin'  # change header at the very top of admin panel
admin.site.index_title = 'Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')),
    path('store/', include('store.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]
