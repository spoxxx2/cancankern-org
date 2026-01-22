# Use a lightweight Linux base
FROM debian:bullseye-slim

# Install dependencies for C++, Python, and JSON processing
RUN apt-get update && apt-get install -y \
    g++ \
    python3 \
    python3-pip \
    jq \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy your hardwired strategy files
COPY aud_engine.cpp .
COPY strategy.cpp .

# Compile the engines during the build process
RUN g++ -o aud_engine aud_engine.cpp && \
    g++ -o strategy_manifest strategy.cpp

# Set the organization branding
ENV ORG="CanCan Kern"
ENV SITE="cancankern.org"

# Default command: show the strategy manifest
CMD ["./strategy_manifest"]
