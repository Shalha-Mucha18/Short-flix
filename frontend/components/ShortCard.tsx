import { Short } from "@/types";

type Props = {
  short: Short;
  isActive: boolean;
  isFavorite: boolean;
  onSelect: (id: number) => void;
  onToggleFavorite: (id: number) => void;
};

export function ShortCard({
  short,
  isActive,
  isFavorite,
  onSelect,
  onToggleFavorite,
}: Props) {
  const isYouTube = /youtube\.com|youtu\.be/.test(short.videoUrl);

  return (
    <article
      className={`short-card ${isActive ? "short-card--active" : ""}`}
      onClick={() => onSelect(short.id)}
    >
      {isYouTube ? (
        <div className="short-thumb short-thumb--youtube">
          <span>YouTube Preview</span>
        </div>
      ) : (
        <video
          src={short.videoUrl}
          muted
          loop
          playsInline
          preload="metadata"
          controls={false}
          aria-label={`Preview for ${short.title}`}
        />
      )}
      <button
        type="button"
        className={`favorite ${isFavorite ? "favorite--on" : ""}`}
        onClick={(event) => {
          event.stopPropagation();
          onToggleFavorite(short.id);
        }}
        aria-label={isFavorite ? "Unfavorite" : "Favorite"}
      >
        {isFavorite ? "♥" : "♡"}
      </button>
      <div className="short-card__body">
        <h3 className="short-card__title">{short.title}</h3>
        <div className="short-card__tags">
          {short.tags.map((tag) => (
            <span className="badge" key={tag}>
              #{tag}
            </span>
          ))}
        </div>
      </div>
    </article>
  );
}
