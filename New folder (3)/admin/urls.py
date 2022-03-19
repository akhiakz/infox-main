from . import views
from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[ 
    re_path(r'^$',views.index,name='index'),

    re_path(r'^BRadmin_Reportedissue_department$', views.BRadmin_Reportedissue_department, name='BRadmin_Reportedissue_department'),
    re_path(r'^BRadmin_Reportedissue/(?P<id>\d+)$', views.BRadmin_Reportedissue, name='BRadmin_Reportedissue'),
    
    re_path(r'^BRadmin_ReportedissueShow/(?P<id>\d+)$', views.BRadmin_ReportedissueShow, name='BRadmin_ReportedissueShow'),
    re_path(r'^BRadmin_ReportedissueShow1/(?P<id>\d+)$', views.BRadmin_ReportedissueShow1, name='BRadmin_ReportedissueShow1'),

    # re_path(r'^BRadmin_ReportedissueTrainer$', views.BRadmin_ReportedissueTrainer, name='BRadmin_ReportedissueTrainer'),
    # re_path(r'^BRadmin_ReportedissueTrainer1/(?P<id>\d+)$', views.BRadmin_ReportedissueTrainer1, name='BRadmin_ReportedissueTrainer1'),

    # re_path(r'^BRadmin_ReportedissueProjectManager$', views.BRadmin_ReportedissueProjectManager, name='BRadmin_ReportedissueProjectManager'),
    # re_path(r'^BRadmin_ReportedissueProjectManager1/(?P<id>\d+)$', views.BRadmin_ReportedissueProjectManager1, name='BRadmin_ReportedissueProjectManager1'),

    # re_path(r'^BRadmin_ReportedissueTeamLeader$', views.BRadmin_ReportedissueTeamLeader, name='BRadmin_ReportedissueTeamLeader'),
    # re_path(r'^BRadmin_ReportedissueTeamLeader1/(?P<id>\d+)$', views.BRadmin_ReportedissueTeamLeader1, name='BRadmin_ReportedissueTeamLeader1'),
    
    # re_path(r'^BRadmin_ReportedissueDevelopers$', views.BRadmin_ReportedissueDevelopers, name='BRadmin_ReportedissueDevelopers'),
    # re_path(r'^BRadmin_ReportedissueDevelopers1/(?P<id>\d+)$', views.BRadmin_ReportedissueDevelopers1, name='BRadmin_ReportedissueDevelopers1'),
        
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT) 
