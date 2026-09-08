import { fmt } from '../lib/api'
import type { Shot, Warning } from '../lib/types'

type Props = {
  items: Shot[]
  warnings: Warning[]
  onRemove: (id: string) => void
  onMove: (id: string, dir: -1 | 1) => void
  onExport: () => void
  onClear: () => void
}

export function Timeline({ items, warnings, onRemove, onMove, onExport, onClear }: Props) {
  const total = items.reduce((a, s) => a + (s.t_out - s.t_in), 0)
  const warnAfter = new Map<string, Warning>()
  for (const w of warnings) warnAfter.set(w.pair[0], w)
  const starts: number[] = []
  items.reduce((acc, s) => {
    starts.push(acc)
    return acc + (s.t_out - s.t_in)
  }, 0)
  return (
    <div className="timeline">
      <div className="tl-head">
        <h3>Timeline <span>{items.length} shots · {fmt(total)}</span></h3>
        <div>
          <button onClick={onExport} disabled={!items.length}>Export EDL</button>
          <button onClick={onClear} disabled={!items.length} className="ghost">Clear</button>
        </div>
      </div>
      <div className="tl-track">
        {items.map((s, i) => {
          const start = starts[i]
          const w = warnAfter.get(s.shot_id)
          return (
            <div key={s.shot_id} className="tl-item" style={{ flexGrow: Math.max(1, s.t_out - s.t_in) }}>
              <img src={s.thumbnail_uri} alt="" />
              <div className="tl-meta">
                <span>{fmt(start)}</span>
                <span>{s.film_title}</span>
              </div>
              <div className="tl-btns">
                <button onClick={() => onMove(s.shot_id, -1)} disabled={i === 0}>‹</button>
                <button onClick={() => onRemove(s.shot_id)}>×</button>
                <button onClick={() => onMove(s.shot_id, 1)} disabled={i === items.length - 1}>›</button>
              </div>
              {w && i < items.length - 1 && (
                <div className={`warn ${w.severity}`} title={w.explanation}>⚠ {w.rule}</div>
              )}
            </div>
          )
        })}
        {!items.length && <div className="tl-empty">Add shots from search results, or ask for a cut.</div>}
      </div>
      {warnings.length > 0 && (
        <ul className="warn-list">
          {warnings.map((w, i) => (
            <li key={i} className={w.severity}>
              <b>{w.severity}</b> {w.pair[0]} → {w.pair[1]}: {w.explanation}
            </li>
          ))}
        </ul>
      )}
    </div>
  )
}
