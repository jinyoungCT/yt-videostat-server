import httplib2
import os
import sys

from flask import Flask, redirect
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow
from googleapiclient.discovery import build


app = Flask(__name__)

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

<<<<<<< HEAD
    print(ret)
    r = str(ret).split(",")
    returnStrings = str(r[3:])
    
=======
    r = str(ret).split(",")
    returnStrings = str(r[3:])

>>>>>>> ceb444362a2835ce8b0189c0ec79e0db13a99271
    return returnStrings

if __name__ == "__main__": 
    app.run(host='localhost', port='8080', debug=True)