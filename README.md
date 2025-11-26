Short-flix is a FastAPI backend plus a Next.js 14 frontend. The backend follows a production-style layout in `backend/app` with versioned routers under `api/v1/routes`, schemas, services, and core config; `api/shorts.py` re-exports the same app/handler for Vercel. It exposes `GET /api/shorts` with filtering plus optional `POST /api/shorts` to append in-memory items. The frontend now lives in `frontend/` (Next.js `app/` directory inside) and renders a Netflix-style grid, hero, player, search, tag chips, and local favorites.

Run the backend locally:
- `pip install -r requirements.txt`
- `uvicorn backend.app.main:app --reload --port 8000`

Run the frontend locally:
- `cd frontend`
- `npm install`
- `NEXT_PUBLIC_API_BASE=http://localhost:8000 npm run dev`

Deploy to Vercel: leave the repo as-is. `vercel.json` routes `/api/shorts` to the Python serverless function, and the root Next.js project builds the UI. Improvements to add with more time: persistence (Supabase/Planetscale), upload + thumbnail generation, auth-backed favorites, and better observability. Built with help from ChatGPT for scaffolding and ideation.
