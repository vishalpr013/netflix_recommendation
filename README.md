# 🎬 Netflix Movie Recommendation System

A sophisticated content-based movie recommendation system built with Python and Streamlit. This application suggests similar movies based on genres, keywords, cast, and crew using advanced machine learning techniques.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🌟 Features

- **Smart Recommendations**: Uses TF-IDF vectorization and cosine similarity for accurate movie suggestions
- **Beautiful UI**: Netflix-inspired interface with a clean, modern design
- **Movie Posters**: Displays high-quality movie posters fetched from TMDB API
- **Detailed Information**: Shows ratings, release dates, genres, and plot overviews
- **Similarity Scores**: Displays percentage match for each recommendation
- **Customizable**: Adjust the number of recommendations (3-10 movies)
- **Interactive Filters**: Toggle movie details and similarity scores on/off
- **Fast Performance**: Cached data loading for optimal speed

## 📸 Screenshots

*Add your screenshot here after deploying*

## 🛠️ Technologies Used

- **Python 3.8+**: Core programming language
- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Scikit-learn**: Machine learning (TF-IDF, Cosine Similarity)
- **Requests**: HTTP library for API calls
- **TMDB API**: Movie data and posters

## 📋 Prerequisites

Before running this project, make sure you have:

- Python 3.8 or higher installed
- pip (Python package manager)
- A TMDB API key (free - [Get it here](https://www.themoviedb.org/settings/api))

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/vishalpr013/netflix_recommendation.git
   cd netflix_recommendation
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

5. **Download the preprocessed data**
   
   Due to GitHub file size limitations, you need to generate `movie_data.pkl`:
   - Open and run the Jupyter notebook `movie_recommendation.ipynb`
   - This will process the CSV files and generate `movie_data.pkl`
   - Alternatively, download it from [Google Drive Link - Add your link here]

6. **Run the application**
   ```bash
   streamlit run app.py
   ```

7. **Open your browser**
   
   The app will automatically open at `http://localhost:8501`

## 📁 Project Structure

```
netflix_recommendation/
│
├── app.py                          # Main Streamlit application
├── movie_recommendation.ipynb      # Jupyter notebook with model training
├── movie_data.pkl                  # Preprocessed movie data (generate this)
├── tmdb_5000_movies.csv           # TMDB movies dataset
├── tmdb_5000_credits.csv          # TMDB credits dataset
├── requirements.txt               # Python dependencies
├── .gitignore                     # Git ignore file
└── README.md                      # Project documentation
```

## 🎯 How It Works

### 1. **Data Preprocessing**
   - Loads movie data from TMDB datasets
   - Extracts features: genres, keywords, cast, and crew
   - Combines features into a single text "tag" for each movie

### 2. **Feature Extraction**
   - Uses TF-IDF (Term Frequency-Inverse Document Frequency) vectorization
   - Converts text data into numerical vectors
   - Removes common English stop words

### 3. **Similarity Calculation**
   - Computes cosine similarity between all movie vectors
   - Creates a similarity matrix for efficient lookups

### 4. **Recommendation Generation**
   - Finds the selected movie in the dataset
   - Retrieves top N most similar movies based on cosine similarity
   - Fetches additional details and posters from TMDB API

## 🎨 Usage

1. **Select a Movie**: Use the dropdown to search and select a movie
2. **Adjust Settings**: Use the sidebar to customize:
   - Number of recommendations (3-10)
   - Show/hide movie details
   - Show/hide similarity scores
3. **Get Recommendations**: Click the "Get Recommendations" button
4. **Explore Results**: View recommended movies with posters, ratings, and details

## 📊 Dataset

This project uses the TMDB 5000 Movie Dataset, which includes:
- 4,800+ movies
- Movie metadata (title, genres, keywords, budget, revenue)
- Cast and crew information
- User ratings and vote counts

**Source**: [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

## 🔑 API Configuration

The app uses TMDB API for fetching movie posters and additional details. The API key is included in the code for demonstration purposes. For production use:

1. Get your own API key from [TMDB](https://www.themoviedb.org/settings/api)
2. Replace the API key in `app.py`:
   ```python
   api_key = "YOUR_API_KEY_HERE"
   ```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🐛 Known Issues

- TMDB API connection may fail due to network restrictions (firewall/antivirus)
- Some movie posters may not load if they're not available in TMDB database
- Large datasets may take time to load initially

## 🔮 Future Enhancements

- [ ] Add collaborative filtering for hybrid recommendations
- [ ] Implement user ratings and watchlist
- [ ] Add movie search with autocomplete
- [ ] Include movie trailers from YouTube API
- [ ] Add genre-based filtering
- [ ] Deploy on cloud platform (Streamlit Cloud, Heroku, or AWS)
- [ ] Add user authentication
- [ ] Create a recommendation history feature

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Vishal PR**
- GitHub: [@vishalpr013](https://github.com/vishalpr013)
- Project Link: [https://github.com/vishalpr013/netflix_recommendation](https://github.com/vishalpr013/netflix_recommendation)

## 🙏 Acknowledgments

- [TMDB](https://www.themoviedb.org/) for providing the movie database and API
- [Streamlit](https://streamlit.io/) for the amazing web framework
- [Kaggle](https://www.kaggle.com/) for hosting the dataset
- All contributors and supporters of this project

## 📞 Support

If you have any questions or run into issues, please:
- Open an issue on GitHub
- Contact me through GitHub

---

<p align="center">Made with ❤️ by Vishal PR</p>
<p align="center">⭐ Star this repo if you find it helpful!</p>
