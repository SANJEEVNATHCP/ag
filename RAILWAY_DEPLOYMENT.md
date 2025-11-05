# Railway Deployment Guide for Hugafu Backend

This guide will help you deploy the Hugafu Flask backend on Railway.

## 🚀 Quick Deployment Steps

### 1. Prerequisites
- GitHub account
- Railway account (sign up at [railway.app](https://railway.app))
- Your code pushed to GitHub

### 2. Deploy to Railway

#### Option A: Deploy from GitHub (Recommended)

1. **Go to Railway Dashboard**
   - Visit [railway.app](https://railway.app)
   - Click "Start a New Project"

2. **Connect GitHub Repository**
   - Select "Deploy from GitHub repo"
   - Authorize Railway to access your repositories
   - Select your `hugafu` repository
   - Railway will auto-detect it's a Python project

3. **Configure Environment Variables**
   Click on your service → Variables → Add the following:

   ```
   SECRET_KEY=your-secret-key-here
   OPENAI_API_KEY=your-openai-api-key
   GOOGLE_API_KEY=your-google-api-key
   ALLOWED_ORIGINS=https://your-netlify-app.netlify.app
   FLASK_ENV=production
   PORT=8000
   ```

4. **Deploy**
   - Railway will automatically build and deploy
   - Wait for deployment to complete (usually 2-5 minutes)

#### Option B: Deploy via Railway CLI

```bash
# Install Railway CLI
npm i -g @railway/cli

# Login to Railway
railway login

# Initialize project
railway init

# Link to existing project (or create new)
railway link

# Deploy
railway up
```

### 3. Post-Deployment Configuration

#### A. OneDrive Model Download
The app will automatically download the AI model from OneDrive on first startup using `download_model.py`.

#### B. Get Your Railway URL
- Go to your Railway dashboard
- Click on your service
- Find the URL under "Settings" → "Domains"
- It will look like: `https://your-app.railway.app`

#### C. Update Frontend
Update the `API_BASE_URL` in your Netlify frontend (`js/app.js`):
```javascript
const API_BASE_URL = 'https://your-app.railway.app';
```

#### D. Configure CORS
Add your Netlify URL to environment variables:
```
ALLOWED_ORIGINS=https://your-netlify-app.netlify.app,https://another-domain.com
```

### 4. Database Configuration

Railway automatically provides:
- **SQLite**: Already configured in the project
- **PostgreSQL** (Optional): Can be added as a Railway service

To add PostgreSQL:
1. Click "New" → "Database" → "PostgreSQL"
2. Railway will provide `DATABASE_URL`
3. Update your backend to use PostgreSQL instead of SQLite

## 📋 Configuration Files

### `railway.json`
- Defines build and deployment configuration
- Sets start command and health checks
- Configures restart policy

### `nixpacks.toml`
- Railway uses Nixpacks for builds
- Specifies Python version (3.13)
- Defines install and build phases
- Downloads model during build

### `Procfile`
- Fallback for Heroku-style deployment
- Defines web process with Gunicorn

### `runtime.txt`
- Specifies Python version
- Used by buildpacks

## 🔧 Environment Variables

Required variables:

| Variable | Description | Example |
|----------|-------------|---------|
| `SECRET_KEY` | Flask secret key | `your-random-secret-key-123` |
| `OPENAI_API_KEY` | OpenAI API key | `sk-...` |
| `GOOGLE_API_KEY` | Google Generative AI key | `AIza...` |
| `ALLOWED_ORIGINS` | CORS allowed origins | `https://app.netlify.app` |
| `FLASK_ENV` | Environment | `production` |
| `PORT` | Port number | `8000` (auto-set by Railway) |

Optional variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL URL | SQLite file |
| `FIREBASE_CREDS` | Firebase credentials JSON | Not set |
| `MAX_UPLOAD_SIZE` | Max file upload (MB) | `16` |

## 🎯 Project Structure

```
hugafu/
├── backend/              # Flask application
│   ├── app.py           # Main Flask app
│   ├── routes/          # API routes
│   ├── models/          # Database models
│   └── ai/              # AI modules
├── frontend/            # Templates (optional on Railway)
├── database/            # SQLite & Firebase config
├── wsgi.py             # Production entry point
├── requirements.txt    # Python dependencies
├── railway.json        # Railway configuration
├── nixpacks.toml       # Build configuration
├── Procfile            # Process definition
├── runtime.txt         # Python version
└── download_model.py   # Download AI model from OneDrive
```

## 🔍 Monitoring & Logs

### View Logs
1. Go to Railway dashboard
2. Click on your service
3. Go to "Deployments" tab
4. Click on latest deployment
5. View real-time logs

### Monitor Performance
- Railway provides metrics for CPU, memory, network
- Set up alerts for crashes or high resource usage

## 🐛 Troubleshooting

### Build Fails
- Check `requirements.txt` for incompatible packages
- Verify Python version in `runtime.txt` and `nixpacks.toml`
- Check Railway logs for specific error

### App Crashes After Deployment
- Check environment variables are set correctly
- Verify `SECRET_KEY` is configured
- Check logs for import errors or missing dependencies

### Model Download Fails
- Check OneDrive URL in `download_model.py`
- Verify the download link is accessible
- Check Railway build logs

### CORS Errors
- Verify `ALLOWED_ORIGINS` includes your Netlify URL
- Check frontend is using correct Railway URL
- Ensure no trailing slashes in URLs

### Database Issues
- SQLite works out of the box
- For PostgreSQL, ensure `DATABASE_URL` is set
- Check database file permissions

## 🔐 Security Best Practices

1. **Never commit secrets**
   - Use Railway environment variables
   - Add `.env` to `.gitignore`

2. **Use strong SECRET_KEY**
   ```bash
   python -c "import secrets; print(secrets.token_hex(32))"
   ```

3. **Configure CORS properly**
   - Only allow trusted domains
   - Don't use `*` in production

4. **Keep dependencies updated**
   ```bash
   pip list --outdated
   pip install --upgrade package-name
   ```

## 💰 Pricing

Railway offers:
- **Free Tier**: $5 of usage per month
- **Pro Plan**: Pay-as-you-go after free tier
- **Estimated cost**: ~$5-10/month for small apps

## 🔄 Continuous Deployment

Railway automatically redeploys when you push to GitHub:

1. Make changes to your code
2. Commit and push to GitHub
3. Railway detects changes and redeploys
4. Monitor deployment in Railway dashboard

## 📚 Additional Resources

- [Railway Documentation](https://docs.railway.app)
- [Railway Discord Community](https://discord.gg/railway)
- [Nixpacks Documentation](https://nixpacks.com)
- [Gunicorn Documentation](https://docs.gunicorn.org)

## ✅ Deployment Checklist

Before deploying:

- [ ] Code pushed to GitHub
- [ ] All environment variables documented
- [ ] `requirements.txt` up to date
- [ ] OneDrive model URL configured
- [ ] CORS origins configured
- [ ] Secret key generated
- [ ] Railway account created

After deploying:

- [ ] App accessible via Railway URL
- [ ] Health check passing
- [ ] Model downloaded successfully
- [ ] API endpoints responding
- [ ] Frontend connected to backend
- [ ] CORS working correctly
- [ ] Database initialized

## 🎉 Success!

Once deployed, your backend will be available at:
```
https://your-app.railway.app
```

Update your Netlify frontend to use this URL and you're ready to go! 🚀
