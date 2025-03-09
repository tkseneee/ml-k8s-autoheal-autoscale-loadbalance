# ML Model Deployment with Kubernetes: Autoheal, Autoscale & Load Balancing  

This repository demonstrates deploying a **Machine Learning (ML) model** using **FastAPI** and Kubernetes, showcasing capabilities such as **auto-healing, auto-scaling, and load balancing**. The model predicts the class of an **Iris flower** based on input features.  

## 🚀 Features  
✅ **Containerized ML App** using FastAPI and Docker  
✅ **Kubernetes Deployment** with YAML manifests  
✅ **Auto-healing**: Kubernetes recreates failed pods  
✅ **Auto-scaling**: Horizontal Pod Autoscaler (HPA) scales based on CPU usage  
✅ **Load Balancing**: Kubernetes LoadBalancer service distributes traffic  
✅ **Load Testing**: Simulates **5000 requests** to test scalability  

---

## 📂 Project Structure  
```bash
.
├── Dockerfile                  # Docker configuration for containerizing the ML app
├── README.md                    # Project documentation (this file)
├── app.py                        # FastAPI application for serving the ML model
├── iris_model.pkl                # Trained model file (pickle format)
├── kubernetes_steps.txt          # Kubernetes commands used in the session
├── load_test.py                  # Script to send multiple requests for load testing
├── ml-deployment.yaml            # Kubernetes deployment manifest
├── ml-service.yaml               # Kubernetes service manifest
├── train_model.py                # Script to train and save the ML model
├── requirements.txt              # Python dependencies
```

---

## 🛠️ Setup Instructions  

### 1️⃣ **Train the Model**  
Before deploying, generate the model (`iris_model.pkl`) using:  
```bash
python train_model.py
```

### 2️⃣ **Build and Run Docker Container**  
```bash
docker build -t ml-api .
docker tag ml-api ml-api:latest
```

### 3️⃣ **Deploy the ML App in Kubernetes**  
Ensure Kubernetes is running and apply the deployment and service:  
```bash
kubectl apply -f ml-deployment.yaml
kubectl apply -f ml-service.yaml
```

### 4️⃣ **Check Deployment Status & Exposed Port**  
```bash
kubectl get pods
kubectl get svc -A  # Get service details including exposed port
```

### 5️⃣ **Test the API**  
Once deployed, test the model API with a sample request:  
```bash
curl -X POST "http://localhost:<port>/predict" -H "Content-Type: application/json" -d "{\"features\": [5.1, 3.5, 1.4, 0.2]}"
```

---

## 📈 **Enable Auto-Scaling**  
Configure **Horizontal Pod Autoscaler (HPA)** to scale based on CPU usage:  
```bash
kubectl autoscale deployment ml-deployment --cpu-percent=50 --min=1 --max=5
```

Verify the scaling status:  
```bash
kubectl get hpa
```

---

## 🔄 **Simulate Auto-Healing**  
Delete a running pod and watch Kubernetes recreate it automatically:  
```bash
kubectl delete pod <pod-name>
kubectl get pods  # New pod will be created
```

---

## 🌍 **Test Load Balancing & Auto-Scaling**  
Run the load testing script (`load_test.py`) in a separate terminal to send **5000 requests**:  
```bash
python load_test.py
```
Monitor the pod scaling in real-time:  
```bash
kubectl get pods -w
```

---

## 🛑 **Clean Up Deployment**  
To delete all resources and stop the application:  
```bash
kubectl delete deployment ml-deployment
kubectl delete service ml-service
```

---

## 🚀 **Next Steps**  
🔹 Deploy the setup on **cloud-managed Kubernetes services** like **AWS EKS, Azure AKS, or Google GKE** for production scalability.  

---

## 📌 **Author**  
👨‍💻 **Dr T.K.Senthil Kumar**  
📧 tkseneee@gmail.com  
🔗 www.linkedin.com/in/drtksenthil

---

This repository is designed to help **Data Scientists and MLOps engineers** understand **how Kubernetes enhances ML application deployment** by adding **scalability, resilience, and efficient resource management**. 🚀  

Happy Deploying! 🚀⚡  

#Kubernetes #MLOps #MachineLearning #FastAPI #AutoScaling #LoadBalancing #Docker

