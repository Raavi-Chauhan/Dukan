**Project Overview**

This project aims to Deploy the Web application of Django using Devops Culture.

**Features**

- **User-Friendly Interface**: A simple and intuitive web interface for the customer for shopping.
- **Continuous Integration/Continuous Deployment (CI/CD)**: Automated deployment pipeline using Git, Jenkins, Docker, and Kubernetes.

#### Technologies Used

- **Python**: The core programming language used for the project.
- **Django**: For building the web application.
- **Docker**: For containerizing the application.
- **Jenkins**: For automating the CI/CD pipeline.
- **Kubernetes**: For deploying and managing containerized applications in a clustered environment.
- **Git**: For version control and source code management.

#### Deployment

The project includes a Jenkinsfile and Dockerfile to automate the build, test, and deployment processes. The CI/CD pipeline ensures that every change is tested and deployed seamlessly.

1. **Jenkins Pipeline Setup**
   - Set up Jenkins with necessary plugins for Git, Docker, and Kubernetes.
   - Create a Jenkins job pipeline and point it to the repository.

2. **Docker Setup**
   - Build the Docker image.
   - Run the Docker container.

3. **Kubernetes Deployment**
   - Create Kubernetes deployment and service files.
   - Deploy to the Kubernetes cluster.

#### Usage

1. Navigate to the application URL.

#### Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

#### Acknowledgments

- Special thanks to Anurag from which I get the web application.
- Thanks to the open-source community for the tools and libraries that made this project possible.
