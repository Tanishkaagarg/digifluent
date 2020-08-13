from django.urls import path

from . import views

urlpatterns =[path("", views.index, name="index"),
            path("single", views.single, name="single"),
            path("contact", views.contact, name="contact"),
            path("services", views.services, name="services"),
            path("socialmediamarketing", views.socialmediamarketing, name="socialmediamarketing"),
            path("branding", views.branding, name="branding"),
            path("creative", views.creative, name="creative"),
            path("sem", views.sem, name="sem"),
            path("email", views.email, name="email"),
            path("webdesigning", views.webdesigning, name="webdesigning"),
            path("facebook", views.facebook, name="facebook"),
            path("google", views.google, name="google"),
            path("influencer", views.influencer, name="influencer"),
            path("content", views.content, name="content"),
            path("graphic", views.graphic, name="graphic"),
            path("success", views.successView, name="success"),
            path("seo", views.seo, name="seo")]