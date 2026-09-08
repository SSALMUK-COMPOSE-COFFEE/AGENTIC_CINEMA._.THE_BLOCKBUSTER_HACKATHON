export function SqlPanel({ sql, count, ms }: { sql: string | null; count: number | null; ms: number | null }) {
  if (!sql) return null
  return (
    <details className="sql-panel" open>
      <summary>
        Query the Librarian ran on ClickHouse
        {count != null && <span>{count} rows</span>}
        {ms != null && <span>{ms} ms</span>}
      </summary>
      <pre>{sql}</pre>
    </details>
  )
}
