# 🚀 Streamlit Cloud Deployment Guide

## Deploy Your Manufacturer Finder Tool to Streamlit Cloud

This guide will help you deploy your professional Manufacturer Finder application to Streamlit Cloud for easy access from anywhere.

---

## 📋 Prerequisites

Before deploying, ensure you have:

✅ A GitHub account  
✅ Your OpenAI API key  
✅ This project uploaded to a GitHub repository

---

## 🎯 Quick Deployment Steps

### Step 1: Push Code to GitHub

1. **Create a new GitHub repository** (if you haven't already)

2. **Initialize git and push your code**:

```bash
cd "/Users/abhinav/Desktop/DynaPrice Internship/Manufacturing tool"

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - Manufacturer Finder Tool"

# Add remote (replace with your GitHub repo URL)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Push to GitHub
git push -u origin main
```

**Important**: Make sure `.gitignore` is properly set up to exclude:
- `secrets.toml` (contains your API key)
- `*.xlsx` files (analysis results)
- `__pycache__/`
- `.env`

---

### Step 2: Deploy on Streamlit Cloud

1. **Go to Streamlit Cloud**:
   - Visit https://share.streamlit.io/
   - Sign in with your GitHub account

2. **Click "New app"**

3. **Configure your deployment**:
   ```
   Repository: YOUR_USERNAME/YOUR_REPO_NAME
   Branch: main
   Main file path: app.py
   App URL: choose a custom URL (e.g., manufacturer-finder)
   ```

4. **Click "Deploy"**

---

### Step 3: Configure Secrets (API Key)

**Critical**: You need to add your OpenAI API key to Streamlit Cloud secrets.

1. In Streamlit Cloud, go to your app's settings (⚙️ icon)

2. Navigate to **"Secrets"** section

3. Add your secrets in TOML format:

```toml
OPENAI_API_KEY = "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"
```

4. Click **"Save"**

5. Your app will automatically restart with the new configuration

---

## 🎨 Your Deployed App Features

Once deployed, your app will have:

✅ **Professional corporate UI** with gradient headers  
✅ **Secure API key handling** (stored in Streamlit secrets)  
✅ **Three main tabs**:
   - 📤 Upload & Analyze
   - 📊 Results Dashboard
   - 📈 Analytics

✅ **Real-time progress tracking**  
✅ **Excel report downloads**  
✅ **Responsive design** for all screen sizes

---

## 🔒 Security Best Practices

### ✅ DO:
- Store API keys in Streamlit Cloud secrets
- Use the `.gitignore` file provided
- Regularly rotate API keys
- Monitor API usage on OpenAI dashboard

### ❌ DON'T:
- Commit `secrets.toml` to GitHub
- Hardcode API keys in your code
- Share your API keys publicly
- Push temporary Excel files to GitHub

---

## 🛠️ Local Testing Before Deployment

Test your app locally before deploying:

```bash
# Make sure you're in the project directory
cd "/Users/abhinav/Desktop/DynaPrice Internship/Manufacturing tool"

# Create local secrets file
cp .streamlit/secrets.toml.example .streamlit/secrets.toml

# Edit secrets.toml and add your API key
nano .streamlit/secrets.toml

# Run the app
streamlit run app.py
```

Your app will open at http://localhost:8501

---

## 📊 Accessing Environment Variables in Code

The app is configured to read the API key from Streamlit secrets:

```python
# In app.py, this automatically works:
api_key = st.secrets.get("OPENAI_API_KEY", os.getenv('OPENAI_API_KEY', ''))
```

**Priority order**:
1. Streamlit Cloud secrets (production)
2. Environment variables (local development)
3. Manual input in UI (user override)

---

## 🔧 Updating Your Deployed App

To update your app after making changes:

```bash
# Make your code changes

# Commit and push to GitHub
git add .
git commit -m "Update app features"
git push origin main
```

Streamlit Cloud will **automatically redeploy** your app within minutes!

---

## 📱 Sharing Your App

Once deployed, you'll get a URL like:
```
https://YOUR-APP-NAME.streamlit.app
```

Share this URL with:
- ✅ Your team members
- ✅ Stakeholders
- ✅ Procurement department
- ✅ Management

The app is **publicly accessible** by default. To restrict access:
- Use Streamlit Cloud's authentication features (available in paid plans)
- Or implement custom authentication in your app

---

## 🐛 Troubleshooting

### Problem: App crashes on startup
**Solution**: Check Streamlit Cloud logs for error messages. Common issues:
- Missing dependencies in `requirements.txt`
- Missing API key in secrets
- Syntax errors in code

### Problem: API key not working
**Solution**: 
1. Verify the API key is correctly added in Streamlit secrets
2. Check for extra spaces or line breaks
3. Ensure the key has sufficient credits in OpenAI

### Problem: File upload not working
**Solution**: 
- Streamlit Cloud has file size limits (200MB default)
- For larger files, consider pagination or batch processing

### Problem: Slow performance
**Solution**:
- The free tier has resource limits
- Consider upgrading to Streamlit Cloud Pro for better performance
- Optimize your code (reduce API calls, cache results)

---

## 💰 Cost Considerations

### Streamlit Cloud:
- **Free tier**: Perfect for testing and light use
- **Pro tier** ($20/month): Better performance, custom domains, authentication

### OpenAI API:
- **GPT-4-mini**: ~$0.15 per 1000 parts analyzed
- Monitor usage at https://platform.openai.com/usage

**Example costs**:
- 100 parts analysis: ~$1.50
- 1,000 parts analysis: ~$15
- 10,000 parts analysis: ~$150

---

## 📞 Support & Resources

- **Streamlit Docs**: https://docs.streamlit.io/
- **Streamlit Cloud Docs**: https://docs.streamlit.io/streamlit-community-cloud
- **OpenAI API Docs**: https://platform.openai.com/docs
- **GitHub Issues**: Report problems in your repository

---

## ✅ Deployment Checklist

Before going live, verify:

- [ ] Code pushed to GitHub
- [ ] `.gitignore` excludes sensitive files
- [ ] `requirements.txt` is up to date
- [ ] API key added to Streamlit secrets
- [ ] App tested locally
- [ ] App deployed successfully
- [ ] API key verified in production
- [ ] Test upload and analysis works
- [ ] Share URL with team
- [ ] Monitor initial usage
- [ ] Set up OpenAI usage alerts

---

## 🎉 You're Ready!

Your professional Manufacturer Finder tool is now deployed and accessible from anywhere!

**Your deployment URL**: `https://[your-app-name].streamlit.app`

**Next steps**:
1. Test the deployed app thoroughly
2. Share with your team
3. Gather feedback
4. Iterate and improve

---

**Deployed by DynaPrice | Manufacturing Intelligence Solutions**

