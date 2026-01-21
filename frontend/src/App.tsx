import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import BrandConfig from './pages/BrandConfig';
import { LayoutGrid, Settings, Terminal, Activity } from 'lucide-react';

function App() {
  return (
    <Router>
      <div className="app-container">
        <nav className="sidebar glass-card">
          <div className="nav-logo">
            <Activity className="accent-icon" />
            <span>AutoAgent</span>
          </div>
          <div className="nav-links">
            <Link to="/" className="nav-link">
              <LayoutGrid size={20} />
              <span>Dashboard</span>
            </Link>
            <Link to="/brands" className="nav-link">
              <Settings size={20} />
              <span>Brands</span>
            </Link>
          </div>
          <div className="nav-footer">
            <div className="status-item">
              <div className="live-indicator"></div>
              <span>Agent Online</span>
            </div>
          </div>
        </nav>

        <main className="main-content">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/brands" element={<BrandConfig />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
