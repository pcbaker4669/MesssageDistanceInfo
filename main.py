import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("iterative_cascades.csv")

# Inspect the unique values in the 'branch' column
print("Unique branches:", df['branch'].unique())

branches =  ['NEJMoa1404037', 'NEJMoa1206809', 'NEJMoa1000727', 'NEJMoa1103507',
 'NEJMoa1304127', 'NEJMoa1003833', 'NEJMoa1003114', 'NEJMoa072761',
 'NEJMoa1014296', 'NEJMoa1200303', 'NEJMoa1112010', 'NEJMoa0804748',
 'NEJMoa1102287', 'NEJMoa0907413', 'NEJMoa021134', 'NEJMoa1200850']

# Filter for a single cascade based on a valid 'branch' value
for valid_branch in branches:
    print("vb = ", valid_branch)
    # valid_branch = "NEJMoa1404037"  # Example branch; replace with a valid one from the dataset
    cascade_df = df[df['branch'] == valid_branch].sort_values(by="level")

    # Ensure the DataFrame is not empty
    if cascade_df.empty:
        print(f"No data found for branch: {valid_branch}")
    else:
        # Check available levels
        print("Available levels:", cascade_df['level'].unique())

        # Attempt to extract the original message
        if 0 in cascade_df['level'].values:
            original_message = cascade_df[cascade_df['level'] == 0]['Answer'].iloc[0]
        else:
            print("No level 0 found; using the first available message as the original.")
            original_message = cascade_df['Answer'].iloc[0]  # Use the first message in the cascade

        # Extract all messages in the cascade
        messages = cascade_df['Answer'].tolist()

        # Compute semantic similarity for each level
        vectorizer = TfidfVectorizer().fit([original_message] + messages)
        tfidf_matrix = vectorizer.transform(messages)
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix).flatten()

        # Compute text lengths as a proxy for distortion
        text_lengths = [len(msg.split()) for msg in messages]

        # Print results
        for i, (msg, sim, length) in enumerate(zip(messages, similarity, text_lengths)):
            print(f"Level {i}: Similarity={sim:.2f}, Length={length}")

        # Plot results
        plt.figure(figsize=(10, 6))
        plt.plot(range(len(messages)), similarity, label="Semantic Similarity", marker='o')
        # plt.plot(range(len(messages)), text_lengths, label="Text Length", marker='o')
        plt.legend()
        plt.xlabel("Level")
        plt.ylabel("Metric")
        plt.title(f"Cascade Metrics: {valid_branch}")
        plt.grid(True)
        plt.show()