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

**Option: Using Vercel CLI (Recommended)**
```bash
# Install Vercel CLI globally
npm i -g vercel

# Run from project root
vercel dev
```
Live available at: https://task-one-brown-60.vercel.app/



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


