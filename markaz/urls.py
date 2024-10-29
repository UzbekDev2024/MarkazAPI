from django.urls import path
from .views import (XonaListAPIView,
                    XonaCreateAPIView, OqituvchiCreateAPIView,
                    FanCreateAPIView, OqituvchiListAPIView,
                    OquvchiListAPIView, FanListAPIView, OquvchiCreateAPIView,
# XonaListAPI, XonaDetail,
xona_list, xona_detail
                    )


urlpatterns = [

            path("xonaList", xona_list),
            # path("xonaList/", XonaListAPI.as_view()),
            path("xonaDetail/<int:pk>/", xona_detail),
            # path("xonaDetail/<int:pk>/", XonaDetail.as_view()),


            # path("xonaList/", XonaListAPIView.as_view()),
            # path("xonaCreate/", XonaCreateAPIView.as_view()),
            # path("teacherCreate/", OqituvchiCreateAPIView.as_view()),
            # path("teacherList/", OqituvchiListAPIView.as_view()),
            # path("oquvchiList/", OquvchiListAPIView.as_view()),
            # path("oquvchiCreate/", OquvchiCreateAPIView.as_view()),
            # path("fanList/", FanListAPIView.as_view()),
            # path("fanCreate/", FanCreateAPIView.as_view()),
    ]
