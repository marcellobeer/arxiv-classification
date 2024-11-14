import streamlit as st
import pickle
import numpy as np
import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModel

# Load models and data
@st.cache_resource
def load_resources():
    with open('physics_classifier.pkl', 'rb') as f:
        model_data = pickle.load(f)
    embeddings = np.load('paper_embeddings.npy')
    papers_df = pd.read_pickle('papers_df.pkl')
    tokenizer = AutoTokenizer.from_pretrained('allenai/scibert_scivocab_uncased')
    model = AutoModel.from_pretrained('allenai/scibert_scivocab_uncased')
    return model_data, embeddings, papers_df, tokenizer, model

def get_embedding(text, tokenizer, model):
    encoded = tokenizer(
        text,
        padding=True,
        truncation=True,
        max_length=512,
        return_tensors='pt'
    )
    with torch.no_grad():
        outputs = model(**encoded)
        return outputs.last_hidden_state[:, 0, :].numpy()[0]

def find_similar_papers(query_embedding, embeddings, papers_df, top_k=5):
    similarities = np.dot(embeddings, query_embedding) / (
        np.linalg.norm(embeddings, axis=1) * np.linalg.norm(query_embedding)
    )
    top_indices = np.argsort(similarities)[-top_k:][::-1]
    return papers_df.iloc[top_indices], similarities[top_indices]

# Page config
st.set_page_config(
    page_title="Physics Paper Analyzer",
    page_icon="📚",
    layout="wide"
)

# Main app
st.title('Physics Paper Analyzer 📚')
st.write('Enter a physics paper title and abstract to classify it and find similar papers.')

# Load resources
model_data, embeddings, papers_df, tokenizer, model = load_resources()
classifier = model_data['classifier']
label_encoder = model_data['label_encoder']

# Input fields
abstract = st.text_area("Paper Abstract", height=150)

if st.button('Analyze Paper'):
    if abstract:
        with st.spinner('Analyzing paper...'):
            # Get embedding and predictions
            paper_embedding = get_embedding(abstract, tokenizer, model)
            prediction = classifier.predict([paper_embedding])[0]
            probabilities = classifier.predict_proba([paper_embedding])[0]

            # Classification Results
            st.subheader('Classification Results')
            predicted_category = label_encoder.inverse_transform([prediction])[0]
            st.markdown(f"### Predicted Category: `{predicted_category}`")

            # Plot probabilities
            prob_df = pd.DataFrame({
                'Category': label_encoder.classes_,
                'Probability': probabilities
            }).sort_values('Probability', ascending=True)
            st.bar_chart(prob_df.set_index('Category'))

            # Similar Papers
            st.subheader('Similar Papers')
            similar_papers, similarities = find_similar_papers(paper_embedding, embeddings, papers_df)

            for i, (_, paper) in enumerate(similar_papers.iterrows()):
                expander_title = f"{paper['title']}"
                with st.expander(expander_title, expanded=False):
                    st.markdown(f"**Category:** {paper['category']}")
                    st.markdown(f"**Similarity Score:** {similarities[i]:.4f}")
                    st.markdown("**Abstract:**")
                    st.markdown(paper['abstract'])
    else:
        st.warning('Please enter an abstract.')
