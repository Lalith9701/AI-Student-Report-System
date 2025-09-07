import pandas as pd
import os

def analyze_data(filepath):
    df = pd.read_csv(filepath)
    df.columns = df.columns.str.strip().str.lower()

    # Detect marks column
    if "marks" in df.columns:
        marks_col = "marks"
    elif "score" in df.columns:
        marks_col = "score"
    elif "total" in df.columns:
        marks_col = "total"
    else:
        raise KeyError("CSV must have a column for marks/score/total")

    # Performance categorization
    df["Performance"] = df[marks_col].apply(
        lambda x: "Excellent" if x >= 85 else ("Average" if x >= 60 else "Needs Improvement")
    )

    # Rank students
    df['rank'] = df[marks_col].rank(ascending=False, method='min').astype(int)
    df = df.sort_values(by=marks_col, ascending=False)

    # Save processed file
    processed_filename = "processed_" + os.path.basename(filepath)
    df.to_csv(os.path.join("uploads", processed_filename), index=False)

    # Convert to list of dicts
    results = df.to_dict(orient='records')
    return results, processed_filename
