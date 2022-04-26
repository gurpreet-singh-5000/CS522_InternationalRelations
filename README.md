# CS522_InternationalRelations
Social networks exist all around us. Our friend circles, our professional spaces, and vacation hubs are all big intertwined networks of people connected to one another. They are large data structures that are capable of being exploited to know a lot about the space, its properties, and behaviour. Signed social networks are a type of social network that introduces a dichotomy (usually) in edges, usually categorized into positive and negative edges. In most cases, a positive edge signifies a friendship or positive element (based on the use case of the social network), and a negative edge represents an animosity or negative element. Signed social networks can even go one step further by adding weights to edges, depicting the severity of a good or bad relationship. Such networks end up holding a lot of information and can speak volumes about the nodes, the relationships between them, and what they currently or could represent.<br><br>

A lot of the work done in this paper revolves around the use of the balance theorem, a powerful theorem that revolves around stabilizing unstable triangles or triads of nodes embedded in a signed social network. The balance theorem allows only a certain amount of combinations to exist in such triads. To be specific, only triads with zero or two negative edges are said to be stable, and all unstable configurations (having one or three negative edges) are to be shifted into a stable state by attaining one of the possible two stable configurations. For signed social networks with edge weights, a modification of the standard balance theorem has been used in the analysis.<br><br>

Currently, the Russia-Ukraine war has caught all headlines and seems to be a puzzle to most as it has seemed to occur suddenly, out of nowhere. Countless deaths, destruction of property, and unnecessary violence all come hand-in-hand with war. Looking at this issue more closely, from an international relations standpoint, we can individually analyse and introspect various other factors and their spreading through the world social network. Understanding dynamics between different countries can help figure out the reasoning for why such conflicts arise and help us become better prepared to tackle such situations if they were to arise in the future. Predicting the Russia-Ukraine War itself, its outcomes, consequences, estimated time of ending, and severe repercussions if any can all be tried using social networks and their analysis. Attempts to do the same are rarely futile, and often provide a positive effect in one form or the other.<br><br> 

In his book ‘The Better Angels of Nature’’, Steven Pinker talks about the various reasons why violence has declined over time. Though it is something that doesn’t really sound right at first glance, it is actually quite intuitive the more we think about it and is only backed by data. It is something we all should strive to work towards, and achieve. A better understanding of the world and international relations dynamics has also been a key reason for taking precautionary measures and avoiding conflict as much as possible.<br><br>

Our analysis consists of exploration three different areas. Firstly, we understand and reason temporal behaviour of alliances, disputes and signed networks at an international relation level. Secondly, we look at the effect of changing a couple key relations at the international level, and their effect in their relationships with and between other countries. Finally, we analyse how the Russia-Ukraine War has changed the dynamics of the world, and the formation of coalitions as a result of the same.<br><br>

This project has been done by Gurpreet Singh (2018CSB1092), Vikram Setty (2018MED1010), and Parnavi Shrikhande (2018MED1007) as a part of the course CS522 (Social Computing and Networks) under the guidance of Dr. Sudarshan Iyengar at IIT Ropar.

## Instructions to run temporal analysis:

'CS522_InternationalRelations.ipynb' is the Notebook which contains the related code. The various features of the data can be analyzed by running individual cells.<br>
'COW country codes.csv' (country codes), 'alliance_v4.1_by_dyad_yearly.csv' (alliance data) and 'dyadic_mid_4.02.csv' (disputes data) contain the datasets.<br>
Some sample images are attached to show the output of different cells of the notebook.<br>

## Instructions to run Analysing Changes in World Dynamics:

Firstly, navigate into the correct directory<br><br>

Initially, run the following command to get the graph and visualized pictures saved.

    python3 initial_analysis.py
Then, run the following commands for running the different analysis cases:

    python3 analysis1.py

    python3 analysis2.py

    python3 analysis3.py
## Instructions to run Analysing Coalitions:

Firstly, navigate into the correct directory<br><br>

Run the following command to get the desired output from the code.

    python3 before_after_coalitions.py
