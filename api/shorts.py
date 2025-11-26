from http.server import BaseHTTPRequestHandler
import json

_SHORTS = [
    {"id": 1, "videoUrl": "https://www.w3schools.com/html/mov_bbb.mp4", "title": "Travel Reel", "tags": ["adventure", "outdoors", "cinematic"]},
    {"id": 2, "videoUrl": "https://samplelib.com/lib/preview/mp4/sample-5s.mp4", "title": "City Pulse", "tags": ["city", "nightlife", "lights"]},
    {"id": 3, "videoUrl": "https://samplelib.com/lib/preview/mp4/sample-10s.mp4", "title": "Calm Shores", "tags": ["ocean", "drone", "relax"]},
    {"id": 4, "videoUrl": "https://samplelib.com/lib/preview/mp4/sample-15s.mp4", "title": "Hike Time", "tags": ["mountains", "trail", "nature"]},
]

class handler(BaseHTTPRequestHandler):
    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers(200)

    def do_GET(self):
        self._set_headers(200)
        self.wfile.write(json.dumps(_SHORTS).encode())

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = json.loads(self.rfile.read(content_length)) if content_length else {}
        if not body.get('tags'):
            self._set_headers(400)
            self.wfile.write(json.dumps({'detail': 'At least one tag is required.'}).encode())
            return
        next_id = max((s['id'] for s in _SHORTS), default=0) + 1
        new_short = {'id': next_id, 'videoUrl': body.get('videoUrl', ''), 'title': body.get('title', ''), 'tags': body.get('tags', [])}
        _SHORTS.append(new_short)
        self._set_headers(201)
        self.wfile.write(json.dumps(new_short).encode())

    def do_DELETE(self):
        try:
            short_id = int(self.path.split('/')[-1])
            for i, s in enumerate(_SHORTS):
                if s['id'] == short_id:
                    _SHORTS.pop(i)
                    self._set_headers(204)
                    return
            self._set_headers(404)
            self.wfile.write(json.dumps({'detail': 'Short not found'}).encode())
        except ValueError:
            self._set_headers(400)
            self.wfile.write(json.dumps({'detail': 'Invalid id'}).encode())
