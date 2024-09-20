# ai-makers-space-midterm
## 📑 Live Session Resources, recorded Tuesday, Sep 17

[Midterm Certification Challenge](https://docs.google.com/forms/d/e/1FAIpQLSc1R1Y3H2IEwPAmd8nwqIsBpftkEjOVE_mRie9wKMXC2k3CJw/viewform?usp=sf_link)

[AIE4_Session11_Midterm](https://www.canva.com/design/DAGRC5C0bTg/l-htzEUvfL39QaOBm3bVDQ/edit?utm_content=DAGRC5C0bTg&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

[Video Conferencing, Web Conferencing, Webinars, Screen Sharing](https://us02web.zoom.us/rec/share/Z3Y7q63TxZ6gm1iGt5dnvAFSbCYYjYi3XH0pdK-H8IwliplCtQbvGHh5sNevTM9M.hhw2dEA8kC1l5iQ4)

Passcode: @!u?qD1!

[Feedback: AIE4 Cohort](https://docs.google.com/forms/d/e/1FAIpQLSeG6R0y5IufyNbvG8NMTBKKcqtSdQ9vie2rJqIGhgoyEn8nAQ/viewform?usp=sf_link)

# Overview

Welcome to the middle of the course!  We’ve made it 5 weeks so far and covered a lot of ground!  Let’s recall where we’ve been! 

- Week 1: Prompt Engineering & Retrieval Augmented Generation
- Week 2: End-to-End RAG Applications
- Week 3: Agents
- Week 4: Synthetic Data Generation & Evaluation
- Week 5: Fine-Tuning LLMs and Embedding Models

Now, **it’s time to put your skills to the tes**t.  Do you understand the concepts and code we need to build, ship, and share production LLM applications?  

During this session, we’ll assign your Midterm, which you must complete to receive a certification 🎖️.

# Introduction

Last week, we heard from [Phil Mui](https://www.linkedin.com/in/philmui/) of SalesForce about what they’re building out with their new [AgentForce](https://www.salesforce.com/agentforce/) initiative.  This week, at [DreamForce](https://www.salesforce.com/dreamforce), they’re making a big stir!

[Phil Mui CLIP 2.mp4](https://prod-files-secure.s3.us-west-2.amazonaws.com/d7a211dd-f900-47ac-8e0e-f6b027cb71b3/221519b1-f696-4220-9374-91465c0771e0/Phil_Mui_CLIP_2.mp4)

We heard about specific job titles that Phil is working on.  This is similar to the landscape across the industry: people are feeling out what’s needed most at the edge.

- AI System Engineers
- Infrastructure: Infra / AI Ops Engineers
- AI Eng Manager/Director
- Frontend Architect
- Evaluation & Performance Engineers
- AI Solution Engineers

With this rapidly evolving edge of the field in mind, let’s create a story - a real potential scenario you might face in the industry today - and put **you** in the driver’s seat.

## Background and Context

The CEO and corporate, with permission of the board, have assembled a crack data science and engineering team to take advantage of RAG, agents, and all of the latest open-source technologies emerging in the industry.  This time it's for real though.  This time, the company is aiming squarely at some Return On Investment - some ROI - on its research and development dollars.

## The Problem

**You are an AI Solutions Engineer**.  You've worked directly with internal stakeholders to identify a problem: `people are concerned about the implications of AI, and no one seems to understand the right way to think about building ethical and useful AI applications for enterprises.` 

This is a big problem and one that is rapidly changing.  Several people you interviewed said that *they could benefit from a chatbot that helped them understand how the AI industry is evolving, especially as it relates to politics.*  Many are interested due to the current election cycle, but others feel that some of the best guidance is likely to come from the government.

## Task 1: Dealing with the Data

You identify the following important documents that, if used for context, you believe will help people understand what’s happening now:

1. 2022: [Blueprint for an AI Bill of Rights: Making Automated Systems Work for the American People](https://www.whitehouse.gov/wp-content/uploads/2022/10/Blueprint-for-an-AI-Bill-of-Rights.pdf) (PDF)
2. 2024: [National Institute of Standards and Technology (NIST) Artificial Intelligent Risk Management Framework](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) (PDF)

Your boss, the SVP of Technology, green-lighted this project to drive the adoption of AI throughout the enterprise.  It will be a nice showpiece for the upcoming conference and the big AI initiative announcement the CEO is planning.

<aside>
📝

Task 1: Review the two PDFs and decide how best to chunk up the data with a single strategy to optimally answer the variety of questions you expect to receive from people.

*Hint: Create a list of potential questions that people are likely to ask!*

</aside>

✅ Deliverables:

1. Describe the default chunking strategy that you will use.
2. Articulate a chunking strategy that you would also like to test out.
3. Describe how and why you made these decisions

## Task 2: Building a Quick End-to-End Prototype

**You are an AI Systems Engineer**.  The SVP of Technology has tasked you with spinning up a quick RAG prototype for answering questions that internal stakeholders have about AI, using the data provided in Task 1.

<aside>
📝

Task 2: Build an end-to-end RAG application using an industry-standard open-source stack and your choice of commercial off-the-shelf models

</aside>

✅ Deliverables:

1. Build a prototype and deploy to a Hugging Face Space, and ~~include the public URL link to your space~~  create a short (< 2 min) loom video demonstrating some initial testing inputs and outputs.
2. How did you choose your stack, and why did you select each tool the way you did?

## Task 3: Creating a Golden Test Data Set

**You are an AI Evaluation & Performance Engineer.**  The AI Systems Engineer who built the initial RAG system has asked for your help and expertise in creating a "Golden Data Set."

<aside>
📝

Task 3: Generate a synthetic test data set and baseline an initial evaluation

</aside>

✅ Deliverables:

1. Assess your pipeline using the RAGAS framework including key metrics faithfulness, answer relevancy, context precision, and context recall.  Provide a table of your output results.
2. What conclusions can you draw about performance and effectiveness of your pipeline with this information?

## Task 4: Fine-Tuning Open-Source Embeddings

**You are an Machine Learning Engineer.**  The AI Evaluation and Performance Engineer has asked for your help in fine-tuning the embedding model used in their recent RAG application build.

<aside>
📝

Task 4: Generate synthetic fine-tuning data and complete fine-tuning of the open-source embedding model

</aside>

✅ Deliverables

1. Swap out your existing embedding model for the new fine-tuned version.  Provide a link to your fine-tuned embedding model on the Hugging Face Hub.
2. How did you choose the embedding model for this application?

## Task 5: Assessing Performance

**You are the AI Evaluation & Performance Engineer**.  It's time to assess all options for this product.

<aside>
📝

Task 5: Assess the performance of 1) the fine-tuned model, and 2) the two proposed chunking strategies

</aside>

✅ Deliverables

1. Test the fine-tuned embedding model using the RAGAS frameworks to quantify any improvements.  Provide results in a table.
2. Test the two chunking strategies using the RAGAS frameworks to quantify any improvements. Provide results in a table. 
3. The AI Solutions Engineer asks you “Which one is the best to test with internal stakeholders next week, and why?”

## Task 6: Managing Your Boss and User Expectations

**You are the SVP of Technology**.  Given the work done by your team so far, you're now sitting down with the AI Solutions Engineer.  You have tasked the solutions engineer to test out the new application with at least 50 different internal stakeholders over the next month.

1. What is the story that you will give to the CEO to tell the whole company at the launch next month?
2. There appears to be important information not included in our build, for instance, the [270-day update](https://www.whitehouse.gov/briefing-room/statements-releases/2024/07/26/fact-sheet-biden-harris-administration-announces-new-ai-actions-and-receives-additional-major-voluntary-commitment-on-ai/) on the 2023 executive order on [Safe, Secure, and Trustworthy AI](https://www.whitehouse.gov/briefing-room/presidential-actions/2023/10/30/executive-order-on-the-safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence/).  How might you incorporate relevant white-house briefing information into future versions? 

## Your Final Submission

Please include the following in your final submission:

1. A public link to a **written report** addressing each deliverable and answering each question.
2. A public link to any relevant **GitHub repo**
3. A public link to the **final version of your application** on Hugging Face
4. A public link to your **fine-tuned embedding model** on Hugging Face