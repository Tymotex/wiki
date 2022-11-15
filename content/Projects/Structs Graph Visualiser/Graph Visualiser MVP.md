# Graph Visualiser MVP

**Goals**
- ~~Animate static edge adding and removal. Bring in anime.js~~ → on second thoughts… let’s not do static edge adding and removal. It’s a bit of a hassle and we’d actually want to re-layout the graph since adding a static edge could ruin an otherwise aesthetic planar graph.
- **~~Directedness**: need to modify the line SVG for each link to signal direction.~~
- **~~Weightedness**: need to add a weight `<text>` element to the midpoint of each link.~~
    - Furthermore, need to be able to change an edge weight.
- Integrate the graph visualiser into the codebase. Give typings to everything in the graph visualiser beforehand.
- Animate BFS.
- Be able to animate a matrix data structure (should be pretty easy. Just have an HTML table?). It would be challenging to coordinate and sync (probably needs to be embedded in the svg parent of the visualiser)
- Bring the graph to the Structs codebase.
- Be able to animate a queue. Similar challenges to animating a matrix.
- Animate DFS.

**Issues**
- It would be good to add a vertex or edge without reloading the graph.
    - For adding/removing edges without reloading the graph:
    Just modify the DOM directly. Don’t bother recreating the graph. It’s adding a node that is problematic since we don’t know where to put the node statically.
- ~~Self-linking nodes. Maybe just don’t support them entirely and treat it as bad user input.~~
    - Decided to not support this.
- Weight labels can be blocked by vertices above them.
    - Solved.

**Ideas**
- Add a legend for tracking visited nodes.
- Could be useful to have a split pane UI or just some kind of division.
    - 1 pane for the graph.
    - 1 pane for the supporting data structures which should also be visualised and synced with the graph.

