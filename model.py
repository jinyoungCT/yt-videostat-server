from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Videos(db.Model):
    __tablename__ = 'private_videos'

    id = db.Column(db.String, primary_key=True)
    channel_id = db.Column(db.String(30, 'utf8mb4_unicode_ci'))
    title = db.Column(db.String(30, 'utf8mb4_unicode_ci'))
    status = db.Column(db.String(30, 'utf8mb4_unicode_ci'))
    description =db.Column(db.String(30, 'utf8mb4_unicode_ci'))
    thumbnail = db.Column(db.String(30, 'utf8mb4_unicode_ci')) 
    published_at = db.Column(db.DateTime, default=datetime.utcnow())
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow())
    deleted_at = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, id, channel_id, title, status, descriptpion, 
    thumbnial,published_at, created_at, updated_at, deleted_at):
        self.id = id
        self.channel_id =channel_id
        self.title = title
        self.status = status
        self.description =description
        self.thumbnail = thumbnail
        self.published_at = published_at
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at

class VideoStat(db.Model):
    __tablename__ = 'private_videos_stat'

    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    video_id = db.Column(db.String(30, 'utf8mb4_unicode_ci'))
    stat_type = db.Column(db.String(30, 'utf8mb4_unicode_ci'))
    views = db.Column(db.Integer)
    views_subs = db.Column(db.Integer)
    views_unsubs = db.Column(db.Integer)
    views_red = db.Column(db.Integer)
    avg_per_viewed = db.Column(db.Integer)
    avg_per_viewed_subs = db.Column(db.Integer)
    avg_per_viewed_unsubs = db.Column(db.Integer)
    avg_per_viewed_red = db.Column(db.Integer)
    avg_view_duration = db.Column(db.Integer)
    video_length = db.Column(db.Integer) 
    watch_time = db.Column(db.Integer)
    watch_time_red = db.Column(db.Integer)
    subs_gain = db.Column(db.Integer)
    subs_lost = db.Column(db.Integer)
    subs = db.Column(db.Integer)
    likes = db.Column(db.Integer)
    dislikes = db.Column(db.Integer)
    comment = db.Column(db.Integer)
    sharing = db.Column(db.Integer)
    playlist_add = db.Column(db.Integer)
    playlist_remove = db.Column(db.Integer)
    end_screen_shown = db.Column(db.Integer)
    end_screen_click = db.Column(db.Integer)

    def __init__(self,id,video_id, stat_type, views, views_subs, views_unsubs, views_red, avg_per_viewed, avg_per_viewed_subs, avg_per_viewed_unsubs, avg_per_viewed_red, avg_viewe_duration
    , video_length, watch_time, watch_time_red, subs_gain, subs_lost, subs,likes,dislikes,
    comment, sharing, playlist_add, playlist_remove, end_screen_shown, end_screen_click):
        self.id = id
        self.video_id = video_id
        self.stat_type = stat_type
        self.views = views
        self.views_subs = views_subs
        self.views.unsubs = views.unsubs
        self.views_red = views.redirect
        self.avg_per_viewed = avg_per_viewed
        self.avg_per_viewed_subs = avg_per_viewed_subs
        self.avg_per_viewed_unsubs = avg_per_viewed_unsubs
        self.avg_per_viewed_red = avg_per_viewed_red
        self.avg_viewe_duration = avg_viewe_duration
        self.video_length = video_length
        self.watch_time = watch_time
        self.watch_time_red = watch_time_red
        self.subs_gain = subs_gain
        self.subs_lost = subs_lost
        self.subs = subs
        self.likes = likes
        self.dislikes =dislikes
        self.comment = comment
        self.sharing = sharing
        self.playlist_add = playlist_add
        self.playlist_remove = playlist_remove
        self.end_screen_shown = end_screen_shown
        self.end_screen_click = end_screen_click

class Channels(db.Model):
    __tablename__ = 'private_channels'

    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    channel_id = db.Column(db.String(30, 'utf8mb4_unicode_ci'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    title = db.Column(db.String(30, 'utf8mb4_unicode_ci'))
    thumbnail = db.Column(db.String(30, 'utf8mb4_unicode_ci')) 
    status = db.Column(db.String(30, 'utf8mb4_unicode_ci'))
    linked_at = db.Column(db.String(30, 'utf8mb4_unicode_ci')) 
    published_at = db.Column(db.DateTime, default=datetime.utcnow())
    leaved_at = db.Column(db.DateTime, default=datetime.utcnow())
    cms = db.Column(db.String(30, 'utf8mb4_unicode_ci'))
    company = db.Column(db.String(30, 'utf8mb4_unicode_ci'))
    strike = db.Column(db.Integer)
    total_views = db.Column(db.Integer)
    total_videos = db.Column(db.Integer)
    total_subscribers = db.Column(db.Integer)

    def __init__(self, id, channel_id, created_at, title, thumbnail, status,
    linked_at, published_at, leaved_at, cms, company, strike, total_views,
    total_videos, total_subscribers):
        self.id = id
        self.channe_id = channe_id
        self.title = title
        self.thumbnail = thumbnail
        self.status = status
        self.linked_at = linked_at
        self.published_at = published_at
        self.leaved_at = leaved_at
        self.cms = cms
        self. company = company
        self.strike = strike
        self.total_views = total_views
        self.total_videos = total_videos
        self.total_subscribers = total_subscribers
        
