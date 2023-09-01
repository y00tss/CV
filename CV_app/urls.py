from django.conf import settings
# from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

# different name, yeah
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(('CV.urls', 'CV'), namespace='CV'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
