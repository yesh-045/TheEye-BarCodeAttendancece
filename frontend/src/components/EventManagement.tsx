import React, { useState } from 'react';
import { Search, Plus, Filter, Calendar, Clock, MapPin, Users2 } from 'lucide-react';

const EventManagement = () => {
  const [showCreateForm, setShowCreateForm] = useState(false);

  const events = [
    {
      id: 1,
      name: 'Tech Talk: AI & Future',
      date: '2024-03-20',
      time: '14:00',
      location: 'Main Hall',
      category: 'Tech Talk',
      attendees: 45,
      maxAttendees: 100,
      status: 'upcoming'
    },
    {
      id: 2,
      name: 'Workshop: Web Development',
      date: '2024-03-22',
      time: '15:30',
      location: 'Room 201',
      category: 'Workshop',
      attendees: 28,
      maxAttendees: 50,
      status: 'upcoming'
    }
  ];

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex justify-between items-center">
        <h1 className="text-2xl font-bold text-gray-900">Event Management</h1>
        <button
          onClick={() => setShowCreateForm(true)}
          className="inline-flex items-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700"
        >
          <Plus className="w-4 h-4 mr-2" />
          Create Event
        </button>
      </div>

      {/* Search and Filter */}
      <div className="flex gap-4">
        <div className="flex-1 relative">
          <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-5 h-5" />
          <input
            type="text"
            placeholder="Search events..."
            className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500"
          />
        </div>
        <button className="inline-flex items-center px-4 py-2 border border-gray-300 rounded-lg text-sm font-medium text-gray-700 bg-white hover:bg-gray-50">
          <Filter className="w-4 h-4 mr-2" />
          Filter
        </button>
      </div>

      {/* Event List */}
      <div className="bg-white rounded-xl shadow-sm overflow-hidden">
        <div className="divide-y divide-gray-200">
          {events.map((event) => (
            <div key={event.id} className="p-6 hover:bg-gray-50 transition-colors">
              <div className="flex justify-between items-start">
                <div className="space-y-3">
                  <div>
                    <h3 className="text-lg font-medium text-gray-900">{event.name}</h3>
                    <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800 mt-1">
                      {event.category}
                    </span>
                  </div>
                  <div className="space-y-2">
                    <p className="text-sm text-gray-500 flex items-center">
                      <Calendar className="w-4 h-4 mr-2" />
                      {event.date}
                    </p>
                    <p className="text-sm text-gray-500 flex items-center">
                      <Clock className="w-4 h-4 mr-2" />
                      {event.time}
                    </p>
                    <p className="text-sm text-gray-500 flex items-center">
                      <MapPin className="w-4 h-4 mr-2" />
                      {event.location}
                    </p>
                    <p className="text-sm text-gray-500 flex items-center">
                      <Users2 className="w-4 h-4 mr-2" />
                      {event.attendees}/{event.maxAttendees} attendees
                    </p>
                  </div>
                </div>
                <div className="flex space-x-3">
                  <button className="text-sm text-indigo-600 hover:text-indigo-900">Edit</button>
                  <button className="text-sm text-red-600 hover:text-red-900">Delete</button>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default EventManagement;