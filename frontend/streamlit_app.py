import streamlit as st
from git import Repo
import pandas as pd
from collections import Counter
import shutil
import os

# Function to clone the repository
def clone_repo(git_url, path_to_clone):
    try:
        Repo.clone_from(git_url, path_to_clone)
        return True
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return False

# Function to get commit messages
def get_commits(path):
    repo = Repo(path)
    commits = []
    authors = []
    for commit in repo.iter_commits():
        commits.append(commit.message)
        authors.append(str(commit.author))

    return commits, authors

# Streamlit App
st.title("Git Repository Analyzer")

git_url = st.text_input("Enter the git repository URL:", "")
path_to_clone = "temp_repo"

if st.button("Fetch Commits"):
    if os.path.exists(path_to_clone):
        shutil.rmtree(path_to_clone)
        
    if clone_repo(git_url, path_to_clone):
        commits, authors = get_commits(path_to_clone)

        # # Display Commits

        # Display Committer Stats
        st.subheader("Committer Stats")
        author_count = Counter(authors)
        df = pd.DataFrame(list(author_count.items()), columns=["Author", "Number of Commits"])
        st.table(df)

        # Remove the cloned repo to clean up
        shutil.rmtree(path_to_clone)

    else:
        st.error("Failed to clone the repository.")
