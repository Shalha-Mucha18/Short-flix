from http.server import BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs

_SHORTS = [
    {"id": 1, "videoUrl": "https://www.w3schools.com/html/mov_bbb.mp4", "title": "Travel Reel", "tags": ["adventure", "outdoors", "cinematic"]},
    {"id": 2, "videoUrl": "https://samplelib.com/lib/preview/mp4/sample-5s.mp4", "title": "City Pulse",   "tags": ["city", "nightlife", "lights"]},
    {"id": 3, "videoUrl": "https://samplelib.com/lib/preview/mp4/sample-10s.mp4","title": "Calm Shores",  "tags": ["ocean", "drone", "relax"]},
    {"id": 4, "videoUrl": "https://samplelib.com/lib/preview/mp4/sample-15s.mp4","title": "Hike Time",    "tags": ["mountains", "trail", "nature"]},
]

class handler(BaseHTTPRequestHandler):
    def send_response_data(self, status, data):
        self.send_response(status)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        if data:
            self.wfile.write(json.dumps(data).encode())
    
    def do_OPTIONS(self):
        self.send_response_data(200, None)
    
    def do_GET(self):
        self.send_response_data(200, _SHORTS)
    
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = json.loads(self.rfile.read(content_length).decode()) if content_length else {}
        if not body.get('tags'):
            self.send_response_data(400, {'detail': 'At least one tag is required.'})
            return
        next_id = max((item['id'] for item in _SHORTS), default=0) + 1
        new_short = {'id': next_id, 'videoUrl': body.get('videoUrl', ''), 'title': body.get('title', ''), 'tags': body.get('tags', [])}
        _SHORTS.append(new_short)
        self.send_response_data(201, new_short)
    
    def do_DELETE(self):
        try:
            short_id = int(self.path.rstrip('/').split('/')[-1])
            for i, s in enumerate(_SHORTS):
                if s['id'] == short_id:
                    _SHORTS.pop(i)
                    self.send_response_data(204, None)
                    return
            self.send_response_data(404, {'detail': 'Short not found'})
        except ValueError:
            self.send_response_data(400, {'detail': 'Invalid id'})
