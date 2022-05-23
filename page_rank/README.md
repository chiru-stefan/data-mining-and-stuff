<h3> Papers: </h3>
<h4> <a href="http://ilpubs.stanford.edu:8090/422/1/1999-66.pdf"> The PageRank Citation Ranking: Bringing Order to the Web </a> </h4>
<h4> <a href=http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.330.8697> CONVERGENCE ANALYSIS OF AN IMPROVED PAGERANK ALGORITHM </a>  </h4>

<h3> Summary </h3>
The PageRank algorithm outputs a probability distribution used to represent the likelihood that a person randomly clicking on links will arrive at any particular page. 

PageRank works by counting the number and quality of links to a page to determine a rough estimate of how important the website is. The underlying assumption is that more important websites are likely to receive more links from other websites.


Note:
<it>Non-degenerate vector: vector with all elements &#8800; 0</it>

<h3> Dataset: </h3>
<h4> <a href="https://www.limfinity.com/ir/"> Pagerank and Web-based Information Retrieval - Data </a> </h4>

The input used in this implementation (inputs) is as follows: Note: Each line is 2 values seperated by a space.

    First line: NodesCount EdgesCount (e.g. "5 9")
    NC next lines: NodeID NodeURL (e.g. "1 http://example.com")
    EC next lines: NodeID OutlinkToNodeID (e.g. "1 2")

![img.png](documentation/img.png)

