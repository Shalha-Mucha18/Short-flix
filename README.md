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
API available at http://localhost:3000/api/shorts

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

## AI Usage
This project was developed with the aid of an AI coding assistant. The AI helped:
- Scaffold the monorepo structure for Next.js and Python backend
- Design the "Short-flix" UI with modern aesthetics and responsive CSS
- Debug cross-origin resource sharing (CORS) and API routing issues
- Troubleshoot Vercel deployment issues and switch from FastAPI to BaseHTTPRequestHandler for better serverless compatibility
- Configure the Vercel deployment settings for a seamless hybrid build
