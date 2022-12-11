from django.urls import path
from .views import showdatesPageView
from .views import showfirstdatePageView
from .views import showcasualPageView
from .views import showoutdoorsPageView
from .views import showfancyPageView
from .views import showspiritualPageView
from .views import showproposalPageView
from .views import addDatePageView
from .views import editDatePageView
from .views import showSingleDatePageView
from .views import deleteDatePageView
from .views import showuserPageView

urlpatterns = [
    path("showdates/", showdatesPageView, name="showdates"),
    path("showfirstdate/", showfirstdatePageView, name="first"),
    path("showcasual/", showcasualPageView, name="casual"),
    path("showoutdoors/", showoutdoorsPageView, name="outdoors"),
    path("showfancy/", showfancyPageView, name="fancy"),
    path("showspiritual/", showspiritualPageView, name="spiritual"),
    path("showproposal/", showproposalPageView, name="proposal"),
    path("showuser/", showuserPageView, name="user"),
    path('adddate/', addDatePageView, name='addDate'),
    path('editdate/', editDatePageView, name='editDate'),
    path('showDate/<int:date_id>/', showSingleDatePageView, name= 'showSingleDate'),
    path('deleteDate/<int:date_id>/,', deleteDatePageView, name='deleteDate'),
]
