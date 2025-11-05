# Farmers App - Complete Agriculture Solution

A comprehensive web application for farmers featuring AI-powered disease detection, price prediction, marketplace, government schemes, and multi-language support.

## 🌟 Features

### 1. **Disease Detection** 🔬
- Upload plant images for instant AI-powered disease identification
- Uses pre-trained model (best_model.pth)
- Provides treatment recommendations and preventive measures
- Supports multiple plant diseases including:
  - Apple: Scab, Black Rot, Cedar Apple Rust
  - Tomato: Bacterial Spot, Early Blight, Late Blight
  - Potato: Early Blight, Late Blight

### 2. **Price Prediction** 📈
- Future price predictions for various crops
- Current market prices
- Price trend analysis
- Integrated with Kaggle visualization data
- Supports: Tomato, Potato, Onion, Apple, Banana, Mango, Rice, Wheat, etc.

### 3. **Marketplace** 🛒
- Buy and sell agricultural products
- Direct farmer-to-farmer transactions
- Product listing with images and pricing
- Category-based browsing
- Location-based search

### 4. **Government Schemes** 📋
- Complete information on agricultural schemes
- Eligibility checker
- Application guidelines
- Schemes included:
  - PM-KISAN
  - PMFBY (Crop Insurance)
  - Kisan Credit Card
  - Soil Health Card Scheme
  - PKVY (Organic Farming)
  - e-NAM
  - PMKSY (Irrigation)

### 5. **Farmer Profile** 👤
- User authentication and authorization
- Profile management
- Farm details tracking
- Crop information storage

### 6. **Multi-Language Support** 🌍
- English
- Hindi (हिन्दी)
- Tamil (தமிழ்)
- Expandable to more languages

### 7. **AI Chatbot** 💬
- Agricultural advisory chatbot
- Multi-language support
- Topics covered:
  - Disease management
  - Irrigation advice
  - Fertilizer recommendations
  - Weather information
  - Seed selection
  - Government schemes

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone or navigate to the project directory**
```bash
cd c:\Users\sanje\Documents\hugafu
```

2. **Create a virtual environment (recommended)**
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
copy .env.example .env
# Edit .env file with your configuration
```

5. **Initialize the database**
```bash
python -c "from app import app, db; app.app_context().push(); db.create_all()"
```

6. **Ensure best_model.pth is in the root directory**
The pre-trained disease detection model should be in the project root.

## 🏃‍♂️ Running the Application

1. **Start the Flask server**
```bash
python app.py
```

2. **Access the application**
Open your browser and navigate to:
```
http://localhost:5000
```

## 📁 Project Structure

```
hugafu/
├── app.py                      # Main Flask application
├── models.py                   # Database models
├── requirements.txt            # Python dependencies
├── best_model.pth             # Pre-trained disease detection model
├── .env.example               # Environment variables template
├── routes/
│   ├── disease_detection.py   # Disease detection endpoints
│   ├── price_prediction.py    # Price prediction endpoints
│   ├── marketplace.py         # Marketplace endpoints
│   ├── schemes.py             # Government schemes endpoints
│   ├── profile.py             # User profile endpoints
│   └── chatbot.py             # Chatbot endpoints
├── templates/
│   └── index.html             # Main frontend interface
└── uploads/                   # Uploaded images directory
```

## 🔌 API Endpoints

### Disease Detection
- `POST /api/disease/detect` - Detect disease from uploaded image
- `GET /api/disease/diseases` - Get all detectable diseases
- `GET /api/disease/disease/<disease_name>` - Get specific disease info

### Price Prediction
- `POST /api/price/predict` - Predict future prices
- `GET /api/price/market-prices` - Get current market prices
- `GET /api/price/crops` - Get available crops
- `POST /api/price/compare` - Compare prices across crops

### Marketplace
- `GET /api/marketplace/products` - List all products
- `POST /api/marketplace/products` - Create product listing
- `GET /api/marketplace/products/<id>` - Get product details
- `PUT /api/marketplace/products/<id>` - Update product
- `DELETE /api/marketplace/products/<id>` - Delete product

### Government Schemes
- `GET /api/schemes/all` - Get all schemes
- `GET /api/schemes/<id>` - Get specific scheme
- `POST /api/schemes/check-eligibility` - Check eligibility
- `GET /api/schemes/search?q=<query>` - Search schemes

### User Profile
- `POST /api/profile/register` - Register new user
- `POST /api/profile/login` - User login
- `GET /api/profile/me` - Get current user profile
- `PUT /api/profile/update` - Update profile
- `POST /api/profile/change-password` - Change password

### Chatbot
- `POST /api/chatbot/chat` - Chat with AgriBot
- `GET /api/chatbot/topics` - Get available topics
- `GET /api/chatbot/languages` - Get supported languages

## 🛠️ Technologies Used

- **Backend**: Flask (Python)
- **Database**: SQLite (SQLAlchemy ORM)
- **Machine Learning**: PyTorch, TorchVision
- **Frontend**: HTML, CSS, JavaScript
- **Authentication**: JWT (JSON Web Tokens)
- **Image Processing**: Pillow
- **Data Analysis**: Pandas, NumPy

## 📊 Database Models

- **User**: User authentication and basic info
- **FarmerProfile**: Detailed farmer information
- **Product**: Marketplace product listings
- **DiseaseDetection**: Disease detection history
- **ChatHistory**: Chatbot conversation history

## 🌐 Multi-Language Implementation

The application supports multiple languages through:
1. Language selector in the UI
2. Backend responses in selected language
3. Chatbot responses in user's preferred language

## 🔒 Security Features

- Password hashing using Werkzeug
- JWT-based authentication
- Secure file upload handling
- SQL injection prevention through ORM

## 🎯 Future Enhancements

- Mobile application (Android/iOS)
- Real-time weather integration
- GPS-based location services
- Payment gateway integration
- Push notifications
- Advanced analytics dashboard
- Community forum
- Video tutorials

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## 📝 License

This project is licensed for educational and agricultural development purposes.

## 📧 Support

For support and queries, please contact through the application's chatbot or raise an issue.

## 🙏 Acknowledgments

- Kaggle for agricultural data visualization
- PyTorch community for ML frameworks
- Indian Government for scheme information
- Agricultural experts for domain knowledge

---

**Made with ❤️ for Farmers**
