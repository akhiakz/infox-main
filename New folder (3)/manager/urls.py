from . import views
from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[ 
    re_path(r'^$',views.index,name='index'),

    re_path(r'^MAN_Reportedissue_department$', views.MAN_Reportedissue_department, name='MAN_Reportedissue_department'),
    re_path(r'^MAN_Reportedissue/(?P<id>\d+)$', views.MAN_Reportedissue, name='MAN_Reportedissue'),
    
    re_path(r'^MAN_ReportedissueShow/(?P<id>\d+)$', views.MAN_ReportedissueShow, name='MAN_ReportedissueShow'),
    re_path(r'^MAN_ReportedissueShow1/(?P<id>\d+)$', views.MAN_ReportedissueShow1, name='MAN_ReportedissueShow1'),

    # re_path(r'^MAN_ReportedissueTrainer$', views.MAN_ReportedissueTrainer, name='MAN_ReportedissueTrainer'),
    # re_path(r'^MAN_ReportedissueTrainer1/(?P<id>\d+)$', views.MAN_ReportedissueTrainer1, name='MAN_ReportedissueTrainer1'),

    # re_path(r'^MAN_ReportedissueProjectManager$', views.MAN_ReportedissueProjectManager, name='MAN_ReportedissueProjectManager'),
    # re_path(r'^MAN_ReportedissueProjectManager1/(?P<id>\d+)$', views.MAN_ReportedissueProjectManager1, name='MAN_ReportedissueProjectManager1'),

    # re_path(r'^MAN_ReportedissueTeamLeader$', views.MAN_ReportedissueTeamLeader, name='MAN_ReportedissueTeamLeader'),
    # re_path(r'^MAN_ReportedissueTeamLeader1/(?P<id>\d+)$', views.MAN_ReportedissueTeamLeader1, name='MAN_ReportedissueTeamLeader1'),
    
    # re_path(r'^MAN_ReportedissueDevelopers$', views.MAN_ReportedissueDevelopers, name='MAN_ReportedissueDevelopers'),
    # re_path(r'^MAN_ReportedissueDevelopers1/(?P<id>\d+)$', views.MAN_ReportedissueDevelopers1, name='MAN_ReportedissueDevelopers1'),
        
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT) 
