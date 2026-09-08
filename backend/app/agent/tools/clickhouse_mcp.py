import shutil

from google.adk.tools import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp.client.stdio import StdioServerParameters

from app.config import settings


def clickhouse_env() -> dict[str, str]:
    return {
        "CLICKHOUSE_HOST": settings.clickhouse_host,
        "CLICKHOUSE_PORT": str(settings.clickhouse_port),
        "CLICKHOUSE_USER": settings.clickhouse_user,
        "CLICKHOUSE_PASSWORD": settings.clickhouse_password,
        "CLICKHOUSE_DATABASE": settings.clickhouse_database,
        "CLICKHOUSE_SECURE": str(settings.clickhouse_secure).lower(),
        "CLICKHOUSE_VERIFY": "false",
        "CLICKHOUSE_MCP_SERVER_TRANSPORT": "stdio",
    }


def make_clickhouse_toolset(tool_filter: list[str] | None = None) -> McpToolset:
    command = shutil.which(settings.mcp_clickhouse_command) or settings.mcp_clickhouse_command
    return McpToolset(
        connection_params=StdioConnectionParams(
            server_params=StdioServerParameters(command=command, args=[], env=clickhouse_env()),
            timeout=60,
        ),
        tool_filter=tool_filter or ["run_query", "list_tables"],
    )
