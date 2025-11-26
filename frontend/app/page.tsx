import { ShortsView } from "@/components/ShortsView";
import { Short } from "@/types";

export const revalidate = 0;

async function getShorts(): Promise<Short[]> {
  // On Vercel, skip SSR fetch and let client handle it
  if (process.env.NODE_ENV === "production") {
    return [];
  }
  
  // Only fetch on localhost during development
  const base = process.env.NEXT_PUBLIC_API_BASE || "http://localhost:8000";

  try {
    const response = await fetch(`${base}/api/shorts`, { cache: 'no-store' });
    if (!response.ok) {
      return [];
    }
    return response.json();
  } catch (error) {
    console.error("Error fetching shorts:", error);
    return [];
  }
}

export default async function Home() {
  const shorts = await getShorts();

  return (
    <main className="page">
      <section className="hero">
        <div className="hero__aura" aria-hidden />
        <div className="hero__content">
          <div>
            <span className="hero__pill">
              <span aria-hidden>⚡</span> Curated micro-stories
            </span>
            <h1 className="hero__title">
              Short<span className="hero__accent">-flix</span>
            </h1>
            <p className="hero__desc">
              A cinematic playground for quick clips: FastAPI streams the stories, Next.js
              paints the glossy stage, and the whole thing is ready to ship as a sleek
              serverless drop.
            </p>
          </div>
        </div>
        <div className="hero__badge">
          <span className="badge badge--ghost">Live preview</span>
          <span className="badge badge--accent">Serverless-ready</span>
        </div>
      </section>

      <ShortsView initialShorts={shorts} />
    </main>
  );
}
