# Semantic Nexus

## Overview

**Semantic Nexus** is a comprehensive search engine and information retrieval application designed to enhance user search experience with advanced features. The application integrates voice search capabilities, AI-generated responses, and reference provision to streamline the search process and deliver a user-friendly interface. Built using Docker, this project ensures consistent and scalable deployment.

### Features

- **Voice Search**: Utilize voice recognition to search for information hands-free.
- **AI-Generated Responses**: Receive concise summaries and relevant insights generated by AI based on your search query.
- **Search Engine**: Perform detailed searches with robust filtering and sorting options.
- **Reference Provision**: Access detailed references and links related to your search results in a well-organized card view.

### Demo Video

https://github.com/user-attachments/assets/644a8b87-7348-4130-a974-f89276f6c9ab




## Technologies Used

- **Programming Language**: JavaScript (React) for frontend, Python (FastAPI) for backend
- **Libraries and Frameworks**:
  - React for building the user interface
  - FastAPI for creating the backend API
  - Docker for containerization
  - Web Speech API for voice search functionality
  - Custom AI model for generating responses

## Installation

To get started with Semantic Nexus, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Akshitkt001/SemanticNexus.git
   cd SemanticNexus


## Set Up Backend

Navigate to the backend directory and set up the environment:
1. **Clone the Repository**

   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   Start the FastAPI server:


   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   Set Up Frontend
   Navigate to the frontend directory and install dependencies:


   cd ../frontend
   npm install
   Start the React development server:

   npm start
   Run Docker Containers
   Ensure Docker is installed and running. Use Docker Compose to set  up and run the containers:

   docker-compose up

## Usage

### Open the Application

Launch the frontend application by navigating to [http://localhost:3000](http://localhost:3000) in your web browser. The application will present the following components:

- **Search Bar**: Allows users to enter search queries manually or use voice search.
- **AI Response Section**: Displays a summary generated by the AI based on the search query.
- **Search Results**: Shows detailed results in a card view format, providing organized references and links.

### Perform a Search

- **Voice Search**: Click the microphone icon to start voice recognition and speak your query.
- **Text Search**: Enter your query into the search bar and press Enter or click the search button.

### View Results

The results will be displayed in cards, each providing relevant information and links. The AI-generated response will summarize the main points based on the search query.

## API Documentation

### Endpoints

- **/search**: Performs a search based on the query and returns results and AI-generated response.
  - **Method**: GET
  - **Parameters**:
    - `q`: The search query.

### Examples

For detailed API usage examples, refer to the FastAPI documentation.


## Docker Setup

The project uses Docker to ensure a consistent development and deployment environment. Make sure Docker and Docker Compose are installed. Use the following commands to manage the Docker containers:

- **Build Docker Images:**

  ```bash
  docker-compose build

- **Start Containers:**

  ```bash
  docker-compose up

- **Stop Containers:**

  ```bash
  docker-compose down 

## Contributing

Contributions to Semantic Nexus are welcome! If you find a bug or want to add a new feature, please follow these steps:

1. **Fork the repository.**
2. **Create a new branch** (e.g., `git checkout -b feature/your-feature`).
3. **Make your changes.**
4. **Commit your changes** (e.g., `git commit -am 'Add new feature'`).
5. **Push to the branch** (e.g., `git push origin feature/your-feature`).
6. **Create a new Pull Request.**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or issues, please contact:

- **Akshit Kumar Tiwari** - [GitHub Profile](https://github.com/Akshitkt001)
- **Email**: [akstiwari307@gmail.com]
