# Short-flix

A Netflix-style micro-video platform built with Next.js and FastAPI, designed for serverless deployment on Vercel.

## Tech Stack
- **Frontend**: Next.js (React), TypeScript, Vanilla CSS for premium styling.
- **Backend**: FastAPI (Python)
- **Deployment**: Vercel (Hybrid Next.js + Python Serverless).

## Project Structure
- `frontend/`: Next.js application handling the UI and client-side logic.
- `backend/`: FastAPI 
- `api/`: Serverless entry point adapting FastAPI for Vercel.
- `vercel.json`: Configuration for routing and build processes.

## Improvements
With more time, I would implement:
- **Persistence**: Integrate a database (e.g., PostgreSQL/Supabase) to save videos and favorites permanently.
- **Authentication**: Add user login to sync favorites across devices.
- **Media Hosting**: Upload videos to cloud storage (AWS S3 or Cloudinary) instead of using external links.
- **Infinite Scroll**: Load videos dynamically as the user scrolls.

## AI Usage
This project was developed with the aid of an AI coding assistant. The AI helped:
- Scaffold the monorepo structure for Next.js and FastAPI.
- Design the "Short-flix" UI with modern aesthetics and responsive CSS.
- Debug cross-origin resource sharing (CORS) and API routing issues.
- Configure the Vercel deployment settings for a seamless hybrid build.
