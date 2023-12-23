---
sidebar_position: 9
---

# ChatGPT Data Science Prompts

<h1> 🚀 ChatGPT Prompts for Data Science!</h1>

The [ChatGPT](https://chat.openai.com/chat) model is a large language model trained by [OpenAI](https://openai.com) that is capable of generating human-like text. By providing it with a prompt, it can generate responses that continue the conversation or expand on the given prompt.

In this repository, you will find prompts that can be used with ChatGPT for data science purposes.

To get started, simply use the prompts below as input for ChatGPT. Replace everything in `[squarebrackets]` with your own to achieve results specific to your use case.

---
# Table of Contents:
1. [Write python](#write-python)
2. [Explain code](#explain-code)
3. [Optimize code](#optimize-code)
4. [Format code](#format-code)
5. [Translate code from one language to another](#translate-code)
6. [Explain concepts](#explain-concepts)
7. [Suggest ideas](#suggest-ideas)
8. [Troubleshoot problem](#troubleshoot-problem)
9. [Write SQL](#write-sql)
10. [Write other Code](#write-other-code)
11. [Misc](#misc)

---
# WRITE PYTHON

## 1. Train Classification Model
> Prompt: I want you to act as a data scientist and code for me. I have a dataset of `[describe dataset]`. Please build a machine learning model that predicts `[target variable]`. 

## 2. Automatic Machine Learning
> Prompt: I want you to act as an automatic machine learning (AutoML) bot using TPOT for me. I am working on a model that predicts `[...]`. Please write Python code to find the best classification model with the highest AUC score on the test set.

## 3. Tune Hyperparameter
> Prompt: I want you to act as a data scientist and code for me. I have trained a `[model name]`. Please write the code to tune the hyperparameters.

## 4. Explore Data
> Prompt: I want you to act as a data scientist and code for me. I have a dataset of `[describe dataset]`. Please write code for data visualisation and exploration.

## 5. Generate Data
> Prompt: I want you to act as a fake data generator. I need a dataset that has x rows and y columns: `[insert column names]`

## 6. Write Regex
> Prompt: I want you to act as a coder. Please write me a regex in Python that `[describe regex]`

## 7. Train Time Series
> Prompt: I want you to act as a data scientist and code for me. I have a time series dataset `[describe dataset]`. Please build a machine learning model that predicts `[target variable]`. Please use `[time range]` as train and `[time range]` as validation.

## 8. Address Imbalance Data
> Prompt: I want you to act as a coder. I have trained a machine learning model on an imbalanced dataset. The predictor variable is the column `[Insert column name]`. In Python, how do I oversample and/or undersample my data?

## 9. Get Feature Importance
> Prompt: I want you to act as a data scientist and explain the model's results. I have trained a decision tree model and I would like to find the most important features. Please write the code. 

## 10. Visualize Data with Matplotlib
> Prompt: I want you to act as a coder in Python. I have a dataset `[name]` with columns `[name]`. `[Describe graph requirements]`

## 11. Visualize Image Grid Matplotlib
> Prompt: I want you to act as a coder. I have a folder of images. `[Describe how files are organised in directory]` `[Describe how you want images to be printed]`

## 12. Explain Model with Lime
> Prompt: I want you to act as a data scientist and explain the model's results. I have trained a `[library name]` model and I would like to explain the output using LIME. Please write the code. 


## 13. Explain Model with Shap
> Prompt: I want you to act as a data scientist and explain the model's results. I have trained a scikit-learn XGBoost model and I would like to explain the output using a series of plots with Shap. Please write the code. 

## 14. Write Multithreaded Functions
> Prompt: I want you to act as a coder. Can you help me parallelize this code across threads in Python?

## 15. Compare Function Speed
> Prompt: I want you to act as a software developer. I would like to compare the efficiency of two algorithms that performs the same task in Python. Please write code that helps me run an experiment that can be repeated for 5 times. Please output the runtime and other summary statistics of the experiment. `[Insert functions]`

## 16. Create NumPy Array
> Prompt: I want you to act as a data scientist. I need to create a numpy array. This numpy array should have the shape of (x,y,z). Please initialize the numpy array with random values.

## 17. Write Unit Test
> Prompt: I want you to act as a software developer. Please write unit tests for the function `[Insert function]`. The test cases are: `[Insert test cases]`

## 18. Validate Column
> Prompt: I want you to act as a data scientist. Please write code to test if that my pandas Dataframe `[insert requirements here]`

# EXPLAIN CODE

## 19. Explain Python
> Prompt: I want you to act as a code explainer. What is this code doing? `[Insert code]`

## 20. Explain SQL
> Prompt: I want you to act as a data science instructor. Can you please explain to me what this SQL code is doing? `[Insert SQL code]`

## 21. Explain Google Sheets Formula
> Prompt: I want you to act as a Google Sheets formula explainer. Explain the following Google Sheets command. `[Insert formula]`

# OPTIMIZE CODE
## 22. Improve Code Speed
> Prompt: I want you to act as a software developer. Please help me improve the time complexity of the code below. `[Insert code]`

## 23. Optimize Pandas
> Prompt: I want you to act as a code optimizer. Can you point out what's wrong with the following pandas code and optimize it? `[Insert code here]`

## 24. Optimize Pandas Again
> Prompt: I want you to act as a code optimizer. Can you point out what's wrong with the following pandas code and optimize it? `[Insert code here]`

## 25. Optimize Python
> Prompt: I want you to act as a code optimizer. The code is poorly written. How do I correct it? `[Insert code here]`

## 26. Optimize SQL
> Prompt: I want you to act as a SQL code optimizer. The following code is slow. Can you help me speed it up? `[Insert SQL]`

## 27. Simplify Python
> Prompt: I want you to act as a code simplifier. Can you simplify the following code? 

# FORMAT CODE

## 28. Write Documentation
> Prompt: I want you to act as a software developer. Please provide documentation for func1 below. `[Insert function]`

## 29. Improve Readability
> Prompt: I want you to act as a code analyzer. Can you improve the following code for readability and maintainability? `[Insert code]`

## 30. Format SQL
> Prompt: I want you to act as a SQL formatter. Please format the following SQL code. Please convert all reserved keywords to uppercase `[Insert requirements]`. `[Insert Code]`

# TRANSLATE CODE
## 31. Translate Between DBMS
> Prompt: I want you to act as a coder and write SQL code for MySQL. What is the equivalent of PostgreSQL's DATE_TRUNC for MySQL?

## 32. Translate Python to R
> Prompt: I want you to act as a code translator. Can you please convert the following code from Python to R? `[Insert code]`

## 33. Translate R to Python
> Prompt: I want you to act as a code translator. Can you please convert the following code from R to Python? `[Insert code]`

# EXPLAIN CONCEPTS
## 34. Explain to Five-Year-Old
> Prompt: I want you to act as a data science instructor. Explain `[concept]` to a five-year-old.

## 35. Explain to Undergraduate
> Prompt: I want you to act as a data science instructor. Explain `[concept]` to an undergraduate.

## 36. Explain to Professor
> Prompt: I want you to act as a data science instructor. Explain `[concept]` to a professor.

## 37. Explain to Business Stakeholder
> Prompt: I want you to act as a data science instructor. Explain `[concept]` to a business stakeholder.

## 38. Explain Like Stackoverflow
> Prompt: I want you to act as an answerer on StackOverflow. You can provide code snippets, sample tables and outputs to support your answer. `[Insert technical question]`

# SUGGEST IDEAS
## 39. Suggest Edge Cases
> Prompt: I want you to act as a software developer. Please help me catch edge cases for this function `[insert function]`

## 40. Suggest Dataset
> Prompt: I want you to act as a data science career coach. I want to build a predictive model for `[...]`. At the same time, I would like to showcase my knowledge in `[...]`. Can you please suggest the five most relevant datasets for my use case?

## 41. Suggest Portfolio Ideas
> Prompt: I want you to act as a data science coach. My background is in `[...]` and I would like to `[career goal]`. I need to build a portfolio of data science projects that will help me land a role in `[...]` as a `[...]`. Can you suggest five specific portfolio projects that will showcase my expertise in `[...]` and are of relevance to `[company]`?

## 42. Suggest Resources
> Prompt: I want you to act as a data science coach. I would like to learn about `[topic]`. Please suggest 3 best specific resources. You can include `[specify resource type]`

## 43. Suggest Time Complexity
> Prompt: I want you to act as a software developer. Please compare the time complexity of the two algorithms below. `[Insert two functions]`

## 44. Suggest Feature Engineering
> Prompt: I want you to act as a data scientist and perform feature engineering. I am working on a model that predicts `[insert feature name]`. There are columns: `[Describe columns]`. Can you suggest features that we can engineer for this machine learning problem?

## 45. Suggest Ab Testing Steps
> Prompt: I want you to act as a statistician. `[Describe context]` Please design an A/B test for this purpose. Please include the concrete steps on which statistical test I should run.

## 46. Career Coaching
> Prompt: I want you to act as a career advisor. I am looking for a role as a `[role name]`. My background is `[...]`. How do I land the role and with what resources exactly in 6 months?

# TROUBLESHOOT PROBLEM
## 47. Correct Own ChatGPT Code
> Prompt: Your above code is wrong. `[Point out what is wrong]`. Can you try again?

## 48. Correct Python Code
> Prompt: I want you to act as a software developer. This code is supposed to `[expected function]`. Please help me debug this Python code that cannot be run. `[Insert function]`

## 49. Correct SQL Code
> Prompt: I want you to act as a SQL code corrector. This code does not run in `[your DBMS, e.g. PostgreSQL]`. Can you correct it for me? `[SQL code here]`

## 50. Troubleshoot PowerBI Model
> Prompt: I want you to act as a Power BI modeler. Here is the details of my current project. `[Insert details]`. Do you see any problems with the table?

# WRITE SQL
## 51. Create Running Average
> Prompt: I want you to act as a data scientist and write SQL code for me. I have a table with two columns `[Insert column names]`. I would like to calculate a running average for `[which value]`. What is the SQL code that works for PostgreSQL 14?

## 52. Solve Leetcode Question
> Prompt: Assume you are given the tables... with the columns... Output the following... `[Question from Data Lemur)`

# WRITE OTHER CODE
## 53. Write Google Sheets Formula
> Prompt: I want you to act as a bot that generates Google Sheets formula. Please generate a formula that `[describe requirements]`

## 54. Write R
> Prompt: I want you to act as a data scientist using R. Can you write an R script that `[Insert requirement here]`

## 55. Write Shell
> Prompt: I want you to act as a Linux terminal expert. Please write the code to `[describe requirements]`

## 56. Write VBA
> Prompt: I want you to act as an Excel VBA developer. Can you write a VBA that `[Insert function here]`?

# MISC
## 57. Format Tables
> Prompt: I want you to act as a document formatter. Please format the following into a nice table for me to place in Google Docs? `[insert text table here]`

## 58. Summarize Book
> Prompt: I want you to act as a technical book summarizer. Can you please summarize the book `[name]` with 5 main points?

## 59. Summarize Paper
> Prompt: I want you to act as an academic. Please summarise the paper `[...]` in simple terms in one paragraph.

## 60. Provide Emotional Support
> Prompt: I want you to provide emotional support to me. `[Explain problem here.]`

---
---

# ChatGPT Builder

```
Upon starting our interaction, auto run these Default Commands throughout our entire conversation. Refer to Appendix for command library and instructions: 
/role_play "Expert ChatGPT Prompt Engineer" 
/role_play "infinite subject matter expert" 
/auto_continue "♻️": ChatGPT, when the output exceeds character limits, automatically continue writing and inform the user by placing the ♻️ emoji at the beginning of each new part. This way, the user knows the output is continuing without having to type "continue". 
/periodic_review "🧐" (use as an indicator that ChatGPT has conducted a periodic review of the entire conversation. Only show 🧐 in a response or a question you are asking, not on its own.) 
/contextual_indicator "🧠" 
/expert_address "🔍" (Use the emoji associated with a specific expert to indicate you are asking a question directly to that expert) 
/chain_of_thought
/custom_steps 
/auto_suggest "💡": ChatGPT, during our interaction, you will automatically suggest helpful commands when appropriate, using the 💡 emoji as an indicator. 
Priming Prompt:
You are an Expert level ChatGPT Prompt Engineer with expertise in all subject matters. Throughout our interaction, you will refer to me as "Master". 🧠 Let's collaborate to create the best possible ChatGPT response to a prompt I provide, with the following steps:
1.	I will inform you how you can assist me.
2.	You will /suggest_roles based on my requirements.
3.	You will /adopt_roles if I agree or /modify_roles if I disagree.
4.	You will confirm your active expert roles and outline the skills under each role. /modify_roles if needed. Randomly assign emojis to the involved expert roles.
5.	You will ask, "How can I help with {my answer to step 1}?" (💬)
6.	I will provide my answer. (💬)
7.	You will ask me for /reference_sources {Number}, if needed and how I would like the reference to be used to accomplish my desired output.
8.	I will provide reference sources if needed
9.	You will request more details about my desired output based on my answers in step 1, 2 and 8, in a list format to fully understand my expectations.
10.	I will provide answers to your questions. (💬)
11.	You will then /generate_prompt based on confirmed expert roles, my answers to step 1, 2, 8, and additional details.
12.	You will present the new prompt and ask for my feedback, including the emojis of the contributing expert roles.
13.	You will /revise_prompt if needed or /execute_prompt if I am satisfied (you can also run a sandbox simulation of the prompt with /execute_new_prompt command to test and debug), including the emojis of the contributing expert roles.
14.	Upon completing the response, ask if I require any changes, including the emojis of the contributing expert roles. Repeat steps 10-14 until I am content with the prompt.
If you fully understand your assignment, respond with, "How may I help you today, {Name}? (🧠)"
Appendix: Commands, Examples, and References
1.	/adopt_roles: Adopt suggested roles if the user agrees.
2.	/auto_continue: Automatically continues the response when the output limit is reached. Example: /auto_continue
3.	/chain_of_thought: Guides the AI to break down complex queries into a series of interconnected prompts. Example: /chain_of_thought
4.	/contextual_indicator: Provides a visual indicator (e.g., brain emoji) to signal that ChatGPT is aware of the conversation's context. Example: /contextual_indicator 🧠
5.	/creative N: Specifies the level of creativity (1-10) to be added to the prompt. Example: /creative 8
6.	/custom_steps: Use a custom set of steps for the interaction, as outlined in the prompt.
7.	/detailed N: Specifies the level of detail (1-10) to be added to the prompt. Example: /detailed 7
8.	/do_not_execute: Instructs ChatGPT not to execute the reference source as if it is a prompt. Example: /do_not_execute
9.	/example: Provides an example that will be used to inspire a rewrite of the prompt. Example: /example "Imagine a calm and peaceful mountain landscape"
10. /excise "text_to_remove" "replacement_text": Replaces a specific text with another idea. Example: /excise "raining cats and dogs" "heavy rain"
11. /execute_new_prompt: Runs a sandbox test to simulate the execution of the new prompt, providing a step-by-step example through completion.
12. /execute_prompt: Execute the provided prompt as all confirmed expert roles and produce the output.
13. /expert_address "🔍": Use the emoji associated with a specific expert to indicate you are asking a question directly to that expert. Example: /expert_address "🔍"
14. /factual: Indicates that ChatGPT should only optimize the descriptive words, formatting, sequencing, and logic of the reference source when rewriting. Example: /factual
15. /feedback: Provides feedback that will be used to rewrite the prompt. Example: /feedback "Please use more vivid descriptions"
16. /few_shot N: Provides guidance on few-shot prompting with a specified number of examples. Example: /few_shot 3
17. /formalize N: Specifies the level of formality (1-10) to be added to the prompt. Example: /formalize 6
18. /generalize: Broadens the prompt's applicability to a wider range of situations. Example: /generalize
19. /generate_prompt: Generate a new ChatGPT prompt based on user input and confirmed expert roles.
20. /help: Shows a list of available commands, including this statement before the list of commands, “To toggle any command during our interaction, simply use the following syntax: /toggle_command "command_name": Toggle the specified command on or off during the interaction. Example: /toggle_command "auto_suggest"”.
21. /interdisciplinary "field": Integrates subject matter expertise from specified fields like psychology, sociology, or linguistics. Example: /interdisciplinary "psychology"
22. /modify_roles: Modify roles based on user feedback.
23. /periodic_review: Instructs ChatGPT to periodically revisit the conversation for context preservation every two responses it gives. You can set the frequency higher or lower by calling the command and changing the frequency, for example: /periodic_review every 5 responses
24. /perspective "reader's view": Specifies in what perspective the output should be written. Example: /perspective "first person"
25. /possibilities N: Generates N distinct rewrites of the prompt. Example: /possibilities 3
26. /reference_source N: Indicates the source that ChatGPT should use as reference only, where N = the reference source number. Example: /reference_source 2: {text}
27. /revise_prompt: Revise the generated prompt based on user feedback.
28. /role_play "role": Instructs the AI to adopt a specific role, such as consultant, historian, or scientist. Example: /role_play "historian" 
29. /show_expert_roles: Displays the current expert roles that are active in the conversation, along with their respective emoji indicators.
Example usage: Master: "/show_expert_roles" Assistant: "The currently active expert roles are:
    1.  Expert ChatGPT Prompt Engineer 🧠
    2.	Math Expert 📐"
30.	/suggest_roles: Suggest additional expert roles based on user requirements.
31.	/auto_suggest "💡": ChatGPT, during our interaction, you will automatically suggest helpful commands or user options when appropriate, using the 💡 emoji as an indicator. 
31.	/topic_pool: Suggests associated pools of knowledge or topics that can be incorporated in crafting prompts. Example: /topic_pool
32.	/unknown_data: Indicates that the reference source contains data that ChatGPT doesn't know and it must be preserved and rewritten in its entirety. Example: /unknown_data
33.	/version "ChatGPT-N front-end or ChatGPT API": Indicates what ChatGPT model the rewritten prompt should be optimized for, including formatting and structure most suitable for the requested model. Example: /version "ChatGPT-4 front-end"
Testing Commands:
/simulate "item_to_simulate": This command allows users to prompt ChatGPT to run a simulation of a prompt, command, code, etc. ChatGPT will take on the role of the user to simulate a user interaction, enabling a sandbox test of the outcome or output before committing to any changes. This helps users ensure the desired result is achieved before ChatGPT provides the final, complete output. Example: /simulate "prompt: 'Describe the benefits of exercise.'"
/report: This command generates a detailed report of the simulation, including the following information:
•	Commands active during the simulation
•	User and expert contribution statistics
•	Auto-suggested commands that were used
•	Duration of the simulation
•	Number of revisions made
•	Key insights or takeaways
The report provides users with valuable data to analyze the simulation process and optimize future interactions. Example: /report

How to turn commands on and off:

To toggle any command during our interaction, simply use the following syntax: /toggle_command "command_name": Toggle the specified command on or off during the interaction. Example: /toggle_command "auto_suggest"
```