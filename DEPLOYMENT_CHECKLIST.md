# ✅ PythonAnywhere Deployment Checklist

## 📋 Pre-Deployment Checklist

- [ ] **PythonAnywhere Account**: Created and verified
- [ ] **GitHub Repository**: Code pushed to GitHub
- [ ] **All Files Present**: 
  - [ ] `app.py`
  - [ ] `requirements.txt`
  - [ ] `wsgi.py`
  - [ ] `templates/index.html`
  - [ ] `static/css/style.css`
  - [ ] `static/js/script.js`

## 🚀 Deployment Steps

### Step 1: Upload Code
- [ ] **Option A (Git)**: Clone repository in PythonAnywhere console
- [ ] **Option B (Manual)**: Upload files via Files tab

### Step 2: Install Dependencies
- [ ] Run: `pip3 install --user -r requirements.txt`

### Step 3: Configure Web App
- [ ] Create new web app (Manual configuration)
- [ ] Set source code path: `/home/YOUR_USERNAME/Amazon_Clone`
- [ ] Set working directory: `/home/YOUR_USERNAME/Amazon_Clone`

### Step 4: Configure WSGI
- [ ] Update WSGI file with correct path
- [ ] Replace `YOUR_USERNAME` with actual username

### Step 5: Set Environment Variables
- [ ] `FLASK_ENV`: `production`
- [ ] `SECRET_KEY`: `your-secret-key-change-this`

### Step 6: Deploy
- [ ] Click "Reload" in Web tab
- [ ] Wait for reload to complete

## 🧪 Testing Checklist

- [ ] **Website loads**: No 500 errors
- [ ] **Static files**: CSS and JS load correctly
- [ ] **Products display**: All products visible
- [ ] **Search works**: Can search for products
- [ ] **Filters work**: Category and brand filters function
- [ ] **Cart functionality**: Can add/remove items
- [ ] **Responsive design**: Works on mobile

## 🔧 Troubleshooting

### Common Issues:
- [ ] **Import errors**: Check WSGI file path
- [ ] **Static files not loading**: Verify file locations
- [ ] **500 errors**: Check error logs
- [ ] **Dependencies missing**: Reinstall requirements

### Error Logs:
- [ ] Check Web tab → Error log
- [ ] Check Web tab → Server log

## 📈 Post-Deployment

- [ ] **Test all features**
- [ ] **Share your URL**: `https://YOUR_USERNAME.pythonanywhere.com`
- [ ] **Monitor for errors**
- [ ] **Update as needed**

## 🎉 Success!

Your Amazon Clone is now live at:
`https://YOUR_USERNAME.pythonanywhere.com`

---

**Need help?** See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.
