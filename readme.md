## Steps to containerization and container orchestration 

1. **Setup Dockerfiles and build images**

   Dockerfile is used to containerize your Django API. The Dockerfile specifies that the application will use the Python slim-buster image as the base image, copies the application to the `/app` directory, installs the requirements, switches to a non-root user for security, and finally runs the application using Gunicorn.

   To build the Docker image, navigate to the directory containing the Dockerfile and execute the following command:

   ```
   docker build . -t name-of-image
   ```


2. **Setup Kubernetes Environment**

   Install a Kubernetes distribution. The following set up was done using minikube

   In order to interact with the Kubernetes cluster, you will also need `kubectl` command-line tool.

3. **Setup PostgreSQL Deployment**

  Created Kubernetes manifest file that contains a Deployment for PostgreSQL. The Deployment ensures that one replica of PostgreSQL is always running. It uses a persistent volume claim to store data persistently.

   Create a Secret for the PostgreSQL credentials:

   ```
   kubectl create secret generic postgres-secret --from-literal=POSTGRES_DB=your-db-name --from-literal=POSTGRES_USER=your-user --from-literal=POSTGRES_PASSWORD=your-password
   ```

   Apply the PostgreSQL Deployment and Service by navigating to the directory containing the manifest file and running the following command:

   ```
   kubectl apply -f postgres-deployment.yaml
   ```

4. **Setup Django Deployment**

    Django application Deployment specifies 3 replicas, which means Kubernetes will ensure that 3 instances of your Django API are always running. 

   Create a Secret for the Django credentials:

   ```
   kubectl create secret generic django-secret --from-literal=SECRET_KEY=your-secret-key --from-literal=NAME=your-db-name --from-literal=USER=your-user --from-literal=PASSWORD=your-password
   ```

   Apply the Django Deployment and Service by navigating to the directory containing the manifest file and running the following command:

   ```
   kubectl apply -f django-deployment.yaml
   ```

5. **Run Migrations Job**

   Before the Django API can be used, you need to apply Django migrations. Your manifest file contains a Kubernetes Job that will run these migrations. 

   Apply the job with the following command:

   ```
   kubectl apply -f django-migrate-job.yaml
   ```

6. **Run Data Loader Job**

   After the migrations have been applied, you can load data into your application. You have another Kubernetes Job that loads users from a ConfigMap (kubectl apply -f users-script).

   Apply the job with the following command:

   ```
   kubectl apply -f data-loader-job.yaml
   ```

7. **Configurable Values**

   Below are the configurable values in setup:

   - PostgreSQL and Django Secrets (Database credentials and Django secret key)
   - Number of replicas in PostgreSQL and Django Deployments
   - Resources (requests and limits) for PostgreSQL and Django Pods
   - PersistentVolumeClaim size for PostgreSQL and Django
   - Docker images in Deployments and Jobs
   - Command in Jobs