**Excellent Resources**
- [https://wattenberger.com/blog/d3#drawing-svg-shapes](https://wattenberger.com/blog/d3#drawing-svg-shapes)
- [https://wattenberger.com/blog/react-and-d3](https://wattenberger.com/blog/react-and-d3)
- [https://medium.com/ninjaconcept/interactive-dynamic-force-directed-graphs-with-d3-da720c6d7811](https://medium.com/ninjaconcept/interactive-dynamic-force-directed-graphs-with-d3-da720c6d7811)
- [https://observablehq.com/@d3/force-directed-graph](https://observablehq.com/@d3/force-directed-graph)
- [https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial)
- [http://bl.ocks.org/fancellu/2c782394602a93921faff74e594d1bb1](http://bl.ocks.org/fancellu/2c782394602a93921faff74e594d1bb1)

---

## 13th Aug Notes
Main challenge right now is creating the graph layout from an adjacency matrix/list, then being able to add new vertices and edges to it and have the graph re-layout.

I’ll just use force-directed layout.

Nodes connected by an edge are attracted through Hooke’s Law: $F_s=-kx$.

Nodes are repelled by the repulsive force between them. Coulomb’s Law: $F_c=k\frac{q_1 q_2}{r^2}$.

I’m using D3 and D3-force to generate the graph on the DOM rather than HTML canvas so that we can query and manipulate the graph the same way we do for the linked list and BST.

**Excellent Resources**

**Things to learn**

I need to know the basics of svgs and how to work with them (this would really serve me in general).

I need to learn the basics of d3.

**Current state**
![first demo|400](Projects/Structs%20Graph%20Visualiser/Graph%20Visualiser%20MVP/first-demo.png)

When the button is pressed, it selects a node by ID and changes its fill and radius, then it selects a link by ID and changes its fill and radius.

Every node is assigned an ID and every link is given classnames that they can be queried by. We could make this follow a standard:

- Vertices: `id=vertex-n`, where n is `0, 1, 2 …, numVertices`
- Edges: `class=edge-n-m`, where n and m are `0, 1, 2 …, numVertices`
    - In directed graphs, edge-n-m refers to the edge from n→m specifically.
    - We need to use classnames since it’s not possible to assign multiple IDs to an edge (we wanted multiple IDs so that edge-n-m and edge-m-n refer to the same element, in the case of undirected graphs).

Following this standard makes it easy to lookup the node/edge on the DOM through an adjacency matrix. For example:

![vertex and edge query example|500](Projects/Structs%20Graph%20Visualiser/Graph%20Visualiser%20MVP/vertex-edge-query.png)

When we want to highlight the edge between 0 and 1 as part of a BFS animation for example, then we look up row 0 in the matrix, find an outgoing connection to 1, put it into a visit queue, then start the highlight animation on `.edge-0-1`.

We can now add a new vertex.

![adding vertex screenshot|400](Projects/Structs%20Graph%20Visualiser/Graph%20Visualiser%20MVP/adding-vertex.png)

2 problems arise: 
1. Adding a vertex forcefully reloads the graph since we cannot know where to put the vertex statically. This problem doesn’t exist for vertex removal since we can statically delete the vertex and all its edges.
2. Adding an edge forcefully reloads the graph, but this can be worked around by statically inserting the edge. This also works for edge removal.

Furthermore, when spawning new vertices, they would fly off the screen as you’d expect since there is no link to the new vertex, and so no force is acting to keep the vertex where you’d want it to be. 

I’m clamping the x and y displacement of nodes to be within the svg parent dimensions following this post: [https://stackoverflow.com/questions/9573178/d3-force-directed-layout-with-bounding-box](https://stackoverflow.com/questions/9573178/d3-force-directed-layout-with-bounding-box). This prevents the vertex from flying off the screen.

With this solution however, the vertices will still cluster around the edges, which looks very abnormal. To rectify this, I increased the central force magnitude with `forceManyBody` and `forceCenter`. I saw more natural spacing applied with a higher value for `forceManyBody`.

Also, as a bonus from using D3 and D3-force, the vertices are all draggable by the user, so they can rearrange the graph however they want.

---

## 14th Aug
Goals today: 
- ~~Add a form for highlighting a vertex.~~
- ~~Add a form for highlighting an edge.~~
- ~~Add a form for inserting a new edge.~~
- ~~Add support for directed graphs.~~
- ~~Add support for weighted graphs.~~
- ~~Try disabling the force animation. See: [https://stackoverflow.com/questions/47510853/how-to-disable-animation-in-a-force-directed-graph](https://stackoverflow.com/questions/47510853/how-to-disable-animation-in-a-force-directed-graph).~~

I’ve added some inputs that add new vertices, edges and highlights existing vertices and edges. These were quite straightforward to implement, they just make small changes to the underlying data structures and apply CSS rules after being selected by document.querySelector.

I also added the arrowheads for directed graphs, going both 1-way and 2-ways, and I added labels to the midpoint of the links. I learned about `<defs>`, `<marker>` and the attributes: marker-end and marker-start when implementing the arrowheads, taking inspiration from this example: [http://bl.ocks.org/fancellu/2c782394602a93921faff74e594d1bb1](http://bl.ocks.org/fancellu/2c782394602a93921faff74e594d1bb1). I simply tweaked the attributes until it would fit the current graph proportions.

![final first iteration demo|400](Projects/Structs%20Graph%20Visualiser/Graph%20Visualiser%20MVP/final-first-prototype.png)

![[Projects/Structs Graph Visualiser/assets/Graph-MVP-1.mp4|600]]

---

## 15th Aug
Goals today:
- ~~Upload Gist of App.jsx, record a video, and tell Dom and Joanna.~~

Some further ideas for the graph visualiser: 
- I think it would be very useful to also animate the supporting data structures for the graph. Eg.
for BFS, we could show an animation for the visit queue and how that changes,
or for Dijkstra we could show the predecessor array and priority queue, etc.
- I also think it'd be helpful to show the state of the underlying 
graph data structure, ie. the contents of the adjacency matrix and adjacency 
list. We wouldn't have to animate this, probably

---

## 8th Sep
Goals today:
- Get the graph to render inside the visualiser page of Structs.sh
- Parameterise some sizing and force values.
- Get unanimated add vertex and add edge buttons working.
- Get DFS working and animated.
- Record a sample of DFS to share.

I need to figure out how the BST resets the styling after the animation concludes. I also need to figure out why the attribute animates from black to yellow and note white (the initial fill) to yellow.

![integrated graph visualiser with dfs|700](Projects/Structs%20Graph%20Visualiser/Graph%20Visualiser%20MVP/integrated-prototype-demo.png)

![[Projects/Structs Graph Visualiser/assets/Graph-MVP-2.mp4|600]]

---
## 15th Nov
- Refactored all the rendering code.
- Fixed the arrowhead `<marker>` problem where we couldn't target specific arrowheads to apply styling to.
- Angled the weight labels.
- Fixed animation errors from before (vertices and edges were blacked out when the animation timeline was seeked with the slider).
- Made the graph render statically (as opposed to showing the 'big-bang' animation where all the vertices rapidly move to its equilibrium position).

![[Projects/Structs Graph Visualiser/assets/graph-mvp-15th-nov-demo-vid.mp4|600]]
![[Projects/Structs Graph Visualiser/assets/graph-mvp-15th-nov.png|600]]

Agenda for next meeting:
- Code review.
- Weightedness and directedness checkbox problem: should we have visualiser-specific controller components? Currently it's awkward to do.
- Styling of the highlighted vertices and edges.
