# Lingium: Language Learning Assistant

Lingium is a Streamlit-based web application that uses machine learning to recommend the best Discord servers and resources tailored to your language learning goals. Whether you're preparing for certifications like IELTS or TOEFL, or simply looking to connect with native speakers, Lingium is here to guide you.

## Features
- Personalized recommendations for language learning resources.
- Machine learning-powered Discord server suggestions.
- User-friendly interface built with Streamlit.

## Getting Started

### Prerequisites
- Python 3.8 or higher

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/lingium.git
   ```
2. Navigate to the project directory:
   ```sh
   cd lingium
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Running the App
1. Start the Streamlit server:
   ```sh
   streamlit run app.py
   ```
2. Open the app in your browser at `http://localhost:8501`.

## Project Structure
- `app.py`: Main Streamlit app.
- `home.py`: Home page of the application.
- `train.py`: Script for training the machine learning model.
- `project.py`: Core logic for recommendations.
- `images/`: Contains static assets like logos.
- `requirements.txt`: Python dependencies.
- `.streamlit/config.toml`: Streamlit configuration file.

## License
This project is licensed under the GNU General Public License version 3 (GPLv3).

