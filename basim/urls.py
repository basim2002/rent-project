from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from basim import views

urlpatterns=[
    path('',views.index1,name='index1'),
    path('login',views.userlogin,name='login'),
    path('logout_view',views.logout_view,name='logout_view'),

    path('dashboad',views.dashboad,name='dashboad'),
    path('districtdelete/<int:id>',views.districtdelete,name='districtdelete'),
    path('adddis',views.adddistrict,name='adddis'),
    path('districtview',views.districtview,name='districtview'),
    path('addarea',views.addarea,name='addarea'),
    path('viewarea',views.viewarea,name='viewarea'),
    path('deletearea/<int:id>',views.deletearea,name='deletearea'),

    path('viewbook', views.viewbook, name='viewbook'),
    path('editbook/<int:id>',views.editbook,name='editbook'),
    path('deletebook/<int:id>',views.deletebook,name='deletebook'),
    path('delete_book_category/<int:id>',views.delete_book_category,name='delete_book_category'),
    path('add_book_category', views.add_book_category, name='add_book_category'),
    path('view_book_category', views.view_book_category, name='view_book_category'),
    path('view_cust_bookcategory', views.view_cust_bookcategory, name='view_cust_bookcategory'),
    path('admin_view_feedback', views.admin_view_feedback, name='admin_view_feedback'),
    path('replay_feedback', views.replay_feedback, name='replay_feedback'),
    path('view_replay', views.view_replay, name='view_replay'),
    path('admin_view_dealer',views.admin_view_dealer,name='admin_view_dealer'),



    path('view_customer',views.view_customer,name='view_customer'),
    path('view_customer_admin',views.view_customer_admin,name='view_customer_admin'),
    path('delete_customer/<int:id>',views.delete_customer,name='delete_customer'),
    path('customer_home',views.customer_home,name='customer_home'),
    path('cust_book_view',views.cust_book_view,name='cust_book_view'),
    path('add_customer', views.add_customer, name='add_customer'),
    path('add_feedback', views.add_feedback, name='add_feedback'),
    path('profile',views.profile,name='profile'),
    path('cust_view_feedback',views.cust_view_feedback,name='cust_view_feedback'),


    path('dealer_home',views.dealer_home,name='dealer_home'),
    path('addbook', views.addbook, name='addbook'),
    path('dealer_book_view',views.dealer_book_view,name='dealer_book_view'),
    path('add_dealer', views.add_dealer, name='add_dealer'),
    path('view_dealer',views.view_dealer,name='view_dealer'),
    path('dealer_view_feedback',views.dealer_view_feedback,name='dealer_view_feedback'),
    path('dealer_view_category',views.dealer_view_category,name='dealer_view_category'),
    path('dealer_view_cust',views.dealer_view_cust,name='dealer_view_cust')


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)