"""jobportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from job.views import *
from django.conf import settings
from django.conf.urls.static import static
from job import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("admin_login", views.admin_login, name="admin_login"),
    path("user_login", views.user_login, name="user_login"),
    path("user_signup", views.user_signup, name="user_signup"),
    path("recruiter_signup", views.recruiter_signup, name="recruiter_signup"),
    path("recruiter_login", views.recruiter_login, name="recruiter_login"),
    path("user_home", views.user_home, name="user_home"),
    path("recruiter_home", views.recruiter_home, name="recruiter_home"),
    path("admin_home", views.admin_home, name="admin_home"),
    path("view_users", views.view_users, name="view_users"),
    path("Logout", views.Logout, name="Logout"),
    path("delete_user/<int:pid>", views.delete_user, name="delete_user"),
    path("change_status/<int:pid>", views.change_status, name="change_status"),
    path("recruiter_pending", views.recruiter_pending, name="recruiter_pending"),
    path("recruiter_accepted", views.recruiter_accepted, name="recruiter_accepted"),
    path("delete_recruiter/<int:pid>", views.delete_recruiter, name="delete_recruiter"),
    path("job_list_admin", views.job_list_admin, name="job_list_admin"),
    path("change_adminpwd", views.change_adminpwd, name="change_adminpwd"),
    path("change_userpwd", views.change_userpwd, name="change_userpwd"),
    path("change_recruiterpwd", views.change_recruiterpwd, name="change_recruiterpwd"),
    path("add_job", views.add_job, name="add_job"),
    path("job_list", views.job_list, name="job_list"),
    path("edit_jobdetail/<int:pid>", views.edit_jobdetail, name="edit_jobdetail"),
    path(
        "change_companylogo/<int:pid>",
        views.change_companylogo,
        name="change_companylogo",
    ),
    path("latest_jobs", views.latest_jobs, name="latest_jobs"),
    path("user_latestjobs", views.user_latestjobs, name="user_latestjobs"),
    path("job_detail/<int:pid>", views.job_detail, name="job_detail"),
    path("applyforjob/<int:pid>", views.applyforjob, name="applyforjob"),
    path("applied_candidate", views.applied_candidate, name="applied_candidate"),
    path("contact", views.contact, name="contact"),
    path("user_dashboard", views.user_dashboard, name="user_dashboard"),
    path("recruiter_dashboard", views.recruiter_dashboard, name="recruiter_dashboard"),
]
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
