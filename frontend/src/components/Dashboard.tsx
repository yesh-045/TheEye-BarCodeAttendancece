import React from 'react';
import { Users, Calendar, Clock, TrendingUp } from 'lucide-react';

const Dashboard = () => {
  const stats = [
    { label: 'Active Events', value: '3', icon: Calendar, color: 'bg-blue-500' },
    { label: 'Total Members', value: '156', icon: Users, color: 'bg-green-500' },
    { label: 'Today\'s Attendance', value: '45', icon: Clock, color: 'bg-purple-500' },
    { label: 'Monthly Growth', value: '+12%', icon: TrendingUp, color: 'bg-orange-500' }
  ];

  const upcomingEvents = [
    {
      id: 1,
      name: 'Tech Talk: AI & Future',
      date: '2024-03-20',
      time: '14:00',
      location: 'Main Hall',
      attendees: 45,
      maxAttendees: 100
    },
    {
      id: 2,
      name: 'Workshop: Web Development',
      date: '2024-03-22',
      time: '15:30',
      location: 'Room 201',
      attendees: 28,
      maxAttendees: 50
    }
  ];

  return (
    <div className="space-y-8">
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {stats.map((stat, index) => (
          <div key={index} className="bg-white rounded-xl shadow-sm p-6">
            <div className={`inline-flex p-3 rounded-lg ${stat.color} bg-opacity-10 mb-4`}>
              <stat.icon className={`w-6 h-6 ${stat.color.replace('bg-', 'text-')}`} />
            </div>
            <h3 className="text-2xl font-bold text-gray-900">{stat.value}</h3>
            <p className="text-sm text-gray-500 mt-1">{stat.label}</p>
          </div>
        ))}
      </div>

      <div className="bg-white rounded-xl shadow-sm p-6">
        <h2 className="text-lg font-semibold text-gray-900 mb-6">Upcoming Events</h2>
        <div className="space-y-4">
          {upcomingEvents.map((event) => (
            <div key={event.id} className="border rounded-lg p-4 hover:border-indigo-500 transition-colors">
              <div className="flex justify-between items-start">
                <div>
                  <h3 className="font-medium text-gray-900">{event.name}</h3>
                  <div className="mt-1 space-y-1">
                    <p className="text-sm text-gray-500 flex items-center">
                      <Calendar className="w-4 h-4 mr-2" />
                      {event.date} at {event.time}
                    </p>
                    <p className="text-sm text-gray-500 flex items-center">
                      <Users className="w-4 h-4 mr-2" />
                      {event.attendees}/{event.maxAttendees} attendees
                    </p>
                  </div>
                </div>
                <span className="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-green-100 text-green-800">
                  Active
                </span>
              </div>
              <div className="mt-4">
                <div className="w-full bg-gray-200 rounded-full h-2">
                  <div 
                    className="bg-indigo-600 h-2 rounded-full" 
                    style={{ width: `${(event.attendees / event.maxAttendees) * 100}%` }}
                  ></div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Dashboard;