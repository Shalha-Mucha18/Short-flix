<h1 align="center">Short-flix</h1>

Short-flix is a polished mini-Netflix experience: FastAPI powers a lightweight shorts API, and Next.js 14 renders a cinematic grid with search, tags, favorites, and add/delete actions. The backend follows a production-style layout (`backend/app` with versioned routers, schemas, services, and core config). `api/shorts.py` re-exports the same app/handler for Vercel so the API deploys as a serverless function. The frontend lives in `frontend/` (Next.js `app/` dir) and consumes the live `/api/shorts` endpoint.

### Local development
- Backend: `pip install -r requirements.txt` then `uvicorn backend.app.main:app --reload --port 8000`
- Frontend: `cd frontend && npm install && NEXT_PUBLIC_API_BASE=http://localhost:8000 npm run dev`

### Deployment (Vercel)
- Repo is preconfigured with `vercel.json` to route `/api/shorts` to the Python function and build the Next.js app from `frontend/next.config.js`.
- Set `NEXT_PUBLIC_API_BASE` blank/omitted in Vercel to use the same origin; point it elsewhere only if hosting the API separately.
- Deploy via Vercel CLI (`vercel`, then `vercel --prod`) or the dashboard.

### Tech stack
- Backend: FastAPI, Mangum (for serverless adapter), pydantic-settings
- Frontend: Next.js 14 (App Router), React 18

### Roadmap ideas
- Persistent storage (Supabase/PlanetScale) instead of in-memory shorts
- Upload pipeline with thumbnail generation and basic moderation
- Auth-backed favorites and rate limiting
- Observability (logging/metrics/tracing) and e2e tests

Built with help from ChatGPT for scaffolding and refinement.
