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
        A formatted string containing the title, authors, year, URL, and abstract of the retrieved papers.
    """
    client = arxiv.Client()
    search = arxiv.Search(query=query, 
                          max_results=max_results,
                         sort_by=arxiv.SortCriterion.Relevance)
    
    results = []
    for paper in client.results(search):
        # Extract authors into a comma-separated string
        authors = ", ".join([author.name for author in paper.authors])
        year = paper.published.year
        
        # Provide ALL the metadata the agent needs to write citations
        results.append(
            f"Title: {paper.title}\n"
            f"Authors: {authors}\n"
            f"Year: {year}\n"
            f"URL: {paper.entry_id}\n"
            f"Abstract: {paper.summary}"
        )
        
    if not results:
        return "No papers found for this query."
        
    return "\n\n---\n\n".join(results)
