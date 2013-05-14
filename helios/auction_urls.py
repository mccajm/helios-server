from django.conf.urls.defaults import *

from helios.views import *

urlpatterns = patterns('',
    (r'^/items$', one_auction_parameters),
    (r'^/save_questions$', one_auction_save_questions),
 )