import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def test_health():
    """Test health endpoint"""
    response = requests.get(f"{BASE_URL}/health")
    print(f"Health Check: {response.status_code} - {response.json()}")
    return response.status_code == 200

def test_register():
    """Test user registration"""
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpassword123",
        "full_name": "Test User"
    }
    
    response = requests.post(f"{BASE_URL}/api/v1/register", json=user_data)
    print(f"Register: {response.status_code} - {response.json()}")
    return response.status_code == 200

def test_login():
    """Test user login"""
    login_data = {
        "username": "testuser",
        "password": "testpassword123"
    }
    
    response = requests.post(f"{BASE_URL}/api/v1/login", json=login_data)
    print(f"Login: {response.status_code} - {response.json()}")
    
    if response.status_code == 200:
        token = response.json()["access_token"]
        return token
    return None

def test_protected_route(token):
    """Test protected route with token"""
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/api/v1/me", headers=headers)
    print(f"Get User Info: {response.status_code} - {response.json()}")
    return response.status_code == 200

def test_conversation_flow(token):
    """Test conversation creation and messaging"""
    headers = {"Authorization": f"Bearer {token}"}
    
    # Create conversation
    conv_data = {"title": "Test Fashion Chat"}
    response = requests.post(f"{BASE_URL}/api/v1/conversations", json=conv_data, headers=headers)
    print(f"Create Conversation: {response.status_code} - {response.json()}")
    
    if response.status_code == 200:
        conv_id = response.json()["id"]
        
        # Add message
        message_data = {
            "content": "What's trending in fashion this season?",
            "role": "user"
        }
        response = requests.post(
            f"{BASE_URL}/api/v1/conversations/{conv_id}/messages", 
            json=message_data, 
            headers=headers
        )
        print(f"Add Message: {response.status_code} - {response.json()}")
        
        # Get conversations
        response = requests.get(f"{BASE_URL}/api/v1/conversations", headers=headers)
        print(f"Get Conversations: {response.status_code} - {response.json()}")

def run_tests():
    """Run all tests"""
    print("Starting API Tests...\n")
    
    print("1. Testing Health Check...")
    if not test_health():
        print("❌ Health check failed!")
        return
    
    print("\n2. Testing User Registration...")
    if not test_register():
        print("❌ Registration failed!")
        return
    
    print("\n3. Testing User Login...")
    token = test_login()
    if not token:
        print("❌ Login failed!")
        return
    
    print("\n4. Testing Protected Route...")
    if not test_protected_route(token):
        print("❌ Protected route failed!")
        return
    
    print("\n5. Testing Conversation Flow...")
    test_conversation_flow(token)
    
    print("\n✅ All tests completed!")

if __name__ == "__main__":
    run_tests()