from django.conf.urls import patterns, url
import views
import receivers

urlpatterns = patterns('',
        url(r'^pack/$', views.SavePackView.as_view()),
        )

