"""donvol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from app import views
from django.conf import settings 
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views
from app.forms import MyPasswordResetForm, MySetPasswordForm


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("gallery", views.gallery, name="gallery"),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm_.html',form_class=MySetPasswordForm),name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),

    #Donor URLS
    path("donor/login-donor", views.login_donor.as_view(), name="login_donor"),
    path("donor/signup-donor/", views.signup_donor.as_view(), name="signup_donor"),
    path("donor/index-donor", views.index_donor, name="index_donor"),
    path("donor/donate-now/", views.donate_now.as_view(), name="donate_now"),
    path("donor/donation-history/", views.donation_history, name="donation_history"),
    path("donor/profile-donor/", views.profile_donor.as_view(), name="profile_donor"),
    
    path("donor/changepwd-donor/", views.changepwd_donor.as_view(), name="changepwd_donor"),
    path(
        "donor/donationdetail-donor/<int:pid>",
        views.donationdetail_donor,
        name="donationdetail_donor",
    ),



    #Volunteer URLS
    path("volunteer/login-volunteer", views.login_volunteer.as_view(), name="login_volunteer"),
    path("volunteer/signup-volunteer/", views.signup_volunteer.as_view(), name="signup_volunteer"),
    path("volunteer/index-volunteer/", views.index_volunteer, name="index_volunteer"),
    path("volunteer/changepwd-volunteer/", views.changepwd_volunteer.as_view(), name="changepwd_volunteer"),
    path("volunteer/collection-req/", views.collection_req, name="collection_req"),
    path("volunteer/profile-volunteer/", views.profile_volunteer.as_view(), name="profile_volunteer"),

    path(
        "volunteer/donationcollection-detail/<int:pid>",
        views.donationcollection_detail.as_view(),
        name="donationcollection_detail",
    ),
    path(
        "volunteer/donationdelivered-volunteer/",
        views.donationdelivered_volunteer,
        name="donationdelivered_volunteer",
    ),
     path(
        "volunteer/donationnotrec-volunteer/",
        views.donationnotrec_volunteer,
        name="donationnotrec_volunteer",
    ),
     path(
        "volunteer/donationrec-detail/<int:pid>",
        views.donationrec_detail.as_view(),
        name="donationrec_detail",
    ),
    path(
        "volunteer/donationrec-volunteer/",
        views.donationrec_volunteer,
        name="donationrec_volunteer",
    ),
    
    # Admin URLS
    path("admin-panel/login-admin", views.login_admin.as_view(), name="login_admin"),
    path("admin-panel/index-admin/", views.index_admin, name="index_admin"),
    path("admin-panel/accepted-donation/", views.accepted_donation, name="accepted_donation"),
    path("admin-panel/add-area/", views.add_area.as_view(), name="add_area"),
    path("admin-panel/accepted-volunteer/", views.accepted_volunteer, name="accepted_volunteer"),
    path("admin-panel/all-donations/", views.all_donations, name="all_donations"),
    path("admin-panel/all-volunteer/", views.all_volunteer, name="all_volunteer"),
    path("admin-panel/changepwd-admin/", views.changepwd_admin.as_view(), name="changepwd_admin"),
    path("admin-panel/donationrec-admin/", views.donationrec_admin, name="donationrec_admin"),
    path("admin-panel/edit-area/<int:pid>", views.edit_area.as_view(), name="edit_area"),
    path("admin-panel/manage-area/", views.manage_area, name="manage_area"),
    path("admin-panel/manage-donor/", views.manage_donor, name="manage_donor"),
    path("admin-panel/new-volunteer/", views.new_volunteer, name="new_volunteer"),
    path("admin-panel/pending-donation/", views.pending_donation, name="pending_donation"),
    path("admin-panel/rejected-donation/", views.rejected_donation, name="rejected_donation"),
    path("admin-panel/rejected-volunteer/", views.rejected_volunteer, name="rejected_volunteer"),
    path("admin-panel/view-donordetail/<int:pid>", views.view_donordetail, name="view_donordetail"),

    path(
        "admin-panel/donationnotrec-admin/", views.donationnotrec_admin, name="donationnotrec_admin"
    ),
    path(
        "admin-panel/accepted-donationdetail/<int:pid>",
        views.accepted_donationdetail.as_view(),
        name="accepted_donationdetail",
    ),
    path(
        "admin-panel/donationdelivered-admin/",
        views.donationdelivered_admin,
        name="donationdelivered_admin",
    ),
    path(
        "admin-panel/view-donationdetail/<int:pid>",
        views.view_donationdetail.as_view(),
        name="view_donationdetail",
    ),
    path(
        "admin-panel/view-volunteerdetail/<int:pid>",
        views.view_volunteerdetail.as_view(),
        name="view_volunteerdetail",
    ),
    path(
        "admin-panel/volunteerallocated-donation/",
        views.volunteerallocated_donation,
        name="volunteerallocated_donation",
    ),
    
    #Common URL
    path("logout/", views.logoutView, name="logout"),
    path('delete_donation/<int:pid>', views.delete_donation, name='delete_donation'),
    path('delete_volunteer/<int:pid>',views.delete_volunteer,name='delete_volunteer'),
    path('delete_area/<int:pid>',views.delete_area, name='delete_area'),
    path('delete-donor/<int:pid>',views.delete_donor, name='delete_donor'),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
 ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

