import { Play, Square, Search, FileText, Cpu, Send, Terminal as TerminalIcon } from 'lucide-react';

const Dashboard = () => {
    const modules = [
        { title: 'Discovery', icon: <Search size={24} />, status: 'idle', description: 'Monitor YouTube & X sources' },
        { title: 'Transcription', icon: <FileText size={24} />, status: 'running', description: 'Process videos to text' },
        { title: 'Evaluation', icon: <Cpu size={24} />, status: 'idle', description: 'AI Brand Fit Analysis' },
        { title: 'Publishing', icon: <Send size={24} />, status: 'pending', description: 'Post to Blog & Socials' },
    ];

    return (
        <div className="dashboard-view">
            <header className="page-header">
                <h1>Modular Control Center</h1>
                <p className="text-muted">Manage and monitor automation stages in isolation.</p>
            </header>

            <section className="modules-grid">
                {modules.map((mod) => (
                    <div key={mod.title} className="glass-card module-card">
                        <div className="module-header">
                            <div className="module-icon-wrapper">
                                {mod.icon}
                            </div>
                            <span className={`status-badge status-${mod.status}`}>{mod.status}</span>
                        </div>
                        <h3>{mod.title}</h3>
                        <p>{mod.description}</p>
                        <div className="module-actions">
                            {mod.status === 'running' ? (
                                <button className="btn btn-outline danger-hover">
                                    <Square size={16} /> Stop
                                </button>
                            ) : (
                                <button className="btn btn-primary">
                                    <Play size={16} /> Start
                                </button>
                            )}
                        </div>
                    </div>
                ))}
            </section>

            <section className="glass-card console-view">
                <div className="console-header">
                    <div className="header-left">
                        <TerminalIcon size={18} />
                        <span>Agent Console</span>
                    </div>
                    <div className="header-right">
                        <div className="live-indicator"></div>
                        <span>Live Feed</span>
                    </div>
                </div>
                <div className="console-output">
                    <div className="log-line"><span className="log-time">[08:42:10]</span> <span className="log-system">SYSTEM:</span> Agent initialized.</div>
                    <div className="log-line"><span className="log-time">[08:42:15]</span> <span className="log-info">INFO:</span> Polling YouTube channel 'Kango Anywhere'...</div>
                    <div className="log-line"><span className="log-time">[08:43:02]</span> <span className="log-success">SUCCESS:</span> New content found: 'Exploring Outback'.</div>
                    <div className="log-line"><span className="log-time">[08:43:05]</span> <span className="log-info">INFO:</span> Starting transcription via youtubetotranscript.com...</div>
                    <div className="log-line typing">_</div>
                </div>
            </section>
        </div>
    );
};

export default Dashboard;
