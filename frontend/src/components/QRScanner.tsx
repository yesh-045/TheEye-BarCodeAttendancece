import React, { useState } from 'react';
import { QrCode, User, CheckCircle, XCircle } from 'lucide-react';

const QRScanner = () => {
  const [scanStatus, setScanStatus] = useState<'idle' | 'success' | 'error'>('idle');
  const [memberInfo, setMemberInfo] = useState(null);

  return (
    <div className="max-w-2xl mx-auto space-y-8">
      <div className="text-center">
        <h1 className="text-2xl font-bold text-gray-900">QR Scanner</h1>
        <p className="mt-2 text-gray-600">Scan member QR codes to mark attendance</p>
      </div>

      {/* Scanner Viewport */}
      <div className="relative aspect-square max-w-md mx-auto">
        <div className="absolute inset-0 border-2 border-dashed border-gray-300 rounded-lg flex items-center justify-center">
          {scanStatus === 'idle' && (
            <div className="text-center p-8">
              <QrCode className="w-12 h-12 mx-auto text-gray-400 mb-4" />
              <p className="text-gray-500">Position the QR code within the frame</p>
            </div>
          )}
          {scanStatus === 'success' && (
            <div className="text-center p-8">
              <CheckCircle className="w-12 h-12 mx-auto text-green-500 mb-4" />
              <p className="text-green-600">Successfully scanned!</p>
            </div>
          )}
          {scanStatus === 'error' && (
            <div className="text-center p-8">
              <XCircle className="w-12 h-12 mx-auto text-red-500 mb-4" />
              <p className="text-red-600">Invalid or unrecognized QR code</p>
            </div>
          )}
        </div>
      </div>

      {/* Manual Entry */}
      <div className="bg-white rounded-lg shadow-sm p-6">
        <h2 className="text-lg font-medium text-gray-900 mb-4">Manual Entry</h2>
        <div className="space-y-4">
          <div>
            <label htmlFor="memberId" className="block text-sm font-medium text-gray-700">
              Member ID
            </label>
            <input
              type="text"
              id="memberId"
              className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
              placeholder="Enter member ID"
            />
          </div>
          <button className="w-full inline-flex justify-center items-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700">
            <User className="w-4 h-4 mr-2" />
            Mark Attendance
          </button>
        </div>
      </div>

      {/* Recent Scans */}
      <div className="bg-white rounded-lg shadow-sm p-6">
        <h2 className="text-lg font-medium text-gray-900 mb-4">Recent Scans</h2>
        <div className="space-y-4">
          {[1, 2, 3].map((scan) => (
            <div key={scan} className="flex items-center justify-between p-4 bg-gray-50 rounded-lg">
              <div className="flex items-center">
                <div className="w-10 h-10 bg-gray-200 rounded-full flex items-center justify-center">
                  <User className="w-6 h-6 text-gray-500" />
                </div>
                <div className="ml-4">
                  <p className="text-sm font-medium text-gray-900">Member #{scan}</p>
                  <p className="text-xs text-gray-500">Scanned 2 minutes ago</p>
                </div>
              </div>
              <CheckCircle className="w-5 h-5 text-green-500" />
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default QRScanner;