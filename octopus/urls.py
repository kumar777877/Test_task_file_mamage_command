from django.contrib import admin
from django.urls import path

admin.site.site_header = "Octopus"
admin.site.site_title = "Octopus Portal"
admin.site.index_title = "Welcome to Octopus"


urlpatterns = [
    path("admin/", admin.site.urls),
]
