
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

## Demo Walkthrough

`https://www.loom.com/share/abc123xyz456](https://www.loom.com/share/fa0e6dc9ddae439f903f59e272b7355f?sid=819c07dd-a927-4edc-9f23-7f6980ad59e8`


## Challenges I Faced

- **React-Vite caching issues**: Updates to App.tsx were not reflecting due to Vite's hot module cache. This was solved by fully restarting the dev server and clearing the browser cache.

- **Button state logic**: Replacing radio buttons with visually distinct toggles required precise use of Tailwind utility classes to reflect active/hover/pressed states.

- **Tailwind class purging**: Ensured Tailwind didn't purge dynamic utility classes by verifying the correct `content` paths in `tailwind.config.js`.

- **Deployment memory constraint**: Although the web app was fully functional, backend deployment on platforms like Render failed due to RAM limits when using transformer models. Lighter alternatives were explored, but final resolution was deferred due to concurrent end-semester exams.

- Open port detection on serverless platforms**: On Render and Railway, the backend service failed to detect open ports because the server was either bound incorrectly or was killed silently due to memory usage. This required environment-aware port binding and memory-efficient model loading.

- **Backend and frontend decoupling** : Maintaining seamless integration between a separately deployed frontend (on Vercel) and backend (on Render/Fly.io) required correctly managing CORS policies, BASE_URL environment variables, and deployment timing to prevent API misfires during live testing.
## License

MIT License
