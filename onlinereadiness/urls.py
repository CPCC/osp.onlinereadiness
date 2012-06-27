from django.conf.urls.defaults import *

from onlinereadiness import views

urlpatterns = patterns('',
    (r'^show/$', views.online_readiness_show_assessment, {}, 'online-readiness-show-assessment'),
    (r'^get/results/(?P<student_id>\d+)/$', views.online_readiness_student_results, {}, 'online-readiness-student-results'),
    (r'^get/result-initial/(?P<result_id>\d+)/$', views.online_readiness_get_result, {'is_initial':True}, 'online-readiness-get-result-initial'),
    (r'^get/result/(?P<result_id>\d+)/$', views.online_readiness_get_result, {'is_initial':False}, 'online-readiness-get-result'),
)
