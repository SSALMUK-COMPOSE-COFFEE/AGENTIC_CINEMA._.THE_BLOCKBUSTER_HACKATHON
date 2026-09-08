import { useRef } from 'react'
import { fmt } from '../lib/api'
import type { Shot } from '../lib/types'

type Props = {
  shot: Shot
  onAdd?: (s: Shot) => void
  onSimilar?: (s: Shot) => void
  compact?: boolean
}

export function ShotCard({ shot, onAdd, onSimilar, compact }: Props) {
  const video = useRef<HTMLVideoElement>(null)
  const chips = [shot.time_of_day, shot.interior, shot.shot_size?.toUpperCase(), shot.people_count != null ? `${shot.people_count}p` : null, shot.tension ? `T${shot.tension}` : null].filter(Boolean)
  return (
    <div
      className={`card${compact ? ' compact' : ''}`}
      onMouseEnter={() => video.current?.play().catch(() => undefined)}
      onMouseLeave={() => {
        if (video.current) {
          video.current.pause()
          video.current.currentTime = 0
        }
      }}
    >
      <div className="thumb">
        <img src={shot.thumbnail_uri} alt="" loading="lazy" />
        <video ref={video} src={shot.proxy_uri} muted loop playsInline preload="none" />
        <span className="tc">{fmt(shot.t_in)} – {fmt(shot.t_out)}</span>
        {shot.dist != null && <span className="dist">{shot.dist.toFixed(3)}</span>}
      </div>
      {!compact && (
        <>
          <div className="film">{shot.film_title}</div>
          <div className="caption">{shot.caption}</div>
          <div className="chips">{chips.map((c, i) => <span key={i}>{c}</span>)}</div>
          <div className="actions">
            {onAdd && <button onClick={() => onAdd(shot)}>+ Timeline</button>}
            {onSimilar && <button onClick={() => onSimilar(shot)}>Similar</button>}
          </div>
        </>
      )}
    </div>
  )
}
