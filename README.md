# STA2453: Data Science Methods, Collaborations, and Communication (Fall 2026)

## Overview

Welcome to STA2453 for Fall 2026. In general the aim of the class is to provide you with applied data science skills that you can use in industry.

The 12-week semester is broken into three parts, each of four weeks. 
So the normal cadence of class is three weeks of learning and then in the fourth week you will submit an assignment on the Monday, and complete an in-class exam on the Wednesday.

- Part 1 (Weeks 1-4): Foundations: *You will set up a reproducible workflow and use it to write a short paper from real data. We will use this motivation to learn to use uv, Python, Git and GitHub, GitHub Actions, and Quarto, to make graphs and tables, and to write clearly.*
- Part 2 (Weeks 5-8): Forecasting: *You will make and communicate a probabilistic forecast of a real election, using some combination of published polls and silicon samples (although you are not evaluated on the accuracy of the forecast itself). We will use this motivation to learn to use REST and LLM APIs, statistical sampling, and poststratification, as well as how to build a website to communicate a result.*
- Part 3 (Weeks 9-12): AI evaluation: *You will evaluate an AI model. You will learn what a benchmark is, why many are less extensive than they look, how to write evaluation items and rubrics, come to understand the headache that is using a model as a grader, and also how to use a variety of different models.*

## Assessment

| Component | Weight |
|:---|---:|
| Part 1: Donaldson assignment and in-class exam I | 30 |
| Part 2: Election assignment and in-class exam II | 30 |
| Part 3: Eval assignment and in-class exam III | 30 |
| ISLR/P in-class presentation | 10 |
| (Optional) Final exam | You can use your score in this to replace your score in one Part |

### Notes

