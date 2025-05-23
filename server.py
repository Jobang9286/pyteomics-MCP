from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base

mcp = FastMCP("pyteomics_mcp", prompt_template=base)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:mcp", host="0.0.0.0", port=8000)
