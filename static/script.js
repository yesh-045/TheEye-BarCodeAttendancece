// Global variable to track whether the QR code has been scanned
let scanning = true;

function fetchQRData() {
    if (!scanning) return;

    fetch('/qrdata')
        .then(response => response.json())
        .then(data => {
            if (data.qr_data) {
                // Display QR code data as a pop-up
                alert('QR Code Data: ' + data.qr_data);

                // Ask the user if they want to scan again
                let scanAgain = confirm('Do you want to scan again?');

                if (!scanAgain) {
                    // Stop scanning by sending a request to close the camera
                    scanning = false;
                    fetch('/stop_scan');
                }
            }
        });
}

// Call the fetchQRData function every 3 seconds to check for new QR data
setInterval(fetchQRData, 3000); // 3000ms = 3 seconds