- Your mark for each Part is the average of your assignment mark and your exam mark. For instance, if for Part 1 you got 95% on the assignment and 50% on the exam then you would get 72.5%, which is 21.75/30.
- One section of the in-class exam is about your assignment. You should expect a mix of MCQ, short answer, and essay questions.
- The final exam is optional but can be used to replace one Part. If your final exam mark is higher than your lowest Part mark, it takes that Part's 30 per cent. Otherwise it does not count. Think of it as a back-up in case something happens during the semester.
- Due dates:
    - Part 1: Assignments are due Monday 28 September and the in-class exam is Wednesday 30 September.
    - Part 2: Toronto teams assignments are due Sunday 25 October, US teams assignments are due Monday 2 November, and the in-class exam is Wednesday 4 November.
    - Part 3: Assignments are due Monday 30 November and the in-class exam is Wednesday 2 December.
    - ISLR/P: Make a PR to the class repo (https://github.com/RohanAlexander/sta2453) by EOD Monday before class in the week you pick (Week 3, 5, 6, 7, 9, 10).
    - Final exam: During exam period.
    - All submissions must be made by the end of the day. Extensions are difficult to accommodate because I need time to personalize the exam.
- Team size:
    - For Assignment I please work individually. 
    - For Assignment II, please work in teams of two or three.
    - For Assignment III, you are welcome to work individually or in a group of any size.
    - ISLR/P: Please work in a group of two to three, so that we have six groups in total.
- Details:
    - Assignment I is the [Donaldson paper](https://tellingstorieswithdata.com/25-papers.html#sec-paper-one). Please submit a link to your GitHub repo via Quercus.
    - For Assignment II you can pick whether you use synthetic samples to forecast the Toronto municipal election or the US midterms depending on your interest and schedule. In either case, please submit a link to your GitHub repo via Quercus and don't modify the repo after the due date. You should have everything in that one repo, including a website that you deploy using GitHub Pages to communicate your work and forecast. The repo should be completely reproducible, and if there is something you can't include in it, for instance the raw CCES data, then you should explain why and how to get it and where I should put it in the repo (ideally you'd include a sample with the right filenames etc.) in the README. An example of a website built to communicate synthetic samples is [here](https://rohanalexander.github.io/synthetic_voter_project/).
        - The Toronto municipal election is on Monday 26 October, so you need to provide forecasts for the mayor and all 25 wards. There is almost no published polling so much of it will be synthetic, and Open Data Toronto has ward-level census profiles which will be helpful for post-stratification. 
        - The US midterms are Tuesday 3 November, so you need to provide forecasts for all congressional, Senate, and gubernatorial elections. There is plenty of polling available, and you can use the CCES to help with post-stratification.
    - An explicit rubric will be provided closer to the submission date, but broadly, Assignment III requires you to build an AI benchmark and then evaluate some models and put together a website or paper explaining your benchmark and its performance. Partly you will be assessed against Reuel et al. (2024).
    - For the *ISLR/P* presentation please make 20 minutes of content on the assigned topic (Chapter 2.1, Chapter 3.1 and 3.2, Chapter 4.3, Chapter 5.1, Chapter 6.2, Chapter 8.1). You should create slides using Quarto and create a Quarto doc with code that people can work through for 10 minutes after that.


## Schedule

### Part 1: Foundations

#### Week 1 (starts Monday 7 September)

*Python set-up with uv, workflow, version control with Git and GitHub, and GitHub Actions.*

- Readings
    - De Angelis, Inessa, 2026, "Using GitHub Actions for Computational Communication Research", [10.31235/osf.io/uqf6n_v1](https://doi.org/10.31235/osf.io/uqf6n_v1).
    - Bryan, Jennifer, 2018, "Excuse Me, Do You Have a Moment to Talk About Version Control?", *The American Statistician*, [10.1080/00031305.2017.1399928](https://doi.org/10.1080/00031305.2017.1399928).
    - Wilson, Greg, et al., 2017, "Good enough practices in scientific computing", *PLOS Computational Biology*, [10.1371/journal.pcbi.1005510](https://doi.org/10.1371/journal.pcbi.1005510).
- Class (Wednesday 9 September)
    - (Housekeeping) Set up uv, Python, R, RStudio, VS Code, and GitHub.
    - (Demonstration) Set-up and run GitHub Actions daily to gather the shelter data.
    - (Guest) Inessa De Angelis on GitHub Actions.

#### Week 2 (starts Monday 14 September)

*Using Quarto to make papers, slides, and websites; making graphs and tables with R; working in groups; deploying with GitHub Pages; reading and cleaning data with polars; reading and writing Parquet files; version control in groups: PRs, reviews, conflicts.*

- Readings
    - Timbers, Tiffany A., Joel Ostblom, Florencia D'Andrea, Rodolfo Lourenzutti, and Daniel Chen, 2025, *Reproducible and Trustworthy Workflows for Data Science*, (the version control chapters), https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/.
    - Polars User Guide, "Getting started" and "Concepts", https://docs.pola.rs. 
    - The Parquet page of the Apache Arrow Python docs, https://arrow.apache.org/docs/python/parquet.html.
    - Healy, Kieran, 2026, *Data Visualization: A Practical Introduction*, [Chapter 1](https://socviz.co).
    - Alexander, Rohan, 2023, *Telling Stories with Data*, [Chapter 5](https://tellingstorieswithdata.com/05-graphs_tables_maps.html).
- Class (Wednesday 16 September)
    - (Quiz) Week 1 readings and class.
    - (Housekeeping) Form six *ISLR/P* groups and pick dates.
    - (Demonstration) Quarto; polars and Parquet on the shelter data.
    - (Worksheet) Build a website with Quarto and deploy it with GitHub Pages.
    - (Guest) Annie Collins.

#### Week 3 (starts Monday 21 September)

*Writing papers.*

- Readings
    - Alexander, Rohan, 2023, *Telling Stories with Data*, [Chapter 4](https://tellingstorieswithdata.com/04-writing_research.html).
    - King, Stephen, 2000, *On Writing*, pp. 111-137.
    - Zinsser, William, 1976, *On Writing Well*, pp. 6-32 and 169-177.
    - King, Gary, 2006, "Publication, Publication", *PS: Political Science & Politics*, [10.1017/S1049096506060252](https://doi.org/10.1017/S1049096506060252).
    - Mensh, Brett, and Konrad Kording, 2017, "Ten simple rules for structuring papers", *PLOS Computational Biology*, [10.1371/journal.pcbi.1005619](https://doi.org/10.1371/journal.pcbi.1005619).
    - *ISLR/P*, Chapter 2.1 "What is Statistical Learning?"
- Class (Wednesday 23 September)
    - (Quiz) Weeks 1 and 2 readings and class, what the Donaldson paper expects, and *ISLR/P* Chapter 2.1.
    - (ISLR/P) Bolong Tang, Peize Zhang, Yi zhi Zhang.
    - (Lecture) Features of good writing by section: title, abstract, introduction, data, model, results, discussion.
    - (Worksheet) Draft a paper from three sets of results and then edit three drafts.
    - (Worksheet, 30 min) Referee a Donaldson-style paper written entirely by a model: is it any good, and how do you know?
    - Donaldson paper questions.

#### Week 4 (starts Monday 28 September): Assignment I and in-class exam I

- Monday 28 September: Donaldson paper due EOD (https://tellingstorieswithdata.com/25-papers.html#sec-paper-one).
- Wednesday 30 September: Exam I.

### Part 2: Forecasting

#### Week 5 (starts Monday 5 October)

*Silicon sampling; getting set up: an OpenRouter key, open-weight models (DeepSeek V4, GLM-5.3, Muse Glimmer 30B), and OpenCode; calling an LLM API from Python: structured outputs, temperature, batching, caching, cost tracking; persona prompts from census marginals; comparing a silicon sample against a real poll; detecting mode collapse.*

- Readings
    - Argyle, Lisa P., et al, 2023, "Out of One, Many: Using Language Models to Simulate Human Samples", *Political Analysis*, [10.1017/pan.2023.2](https://doi.org/10.1017/pan.2023.2).
    - Bisbee, James, et al, 2024, "Synthetic Replacements for Human Survey Data? The Perils of Large Language Models", *Political Analysis* [10.1017/pan.2024.5](https://doi.org/10.1017/pan.2024.5).
    - Heath, Oscar, and Rohan Alexander, 2026, "Correcting Mode Collapse in Silicon Sampling with Semantic Similarity Rating", https://arxiv.org/abs/2607.28550
    - Murray, Ellie and Rohan Alexander, 2026, "How analyst choices affect silicon samples from the 2025 CES", https://osf.io/preprints/socarxiv/cxrk6_v1
    - *ISLR/P*, Chapter 3.1 and 3.2 "Simple Linear Regression" "Multiple Linear Regression"
- Class (Wednesday 7 October)
    - (ISLR/P) Siyi Zhu, Coco Liu, Jingxuan Feng, Jingwen Zhong.
    - (Demonstration) OpenRouter, open weights, structured outputs, caching and cost, OpenCode.
    - (Lecture) What a silicon sample is, and the two ways it fails: wrong marginal, collapsed spread
    - (Demonstration) 300 personas from census marginals; a mayoral or generic-ballot question with structured output; compare marginal and variance to a published poll
    - (Worksheet) Same question, different model and different prompt: which moved the answer more?
    - (Guest) Oscar Heath.

#### Week 6 (starts Monday 12 October)

*Polls, poststratification, and scoring; getting polls and results from an API or a scraped table; building a poststratification frame from the census; a small regularized or multilevel model on real plus silicon respondents, poststratified; Brier and log scores; communicating uncertainty with quantile dotplots, fan charts.*

- Readings
    - Gelman, Andrew, et al, 2020, "Information, Incentives, and Goals in Election Forecasts", *Judgment and Decision Making*, [10.1017/S1930297500007981](https://doi.org/10.1017/S1930297500007981).
    - Wang, Wei, et al, 2015, "Forecasting Elections with Non-Representative Polls", *International Journal of Forecasting*, [10.1016/j.ijforecast.2014.06.001](https://www.sciencedirect.com/science/article/abs/pii/S0169207014000879).
    - Shirani-Mehr, Houshmand, et al, 2018, "Disentangling Bias and Variance in Election Polls", *Journal of the American Statistical Association*, [10.1080/01621459.2018.1448823](https://doi.org/10.1080/01621459.2018.1448823).
    - Kay, Matthew, et al, 2016, "When (ish) is My Bus? User-centered Visualizations of Uncertainty in Everyday, Mobile Predictive Systems", *CHI 2016*, [10.1145/2858036.2858558](https://doi.org/10.1145/2858036.2858558).
    - *ISLR/P*, Chapter 4.3 "Logistic Regression"
- Class (Wednesday 14 October)
    - (Quiz) Week 5 readings and class, and *ISLR/P* Chapters 3.1 and 3.2.
    - (ISLR/P) Josh Campbell, Graham Sayle, Kyle Dong, and Gerry Peng.
    - (Lecture) What a forecast is a forecast of; bias and variance in polls; why 70 per cent is not "will win"
    - (Demonstration) Pull the polls; build the frame; fit; poststratify; win probability with an interval; score a set of 2022 forecasts against the 2022 results with Brier and log score
    - (Worksheet) Teams commit a first-cut forecast to the class repo by PR, and review each other's assumptions in the PR

#### Week 7 (starts Monday 19 October)

*Docker; data management: file and variable names, codebooks, folder layout, documentation; model interpretation: marginal effects for linear, logistic, and multinomial models.*

- Readings
    - Gold, Alex, 2024, *DevOps for Data Science*, Chapter 6 "Demystifying Docker", https://do4ds.com.
    - Nüst, Daniel, et al., 2020, "Ten Simple Rules for Writing Dockerfiles for Reproducible Data Science", *PLOS Computational Biology*, [10.1371/journal.pcbi.1008316](https://doi.org/10.1371/journal.pcbi.1008316).
    - Lewis, Crystal, 2024, Data Management in Large-Scale Education Research, Chapters 3, 4, 5, and 9, https://datamgmtinedresearch.com.
    - *ISLR/P*, Chapter 5.1 "Cross-Validation"
- Class (Wednesday 21 October)
    - (Quiz) Week 6 readings and class, and *ISLR/P* Chapters 4.3 and 5.1.
    - (ISLR/P) Danika Anoutchina, Maggie Huang, Shrey Sati, Daniel Gutkin.
    - (Demonstration) Put the Week 6 pipeline in a container and run it; marginal effects from the vote model; a data dictionary and folder layout for the project repo
    - (Worksheet) Team time

#### Reading Week (26-30 October): Assignment II

- For the teams forecasting the Toronto municipal election, your assignment is due EOD Sunday 25 October.

#### Week 8 (starts Monday 2 November): Assignment II and in-class exam II

- Monday 2 November: For teams forecasting the US midterms, your assignment is due EOD Monday 2 November.
- Wednesday 4 November: In-class exam II.

### Part 3: Evals

#### Week 9 (starts Monday 9 November)

*What is a benchmark? Building evals: items, ground truth, rubrics, runners; benchmark cards and model cards.*

- Readings
    - Reuel, Anka, Amelia Hardy, Chandler Smith, Max Lamparth, Malcolm Hardy, and Mykel J. Kochenderfer, 2024, "BetterBench: Assessing AI Benchmarks, Uncovering Issues, and Establishing Best Practices", *arXiv*, [10.48550/arXiv.2411.12990](https://arxiv.org/abs/2411.12990).
    - Alexander, Rohan, 2026, "Iterated creation, grading, and revision of data science projects by language models".
    - Garcia Mejia, Mariana and Rohan Alexander, 2026, "If it bleeds, it leads? Evaluating whether LLMs can identify what is newsworthy", https://doi.org/10.31235/osf.io/y6nqj_v1.
    - Cummins-Mburu, Benedict, Mariana Garcia Mejia, Oscar Heath, Sabrina Kreyzerman, Ellie Murray, Arusan Surendiran and Rohan Alexander, 2026, "`GardenBench`: A lightweight, daily evaluation of LLM capabilities"
    - Anthropic, (2026) "System Card: Claude Mythos Preview".
    - *ISLR/P*, Chapter 6.2 "Shrinkage Methods".
- Class (Wednesday 11 November)
    - (ISLR/P) Sean Murphy, Siddharth Singh Taragi, Allwin, Vijval.
    - (Lecture) What a benchmark is and what it can claim
    - (Demonstration) Build a small benchmark as a class: pick a task, write 20 items, agree a rubric, run three models through OpenRouter, grade by hand
    - (Worksheet) Score the class benchmark against the BetterBench checklist. Which criteria did we fail in the first hour?
    - (Guest) Sabrina, Mariana, Benedict, and Oscar on `GardenBench`.

#### Week 10 (starts Monday 16 November)

*Evaluating benchmarks; the statistics of evals: standard errors, clustering by item, paired comparisons between models; validating a model as a grader against human labels; contamination and leakage.*

- Readings
    - Miller, Evan, 2024, "Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations", *arXiv*, [10.48550/arXiv.2411.00640](https://arxiv.org/abs/2411.00640).
    - Biderman, Stella, et al., 2024, "Lessons from the Trenches on Reproducible Evaluation of Language Models", *arXiv*, [10.48550/arXiv.2405.14782](https://arxiv.org/abs/2405.14782).
    - Singh, Shivalika, et al., 2025, "The Leaderboard Illusion", *arXiv*, [10.48550/arXiv.2504.20879](https://arxiv.org/abs/2504.20879).
    - Kapoor, Sayash, and Arvind Narayanan, 2023, "Leakage and the Reproducibility Crisis in Machine-Learning-Based Science", *Patterns*, [10.1016/j.patter.2023.100804](https://www.sciencedirect.com/science/article/pii/S2666389923001599).
    - *ISLR/P*, Chapter 8.1.
- Class (Wednesday 18 November)
    - (Quiz) Week 9 readings and class, and *ISLR/P* Chapters 6.2 and 8.1.
    - (ISLR/P) Group 6.
    - (Lecture) Variance in evals: items, sampling, prompts, judges; contamination; what a two-point difference on a leaderboard means with 200 items
    - (Demonstration) Calibrate a model-as-judge using the Week 3 referee reports as the human labels; watch the ranking move when the judge changes
    - (Worksheet) Add error bars to the class benchmark following Miller. Which differences survive?

#### Week 11 (starts Monday 23 November)

- Class (Wednesday 25 November)
    - Please feel free to use this time to implement your group AI benchmark.

#### Week 12 (starts Monday 30 November): Assignment III and in-class exam III

- Monday 30 November: Part 3 assignment (AI benchmark) due EOD.
- Wednesday 2 December: In-class exam III.

#### Exam period

(Optional) Final exam, all three parts.

