from django.conf.urls import url

from consumer import views


urlpatterns = [
    url(r'create-channel/', views.consumerView.open_signaling_channel, name='create_channel'),
    url(r'delete-channel/', views.classRoomView.delete_signaling_channel, name='delete_channel')
]
