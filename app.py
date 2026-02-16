import streamlit as st
import pandas as pd
import requests
import pickle
import time

# Page configuration
st.set_page_config(
    page_title="Netflix Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# Load movie data and cosine similarity matrix
@st.cache_data
def load_data():
    with open('movie_data.pkl', 'rb') as file:
        movies, cosine_sim = pickle.load(file)
    return movies, cosine_sim

movies, cosine_sim = load_data()

# Load additional movie details from CSV
@st.cache_data
def load_movie_details():
    movies_df = pd.read_csv('tmdb_5000_movies.csv')
    return movies_df

movies_details = load_movie_details()

# Function to fetch movie details from API
@st.cache_data(show_spinner=False)
def fetch_movie_details(movie_id):
    try:
        movie_id = int(movie_id)
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json'
        }
        
        time.sleep(0.1)
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        return {
            'poster': f"https://image.tmdb.org/t/p/w500/{data.get('poster_path')}" if data.get('poster_path') else None,
            'overview': data.get('overview', 'No overview available'),
            'rating': data.get('vote_average', 0),
            'release_date': data.get('release_date', 'N/A'),
            'genres': [g['name'] for g in data.get('genres', [])]
        }
    except Exception as e:
        print(f"Error fetching details for movie_id {movie_id}: {str(e)}")
        return None

# Enhanced recommendation function with similarity scores
def get_recommendations(title, num_recommendations=5):
    try:
        idx = movies[movies['title'] == title].index[0]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:num_recommendations+1]
        
        movie_indices = [i[0] for i in sim_scores]
        similarity_scores = [i[1] for i in sim_scores]
        
        recommendations = movies[['title', 'movie_id']].iloc[movie_indices].copy()
        recommendations['similarity_score'] = similarity_scores
        
        return recommendations
    except IndexError:
        st.error("Movie not found in database!")
        return None

# Custom CSS
st.markdown("""
    <style>
    .movie-card {
        border-radius: 10px;
        padding: 10px;
        background-color: #f0f2f6;
        margin-bottom: 10px;
    }
    .similarity-badge {
        background-color: #0A6BCB;
        color: white;
        padding: 3px 8px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Main UI
st.markdown("<h1 style='text-align: center; color: #E50914;'>🎬 Netflix Movie Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>Discover movies tailored to your taste using advanced content-based filtering</p>", unsafe_allow_html=True)

st.markdown("---")

# Sidebar for filters
with st.sidebar:
    st.header("⚙️ Settings")
    num_recommendations = st.slider("Number of recommendations", min_value=3, max_value=10, value=5, step=1)
    show_details = st.checkbox("Show movie details", value=True)
    show_similarity = st.checkbox("Show similarity scores", value=True)
    
    st.markdown("---")
    st.markdown("### About")
    st.info("This recommendation system uses **content-based filtering** with TF-IDF vectorization and cosine similarity based on movie genres, keywords, cast, and crew.")

# Search and select movie
col1, col2 = st.columns([3, 1])
with col1:
    selected_movie = st.selectbox('🔍 Select or search for a movie:', movies['title'].values, key='movie_select')
with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    recommend_btn = st.button('🎯 Get Recommendations', use_container_width=True)

if recommend_btn:
    with st.spinner('Finding the best recommendations for you...'):
        recommendations = get_recommendations(selected_movie, num_recommendations)
        
        if recommendations is not None and len(recommendations) > 0:
            st.success(f"✨ Found {len(recommendations)} movies similar to **{selected_movie}**")
            st.markdown("---")
            
            # Display recommendations
            for i in range(len(recommendations)):
                movie_title = recommendations.iloc[i]['title']
                movie_id = recommendations.iloc[i]['movie_id']
                similarity = recommendations.iloc[i]['similarity_score']
                
                # Fetch movie details
                movie_info = fetch_movie_details(movie_id)
                
                # Create columns for layout
                col_poster, col_details = st.columns([1, 3])
                
                with col_poster:
                    if movie_info and movie_info['poster']:
                        st.image(movie_info['poster'], use_container_width=True)
                    else:
                        st.markdown("<div style='text-align: center; font-size: 60px;'>🎬</div>", unsafe_allow_html=True)
                
                with col_details:
                    # Title and similarity score
                    title_html = f"<h3 style='margin-bottom: 5px;'>{i+1}. {movie_title}</h3>"
                    st.markdown(title_html, unsafe_allow_html=True)
                    
                    if show_similarity:
                        similarity_percent = int(similarity * 100)
                        st.markdown(f"<span class='similarity-badge'>{similarity_percent}% Match</span>", unsafe_allow_html=True)
                    
                    if show_details and movie_info:
                        # Display movie details
                        col_a, col_b, col_c = st.columns(3)
                        with col_a:
                            st.markdown(f"**⭐ Rating:** {movie_info['rating']}/10")
                        with col_b:
                            st.markdown(f"**📅 Release:** {movie_info['release_date'][:4] if movie_info['release_date'] != 'N/A' else 'N/A'}")
                        with col_c:
                            if movie_info['genres']:
                                st.markdown(f"**� Genre:** {', '.join(movie_info['genres'][:2])}")
                        
                        # Overview
                        with st.expander("📖 See overview"):
                            st.write(movie_info['overview'])
                
                st.markdown("---")
        else:
            st.warning("No recommendations found. Please try another movie.")

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888; font-size: 12px;'>Built with ❤️ using Streamlit | Data from TMDB</p>", unsafe_allow_html=True)
