import React, { useState, useEffect } from 'react';
import { Search, Brain, Loader2, Github, Linkedin, BookmarkMinus } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import ParticlesBackground from './components/ParticlesBackground';

interface Thread {
  title: string;
  content: string;
  tags: string[];
  source: string;
  timestamp: string;
  relevance_score?: number;
}

function App() {
  const [query, setQuery] = useState('');
  const [isSearching, setIsSearching] = useState(false);
  const [results, setResults] = useState<Thread[]>([]);
  // const [error, setError] = useState<string | null>(null);
  const [showWhyThis, setShowWhyThis] = useState(true);
  const [searchMode, setSearchMode] = useState<'semantic' | 'live'>('live');
  const [toast, setToast] = useState('');
  const [savedThreads, setSavedThreads] = useState<Thread[]>(() => {
    const stored = localStorage.getItem('savedThreads');
    return stored ? JSON.parse(stored) : [];
  });

  useEffect(() => {
    if (toast) {
      const timer = setTimeout(() => setToast(''), 2000);
      return () => clearTimeout(timer);
    }
  }, [toast]);

  const handleSave = (thread: Thread) => {
    if (savedThreads.some(t => t.title === thread.title)) return;
    const updated = [...savedThreads, thread];
    setSavedThreads(updated);
    localStorage.setItem('savedThreads', JSON.stringify(updated));
    setToast('Saved for later');
  };

  const handleRemove = (thread: Thread) => {
    const updated = savedThreads.filter(t => t.title !== thread.title);
    setSavedThreads(updated);
    localStorage.setItem('savedThreads', JSON.stringify(updated));
    setToast('Removed from saved');
  };

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!query.trim()) return;

    setIsSearching(true);
    // setError(null);

    try {
      const BASE_URL = 'http://localhost:5000'; // Flask backend port
      const endpoint = searchMode === 'semantic' ? '/search' : '/live';
      // const response = await fetch(endpoint, {
      const response = await fetch(`${BASE_URL}${endpoint}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query }),
      });
      if (!response.ok) throw new Error('Server error');
      const data = await response.json();
      setResults(data.results || []);
    } catch (err) {
      // console.error(err);
      // setError('Backend not responding. Showing mock data.');
    } finally {
      setIsSearching(false);
    }
  };
  const getTagColor = (tag: string): string => {
    const colors: Record<string, string> = {
      AI: 'bg-indigo-500/50',
      Technology: 'bg-purple-500/50',
      Discussion: 'bg-emerald-500/50',
      Trending: 'bg-orange-500/50',
    };
    return colors[tag] || 'bg-blue-500/50';
  };

  return (
    <div className="min-h-screen bg-dark-900 relative overflow-hidden">
      <ParticlesBackground />
      <div className="absolute inset-0 animated-gradient -z-10" />

      {toast && (
        <div className="fixed bottom-24 left-1/2 transform -translate-x-1/2 bg-white text-gray-900 px-6 py-2 rounded shadow-md z-50 text-sm font-medium">
          {toast}
        </div>
      )}

      <div className="max-w-7xl mx-auto px-4 py-12">
        <motion.div className="text-center mb-16" initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.8 }}>
          <motion.div className="flex items-center justify-center mb-6" animate={{ scale: [1, 1.1, 1], rotate: [0, 5, -5, 0] }} transition={{ duration: 2, repeat: Infinity, repeatDelay: 3 }}>
            <Brain className="w-16 h-16 text-indigo-400" />
          </motion.div>
          <h1 className="font-serif text-5xl md:text-7xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-indigo-400 to-purple-400 mb-6">
            Discover Threads That Match Your Vibe
          </h1>
          <p className="text-gray-400 text-xl max-w-2xl mx-auto">
            Explore intelligent discussions on any topic using advanced AI search
          </p>
        </motion.div>

        <motion.form onSubmit={handleSearch} className="max-w-3xl mx-auto mb-16" initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.8, delay: 0.2 }}>
          <div className="glass-card rounded-2xl p-8 space-y-6">
            <div className="relative">
              <Search className="absolute left-4 top-4 h-6 w-6 text-gray-400" />
              <input type="text" value={query} onChange={(e) => setQuery(e.target.value)} placeholder="What do you want to explore?" className="w-full pl-14 pr-4 py-4 rounded-xl bg-dark-800 border border-gray-700 text-white placeholder-gray-400 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-500/20 outline-none transition-all" />
            </div>

            <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
              <div className="flex gap-6">
                <label className="inline-flex items-center text-sm text-gray-300">
                  <input type="radio" checked={searchMode === 'semantic'} onChange={() => setSearchMode('semantic')} className="form-radio mr-2 text-indigo-500" />
                   Semantic Search
                </label>
                <label className="inline-flex items-center text-sm text-gray-300">
                  <input type="radio" checked={searchMode === 'live'} onChange={() => setSearchMode('live')} className="form-radio mr-2 text-indigo-500" />
                   Live Threads
                </label>
              </div>

              <motion.button type="submit" disabled={isSearching} className="bg-gradient-to-r from-indigo-500 to-purple-500 text-white px-8 py-3 rounded-xl font-medium flex items-center space-x-2 hover:opacity-90 transition-all disabled:opacity-70 disabled:cursor-not-allowed" whileHover={{ scale: 1.02 }} whileTap={{ scale: 0.98 }}>
                {isSearching ? <Loader2 className="w-5 h-5 animate-spin" /> : <Search className="w-5 h-5" />}
                <span>Search</span>
              </motion.button>
            </div>
          </div>
        </motion.form>

        {results.length > 0 && (
          <div className="mb-4 text-right">
            <label className="inline-flex items-center cursor-pointer text-sm text-gray-300">
              <input type="checkbox" className="form-checkbox mr-2 text-indigo-500" checked={showWhyThis} onChange={() => setShowWhyThis(!showWhyThis)} />
              Show “Why this?” explanation
            </label>
          </div>
        )}

        <AnimatePresence>
          {results.length > 0 && (
            <motion.div className="grid grid-cols-1 md:grid-cols-2 gap-6" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}>
              {[...results].sort((a, b) => (b.relevance_score ?? 0) - (a.relevance_score ?? 0)).map((result, index) => (
                <motion.div key={index} className="glass-card rounded-xl p-6 hover:bg-white/15 transition-all cursor-pointer" initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.5, delay: index * 0.1 }} whileHover={{ scale: 1.02 }}>
                  <h3 className="text-xl font-semibold text-white mb-3">{result.title}</h3>
                  {result.content && <p className="text-gray-300 mb-4">{result.content}</p>}
                  <div className="flex flex-wrap gap-2 mb-4">
                    {result.tags.map((tag, i) => (
                      <span key={i} className={`${getTagColor(tag)} text-white text-sm px-3 py-1 rounded-full`}>{tag}</span>
                    ))}
                  </div>
                  <div className="flex justify-between text-sm text-gray-400 mb-2">
                    <span>{result.source}</span>
                    <span>{result.timestamp}</span>
                  </div>
                  {showWhyThis && result.relevance_score && (
                    <p className="text-xs italic text-indigo-300 mt-1">
                      Why this? Matched with {Math.round(result.relevance_score * 100)}% relevance
                    </p>
                  )}
                  <button onClick={() => handleSave(result)} className="text-sm mt-3 text-indigo-400 hover:text-indigo-200">
                    Save for Later
                  </button>
                </motion.div>
              ))}
            </motion.div>
          )}
        </AnimatePresence>

        {/* Saved Threads */}
        {savedThreads.length > 0 && (
          <div className="mt-16">
            <h2 className="text-2xl font-bold text-white mb-4">📌 Saved Threads</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              {savedThreads.map((t, i) => (
                <div key={i} className="glass-card rounded-xl p-6 text-white">
                  <h3 className="text-lg font-semibold mb-2">{t.title}</h3>
                  <p className="text-gray-300 mb-2">{t.content}</p>
                  <div className="flex justify-between text-sm text-gray-400 mb-2">
                    <span>{t.source}</span>
                    <span>{t.timestamp}</span>
                  </div>
                  <div className="flex flex-wrap gap-2 mb-4">
                    {t.tags.map((tag, idx) => (
                      <span key={idx} className={`${getTagColor(tag)} text-white text-sm px-3 py-1 rounded-full`}>{tag}</span>
                    ))}
                  </div>
                  <button onClick={() => handleRemove(t)} className="text-sm inline-flex items-center text-red-400 hover:text-red-300">
                    <BookmarkMinus className="w-4 h-4 mr-1" /> Remove
                  </button>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>

      <motion.footer className="fixed bottom-0 left-0 right-0 glass-card border-t border-white/10 py-4" initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.8, delay: 0.4 }}>
        <div className="max-w-7xl mx-auto px-4 flex justify-center space-x-6">
          <a href="https://github.com/Harsh24567" target="_blank" rel="noopener noreferrer" className="text-gray-400 hover:text-white transition-colors"><Github className="w-6 h-6" /></a>
          <a href="https://linkedin.com/in/harsh-mall-187a8a245" target="_blank" rel="noopener noreferrer" className="text-gray-400 hover:text-white transition-colors"><Linkedin className="w-6 h-6" /></a>
        </div>
      </motion.footer>
    </div>
  );
}

export default App;