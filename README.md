https://github.com/epfl-dlab/mdic/tree/master/data
https://github.com/epfl-dlab/mdic/blob/master/data/iterative_cascades.csv

https://chatgpt.com/c/676c0b0c-85d0-8010-8106-686a7de0683f


@inproceedings{horta_ribeiro_message_2019,
author={Ribeiro, Manoel Horta and Gligori\'c, Kristina and West, Robert},
title={Message Distortion in Information Cascades},
booktitle={Proceedings of the 2019 World Wide Web Conference},
year={2019},
}

If you want to quickly and efficiently compare the data in iterative_cascades.csv with your Perceptual Drift Index (PDI) model for a preliminary study, here’s a streamlined approach:

Steps for a Minimal Yet Effective Comparison
1. Focus on One Cascade
Rationale: Analyzing one message cascade is sufficient to demonstrate your model’s applicability without overextending resources.
Action:
Select a single cascade from the iterative_cascades.csv file, identified by its branch or cascade_id.
Filter the dataset for this cascade to trace the message across its iterative transformations.
2. Define Metrics for Comparison
Use your model’s PDI components:

Fidelity Drift (FDr): Measure the absolute differences in text attributes (e.g., word count, sentiment, or similarity score).
Plausibility Drift (PDr): Compare directional changes in message attributes (e.g., whether it becomes more positive, negative, or neutral).
Failed Runs: Determine if the final message deviates drastically from the original (e.g., high semantic dissimilarity).
Compute analogous metrics from the dataset to compare with your model’s predictions.

3. Extract Key Features from the Data
From the Dataset:
Extract level (iteration number) and Answer (message text).
Features to Compute:
Semantic Similarity:
Use a text similarity metric (e.g., cosine similarity of word embeddings or a basic Levenshtein distance) to compare each message to the original.
Text Length:
Analyze changes in text length as a proxy for distortion.
Sentiment:
Compute sentiment scores (positive/negative/neutral) to capture directional plausibility drift.
4. Compare Results
Run Your Model:
Simulate a message cascade using your PDI model with parameters matching the observed cascade (e.g., chain length, node bias, sensitivity).
Align Observed vs. Predicted:
Compare the dataset’s metrics (e.g., semantic similarity) with your model’s calculated fidelity and plausibility drifts.
5. Visualize and Summarize
Create a simple plot showing:
Fidelity Drift: Cumulative absolute changes over iterations.
Plausibility Drift: Directional change across levels.
Highlight the general agreement between the observed and simulated results, emphasizing trends rather than exact matches.