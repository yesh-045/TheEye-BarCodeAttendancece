import React, { useState } from 'react';
import { 
  LayoutDashboard, 
  Calendar, 
  QrCode, 
  BarChart3, 
  Users,
} from 'lucide-react';
import Dashboard from './components/Dashboard';
import EventManagement from './components/EventManagement';
import QRScanner from './components/QRScanner';
import Members from './components/Members';

function App() {
  const [activeTab, setActiveTab] = useState('dashboard');

  const navigation = [
    { id: 'dashboard', name: 'Dashboard', icon: LayoutDashboard },
    { id: 'events', name: 'Events', icon: Calendar },
    { id: 'scanner', name: 'QR Scanner', icon: QrCode },
    { id: 'members', name: 'Members', icon: Users }
  ];

  const renderContent = () => {
    switch (activeTab) {
      case 'dashboard':
        return <Dashboard />;
      case 'events':
        return <EventManagement />;
      case 'scanner':
        return <QRScanner />;
      case 'members':
        return <Members />;
      default:
        return <Dashboard />;
    }
  };

  return (
    <div className="flex h-screen bg-gray-50">
      {/* Sidebar */}
      <div className="w-64 bg-white border-r border-gray-200">
        <div className="p-6">
          <h1 className="text-2xl font-bold text-indigo-600">ClubTrack</h1>
        </div>
        <nav className="mt-4">
          {navigation.map((item) => (
            <button
              key={item.id}
              onClick={() => setActiveTab(item.id)}
              className={`w-full flex items-center px-6 py-3 text-sm font-medium ${
                activeTab === item.id
                  ? 'text-indigo-600 bg-indigo-50'
                  : 'text-gray-600 hover:text-indigo-600 hover:bg-gray-50'
              }`}
            >
              <item.icon className="w-5 h-5 mr-3" />
              {item.name}
            </button>
          ))}
        </nav>
      </div>

      {/* Main Content */}
      <div className="flex-1 overflow-auto">
        <main className="p-8">
          {renderContent()}
        </main>
      </div>
    </div>
  );
}

export default App;