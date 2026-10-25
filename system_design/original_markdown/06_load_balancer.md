Title: The Definitive Guide to Load Balancers

URL Source: https://newsletter.francofernando.com/p/the-definitive-guide-to-load-balancers

Published Time: 2025-03-14T10:05:46+00:00

Markdown Content:
Hi Friends,

Welcome to the 113th issue of the Polymathic Engineer.

This week we'll dive deep into how load balancers work. We'll look at different types and methods, as well as more advanced ideas and tips that you can use to make load balancing work better in your own systems.

The outline will be as as follows:

*   Why load balancers matter

*   Load balancers fundamentals

*   Types of load balancers

*   Load balancing algorithms

*   Advanced features

*   Redundancy

*   Scaling

Project-based learning is the best way to develop technical skills. [CodeCrafters](https://app.codecrafters.io/join?via=FrancoFernando)is an excellent platform for practicing exciting projects, such as building your version of Redis, Kafka, [DNS server](https://app.codecrafters.io/join/dns-server?via=francofernando), SQLLite, or Git from scratch.

[Sign up, and become a better software engineer](https://app.codecrafters.io/join?via=FrancoFernando).

Load balancers are critical parts of any distributed system. To see why they are so important, let's start with a simple use case. Suppose you have a client that sends requests to a server.

The server runs some business logic, fetches data from a database, and returns responses to the client. All this works perfectly fine when traffic is low. But what happens when your system grows and the server gets thousands of requests at once?

A single server has limited resources and throughput; as requests pile up, response times get much slower. Eventually, your server gets overwhelmed, which will cause timeout problems, failed requests, and angry users.

This is where scaling comes in, and you have two main options. You can make your server more powerful by adding more CPU, RAM, or storage through _vertical scaling_. This method is simple, but a single machine can only hold so much hardware, and as you get closer to those limits, costs go up very quickly.

_Horizontal scaling_, on the other hand, adds more computers to spread out the work. It offers practically unlimited scaling potential, but introduces a critical question: how do clients know which server to connect to?

This is precisely where load balancers come in handy. A load balancer sits between your clients and your server pool. It sends requests to various servers, distributing requests across multiple servers.

In theory, if you add more servers with the same amount of resources, your system should be able to handle a proportionally larger load. But this only works if the requests are spread out fairly.

A load balancer's main job is to ensure that no server gets too busy while the others do nothing. This makes your system more resilient and able to handle more traffic.

A load balancer is placed between a set of clients and a set of servers and acts as a reverse proxy, directing requests from clients to the servers. Its main job is to make sure that no one server is overloaded while other servers aren't being used.

![Image 1](https://substackcdn.com/image/fetch/$s_!yFg8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff9852388-ff97-4c5f-b794-47063f351963_613x250.png)

You can put load balancers in different parts of your system. Most of the time, they're put between clients and web servers, but you can also put them between servers and databases or at the DNS layer.

There are multiple benefits you get when using load balancers:

*   Load balancers spread client requests across servers so that your hardware is used most efficiently. This means you use the resources you already have better before you need to add more.

*   Load balancers help keep response times low by sending requests to the sites that aren't busy. Users get faster responses, which means a better experience.

*   If a server fails or needs maintenance, the load balancer stops sending data to it on its own. Users will not notice any break in service this way.

*   Load balancers make it simple to add or remove servers. Users won't be affected when you take servers offline for updates or add more ones when traffic goes up.

Now that we understand what load balancers do and why they're valuable, let's look at the different kinds and when to use each one.

There are different ways to categorize load balancers. Let's look at the most common types and when to use them. The first categorization distinguishes between hardware and software load balancers.

**Hardware load balancers** are physical devices that can handle high traffic volumes from many kinds of applications. They can also run multiple virtual load balancer instances on the same device. Hardware load balancers are very efficient but also expensive. Popular vendors include Citrix and Radware.

**Software load balancers** run on standard servers. They are usually more flexible and cheaper, easier to keep up to date and can be installed in cloud environments. Nginx, HAProxy, and cloud services like AWS Elastic Load Balancing are all examples.

The second key way to group load balancers is by the network layer where they work.

**Layer 4 load balancers** (Transport layer) redirect traffic based only on IP addresses and TCP/UDP ports. They don't look at what's inside the packets and don't need to decrypt HTTPS traffic. This makes them faster but less flexible because they can't make routing decisions based on the content of requests.

[![Image 2](https://substackcdn.com/image/fetch/$s_!9go6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6dfcfbc4-b4ea-4172-aacb-bd7ac2fa85a3_851x354.png)](https://substackcdn.com/image/fetch/$s_!9go6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6dfcfbc4-b4ea-4172-aacb-bd7ac2fa85a3_851x354.png)

**Layer 7 load balancers** (Application layer) can look at the content of each request, including HTTP headers, cookies, and URLs. This lets them make smarter routing decisions:

*   They can route requests based on the URL path (like sending /api/* to one set of servers and /images/* to another)

*   They can check cookies to keep a user on the same server (session persistence)

*   They can cache responses for common requests

*   They can add or modify HTTP headers

[![Image 3](https://substackcdn.com/image/fetch/$s_!Nqpy!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe1f0a0f5-cfbb-4cfc-8a37-79ff02330ecb_857x358.png)](https://substackcdn.com/image/fetch/$s_!Nqpy!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe1f0a0f5-cfbb-4cfc-8a37-79ff02330ecb_857x358.png)

However, Layer 7 load balancers requires more processing power since they have to inspect each request in detail. They also need to decrypt HTTPS traffic to see what's inside.

In most cases, Layer 7 load balancers give you more control and options, but Layer 4 might be better if speed and ease of use are the most important things to you.

There are still two crucial questions to answer. The first is how a load balancer knows which servers to distribute the traffic to. The second is how it decides which server gets each request.
