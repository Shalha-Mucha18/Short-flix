import { ShortsView } from "@/components/ShortsView";
import { Short } from "@/types";

export const revalidate = 0;

async function getShorts(): Promise<Short[]> {
  let base = "";
  
  // In production (Vercel), use the deployment URL
  if (process.env.NODE_ENV === "production") {
    base = process.env.VERCEL_URL 
      ? `https://${process.env.VERCEL_URL}` 
      : "";
  } else if (process.env.NEXT_PUBLIC_API_BASE) {
    base = process.env.NEXT_PUBLIC_API_BASE;
  } else {
    base = "http://localhost:8000";
  }
  
  base = base.replace(/\/$/, "");

  try {
    const url = `${base}/api/shorts`;
    console.log("Fetching from:", url);
    const response = await fetch(url, { cache: 'no-store' });

    if (!response.ok) {
      console.error(`Failed to fetch shorts: ${response.status} ${response.statusText}`);
      throw new Error(`Failed to fetch shorts: ${response.statusText}`);
    }

    const data = await response.json();
    console.log("Fetched shorts:", data.length);
    return data;
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
