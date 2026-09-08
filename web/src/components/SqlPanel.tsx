export function SqlPanel({ sql, count, ms, queryMs }: { sql: string | null; count: number | null; ms: number | null; queryMs: number | null }) {
  if (!sql) return null
  return (
    <details className="sql-panel" open>
      <summary>
        Query the Librarian ran on ClickHouse
        {count != null && <span>{count} rows</span>}
        {queryMs != null && <span>ClickHouse {queryMs} ms</span>}
        {ms != null && <span>agent round-trip {(ms / 1000).toFixed(1)} s</span>}
      </summary>
      <pre>{sql}</pre>
    </details>
  )
}
