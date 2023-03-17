from django.contrib import admin
from .models import Posts,Comments,Downvote_comments,DownVotes,Upvotes,Upvotes_comments
# Register your models here.
admin.site.register(Posts)
admin.site.register(Comments)
admin.site.register(DownVotes)
admin.site.register(Downvote_comments)
admin.site.register(Upvotes)
admin.site.register(Upvotes_comments)