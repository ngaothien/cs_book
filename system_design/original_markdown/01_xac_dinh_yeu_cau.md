Title: Requirements

URL Source: https://newsletter.francofernando.com/p/requirements-the-foundation-of-good

Published Time: 2025-08-15T08:40:28+00:00

Markdown Content:
Hi Friends,

Welcome to the 135th issue of the Polymathic Engineer.

Imagine you're in a system design interview, and the interviewer asks you to "design a messaging system." The first thing that might come to your mind is brainstorming a technical solution: Should I use Kafka? Load balancers may help? How many servers do I need?

However, if you start with the technical stuff, you miss the most critical part of the design process. Even the best technical answer can't help you if you don't make your requirements clear.

This week, we will discuss which kind of requirements you need to consider, and how they can impact your design choices. The outline is as follows:

*   Why Requirements Matter

*   Functional Requirements: What the System Does

*   Non-Functional Requirements: How the System Behaves

*   Availability and Reliability

*   Scalability and Performance

*   Durability and Consistency

*   Maintainability

*   Security

*   Cost Optimization

Project-based learning is the best way to develop technical skills. [CodeCrafters](https://app.codecrafters.io/join?via=FrancoFernando)is an excellent platform for practicing exciting projects, such as building your version of Redis, Kafka, [DNS server](https://app.codecrafters.io/join/dns-server?via=francofernando), SQLite, or Git from scratch.

[Sign up, and become a better software engineer](https://app.codecrafters.io/join?via=FrancoFernando).

There is a reason why interviewers often use purposely vague language when talking about problems. If they say something like "build a messaging platform," or "design a YouTube-like system" they're not being lazy. They want to learn more about how you think.

They want to see how you deal with ambiguity, if you can figure out what a complex system is made of, how you break down problems into doable parts, and if you can ask the right questions.

Even in real-world software development, requirements aren't always laid out in front of you. Product managers set broad goals, stakeholders have different interests, and users often have trouble describing exactly what they need. Learning how to deal with ambiguity is an essential skill for engineers.

The cool thing is that once you have precise requirements, they will help you make all of your critical decisions. Let's use the messaging system again as an example, and say you've agreed on the following non-functional requirements:

*   **Scalable**: Handle millions of messages per day

*   **Highly available**: 99.9% uptime

*   **Fast**: Low-latency message delivery

These four words may not seem like much, but they can help you a lot.

To be _scalable_, you need to be able to handle a lot of writes and reads. For writes, you need to partition messages across multiple queues without having a single bottleneck. When choosing a partitioning method, you should think about how the messages need to be ordered.

_High availability_ means you need replication. Should I use leader-based or leaderless replication? Leader-based is safer, but you need to figure out how to pick a leader. If you want _fast delivery_, you might think about things like batching and compression.

Each requirement leads to specific architectural patterns and technology choices. Without these requirements, you would be making choices at random and have no way to explain them.

Before thinking about the design of any system, you have to answer two fundamental questions: "_What should this system do?_" and "_How well should it do it?_" These questions map directly to the two types of requirements every engineer needs to understand.

Functional requirements are the behaviors and features that your system must have. They describe the main functionalities, like what users can do and what can expect to happen in reaction.

You can think of functional requirements as the job description for the system. For a messaging system, they could look like these:

*   Users can send messages to other users

*   Messages are delivered to the correct recipients

*   Users can create group conversations

*   The system stores message history

*   Users receive notifications for new messages

It's usually easy to figure out these requirements, especially for systems we use every day. When someone asks you to design "a system like X," you can quickly name the main features like search for material, post tweets, and follow other users.

But this is where it starts to get tricky. The interviewer might only tell you the first part, which is "Design a system that works like X." You need to start with the users and work backwards to figure out what the system needs to do.

![Image 1](https://substackcdn.com/image/fetch/$s_!SpuB!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F418c3c87-99d0-40ab-a5c1-437f6d5d61de_1170x278.png)

This is where Amazon's method of [working backwards](https://aws.amazon.com/blogs/smb/working-backwards-to-drive-customer-experience-and-smb-innovation-forward) really helps. You need to know who will use your system and how they'll use it before you get into the hard stuff.

Before everything else, you should ask yourself who are the customers. These could be end users, other tools, or even teams inside the company. For a YouTube-like system, you have two main types of customers: people who make videos and those who watch them. For a rate-limiting system, the customers are services that need protection from overload.

Once you know the customers, find out the main steps that they take. Viewers need to search, watch, and interact with videos. Content creators need to upload, manage, and analyze their content. Each of these workflows represents a possible set of functional requirements.

The interviewer is your product owner here. They will help you narrow down which functionalities matter most. Don't try to design all of YouTube in 45 minutes. Instead, focus on the most important parts that the interviewer wants.

Sometimes interviewers will ask you to take your functional requirements one step further and express them as APIs. Now is the time to use what you know about REST and RPC standards. For example, if your functional requirements are that users can send messages, retrieve their message history, and create group conversations, your REST API might look like:

```
POST /messages
GET /users/{id}/messages
POST /conversations
```

Non-functional requirements define the qualities and constraints of a system. They don't describe what the system does, but how well it does it.

Using our messaging system as an example again, some examples of non-functional needs could be: :

*   The system should handle 1 million messages per day (scalability)

*   Message delivery should happen within 100 milliseconds (performance)

*   The system should be available 99.9% of the time (availability)

*   Messages should never be lost once sent (durability)

Here is the challenging part. Non-functional requirements are often unstated in interviews. They might not be brought up at all, so it's up to you to decide what's important.

However, if you proactively find and explain non-functional requirements, you show that you know the difference between building a system that works and building a system that works well in production.

Non-functional requirements become your guide whenever you have to make design choices. Should you use a single database or multiple databases? Should you prioritize consistency or availability? Should you optimize for reads or writes? If you don’t have clear non-functional requirements, these choices are arbitrary. With them, it's much easier to see how to move forward.
