from django.conf.urls.defaults import *

from onlinereadiness import views

urlpatterns = patterns('',
    (r'^show/$', views.online_readiness_show_assessment, {}, 'online-readiness-show-assessment'),
    (r'^get/results/(?P<student_id>\d+)/$', views.online_readiness_student_results, {}, 'online-readiness-student-results'),
    (r'^get/result/(?P<result_id>\d+)/$', views.online_readiness_get_result, {}, 'online-readiness-get-result'),
)
