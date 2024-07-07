# Use the official Bun image as the base
FROM oven/bun:latest as builder

# Set the working directory
WORKDIR /app

# Copy package.json and bun.lockb (if you have one)
COPY package.json bun.lockb* ./

# Install dependencies
RUN bun install --frozen-lockfile

# Copy the rest of the application code
COPY . .

# Build the Nuxt application
RUN bun run build

# Use a lightweight Node.js image for the final stage
FROM node:alpine

# Set the working directory
WORKDIR /app

# Copy the built application from the builder stage
COPY --from=builder /app/.output ./

# Expose the port the app runs on
EXPOSE 3000

# Set the command to run the application
CMD ["node", "server/index.mjs"]
