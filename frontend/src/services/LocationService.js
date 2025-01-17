
class LocationService {
    getUserLocation(func) {
        let location = {lat: 1, lng: 2}

        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                (position) => {
                    location.lat = position.coords.latitude;
                    location.lng = position.coords.longitude;
                    func(location) // Reset any previous error
                },
                (error) => {
                    switch (error.code) {
                        case error.PERMISSION_DENIED:
                            console.error("User denied the request for Geolocation.")
                            break;
                        case error.POSITION_UNAVAILABLE:
                            console.error("Location information is unavailable.")
                            break;
                        case error.TIMEOUT:
                            console.error("The request to get user location timed out.")
                            break;
                        default:
                            console.error("An unknown error occurred.")
                            break;
                    }
                },
                {enableHighAccuracy: true}
            );
        } else {
            console.error("Geolocation is not supported by this browser.")
        }
    }
}

export default new LocationService();