from . import views

from django.urls import path, re_path


urlpatterns = [
    path('', views.index, name='identities index'),
    path('about', views.about_render, name='about'),
    path('list', views.list, name='identities list'),
    path('merge_profiles', views.merge_profiles, name='merge_profiles'),
    path('profiles', views.index, name='identities index'),
    path('shdb', views.get_shdb_params, name='shdb'),
    re_path(r'^(?P<identity_id>[0-f]+)/$', views.identity, name='show identity'),
    re_path(r'^(?P<identity_id>[0-f]+)/update_enrollment/(?P<organization>[0-9A-Za-z\w|\W]+)$',
            views.update_enrollment, name='update identity'),
    re_path(r'^(?P<identity_id>[0-f]+)/enroll_in/(?P<organization>[0-9A-Za-z\w|\W]+)$',
            views.enroll_to_profile, name='enroll identity'),
    re_path(r'^(?P<identity_id>[0-f]+)/unenroll_from/(?P<organization_info>[0-9A-Za-z\w|\W]+)/ \
            (?P<enrollment_start_date>[0-9A-Za-z\w|\W]+)/(?P<enrollment_end_date>[0-9A-Za-z\w|\W]+)$',
            views.unenroll_profile, name='unenroll identity'),
    re_path(r'^(?P<identity_id>[0-f]+)/merge$', views.merge_to_profile, name='merge to profile'),
    re_path(r'^(?P<profile_uuid>[0-f]+)/unmerge/(?P<identity_id>[0-f]+)$', views.unmerge, name='unmerge identity from a profile'),
    re_path(r'^organizations/$', views.organizations, name='organizations'),
    re_path(r'^organizations/add/$', views.add_organization, name='add_organization'),
    re_path(r'^organizations/edit/(?P<organization>[0-9A-Za-z\w|\W]+)$', views.edit_organization, name='edit_organization'),
    re_path(r'^organizations/delete/(?P<organization>[0-9A-Za-z\w|\W]+)$', views.delete_organization, name='delete_organization'),
    re_path(r'^organizations/add_domain/(?P<organization>[0-9A-Za-z\w|\W]+)$', views.add_domain, name='add_domain'),
    re_path(r'^organizations/delete_domain/(?P<organization>[0-9A-Za-z\w|\W]+)/(?P<domain>[0-9A-Za-z\w|\W]+)$',
            views.delete_domain, name='delete_domain'),
]
