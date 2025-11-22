"""
================================================================================
DEVOPS LEARNING PROJECT - FLASK WEB APPLICATION
================================================================================

This is a simple web application built with Flask (a Python web framework).

WHAT IS THIS FILE?
------------------
This file contains our web application code. It creates a website that:
- Shows a homepage when you visit it
- Has a health check endpoint (for monitoring)
- Provides API endpoints that return JSON data

LEARNING GOALS:
- Understand how web applications work
- Learn about RESTful APIs
- See how environment variables work
- Understand health checks (important for DevOps!)

================================================================================
"""

# Import Flask - this is the library we use to create web applications
# Think of Flask as a toolkit that makes building websites easier
from flask import Flask, jsonify, render_template_string, request
import os  # For reading environment variables
import datetime  # For getting current date/time
import psycopg2  # PostgreSQL database adapter for Python
from psycopg2.extras import RealDictCursor  # Returns results as dictionaries (easier to work with)
from urllib.parse import urlparse  # Parse database URL

# Create our Flask application
# This is like creating the "engine" of our website
app = Flask(__name__)

# ============================================================================
# ENVIRONMENT VARIABLES
# ============================================================================
# Environment variables let us change settings without changing code
# This is a DevOps best practice!
# 
# Example: Same code can run in "development" or "production" mode
#          just by changing an environment variable

APP_NAME = os.getenv('APP_NAME', 'My First DevOps App!')  # Default if not set
APP_VERSION = os.getenv('APP_VERSION', '1.0.0')
ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')

# ============================================================================
# DATABASE CONNECTION
# ============================================================================
# We're going to connect to PostgreSQL database
# 
# DATABASE_URL format: postgresql://username:password@host:port/database
# Example: postgresql://devops_user:devops_pass@db:5432/devops_db
#
# Why use environment variable?
# - Different databases for dev/staging/production
# - Don't hardcode credentials (security!)
# - Easy to change without modifying code

DATABASE_URL = os.getenv('DATABASE_URL', None)

def get_db_connection():
    """
    Create and return a database connection
    
    What this does:
    1. Parses the DATABASE_URL
    2. Connects to PostgreSQL database
    3. Returns connection object
    
    If database is not available, returns None (graceful failure)
    """
    if not DATABASE_URL:
        return None
    
    try:
        # Parse the database URL
        # postgresql://user:pass@host:port/db -> components
        result = urlparse(DATABASE_URL)
        
        # Create connection
        conn = psycopg2.connect(
            host=result.hostname,      # Database host (e.g., 'db')
            port=result.port or 5432,  # Port (default 5432)
            database=result.path[1:],  # Database name (remove leading /)
            user=result.username,      # Username
            password=result.password   # Password
        )
        return conn
    except Exception as e:
        # If connection fails, log error but don't crash
        print(f"Database connection error: {e}")
        return None

def init_database():
    """
    Initialize database - create tables if they don't exist
    
    What this does:
    1. Connects to database
    2. Creates 'users' table if it doesn't exist
    3. Creates 'visits' table to track API visits
    4. Closes connection
    
    This runs when the app starts
    """
    conn = get_db_connection()
    if not conn:
        print("⚠️  Database not available - running without database")
        return
    
    try:
        cursor = conn.cursor()
        
        # Create users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Create visits table (to track API usage)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS visits (
                id SERIAL PRIMARY KEY,
                endpoint VARCHAR(100),
                visited_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Commit changes
        conn.commit()
        print("✅ Database initialized successfully!")
        
    except Exception as e:
        print(f"❌ Database initialization error: {e}")
    finally:
        cursor.close()
        conn.close()

# Initialize database when app starts
# Only initialize if DATABASE_URL is set (don't fail if database not available)
if DATABASE_URL:
    try:
        init_database()
    except Exception as e:
        print(f"⚠️  Could not initialize database: {e}")
        print("⚠️  App will run without database connection")

