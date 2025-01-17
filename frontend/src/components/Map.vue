<script setup>
const props = defineProps(['lat', 'lng'])
</script>

<script>
import 'ol/ol.css';
import {Feature, Map, View} from 'ol';
import TileLayer from 'ol/layer/Tile';
import OSM from 'ol/source/OSM';
import {fromLonLat, useGeographic} from "ol/proj.js";
import VectorSource from "ol/source/Vector.js";
import {Point} from "ol/geom.js";
import {Icon, Style} from "ol/style.js";
import VectorLayer from "ol/layer/Vector.js";

export default {
  data() {
    return {
      map: null,
      view: null,
      markerLayer: null,
      socket: null, // Add socket property
    };
  },
  mounted() {
    useGeographic();
    this.initMap();
    this.placeMarker();
    this.setupWebsocket(); // Initialize WebSocket connection
  },
  methods: {
    initMap() {
      this.view = new View({
        center: [this.lng, this.lat],
        zoom: 2,
      });

      this.map = new Map({
        target: this.$refs.mapContainer,
        layers: [
          new TileLayer({
            source: new OSM(),
          }),
        ],
        view: this.view,
      });
    },
    placeMarker() {
      const markerSource = new VectorSource();

      const markerFeature = new Feature({
        geometry: new Point([this.lng, this.lat]),
      });

      markerFeature.setStyle(
        new Style({
          image: new Icon({
            anchor: [0.5, 1],
            src: "https://cdn-icons-png.flaticon.com/512/684/684908.png",
            scale: 0.1,
          }),
        })
      );

      markerSource.addFeature(markerFeature);

      this.markerLayer = new VectorLayer({
        source: markerSource,
      });

      this.map.addLayer(this.markerLayer);
    },
    updateMapCenter() {
      // Focus on the note coordinates when the coordinates load
      if (this.view) {
        this.view.setCenter([this.lng, this.lat]);
        this.view.setZoom(17);
      }
      this.updateMarker();
    },
    updateMarker() {
      if (this.markerLayer) {
        this.map.removeLayer(this.markerLayer);
      }
      this.placeMarker();
    },
    setupWebsocket() {
      // const websocketURL = URLService.getWebSocketURL();
      let websocketURL = "http://127.0.0.1:8000"
      this.socket = new WebSocket(`${websocketURL}/notes/ws`);

      this.socket.onmessage = (event) => {
        const data = JSON.parse(event.data);
        console.log("WebSocket event:", data.action);

        if (["created", "updated", "deleted"].includes(data.action)) {
          // Assuming the data contains new lat/lng for the marker
          this.lng = data.lng; // Update lng from the received data
          this.lat = data.lat; // Update lat from the received data
          this.updateMapCenter(); // Update the map center and marker
        }
      };

      this.socket.onopen = () => console.log("WebSocket connected");
      this.socket.onclose = () => {
        console.log("WebSocket disconnected. Reconnecting...");
        setTimeout(this.setupWebsocket, 5000); // Automatic reconnection
      };
      this.socket.onerror = (error) => console.error("WebSocket error:", error);
    },
  },
  watch: {
    lat: "updateMapCenter",
    lng: "updateMapCenter",
  },
};
</script>

<template>
  <div class="mapDiv">
    <div id="map" class="map" ref="mapContainer" style="width: 95%; height: 300px;"></div>
  </div>

  <div class="flexContainer">
    <div class="coordinates">
      <p> lat: {{ lat }} | lng: {{ lng }}</p>
    </div>
  </div>
</template>

<style scoped>
.coordinates {
  display: flex;
  justify-content: center;
  width: 95%;
  max-width: 350px;
  background: #b1f3b1;
  border-radius: 10px;
  padding: 6px;
}

.flexContainer {
  margin-top: 6px;
  display: flex;
  justify-content: center;
}

.mapDiv {
  margin-top: 12px;
  display: flex;
  justify-content: center;
}

.map {
  border: 3px solid #0a6300;
  max-width: 500px;
  border-radius: 16px;
  overflow: hidden;
}
</style>