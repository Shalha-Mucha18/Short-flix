import json

# In-memory storage for shorts
# Vercel serverless function
_SHORTS = [
    {"id": 1, "videoUrl": "https://www.w3schools.com/html/mov_bbb.mp4", "title": "Travel Reel", "tags": ["adventure", "outdoors", "cinematic"]},
    {"id": 2, "videoUrl": "https://samplelib.com/lib/preview/mp4/sample-5s.mp4", "title": "City Pulse",   "tags": ["city", "nightlife", "lights"]},
    {"id": 3, "videoUrl": "https://samplelib.com/lib/preview/mp4/sample-10s.mp4","title": "Calm Shores",  "tags": ["ocean", "drone", "relax"]},
    {"id": 4, "videoUrl": "https://samplelib.com/lib/preview/mp4/sample-15s.mp4","title": "Hike Time",    "tags": ["mountains", "trail", "nature"]},
]

def handler(request, context):
    # IMPORTANT: declare global BEFORE any use/assignment inside the function
    global _SHORTS

    path = request.get('path', '')
    method = request.get('method', 'GET')
    
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, DELETE, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Content-Type': 'application/json'
    }
    
    # OPTIONS for CORS preflight
    if method == 'OPTIONS':
        return {'statusCode': 200, 'headers': headers, 'body': ''}

    # GET /api/shorts
    if method == 'GET' and path == '/api/shorts':
        return {'statusCode': 200, 'headers': headers, 'body': json.dumps(_SHORTS)}
    
    # POST /api/shorts
    if method == 'POST' and path == '/api/shorts':
        try:
            body = json.loads(request.get('body', '{}'))
            if not body.get('tags'):
                return {'statusCode': 400, 'headers': headers, 'body': json.dumps({'detail': 'At least one tag is required.'})}
            next_id = max((item['id'] for item in _SHORTS), default=0) + 1
            new_short = {'id': next_id, 'videoUrl': body.get('videoUrl', ''), 'title': body.get('title', ''), 'tags': body.get('tags', [])}
            _SHORTS.append(new_short)
            return {'statusCode': 201, 'headers': headers, 'body': json.dumps(new_short)}
        except Exception as e:
            return {'statusCode': 400, 'headers': headers, 'body': json.dumps({'detail': str(e)})}

    # DELETE /api/shorts/{id}
    if method == 'DELETE' and path.startswith('/api/shorts/'):
        try:
            short_id = int(path.rstrip('/').split('/')[-1])
            # remove in-place to avoid accidental reassignment issues (we still declared global above)
            for i, s in enumerate(_SHORTS):
                if s['id'] == short_id:
                    _SHORTS.pop(i)
                    return {'statusCode': 204, 'headers': headers, 'body': ''}
            return {'statusCode': 404, 'headers': headers, 'body': json.dumps({'detail': 'Short not found'})}
        except ValueError:
            return {'statusCode': 400, 'headers': headers, 'body': json.dumps({'detail': 'Invalid id'})}
        except Exception as e:
            return {'statusCode': 500, 'headers': headers, 'body': json.dumps({'detail': str(e)})}

    return {'statusCode': 404, 'headers': headers, 'body': json.dumps({'detail': 'Not found'})}
