"use client";

import { useEffect, useMemo, useState } from "react";
import { Short } from "@/types";
import { ShortCard } from "./ShortCard";

type Props = {
  initialShorts: Short[];
};

export function ShortsView({ initialShorts }: Props) {
  const [shorts, setShorts] = useState(initialShorts ?? []);
  const [query, setQuery] = useState("");
  const [selectedTag, setSelectedTag] = useState<string | null>(null);
  const [favorites, setFavorites] = useState<number[]>([]);
  const [activeId, setActiveId] = useState<number | null>(
    shorts.length ? shorts[0].id : null,
  );
  const [favoritesOnly, setFavoritesOnly] = useState(false);
  const [newTitle, setNewTitle] = useState("");
  const [newUrl, setNewUrl] = useState("");
  const [newTags, setNewTags] = useState("");
  const [submitState, setSubmitState] = useState<"idle" | "submitting" | "error" | "success">("idle");
  const [submitMessage, setSubmitMessage] = useState("");
  const [deleteState, setDeleteState] = useState<"idle" | "deleting" | "error">("idle");
  const [deleteMessage, setDeleteMessage] = useState("");

  const apiBase = process.env.NEXT_PUBLIC_API_BASE
    ? process.env.NEXT_PUBLIC_API_BASE.replace(/\/$/, "")
    : "";

  const tags = useMemo(() => {
    const unique = new Set<string>();
    shorts.forEach((item) => item.tags.forEach((tag) => unique.add(tag)));
    return Array.from(unique);
  }, [shorts]);

  const filtered = useMemo(() => {
    const normalizedQuery = query.trim().toLowerCase();

    return shorts.filter((item) => {
      const matchesQuery =
        !normalizedQuery ||
        item.title.toLowerCase().includes(normalizedQuery) ||
        item.tags.some((tag) => tag.toLowerCase().includes(normalizedQuery));

      const matchesTag =
        !selectedTag ||
        item.tags.some((tag) => tag.toLowerCase() === selectedTag.toLowerCase());

      const matchesFavorite = !favoritesOnly || favorites.includes(item.id);

      return matchesQuery && matchesTag && matchesFavorite;
    });
  }, [favorites, favoritesOnly, query, selectedTag, shorts]);

  useEffect(() => {
    if (filtered.length === 0) {
      setActiveId(null);
      return;
    }

    const current = filtered.find((item) => item.id === activeId);
    if (!current) {
      setActiveId(filtered[0].id);
    }
  }, [activeId, filtered]);

  const activeShort =
    filtered.find((item) => item.id === activeId) ?? filtered[0] ?? null;

  const isYouTube = (url: string) => /youtube\.com|youtu\.be/.test(url);

  const toYouTubeEmbed = (url: string) => {
    try {
      const u = new URL(url);
      if (u.hostname.includes("youtu.be")) {
        return `https://www.youtube.com/embed/${u.pathname.slice(1)}`;
      }
      if (u.searchParams.get("v")) {
        return `https://www.youtube.com/embed/${u.searchParams.get("v")}`;
      }
      if (u.pathname.startsWith("/embed/")) {
        return url;
      }
    } catch {
      return url;
    }
    return url;
  };

  const toggleFavorite = (id: number) => {
    setFavorites((prev) =>
      prev.includes(id) ? prev.filter((item) => item !== id) : [...prev, id],
    );
  };

  const clearFilters = () => {
    setQuery("");
    setSelectedTag(null);
    setFavoritesOnly(false);
  };

  const handleCreate = async () => {
    if (!newTitle.trim() || !newUrl.trim()) {
      setSubmitState("error");
      setSubmitMessage("Title and video URL are required.");
      return;
    }

    const tags = newTags
      .split(",")
      .map((t) => t.trim())
      .filter(Boolean);

    try {
      setSubmitState("submitting");
      setSubmitMessage("");
      const response = await fetch(`${apiBase ?? ""}/api/shorts`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title: newTitle.trim(), videoUrl: newUrl.trim(), tags }),
      });

      if (!response.ok) {
        throw new Error(await response.text());
      }

      const created: Short = await response.json();
      setShorts((prev) => [...prev, created]);
      setActiveId(created.id);
      setNewTitle("");
      setNewUrl("");
      setNewTags("");
      setSubmitState("success");
      setSubmitMessage("Added!");
      setFavoritesOnly(false);
    } catch (error) {
      console.error(error);
      setSubmitState("error");
      setSubmitMessage("Could not save. Check the URL and try again.");
    } finally {
      setTimeout(() => setSubmitState("idle"), 2000);
    }
  };

  const handleDelete = async (id: number) => {
    try {
      setDeleteState("deleting");
      setDeleteMessage("");
      const response = await fetch(`${apiBase}/api/shorts/${id}`, {
        method: "DELETE",
      });
      if (!response.ok) {
        throw new Error("Failed to delete");
      }
      const updatedFavorites = favorites.filter((item) => item !== id);
      setFavorites(updatedFavorites);

      setShorts((prev) => {
        const updated = prev.filter((item) => item.id !== id);
        const normalizedQuery = query.trim().toLowerCase();
        const nextFiltered = updated.filter((item) => {
          const matchesQuery =
            !normalizedQuery ||
            item.title.toLowerCase().includes(normalizedQuery) ||
            item.tags.some((tag) => tag.toLowerCase().includes(normalizedQuery));

          const matchesTag =
            !selectedTag ||
            item.tags.some((tag) => tag.toLowerCase() === selectedTag.toLowerCase());

          const matchesFavorite = !favoritesOnly || updatedFavorites.includes(item.id);

          return matchesQuery && matchesTag && matchesFavorite;
        });

        setActiveId((current) => {
          if (current === id) {
            return nextFiltered[0]?.id ?? null;
          }
          return current;
        });

        return updated;
      });

      setDeleteState("idle");
      setDeleteMessage("");
    } catch (error) {
      console.error(error);
      setDeleteState("error");
      setDeleteMessage("Could not delete this reel.");
      setTimeout(() => setDeleteState("idle"), 2500);
    }
  };

  return (
    <>
      <section className="filters">
        <div className="filters__row">
          <input
            value={query}
            onChange={(event) => setQuery(event.target.value)}
            placeholder="Search title or tags"
            className="filters__search"
            aria-label="Search videos"
          />
          <button
            className={`chip ${favoritesOnly ? "chip--active" : ""}`}
            onClick={() => setFavoritesOnly((prev) => !prev)}
          >
            Favorites
          </button>
          <button className="chip" onClick={clearFilters}>
            Clear
          </button>
        </div>
        <div className="filters__row">
          <span className="badge">Tags</span>
          <button
            className={`chip ${selectedTag === null ? "chip--active" : ""}`}
            onClick={() => setSelectedTag(null)}
          >
            All
          </button>
          {tags.map((tag) => (
            <button
              key={tag}
              className={`chip ${
                selectedTag?.toLowerCase() === tag.toLowerCase()
                  ? "chip--active"
                  : ""
              }`}
              onClick={() => setSelectedTag(tag)}
            >
              #{tag}
            </button>
          ))}
        </div>
      </section>

      <section className="board">
        <div className="player-panel">
          {activeShort ? (
            <div className="player-card">
              {isYouTube(activeShort.videoUrl) ? (
                <iframe
                  key={activeShort.videoUrl}
                  src={toYouTubeEmbed(activeShort.videoUrl)}
                  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                  allowFullScreen
                  title={activeShort.title}
                  className="player-iframe"
                />
              ) : (
                <video
                  key={activeShort.id}
                  src={activeShort.videoUrl}
                  controls
                  autoPlay
                  playsInline
                  controlsList="nodownload"
                />
              )}
              <div className="player-info">
                <h2 className="player-title">{activeShort.title}</h2>
                <div className="tag-row">
                  {activeShort.tags.map((tag) => (
                    <span key={tag} className="badge">
                      #{tag}
                    </span>
                  ))}
                </div>
              </div>
            </div>
          ) : (
            <div className="empty-state">
              No videos match your filters yet. Try a different search.
            </div>
          )}
          <div className="controls">
            <span>
              🎬 {filtered.length} short{filtered.length === 1 ? "" : "s"}
            </span>
            <div className="control-actions">
              <span>Favorites stay local to your browser.</span>
              {activeShort && (
                <button
                  className="button button--danger button--small"
                  onClick={() => handleDelete(activeShort.id)}
                  disabled={deleteState === "deleting"}
                >
                  {deleteState === "deleting" ? "Deleting…" : "Delete reel"}
                </button>
              )}
            </div>
          </div>
          {deleteMessage && <div className="create-card__status status--error">{deleteMessage}</div>}
        </div>

        <div className="grid">
          <div className="create-card">
            <div className="create-card__header">
              <div>
                <h3>Feature a new reel</h3>
                <p>Drop any video or YouTube link with a title and tags.</p>
              </div>
              <button className="button button--ghost" onClick={clearFilters}>
                Reset filters
              </button>
            </div>
            <div className="create-card__form">
              <input
                className="input"
                placeholder="Title"
                value={newTitle}
                onChange={(e) => setNewTitle(e.target.value)}
              />
              <input
                className="input"
                placeholder="Video URL (mp4 or YouTube link)"
                value={newUrl}
                onChange={(e) => setNewUrl(e.target.value)}
              />
              <input
                className="input"
                placeholder="Tags (comma separated, e.g. travel,city,night)"
                value={newTags}
                onChange={(e) => setNewTags(e.target.value)}
              />
              <button
                className="button"
                onClick={handleCreate}
                disabled={submitState === "submitting"}
              >
                {submitState === "submitting" ? "Adding..." : "Add short"}
              </button>
            </div>
            {submitMessage && (
              <div
                className={`create-card__status ${
                  submitState === "error" ? "status--error" : "status--success"
                }`}
              >
                {submitMessage}
              </div>
            )}
          </div>
          {filtered.length === 0 ? (
            <div className="empty-state">
              Nothing found. Clear filters to see everything.
            </div>
          ) : (
            <div className="grid__layout">
              {filtered.map((short) => (
                <ShortCard
                  key={short.id}
                  short={short}
                  isActive={activeShort?.id === short.id}
                  isFavorite={favorites.includes(short.id)}
                  onSelect={setActiveId}
                  onToggleFavorite={toggleFavorite}
                />
              ))}
            </div>
          )}
        </div>
      </section>
    </>
  );
}
