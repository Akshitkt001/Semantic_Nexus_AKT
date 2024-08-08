# Use the official Node.js image
FROM node:18-slim

# Set the working directory
WORKDIR /usr/src/app

# Copy package.json and package-lock.json into the container
COPY package*.json ./

# Install the dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Specify the command to run your application
CMD ["node", "server.js"]

# Expose the port on which the API Gateway will run
EXPOSE 3000
