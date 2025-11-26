# Short-flix

A Netflix-style micro-video platform built with Next.js and Python, designed for serverless deployment on Vercel.

## Tech Stack
- **Frontend**: Next.js (React), TypeScript, Vanilla CSS for premium styling
- **Backend**: Python (BaseHTTPRequestHandler) - switched from FastAPI for better Vercel compatibility
- **Deployment**: Vercel (Hybrid Next.js + Python Serverless)

## Project Structure
- `frontend/`: Next.js application handling the UI and client-side logic
- `api/`: Python serverless functions for video API endpoints
- `vercel.json`: Configuration for routing and build processes

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

### API (Local Testing)
```bash
# Install Vercel CLI
npm i -g vercel

# Run from project root
vercel dev
```
## Improvements
With more time, I would implement:
- **Persistence**: Integrate a database (e.g., PostgreSQL/Supabase) to save videos and favorites permanently
- **Authentication**: Add user login to sync favorites across devices
- **Media Hosting**: Upload videos to cloud storage (AWS S3 or Cloudinary) instead of using external links
- **Infinite Scroll**: Load videos dynamically as the user scrolls


