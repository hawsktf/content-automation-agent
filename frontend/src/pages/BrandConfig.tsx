import { useState } from 'react';
import { Plus, Trash2, Save, Globe, Info } from 'lucide-react';

const BrandConfig = () => {
    const [brands, setBrands] = useState([
        { id: 1, name: 'Kango Anywhere', mission: 'Content for outback explorers.' },
        { id: 2, name: 'Citizen Erased', mission: 'Dystopian fiction and commentary.' },
    ]);

    return (
        <div className="settings-view">
            <header className="page-header">
                <h1>Brand Configuration</h1>
                <p className="text-muted">Manage your brands and their distinct voices.</p>
            </header>

            <div className="settings-layout">
                <section className="brand-list-section">
                    <div className="section-header">
                        <h2>Active Brands</h2>
                        <button className="btn btn-primary btn-small">
                            <Plus size={16} /> Add Brand
                        </button>
                    </div>

                    <div className="brand-grid">
                        {brands.map(brand => (
                            <div key={brand.id} className="glass-card brand-item">
                                <div className="brand-info">
                                    <h3>{brand.name}</h3>
                                    <p>{brand.mission}</p>
                                </div>
                                <div className="brand-actions">
                                    <button className="btn btn-outline"><Info size={16} /></button>
                                    <button className="btn btn-outline danger-text"><Trash2 size={16} /></button>
                                </div>
                            </div>
                        ))}
                    </div>
                </section>

                <section className="operational-settings glass-card">
                    <div className="section-header">
                        <h2><Globe size={20} /> Operational Settings</h2>
                    </div>

                    <div className="settings-form">
                        <div className="form-group">
                            <label>Google Sheets ID</label>
                            <input type="text" placeholder="Enter Sheet Identifier..." className="glass-input" />
                        </div>

                        <div className="form-row">
                            <div className="form-group">
                                <label>Polling Frequency (s)</label>
                                <input type="number" defaultValue={3600} className="glass-input" />
                            </div>
                            <div className="form-group">
                                <label>Posting Timezone</label>
                                <select className="glass-input">
                                    <option>UTC</option>
                                    <option>US/Pacific</option>
                                    <option>Europe/London</option>
                                </select>
                            </div>
                        </div>

                        <div className="form-group">
                            <label>Firefox Profile Path</label>
                            <input type="text" defaultValue="/home/spoonbill/.mozilla/firefox/automation" className="glass-input" />
                        </div>

                        <button className="btn btn-primary full-width">
                            <Save size={18} /> Save Settings
                        </button>
                    </div>
                </section>
            </div>
        </div>
    );
};

export default BrandConfig;
