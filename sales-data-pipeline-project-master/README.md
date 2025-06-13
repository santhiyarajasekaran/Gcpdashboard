# Web Portal to Upload Files to Google Cloud Storage with Dashboard Visualization

This is a web application built with **Flask** that allows users to upload CSV files. The uploaded files are stored in a **Google Cloud Storage (GCS)** bucket. A **Cloud Function** then automatically loads the data into **BigQuery**, which is visualized using **Looker Studio dashboards**.

## 💻 Run Locally in Visual Studio Code (VS Code)

### ✅ Prerequisites

- Python 3.x installed
- Google Cloud SDK installed and authenticated
- A GCP project with:
  - Cloud Storage
  - BigQuery
  - Cloud Functions
- VS Code with Python extension

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Open in VS Code

- Launch **Visual Studio Code**
- Open the project folder:  
  `File > Open Folder > [your-project-folder]`

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables (Optional for dev)

Create a `.env` file or set variables in `app.py`:

```env
GCP_PROJECT_ID=your-project-id
GCS_BUCKET_NAME=your-bucket-name
```

### 5. Run the Flask App

```bash
python app.py
```

Open your browser and go to `http://127.0.0.1:5000`

---

## 🌐 Features

- Login and file upload through web portal
- Store files in Google Cloud Storage
- Trigger Google Cloud Function on new file upload
- Load CSV data into BigQuery
- Visualize uploaded data in Looker Studio

---

## ☁️ GCP Setup (Summary)

1. Create a **Cloud Storage bucket**
2. Create a **BigQuery dataset and table**
3. Deploy a **Cloud Function** that:
   - Triggers on new file in GCS
   - Reads CSV and loads into BigQuery
4. Connect BigQuery to **Looker Studio** for dashboards

## 📁 Project Structure

```
├── app.py                  # Flask application
├── templates/
│   └── index.html          # Upload UI
├── cloud_function/
│   └── main.py             # GCP Function to load into BigQuery
├── requirements.txt        # Dependencies
└── README.md
```

---
