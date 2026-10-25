Title: Availability

URL Source: https://newsletter.francofernando.com/p/availability

Published Time: 2024-04-06T07:00:42+00:00

Markdown Content:
[![Image 1](https://substackcdn.com/image/fetch/$s_!c3Ff!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb9675ec1-4687-4ad6-a317-e5aabd896225_800x400.jpeg)](https://substackcdn.com/image/fetch/$s_!c3Ff!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb9675ec1-4687-4ad6-a317-e5aabd896225_800x400.jpeg)

Hi Friends,

Welcome to the 66th issue of the Polymathic Engineer newsletter. This week we discuss a critical parameter for every software system: availability.

The outline will be as follows:

*   What does availability mean?

*   What is high availability

*   Design principles

*   Processes

*   KPIs

Availability measures how resistant a system is to failures and remains functional over a specific period. The more a system stays operational when a component fails, the higher its availability.

Availability is critical for many digital applications from e-commerce and payments to delivery, finance, and more. In the Internet age, even a downtime of one hour can costs from $1K to $1M, affect the system credibility, and decrease the customer trust.

For example, think about what could happen if an e-commerce platform had a minute of downtime during a promotional flash sale event. The reputation damage would be terrific.

The importance of availability increased the need for systems or services that are functional for as close to 100% of the time as possible.

There are several ways how availability can be defined. The most common one is the the percentage of time a system has been working and functional. According to this definition, claiming that a system is 99% available means that the system downtime was 3.65 days per year.

[![Image 2](https://substackcdn.com/image/fetch/$s_!yayW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7abb5ab7-cce0-4021-9ced-8ef541cba8ef_1284x1164.png)](https://substackcdn.com/image/fetch/$s_!yayW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7abb5ab7-cce0-4021-9ced-8ef541cba8ef_1284x1164.png)

But the uptime is not the only possible measurement. Every service may have a different measure of availability. For example, you might define availability as the percentage of successfully responses to requests within 100 milliseconds.

According to this definition, claiming that a system is 99% available means that 1 request over 100 doesn’t get any answer within 100 milliseconds. The interesting thing is that the request may fail for different reasons: it may be a bug on the server causing a delayed answer or a network outage so the request has never reached the system.

In theory, availability could be measured from different points of views in case of network failures. From the clients perspective, availability drops, but from the servers perspective availability could be high since the system was always up and running.

However what matters is the availability of the system as a whole, including both clients and servers perspectives.

As we saw, availability is often measured in terms of “nines”. But at which percentage a system can be considered as high available? Is 90% enough? Do we need 99% or even more?

Actually there is no a one size fits all answer. Ideally, we would like to have systems that are 100% available. However, this not only would cost a lot of money, but it would be impossible in practice.
