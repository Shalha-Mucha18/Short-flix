# Short-flix

A Netflix-style micro-video platform built with Next.js and Python, designed for serverless deployment on Vercel.

## Tech Stack
- **Frontend**: Next.js (React), TypeScript, Vanilla CSS for premium styling
- **Backend**: FastAPI

## How to Run Locally

### Prerequisites
- Node.js 18+ and npm
- Python 3.9+

### Frontend
```bash
cd frontend
npm install
npm run dev
```
Open http://localhost:3000

### Backend/API (Local Testing)

**Option 1: Using Vercel CLI (Recommended)**
```bash
# Install Vercel CLI globally
npm i -g vercel

# Run from project root
vercel dev
```
Live available at: https://task-one-brown-60.vercel.app/

**Option 2: Test API directly**
```bash
# The API uses Python's standard library (no dependencies needed)
python3 -c "from api.shorts import handler; print('API loaded successfully')"
```

Note: The backend uses Python's `BaseHTTPRequestHandler` with no external dependencies.

## Deployment
Deployed on Vercel:
- Frontend: Root URL
- API: `/api/shorts`

Push to main branch for auto-deployment.

## Improvements
With more time, I would implement:
- **Persistence**: Integrate a database (e.g., PostgreSQL/Supabase) to save videos and favorites permanently
- **Authentication**: Add user login to sync favorites across devices
- **Media Hosting**: Upload videos to cloud storage (AWS S3 or Cloudinary) instead of using external links
- **Infinite Scroll**: Load videos dynamically as the user scrolls


