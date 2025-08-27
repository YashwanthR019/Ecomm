# 🚀 Deployment Guide - PythonAnywhere

This guide will help you deploy your Amazon Clone Flask application to PythonAnywhere.

## 📋 Prerequisites

1. **PythonAnywhere Account**: Sign up at [www.pythonanywhere.com](https://www.pythonanywhere.com)
2. **GitHub Repository**: Your code should be in a GitHub repository
3. **Basic Git Knowledge**: Understanding of basic Git commands

## 🎯 Step-by-Step Deployment

### Step 1: Sign Up for PythonAnywhere

1. Go to [www.pythonanywhere.com](https://www.pythonanywhere.com)
2. Click "Create a Beginner account" (Free tier)
3. Complete the registration process
4. Verify your email address

### Step 2: Access Your PythonAnywhere Dashboard

1. Log in to your PythonAnywhere account
2. You'll see your dashboard with various tools

### Step 3: Upload Your Code

#### Option A: Using Git (Recommended)

1. **Open a Bash Console**:
   - Click on "Consoles" in your dashboard
   - Click "New Console" → "Bash"

2. **Clone Your Repository**:
   ```bash
   cd ~
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git Amazon_Clone
   cd Amazon_Clone
   ```

3. **Verify Files**:
   ```bash
   ls -la
   ```
   You should see: `app.py`, `requirements.txt`, `wsgi.py`, `templates/`, `static/`

#### Option B: Using File Upload

1. **Open Files Tab**:
   - Click on "Files" in your dashboard
   - Navigate to your home directory

2. **Upload Files**:
   - Upload all your project files
   - Create folders for `templates` and `static`

### Step 4: Install Dependencies

1. **Open a Bash Console** (if not already open)
2. **Navigate to your project**:
   ```bash
   cd ~/Amazon_Clone
   ```

3. **Install Requirements**:
   ```bash
   pip3 install --user -r requirements.txt
   ```

### Step 5: Configure WSGI File

1. **Open Files Tab**
2. **Navigate to** `/var/www/YOUR_USERNAME_pythonanywhere_com_wsgi.py`
3. **Replace the content** with:

```python
import sys
import os

# Add your project directory to the Python path
path = '/home/YOUR_USERNAME/Amazon_Clone'
if path not in sys.path:
    sys.path.append(path)

# Import your Flask app
from app import app as application
```

**Important**: Replace `YOUR_USERNAME` with your actual PythonAnywhere username.

### Step 6: Configure Web App

1. **Go to Web Tab**:
   - Click on "Web" in your dashboard

2. **Add a New Web App**:
   - Click "Add a new web app"
   - Choose "Manual configuration"
   - Select Python version (3.9 or 3.10 recommended)

3. **Configure Source Code**:
   - **Source code**: `/home/YOUR_USERNAME/Amazon_Clone`
   - **Working directory**: `/home/YOUR_USERNAME/Amazon_Clone`

4. **Configure WSGI File**:
   - Click on the WSGI configuration file link
   - Replace the content with the code from Step 5

### Step 7: Set Environment Variables

1. **In the Web tab**, scroll down to "Environment variables"
2. **Add these variables**:
   - `FLASK_ENV`: `production`
   - `SECRET_KEY`: `your-secret-key-change-this`

### Step 8: Reload Your Web App

1. **Go back to Web tab**
2. **Click "Reload"** button
3. **Wait for the reload to complete**

### Step 9: Test Your Application

1. **Click on your website URL** (usually `YOUR_USERNAME.pythonanywhere.com`)
2. **Test all features**:
   - Browse products
   - Search functionality
   - Add items to cart
   - Filter products

## 🔧 Troubleshooting

### Common Issues:

1. **Import Errors**:
   - Check that all files are in the correct location
   - Verify the path in your WSGI file

2. **Static Files Not Loading**:
   - Ensure `static/` folder is in the correct location
   - Check file permissions

3. **Template Errors**:
   - Ensure `templates/` folder is in the correct location
   - Check template syntax

4. **500 Internal Server Error**:
   - Check the error logs in the Web tab
   - Verify all dependencies are installed

### Error Logs:

1. **Go to Web tab**
2. **Click on "Error log"** to see detailed error messages
3. **Check "Server log"** for additional information

## 📈 Updating Your Application

### To update your deployed app:

1. **Pull latest changes** (if using Git):
   ```bash
   cd ~/Amazon_Clone
   git pull origin main
   ```

2. **Install new dependencies** (if any):
   ```bash
   pip3 install --user -r requirements.txt
   ```

3. **Reload your web app**:
   - Go to Web tab
   - Click "Reload"

## 🔒 Security Considerations

1. **Change the secret key** in production
2. **Use environment variables** for sensitive data
3. **Keep dependencies updated**
4. **Monitor error logs regularly**

## 📞 Support

- **PythonAnywhere Help**: [help.pythonanywhere.com](https://help.pythonanywhere.com)
- **Flask Documentation**: [flask.palletsprojects.com](https://flask.palletsprojects.com)

## 🎉 Success!

Once deployed, your Amazon Clone will be accessible at:
`https://YOUR_USERNAME.pythonanywhere.com`

Your e-commerce site is now live on the internet! 🚀
