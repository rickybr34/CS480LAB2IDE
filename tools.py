import arxiv
from smolagents import tool

@tool
def search_arxiv(query: str, max_results: int = 3) -> str:
    """
    Searches arXiv for academic papers based on a query.
    
    Args:
        query: The search terms (e.g., 'Neural SDEs time series').
        max_results: The maximum number of papers to return. Defaults to 3.
        
    Returns:
        A formatted string containing the title and abstracts of the retrieved papers.
    """
    # Initialize the arXiv client and execute the search
    client = arxiv.Client()
    search = arxiv.Search(query=query, max_results=max_results)
    
    results = []
    for paper in client.results(search):
        # Format the output so the LLM can easily parse the metadata
        results.append(f"Title: {paper.title}\nAbstract: {paper.summary}")
        
    if not results:
        return "No papers found for this query."
        
    # Join all paper details into a single text block
    return "\n\n---\n\n".join(results)