
# ThreadSeekerAI

ThreadSeekerAI is a modern AI-powered search interface that allows users to explore relevant discussion threads across different topics using either semantic search or live thread retrieval. It combines the power of SBERT-based semantic similarity with a clean and interactive frontend built in React.

## Features

- Semantic and Live Search modes
- "Why this?" explanation based on relevance score
- Save and remove threads for later reading
- 3D-styled toggle buttons with hover/press effects
- Responsive dark-themed UI using TailwindCSS
- Graceful fallback with mock data if backend is unreachable

## Tech Stack

**Frontend**
- React (Vite + TypeScript)
- Tailwind CSS
- Framer Motion for animation
- Lucide React for icons

**Backend**
- Flask (Python)
- Sentence-Transformers for semantic similarity
- Custom mock thread generator

## Project Structure

```
/src
  App.tsx             # Main frontend component
  /components
    ParticlesBackground.tsx
  /utils
    api.ts            # Handles backend API calls

backend/
  app.py              # Flask backend with /search and /live endpoints
  thread_data.json    # Source data for semantic search
```

## Setup Instructions

1. **Clone the repository**  
   `git clone <repo_url> && cd ThreadSeekerAI`

2. **Install frontend dependencies**  
   `cd frontend`  
   `npm install`

3. **Start the frontend dev server**  
   `npm run dev`

4. **Run the Flask backend**
   ```
   cd backend
   pip install -r requirements.txt
   python app.py
   ```

5. **Access the app at** `http://localhost:5173`

## Challenges I Faced

- **React-Vite caching issues**: Updates to App.tsx were not reflecting due to Vite's hot module cache. This was solved by fully restarting the dev server and clearing the browser cache.
- **Button state logic**: Replacing radio buttons with visually distinct toggles required precise use of Tailwind utility classes to reflect active/hover/pressed states.
- **Thread title formatting**: Needed to remove analysis suffixes like " - Analysis 5" from thread titles in the dataset for a cleaner display.
- **Tailwind class purging**: Ensured Tailwind didn't purge dynamic utility classes by verifying the correct `content` paths in `tailwind.config.js`.

## License

MIT License
