import httplib2
import os
import sys

from flask import Flask, redirect, render_template
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow
from googleapiclient.discovery import build

from flask_sqlalchemy import SQLAlchemy
from model import Videos
from model import VideoStat, Channels

app = Flask(__name__)

#database config
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:stzu7734@localhost:3306/dataLake'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#oauth2 config
CLIENT_SECRETS_FILE = "client_secret.json"
YOUTUBE_READ_WRITE_SCOPE = "https://www.googleapis.com/auth/youtube"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
MISSING_CLIENT_SECRETS_MESSAGE = """missing key"""


def get_authenticated_service(args):
  flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
    scope=YOUTUBE_READ_WRITE_SCOPE,
    message=MISSING_CLIENT_SECRETS_MESSAGE)

  storage = Storage("%s.json" % sys.argv[0])
  credentials = storage.get()

  if credentials is None or credentials.invalid:
    credentials = run_flow(flow, storage, args)

  return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    http=credentials.authorize(httplib2.Http()))

def set_video_localization(youtube, args):
  results = youtube.videos().list(
    part='snippet,localizations',
    id=args.video_id
  ).execute()
  video = results['items'][0]
  return results

argparser.add_argument("video_id",
    help="Optional ID of video to find.")
args = argparser.parse_args()

@app.route("/", methods =['GET'])
def index():
    return "Hello"

@app.route("/test", methods=['GET'])
def getvideo():
    youtube = get_authenticated_service(args)
    res = set_video_localization(youtube,id="mCR7NLlGG1A")
    return res

@app.route("/api", methods=['GET'])
def getAPI():
    apiKey = "AIzaSyDJc-W-mpF_3_yJfhFVs4pBO28Ta_MXbxo"
    vid = "D73zR_fvxiYs"
    url = "https://www.googleapis.com/youtube/v3/videos?id="+vid+"&key="+apiKey+"%20%20%20%20%20%20&part=statistics"
    
    return redirect(url)


@app.route("/video", methods=['GET'])
def test():
    api_key = "AIzaSyDJc-W-mpF_3_yJfhFVs4pBO28Ta_MXbxo"
    api_obj = build('youtube', 'v3', developerKey= api_key)

    video_id = "XP0DigwmNDY"
    response = api_obj.videos().list(part="statistics", id= video_id).execute()
    ret = response["items"]
    if ret ==[]:
      return "404 error vid not found."
    print(ret)
    r = str(ret).split(",")
    returnStrings = str(r[3:])
    return returnStrings


@app.route("/getVideoInfo", methods=['GET'])
def getVideoInfo():
    limit = 20
    title = "가지고 싶으면 들어와!!"
    #from private-videos-tables
    q= db.session.query(Videos).filter(Videos.title==title)[:1]
    
    return render_template('video.html', rows= q)

@app.route("/get3DaysInfo", methods=['Get'])
def get3DaysInfo():
    #private_videos_stat을 사용, stat_ttype=THREEDAYS로 필터링
    videoStat = VideoStat.query.first()

    # query = '''select * from private_videos_stat 
    #         inner join private_videos on private_videos.id=private_videos_stat.video_id
    #         inner join private_channels on private_channels.channel_id = private_videos.channel_id
    #         where private_videos_stat.stat_type = '''+ '"THREEDAYS"'
    stat_type = "THREEDAYS"
    rows = db.session.query(VideoStat).outerjoin(Videos, VideoStat.video_id==Videos.id).outerjoin(Channels, Channels.channel_id==Videos.channel_id).filter(VideoStat.stat_type==stat_type)[:20]
    
    return render_template('threeDays.html', rows= rows)

@app.route("/one")
def one():
  video = Videos.query.first()
  return "hi {0}, {1}".format(video.id, video.title)

if __name__ == "__main__": 
    app.run(host='localhost', port='8080', debug=True)
