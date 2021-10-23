from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('board/', include('board.urls')),
    path('blog/', include('blog.urls')),
    path('polls/', include('polls.urls')),
    path('todo/', include('todo.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
