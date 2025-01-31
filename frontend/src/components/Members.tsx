import React from 'react';
import { Search, Filter, User, BarChart, ChevronRight } from 'lucide-react';

const Members = () => {
  const members = [
    {
      id: 1,
      name: 'Alex Johnson',
      email: 'alex.j@example.com',
      joinDate: '2024-01-15',
      attendance: 85,
      status: 'active'
    },
    {
      id: 2,
      name: 'Sarah Williams',
      email: 'sarah.w@example.com',
      joinDate: '2024-02-01',
      attendance: 92,
      status: 'active'
    }
  ];

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex justify-between items-center">
        <h1 className="text-2xl font-bold text-gray-900">Member Management</h1>
        <button className="inline-flex items-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700">
          Add Member
        </button>
      </div>

      {/* Search and Filter */}
      <div className="flex gap-4">
        <div className="flex-1 relative">
          <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-5 h-5" />
          <input
            type="text"
            placeholder="Search members..."
            className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500"
          />
        </div>
        <button className="inline-flex items-center px-4 py-2 border border-gray-300 rounded-lg text-sm font-medium text-gray-700 bg-white hover:bg-gray-50">
          <Filter className="w-4 h-4 mr-2" />
          Filter
        </button>
      </div>

      {/* Member Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {members.map((member) => (
          <div key={member.id} className="bg-white rounded-xl shadow-sm p-6 hover:shadow-md transition-shadow">
            <div className="flex items-start justify-between">
              <div className="flex items-center">
                <div className="w-12 h-12 bg-gray-100 rounded-full flex items-center justify-center">
                  <User className="w-6 h-6 text-gray-500" />
                </div>
                <div className="ml-4">
                  <h3 className="text-lg font-medium text-gray-900">{member.name}</h3>
                  <p className="text-sm text-gray-500">{member.email}</p>
                </div>
              </div>
              <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${
                member.status === 'active' ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-800'
              }`}>
                {member.status}
              </span>
            </div>

            <div className="mt-6">
              <div className="flex items-center justify-between text-sm text-gray-500 mb-2">
                <span>Attendance Rate</span>
                <span className="font-medium text-gray-900">{member.attendance}%</span>
              </div>
              <div className="w-full bg-gray-200 rounded-full h-2">
                <div 
                  className="bg-indigo-600 h-2 rounded-full" 
                  style={{ width: `${member.attendance}%` }}
                ></div>
              </div>
            </div>

            <div className="mt-6 pt-6 border-t border-gray-200">
              <button className="w-full inline-flex items-center justify-center text-sm text-indigo-600 hover:text-indigo-900">
                View Details
                <ChevronRight className="w-4 h-4 ml-2" />
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Members;