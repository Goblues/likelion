from django.contrib import admin
from django.urls import path, include
import blog.views
import portfolio.views
import accounts.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"),
    path('blog/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),
    # url 패턴을 띄운다고 무조건 html을 여는 것이 아니다.
    # url을 blog / 정수형 path_converter
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
