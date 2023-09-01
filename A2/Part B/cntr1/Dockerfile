# Base image
FROM node:14-alpine

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy app source code
COPY . .

# Build the app
RUN npm run build

# Set environment variables
ENV NODE_ENV=production

# Expose port (change it to the appropriate port used by your React app)
EXPOSE 3000

# Start the app
CMD [ "npm", "start" ]