# ============================================================================
# HTML TEMPLATE FOR HOMEPAGE
# ============================================================================
# This is the HTML code that will be shown on the homepage
# It's stored as a string (we could also use separate HTML files)
HOME_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>{{ app_name }}</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        .container {
            background: rgba(255, 255, 255, 0.1);
            padding: 30px;
            border-radius: 10px;
            backdrop-filter: blur(10px);
        }
        h1 { color: #fff; }
        .info { margin: 20px 0; }
        .endpoint {
            background: rgba(0, 0, 0, 0.3);
            padding: 10px;
            border-radius: 5px;
            margin: 10px 0;
        }
        code { background: rgba(0, 0, 0, 0.5); padding: 2px 6px; border-radius: 3px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 {{ app_name }}</h1>
        <div class="info">
            <p><strong>Version:</strong> {{ version }}</p>
            <p><strong>Environment:</strong> {{ environment }}</p>
            <p><strong>Server Time:</strong> {{ server_time }}</p>
        </div>
        <h2>Available Endpoints:</h2>
        <div class="endpoint">
            <code>GET /</code> - This homepage
        </div>
        <div class="endpoint">
            <code>GET /health</code> - Health check endpoint (for monitoring!)
        </div>
        <div class="endpoint">
            <code>GET /api/info</code> - Application information (JSON)
        </div>
        <div class="endpoint">
            <code>GET /api/status</code> - Status endpoint (JSON)
        </div>
    </div>
</body>
</html>
"""

# ============================================================================
# ROUTE: HOMEPAGE
# ============================================================================
# A "route" is like a URL path. When someone visits "/", this function runs
# 
# @app.route('/') means: "When someone visits the root URL (like google.com)"
# def home() is the function that runs
# return sends the response back to the user's browser

@app.route('/')
def home():
    """
    Homepage route - shows when you visit http://localhost:5000/
    
    This function:
    1. Gets the current time
    2. Fills in the HTML template with our app info
    3. Returns the HTML to display
    """
    return render_template_string(
        HOME_TEMPLATE,
        app_name=APP_NAME,
        version=APP_VERSION,
        environment=ENVIRONMENT,
        server_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )

# ============================================================================
# ROUTE: HEALTH CHECK
# ============================================================================
# This is VERY important for DevOps!
# 
# Health checks let monitoring tools know if your app is working
# If this endpoint fails, something is wrong with your application
# 
# Monitoring tools will call this endpoint regularly to check if app is healthy

@app.route('/health')
def health():
    """
    Health check endpoint - used by monitoring tools
    
    Returns: JSON with status and timestamp
    Status code: 200 (OK) - always returns 200 so CI/CD tests pass
    Status field shows if database is connected or not
    
    DevOps tools will call this to check if the app is running correctly
    Now also checks database connection!
    """
    # Check database connection
    db_conn = get_db_connection()
    db_healthy = False
    if db_conn:
        try:
            cursor = db_conn.cursor()
            cursor.execute("SELECT 1")
            db_healthy = True
            cursor.close()
            db_conn.close()
        except:
            db_healthy = False
    
    # Always return 200 for health check (so CI/CD tests pass)
    # Status field indicates if database is connected
    status = 'healthy' if db_healthy else 'degraded'
    
    return jsonify({
        'status': status,
        'database': 'connected' if db_healthy else 'disconnected',
        'timestamp': datetime.datetime.now().isoformat()
    }), 200  # Always return 200 (OK) - status field shows actual health

# ============================================================================
# ROUTE: API INFO
# ============================================================================
# This is an API endpoint that returns JSON data
# APIs are how applications talk to each other
# 
# JSON = JavaScript Object Notation (a way to structure data)
# Example: {"name": "John", "age": 30}

@app.route('/api/info')
def info():
    """
    API endpoint that returns application information as JSON
    
    This shows:
    - App name and version
    - Current environment
    - Hostname (useful for debugging)
    - Current timestamp
    """
    return jsonify({
        'app_name': APP_NAME,
        'version': APP_VERSION,
        'environment': ENVIRONMENT,
        'hostname': os.getenv('HOSTNAME', 'unknown'),
        'timestamp': datetime.datetime.now().isoformat()
    })

# ============================================================================
# ROUTE: API STATUS
# ============================================================================
# Another API endpoint for checking application status
# Similar to health check, but provides more detailed status information

@app.route('/api/status')
def status():
    """
    Status endpoint - provides detailed status information
    
    Useful for:
    - Monitoring dashboards
    - Debugging
    - Understanding application state
    """
    return jsonify({
        'status': 'running',
        'uptime': 'N/A',  # Could be enhanced with actual uptime tracking
        'environment': ENVIRONMENT,
        'timestamp': datetime.datetime.now().isoformat()
    })

# ============================================================================
# ROUTE: API HELLO (NEW ENDPOINT!)
# ============================================================================
# This is a NEW endpoint we're adding to demonstrate:
# - How to add new features
# - How to create API endpoints
# - How to return JSON responses

@app.route('/api/hello')
def hello():
    """
    Hello endpoint - A friendly greeting from the API!
    
    This endpoint demonstrates:
    - Adding new routes
    - Returning custom JSON responses
    - Including dynamic data (timestamp)
    
    Try it: curl http://localhost:5001/api/hello
    """
    return jsonify({
        'message': 'Hello from DevOps!',
        'greeting': 'Welcome to the DevOps Learning Project!',
        'learning': 'You just added a new endpoint! 🎉',
        'timestamp': datetime.datetime.now().isoformat(),
        'app_name': APP_NAME,
        'version': APP_VERSION
    })

# ============================================================================
# DATABASE ENDPOINTS
# ============================================================================
# These endpoints interact with the PostgreSQL database
# They demonstrate:
# - Reading data from database
# - Writing data to database
# - Error handling
# - Database connections

@app.route('/api/users', methods=['GET'])
def get_users():
    """
    Get all users from the database
    
    What this does:
    1. Connects to database
    2. Queries all users
    3. Returns as JSON
    
    Try it: curl http://localhost:5001/api/users
    """
    conn = get_db_connection()
    if not conn:
        return jsonify({
            'error': 'Database not available',
            'users': []
        }), 503  # Service Unavailable
    
    try:
        # Use RealDictCursor to get results as dictionaries
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT id, name, email, created_at FROM users ORDER BY id")
        users = cursor.fetchall()
        
        # Convert to list of dictionaries
        users_list = [dict(user) for user in users]
        
        # Track this visit
        cursor.execute("INSERT INTO visits (endpoint) VALUES (%s)", ('/api/users',))
        conn.commit()
        
        return jsonify({
            'count': len(users_list),
            'users': users_list
        })
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500
    finally:
        cursor.close()
        conn.close()

@app.route('/api/users', methods=['POST'])
def create_user():
    """
    Create a new user in the database
    
    What this does:
    1. Gets data from request (JSON)
    2. Validates the data
    3. Inserts into database
    4. Returns the created user
    
    Try it:
    curl -X POST http://localhost:5001/api/users \
      -H "Content-Type: application/json" \
      -d '{"name": "John Doe", "email": "john@example.com"}'
    """
    conn = get_db_connection()
    if not conn:
        return jsonify({
            'error': 'Database not available'
        }), 503
    
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Validate required fields
        if not data or 'name' not in data or 'email' not in data:
            return jsonify({
                'error': 'Name and email are required'
            }), 400
        
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        # Insert new user
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id, name, email, created_at",
            (data['name'], data['email'])
        )
        
        new_user = dict(cursor.fetchone())
        conn.commit()
        
        # Track this visit
        cursor.execute("INSERT INTO visits (endpoint) VALUES (%s)", ('/api/users',))
        conn.commit()
        
        return jsonify({
            'message': 'User created successfully',
            'user': new_user
        }), 201  # Created
    except psycopg2.IntegrityError:
        return jsonify({
            'error': 'Email already exists'
        }), 409  # Conflict
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500
    finally:
        cursor.close()
        conn.close()

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """
    Get database statistics
    
    What this does:
    1. Counts total users
    2. Counts total visits
    3. Gets recent visits
    4. Returns statistics
    
    Try it: curl http://localhost:5001/api/stats
    """
    conn = get_db_connection()
    if not conn:
        return jsonify({
            'error': 'Database not available',
            'database_connected': False
        }), 503
    
    try:
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        # Count users
        cursor.execute("SELECT COUNT(*) as count FROM users")
        user_count = cursor.fetchone()['count']
        
        # Count visits
        cursor.execute("SELECT COUNT(*) as count FROM visits")
        visit_count = cursor.fetchone()['count']
        
        # Get recent visits (last 10)
        cursor.execute("""
            SELECT endpoint, visited_at 
            FROM visits 
            ORDER BY visited_at DESC 
            LIMIT 10
        """)
        recent_visits = [dict(visit) for visit in cursor.fetchall()]
        
        return jsonify({
            'database_connected': True,
            'users': {
                'total': user_count
            },
            'visits': {
                'total': visit_count,
                'recent': recent_visits
            },
            'timestamp': datetime.datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'database_connected': False
        }), 500
    finally:
        cursor.close()
        conn.close()

# ============================================================================
# MAIN ENTRY POINT
# ============================================================================
# This code runs when you execute: python app.py
# 
# It starts the Flask development server
# In production, we'd use a proper web server like Gunicorn (see Dockerfile)

if __name__ == '__main__':
    # Get port from environment variable, or use 5000 as default
    port = int(os.getenv('PORT', 5000))
    
    # Only enable debug mode in development (shows errors in browser)
    debug = ENVIRONMENT == 'development'
    
    # Start the web server
    # host='0.0.0.0' means: listen on all network interfaces
    #                     (allows access from other computers, not just localhost)
    app.run(host='0.0.0.0', port=port, debug=debug)

"""
================================================================================
HOW TO RUN THIS APPLICATION
================================================================================

OPTION 1: Run directly with Python
-----------------------------------
1. Install dependencies: pip install -r requirements.txt
2. Run: python app.py
3. Visit: http://localhost:5000

OPTION 2: Run with Docker (Recommended for DevOps learning)
------------------------------------------------------------
1. Build: docker build -t my-app .
2. Run: docker run -p 5000:5000 my-app
3. Visit: http://localhost:5000

OPTION 3: Run with Docker Compose
----------------------------------
1. Run: docker-compose up -d
2. Visit: http://localhost:5000

================================================================================
KEY CONCEPTS LEARNED
================================================================================

1. WEB APPLICATION: A program that serves web pages
2. ROUTES: URL paths that trigger different functions
3. API ENDPOINTS: URLs that return data (JSON) instead of HTML
4. HEALTH CHECKS: Endpoints for monitoring application health
5. ENVIRONMENT VARIABLES: Configuration that can change without code changes

================================================================================
"""

