Title: A Comprehensive Guide to Database Sharding

URL Source: https://newsletter.francofernando.com/p/a-comprehensive-guide-to-database

Published Time: 2025-01-16T13:55:44+00:00

Markdown Content:
Hi Friends,

Welcome to the 105th issue of the Polymathic Engineer newsletter. This week, we will talk about database sharding.

The database is an important part of any application, but it is also one of the hardest to scale horizontally. Sharding is a way to deal with the problems related to database scaling.

The outline is as follows:

*   What is sharding, and why use it

*   Disadvantages of sharding

*   Alternatives to sharding

*   Horizontal vs Vertical partitioning

*   Types of sharding

*   Choosing a shard key

*   Routing Requests

*   Shards rebalancing

Sharding is a powerful technique used to scale databases, allowing them to handle a larger volume of data and a higher number of queries. The idea is to spread the data across several machines, each handling a portion of the whole.

Imagine you have a giant book that's become too big to fit on a single shelf. Sharding is like dividing that book into small chapters and putting them on different shelves.

When an application's data keeps growing, its volume will eventually become large enough that it can't fit on a single machine, or the machine can no longer handle the expected workload.

To work around that, data needs to be split into pieces called shards, small enough to fit into individual nodes. As an additional benefit, the system's capacity for handling requests also increases since the load of accessing the data is spread over more nodes.

![Image 1](https://substackcdn.com/image/fetch/$s_!kIU2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff8ddf746-68ea-422c-b9ee-e1030bc11ccd_932x341.png)

By distributing the data and query load across multiple machines, sharding allows a database to scale horizontally, accommodating growth in a more flexible and cost-effective way than simply upgrading to larger and larger machines (vertical scaling).

As data volume increases, you can add more shards to accommodate the growth. But it’s not only about scalability. By distributing the query load across multiple machines, sharding can significantly improve response times and overall system throughput.

Additionally, sharding makes also the overall system more available. If one shard goes down, the others can continue to operate, reducing the risk of complete system failure.

While sharding can make a database much more scalable, faster, and available, it is not a free lunch since it makes the system design more complicated.

First, managing multiple database instances increases operational complexity since tasks like backups, schema changes, and monitoring become more involved.

Second, implementing sharding requires careful planning and considering factors such as how to route queries to the correct shard and distribute data evenly.

If not well implemented, sharding can lead to uneven data distribution, creating "hot spots" where some shards are overloaded while others are underutilized. Additionally, you may need to rebalance data across shards as your system grows or shrinks, which can be complex and potentially disruptive if not managed properly.

Third, it's essential to remember how operations like joins or group by, become much more complex and less efficient since data needs to be taken from multiple shards and put together. Also transactions are required to atomically update data across multiple partitions, limiting scalability.

So, here are some essential things you need to think about before you shard a database:

- How do you distribute the data across shards? Which are the potential hotspots if data isn't distributed evenly?

- What queries do you run, and how do the tables interact?

- How will data grow over time? How will it need to be redistributed?

What you do will depend on how you answer these questions.

Even though sharding can significantly improve a database's capabilities, it's critical to consider its pros and cons carefully. The benefits of sharding only become clear at a certain size for many applications.

For smaller systems, the extra complexity might not be worth it, and using a different growth strategy might be better.
