# Build-Stage
FROM node:18 AS build

# Set working directory
WORKDIR /app

# Copy package files
COPY package.json package-lock.json ./

COPY http-client ./http-client

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the Vue.js application
RUN npm run build

# Production-Stage
FROM nginx:alpine

# Copy built files to nginx
COPY --from=build /app/dist /usr/share/nginx/html

# Copy nginx configuration to enable connection with the backend
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80
EXPOSE 80

# Start nginxd
CMD ["nginx", "-g", "daemon off;"]